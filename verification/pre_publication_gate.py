#!/usr/bin/env python3
"""Fail-closed pre-publication disclosure gate for EHCOsystem.

The gate is intended to run before any candidate ref is pushed to the public
GitHub repository. It scans every Git object newly reachable from the candidate
relative to an accepted public base, plus commit messages and provider-facing
metadata supplied by the caller. Findings report rule classes without echoing
matched protected values.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from public_disclosure_policy import find_disclosure_violations, run_synthetic_policy_self_test

POLICY_VERSION = "EHCO_PUBLIC_PREPUBLICATION_DISCLOSURE_GATE_V1"
PUBLIC_REPOSITORY = "EHCOnomics-Systems/EHCOsystem"
MAX_BLOB_BYTES = 32 * 1024 * 1024

_SECRET_PATTERNS = [
    ("PRIVATE_KEY_BLOCK", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("GITHUB_CLASSIC_TOKEN", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b")),
    ("GITHUB_FINE_GRAINED_TOKEN", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{30,}\b")),
    ("AWS_ACCESS_KEY", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
]
_FORBIDDEN_ARCHIVE_SUFFIXES = {
    ".7z", ".bz2", ".cab", ".docx", ".gz", ".jar", ".odp", ".ods", ".odt",
    ".pptx", ".rar", ".tar", ".tgz", ".war", ".xlsx", ".xz", ".zip",
}


class GateFailure(RuntimeError):
    pass


def _run_git(root: Path, *args: str, text: bool = True) -> str | bytes:
    try:
        completed = subprocess.run(
            ["git", *args],
            cwd=root,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except subprocess.CalledProcessError as exc:
        raise GateFailure(f"git operation failed: {args[0] if args else 'unknown'}") from exc
    return completed.stdout.decode("utf-8", errors="strict") if text else completed.stdout


def _resolve_commit(root: Path, ref: str) -> str:
    value = _run_git(root, "rev-parse", "--verify", f"{ref}^{{commit}}").strip()
    if not re.fullmatch(r"[0-9a-f]{40}", value):
        raise GateFailure("candidate/base ref did not resolve to a full commit SHA")
    return value


def _candidate_decodings(data: bytes) -> list[str]:
    values: list[str] = []
    for encoding in ("utf-8", "latin-1"):
        values.append(data.decode(encoding, errors="ignore"))
    if b"\x00" in data or data.startswith((b"\xff\xfe", b"\xfe\xff")):
        for encoding in ("utf-16-le", "utf-16-be"):
            values.append(data.decode(encoding, errors="ignore"))
    return values


def _rule_hits(text: str, source: str) -> set[str]:
    hits = {item.rule for item in find_disclosure_violations(text, source)}
    for name, pattern in _SECRET_PATTERNS:
        if pattern.search(text):
            hits.add(name)
    return hits


def _scan_bytes(data: bytes, source: str) -> set[str]:
    hits: set[str] = set()
    for text in _candidate_decodings(data):
        hits.update(_rule_hits(text, source))
    return hits


def _new_objects(root: Path, base_sha: str, candidate_sha: str) -> list[tuple[str, str]]:
    raw = _run_git(root, "rev-list", "--objects", candidate_sha, f"^{base_sha}")
    objects: list[tuple[str, str]] = []
    for line in raw.splitlines():
        if not line:
            continue
        sha, sep, path = line.partition(" ")
        objects.append((sha, path if sep else ""))
    return objects


def _write_receipt(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, dir=path.parent) as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")
        temp_name = handle.name
    os.replace(temp_name, path)


def evaluate(
    root: Path,
    base_ref: str,
    candidate_ref: str,
    ref_names: list[str] | None = None,
    metadata_files: list[Path] | None = None,
    receipt_path: Path | None = None,
) -> tuple[dict, set[str]]:
    run_synthetic_policy_self_test()
    base_sha = _resolve_commit(root, base_ref)
    candidate_sha = _resolve_commit(root, candidate_ref)

    if subprocess.run(
        ["git", "merge-base", "--is-ancestor", base_sha, candidate_sha],
        cwd=root,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode != 0:
        raise GateFailure("accepted public base is not an ancestor of the candidate")

    violations: set[str] = set()
    for ref_name in ref_names or []:
        violations.update(_rule_hits(ref_name, "provider-ref"))

    for metadata_file in metadata_files or []:
        try:
            payload = metadata_file.read_bytes()
        except OSError as exc:
            raise GateFailure("provider metadata file could not be read") from exc
        violations.update(_scan_bytes(payload, "provider-metadata"))

    commits = [
        line
        for line in _run_git(root, "rev-list", "--reverse", f"{base_sha}..{candidate_sha}").splitlines()
        if line
    ]
    for commit_sha in commits:
        message = _run_git(root, "show", "-s", "--format=%B", commit_sha)
        violations.update(_rule_hits(message, "commit-message"))

    blob_count = 0
    opaque_archive_count = 0
    for object_sha, object_path in _new_objects(root, base_sha, candidate_sha):
        object_type = _run_git(root, "cat-file", "-t", object_sha).strip()
        if object_type != "blob":
            continue
        blob_count += 1
        if object_path:
            violations.update(_rule_hits(object_path, "git-path"))
            if Path(object_path).suffix.lower() in _FORBIDDEN_ARCHIVE_SUFFIXES:
                opaque_archive_count += 1
                violations.add("OPAQUE_ARCHIVE_OR_OFFICE_CONTAINER")

        size = int(_run_git(root, "cat-file", "-s", object_sha).strip())
        if size > MAX_BLOB_BYTES:
            violations.add("BLOB_EXCEEDS_PREPUBLICATION_SCAN_LIMIT")
            continue
        data = _run_git(root, "cat-file", "blob", object_sha, text=False)
        violations.update(_scan_bytes(data, "git-blob"))

    tree_sha = _run_git(root, "rev-parse", f"{candidate_sha}^{{tree}}").strip()
    receipt = {
        "schema": "ehco.publication-clearance.v1",
        "policy": POLICY_VERSION,
        "status": "PASS" if not violations else "FAIL",
        "repository": PUBLIC_REPOSITORY,
        "base_sha": base_sha,
        "candidate_sha": candidate_sha,
        "candidate_tree_sha": tree_sha,
        "commit_count": len(commits),
        "new_blob_count": blob_count,
        "provider_ref_count": len(ref_names or []),
        "provider_metadata_file_count": len(metadata_files or []),
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    if opaque_archive_count:
        receipt["opaque_archive_count"] = opaque_archive_count

    if not violations and receipt_path is not None:
        _write_receipt(receipt_path, receipt)
    return receipt, violations


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="origin/main", help="accepted public base ref/SHA")
    parser.add_argument("--candidate", default="HEAD", help="candidate ref/SHA")
    parser.add_argument("--ref-name", action="append", default=[], help="provider-visible ref name to scan")
    parser.add_argument(
        "--metadata-file",
        action="append",
        default=[],
        help="local file containing provider-facing title/body/release metadata to scan",
    )
    parser.add_argument(
        "--receipt",
        default=None,
        help="write PASS receipt here; path should remain outside the public tree (for example .git/...)",
    )
    args = parser.parse_args()

    try:
        root = Path(_run_git(Path.cwd(), "rev-parse", "--show-toplevel").strip())
        receipt, violations = evaluate(
            root=root,
            base_ref=args.base,
            candidate_ref=args.candidate,
            ref_names=args.ref_name,
            metadata_files=[Path(item) for item in args.metadata_file],
            receipt_path=Path(args.receipt) if args.receipt else None,
        )
    except (GateFailure, AssertionError, ValueError) as exc:
        print(f"FAIL pre-publication disclosure gate: {exc}", file=sys.stderr)
        return 2

    if violations:
        print("FAIL pre-publication disclosure gate", file=sys.stderr)
        for rule in sorted(violations):
            print(f"  rule={rule}", file=sys.stderr)
        print("Protected values are intentionally not echoed.", file=sys.stderr)
        return 1

    print(
        "PASS pre-publication disclosure gate "
        f"candidate={receipt['candidate_sha'][:12]} "
        f"base={receipt['base_sha'][:12]} "
        f"commits={receipt['commit_count']} "
        f"new_blobs={receipt['new_blob_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
