#!/usr/bin/env python3
"""Validate the EHCOsystem public dossier, evidence estate, and public boundaries.

The validator uses only the Python standard library. Its result is bounded to
repository identity, structure, manifest integrity, JSON syntax, navigation,
high-confidence secret indicators, licensing presence, and current public
semantic-boundary compliance. It does not execute or observe the Runtime.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import unquote

REPO_ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_ROOT = REPO_ROOT / "evidence" / "public-evidence-companion" / "v1"
DOSSIER_NAME = (
    "EHCO_AI_OS_Governed_Operational_Architecture_"
    "Public_Edition_v1_8_LOCK_FINAL.pdf"
)
DOSSIER_SHA256 = "F489BA01961A12CF101B1F1DF57E6958456A0840BEB798B862FA97ACB030892D"
EXPECTED_PACKETS = [
    "00_DOSSIER_IDENTITY_AND_BOUNDARY",
    "01_INSTANTIATED_STANDING",
    "02_CANONICAL_RUNTIME_SOURCE_BINDING",
    "03_TIER1_AUTHORITY_ENFORCEMENT",
    "04_RUNTIME_PACKET_AND_CONTINUITY_ANCHORS",
    "05_PROOF_COLLAPSE_RECOVERY_AND_RELEASE_ANCHORS",
    "06_OBSERVED_LIVE_CAPTURE_AND_RELEASE_STATUS",
    "07_PUBLIC_BOUNDARIES_AND_DELIVERY_STATUS",
    "08_SUITE_VERIFICATION_AND_FINAL_ZIP",
]

CURRENT_PUBLIC_TEXT = [
    "README.md",
    "LIBRARY.md",
    "GOVERNANCE.md",
    "SECURITY.md",
    "NOTICE.md",
    "getting-started/START-HERE.md",
    "getting-started/reading-order.md",
    "getting-started/repository-map.md",
    "architecture/EHCO-AI-OS-INSTANTIATED-SYSTEM.md",
    "architecture/instantiated-proof-range.md",
    "architecture/ecosystem-components-and-participation.md",
    "architecture/proof-and-status-classes.md",
    "architecture/runtime-repository-and-test-estate-boundary.md",
    "language-model/README.md",
    "dossiers/README.md",
    "evidence/README.md",
    "verification/README.md",
    "releases/PUBLIC-RELEASE-REGISTER.md",
]

ERRORS: list[str] = []
CHECKS = 0


def fail(message: str) -> None:
    ERRORS.append(message)


def checked(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        fail(message)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        fail(f"JSON parse failure: {path.relative_to(REPO_ROOT)}: {exc}")
        return {}


def read_public_text(relative: str) -> str:
    path = REPO_ROOT / relative
    checked(path.is_file(), f"Missing required public text: {relative}")
    if not path.is_file():
        return ""
    try:
        return path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        fail(f"Unable to read required public text: {relative}: {exc}")
        return ""


def validate_repository_residue() -> None:
    forbidden_exact = {
        "UPLOAD_INSTRUCTIONS_DO_NOT_COMMIT.txt",
        "PACKAGE_SHA256SUMS_DO_NOT_COMMIT.txt",
    }
    forbidden_dirs = {
        EVIDENCE_ROOT / "evidence",
        EVIDENCE_ROOT / "dossiers",
        REPO_ROOT / ".import-staging",
    }

    for directory in forbidden_dirs:
        checked(
            not directory.exists(),
            f"Forbidden directory present: {directory.relative_to(REPO_ROOT)}",
        )

    wrong_pdf = REPO_ROOT / "evidence" / "public-evidence-companion" / DOSSIER_NAME
    checked(
        not wrong_pdf.exists(),
        f"Legacy PDF path present: {wrong_pdf.relative_to(REPO_ROOT)}",
    )

    for path in REPO_ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.is_file():
            relative = path.relative_to(REPO_ROOT)
            checked(path.name not in forbidden_exact, f"Upload helper present: {relative}")
            checked(path.suffix.lower() != ".zip", f"ZIP archive present in repository: {relative}")
            checked(
                not re.fullmatch(r"part-\d+", path.name),
                f"Transfer chunk present: {relative}",
            )


def validate_required_public_controls() -> None:
    license_path = REPO_ROOT / "LICENSE"
    boundary_path = (
        REPO_ROOT / "architecture" / "runtime-repository-and-test-estate-boundary.md"
    )
    checked(license_path.is_file(), "Missing root LICENSE")
    checked(boundary_path.is_file(), "Missing Runtime/repository/test-estate boundary")

    if license_path.is_file():
        license_text = license_path.read_text(encoding="utf-8-sig")
        checked(
            license_text.startswith("EHCOnomics Proprietary Public Inspection License v1.0"),
            "Unexpected or missing proprietary license identity",
        )
        checked(
            "This repository is a public architecture, evidence, provenance" in license_text,
            "LICENSE does not state the repository/Runtime boundary",
        )


def validate_semantic_boundaries() -> None:
    texts = {relative: read_public_text(relative) for relative in CURRENT_PUBLIC_TEXT}

    # These phrases are prohibited in current public interpretation documents.
    # Hash-preserved Packets 00-08 are intentionally outside this scan.
    prohibited = {
        "deleted Runtime repository name": "ehco_runtime",
        "private repository locator": "ehconomics/EHCO_AI-OS",
        "current-source-owner claim": "current canonical source owner for EHCO AI-OS",
        "pending Runtime promotion claim": "runtime promotion remains pending",
        "pending-promotion machine state": "source_current_runtime_promotion_pending",
    }
    for relative, text in texts.items():
        lowered = text.lower()
        for label, phrase in prohibited.items():
            checked(
                phrase.lower() not in lowered,
                f"Prohibited {label} in current public text: {relative}",
            )

    boundary = texts["architecture/runtime-repository-and-test-estate-boundary.md"]
    required_boundary_statements = [
        "EHCO AI-OS is the realized Tier 1 Runtime",
        "Those repositories, folders, and files are not the Runtime.",
        "Packet 02",
        "Packet 06",
        "Independent third-party certification or validation is not claimed",
    ]
    for statement in required_boundary_statements:
        checked(
            statement in boundary,
            f"Boundary record missing required statement: {statement}",
        )

    readme = texts["README.md"]
    checked(
        "architecture/runtime-repository-and-test-estate-boundary.md" in readme,
        "README does not link the controlling Runtime/repository boundary",
    )
    checked("(LICENSE)" in readme, "README does not link the root LICENSE")
    checked(
        "This GitHub repository is not the Runtime." in readme,
        "README does not state the repository/Runtime separation",
    )

    evidence_readme = texts["evidence/README.md"]
    checked(
        "It does **not** establish that the files" in evidence_readme,
        "Evidence landing page does not bound Packet 02 artifact identity",
    )
    checked(
        "Packet-integrity `PASS` is not universal behavioral `PASS`." in evidence_readme,
        "Evidence landing page does not distinguish Packet 06 integrity from behavior",
    )
    checked(
        "Historical paths, container names, service names, and port bindings" in evidence_readme,
        "Evidence landing page does not classify historical capture locators",
    )

    release_register = texts["releases/PUBLIC-RELEASE-REGISTER.md"]
    checked("`LICENSE`" in release_register, "Release register does not inventory LICENSE")
    checked(
        "not a Runtime repository" in release_register,
        "Release register does not bound Packet 02",
    )
    checked(
        "integrity `PASS` is not universal behavioral `PASS`" in release_register,
        "Release register does not bound Packet 06",
    )


def validate_dossier() -> None:
    paths = [
        REPO_ROOT / "dossiers" / DOSSIER_NAME,
        EVIDENCE_ROOT
        / "00_DOSSIER_IDENTITY_AND_BOUNDARY"
        / "source_document"
        / DOSSIER_NAME,
    ]
    hashes: list[str] = []
    for path in paths:
        checked(path.is_file(), f"Missing canonical dossier: {path.relative_to(REPO_ROOT)}")
        if path.is_file():
            digest = sha256_file(path)
            hashes.append(digest)
            checked(
                digest == DOSSIER_SHA256,
                f"Dossier SHA-256 mismatch: {path.relative_to(REPO_ROOT)}",
            )
    if len(hashes) == 2:
        checked(hashes[0] == hashes[1], "Canonical dossier copies are not byte-identical")


def safe_manifest_path(value: str) -> bool:
    pure = PurePosixPath(value)
    return (
        bool(value)
        and not pure.is_absolute()
        and ".." not in pure.parts
        and "\\" not in value
    )


def validate_packets_and_manifests() -> dict[str, str]:
    checked(EVIDENCE_ROOT.is_dir(), "Missing evidence/public-evidence-companion/v1 directory")
    actual_dirs = (
        sorted(path.name for path in EVIDENCE_ROOT.iterdir() if path.is_dir())
        if EVIDENCE_ROOT.is_dir()
        else []
    )
    checked(actual_dirs == EXPECTED_PACKETS, f"Packet directory set mismatch: {actual_dirs}")

    manifest_hashes: dict[str, str] = {}
    for packet_name in EXPECTED_PACKETS:
        packet_dir = EVIDENCE_ROOT / packet_name
        manifest_path = packet_dir / "CONTENT_MANIFEST.json"
        detached_path = packet_dir / "CONTENT_MANIFEST.sha256"
        verification_path = packet_dir / "VERIFICATION_RESULT.json"

        checked(manifest_path.is_file(), f"Missing manifest: {manifest_path.relative_to(REPO_ROOT)}")
        checked(detached_path.is_file(), f"Missing detached manifest hash: {detached_path.relative_to(REPO_ROOT)}")
        checked(verification_path.is_file(), f"Missing verification result: {verification_path.relative_to(REPO_ROOT)}")
        if not manifest_path.is_file():
            continue

        manifest = load_json(manifest_path)
        if not isinstance(manifest, dict):
            fail(f"Manifest is not an object: {manifest_path.relative_to(REPO_ROOT)}")
            continue

        files = manifest.get("files")
        checked(isinstance(files, list), f"Manifest files is not a list: {manifest_path.relative_to(REPO_ROOT)}")
        if not isinstance(files, list):
            continue

        checked(manifest.get("file_count") == len(files), f"Manifest file_count mismatch: {packet_name}")
        self_reference = manifest.get("manifest_self_reference", manifest.get("self_reference"))
        checked(self_reference is False, f"Manifest self-reference must be false: {packet_name}")

        seen: set[str] = set()
        for entry in files:
            if not isinstance(entry, dict):
                fail(f"Invalid manifest entry in {packet_name}")
                continue
            relative_value = entry.get("path")
            if not isinstance(relative_value, str) or not safe_manifest_path(relative_value):
                fail(f"Unsafe manifest path in {packet_name}: {relative_value!r}")
                continue
            checked(relative_value not in seen, f"Duplicate manifest path in {packet_name}: {relative_value}")
            seen.add(relative_value)
            target = packet_dir.joinpath(*PurePosixPath(relative_value).parts)
            checked(target.is_file(), f"Manifest target missing: {target.relative_to(REPO_ROOT)}")
            if target.is_file():
                checked(
                    target.stat().st_size == entry.get("bytes"),
                    f"Byte-count mismatch: {target.relative_to(REPO_ROOT)}",
                )
                checked(
                    sha256_file(target) == str(entry.get("sha256", "")).upper(),
                    f"SHA-256 mismatch: {target.relative_to(REPO_ROOT)}",
                )

        manifest_digest = sha256_file(manifest_path)
        manifest_hashes[packet_name] = manifest_digest
        if detached_path.is_file():
            token = detached_path.read_text(encoding="utf-8-sig").strip().split()[0].upper()
            checked(token == manifest_digest, f"Detached manifest hash mismatch: {packet_name}")

        if verification_path.is_file():
            verification = load_json(verification_path)
            if isinstance(verification, dict):
                checked(
                    verification.get("status") == "PASS",
                    f"Verification status is not PASS: {packet_name}",
                )

    return manifest_hashes


def validate_json_syntax() -> None:
    for path in sorted(EVIDENCE_ROOT.rglob("*.json")):
        global CHECKS
        CHECKS += 1
        load_json(path)


def validate_suite(manifest_hashes: dict[str, str]) -> None:
    suite_path = EVIDENCE_ROOT / EXPECTED_PACKETS[8] / "SUITE_MANIFEST.json"
    suite = load_json(suite_path)
    if not isinstance(suite, dict):
        fail("Suite manifest is not an object")
        return

    dossier = suite.get("dossier", {})
    checked(
        isinstance(dossier, dict)
        and str(dossier.get("sha256", "")).upper() == DOSSIER_SHA256,
        "Suite dossier hash mismatch",
    )
    checked(suite.get("prior_packet_count") == 8, "Suite prior_packet_count must be 8")
    checked(suite.get("total_packet_count") == 9, "Suite total_packet_count must be 9")
    checked(
        suite.get("packets_scope") == "PRIOR_PACKETS_00_THROUGH_07",
        "Unexpected suite packet scope",
    )

    packets = suite.get("packets")
    checked(isinstance(packets, list) and len(packets) == 8, "Suite must enumerate Packets 00-07")
    if isinstance(packets, list):
        for index, entry in enumerate(packets):
            if not isinstance(entry, dict):
                fail(f"Invalid suite packet entry at index {index}")
                continue
            expected = EXPECTED_PACKETS[index]
            checked(entry.get("sequence") == index, f"Suite sequence mismatch for {expected}")
            checked(entry.get("directory") == expected, f"Suite directory mismatch at sequence {index}")
            checked(
                str(entry.get("manifest_sha256", "")).upper()
                == manifest_hashes.get(expected),
                f"Suite manifest hash mismatch for {expected}",
            )
            checked(
                entry.get("verification_status") == "PASS",
                f"Suite verification status is not PASS for {expected}",
            )

    closure = suite.get("closure_packet", {})
    checked(
        isinstance(closure, dict) and closure.get("sequence") == 8,
        "Closure packet sequence must be 8",
    )
    checked(
        isinstance(closure, dict) and closure.get("directory") == EXPECTED_PACKETS[8],
        "Closure packet directory mismatch",
    )
    checked(
        isinstance(closure, dict) and closure.get("verification_status") == "PASS",
        "Closure packet verification is not PASS",
    )


def validate_markdown_links() -> None:
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for markdown in sorted(REPO_ROOT.rglob("*.md")):
        if ".git" in markdown.parts:
            continue
        text = markdown.read_text(encoding="utf-8-sig")
        for raw_target in link_pattern.findall(text):
            target = raw_target.strip().strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            resolved = (markdown.parent / target).resolve()
            checked(
                resolved.exists(),
                f"Broken Markdown link in {markdown.relative_to(REPO_ROOT)}: {raw_target}",
            )


def validate_secret_indicators() -> None:
    patterns = {
        "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
        "GitHub classic token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
        "GitHub fine-grained token": re.compile(r"\bgithub_pat_[A-Za-z0-9_]{40,}\b"),
        "OpenAI-style secret key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
        "Slack token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
        "Private key block": re.compile(
            r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"
        ),
    }
    excluded_suffixes = {".pdf", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".zip"}
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() in excluded_suffixes:
            continue
        if path.stat().st_size > 5 * 1024 * 1024:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for label, pattern in patterns.items():
            checked(
                pattern.search(text) is None,
                f"High-confidence {label} indicator in {path.relative_to(REPO_ROOT)}",
            )


def main() -> int:
    validate_repository_residue()
    validate_required_public_controls()
    validate_semantic_boundaries()
    validate_dossier()
    validate_json_syntax()
    manifest_hashes = validate_packets_and_manifests()
    validate_suite(manifest_hashes)
    validate_markdown_links()
    validate_secret_indicators()

    if ERRORS:
        print(f"FAIL: {len(ERRORS)} error(s) across {CHECKS} checks", file=sys.stderr)
        for error in ERRORS:
            print(f"- {error}", file=sys.stderr)
        return 1

    json_count = sum(1 for _ in EVIDENCE_ROOT.rglob("*.json"))
    file_count = sum(1 for path in EVIDENCE_ROOT.rglob("*") if path.is_file())
    print(
        "PASS: EHCOsystem public repository validation "
        f"({CHECKS} checks, {file_count} evidence files, {json_count} JSON files, "
        f"{len(EXPECTED_PACKETS)} packet directories, semantic boundaries enforced)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
