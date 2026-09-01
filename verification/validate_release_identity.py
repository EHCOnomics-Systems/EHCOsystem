#!/usr/bin/env python3
"""Validate EHCOsystem public publication identity and stable repository provenance."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "1.0.0"
TAG = "v1.0.0-public"
TITLE = "EHCOsystem Public Architecture and Evidence Baseline v1.0.0"
STABLE_MANIFEST_ACCEPTED_COMMIT = "eff9301e7c5ddfc0759ee0d7e3c026ad28c5670c"
SOURCE_ONLY_ARTIFACT_DIGEST = "NOT_APPLICABLE_SOURCE_ONLY_PUBLIC_PROJECTION_NO_SEPARATE_BUILD_ARTIFACT"
PACKET_SHA256 = "7F80C27D085AE871A00AED412C6F20EA9A76CB0677C93AEBA381CD1FD70EC8E5"


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def read(relative: str, errors: list[str]) -> str:
    path = ROOT / relative
    if not path.is_file():
        errors.append(f"Missing publication/provenance document: {relative}")
        return ""
    return path.read_text(encoding="utf-8-sig")


def main() -> int:
    errors: list[str] = []
    register = read("releases/PUBLIC-RELEASE-REGISTER.md", errors)
    repo_map = read("getting-started/repository-map.md", errors)
    manifest = read("ehco.repository.yaml", errors)
    provenance = read("PROVENANCE.md", errors)

    for text, label in ((register, "release register"), (repo_map, "repository map")):
        for phrase in (f"Version: `{VERSION}`", f"Tag: `{TAG}`", f"Release title: `{TITLE}`"):
            require(phrase in text, f"Registered release identity missing from {label}: {phrase}", errors)

    for phrase in (
        "CURRENT_PUBLIC_EVIDENCE_IDENTITY",
        PACKET_SHA256,
        "PUBLIC_SAFE_RECORD.json",
        "raw accepted packet",
        "Registered repository release identity and provider-owned GitHub Release materialization",
    ):
        require(phrase in register, f"Publication register missing: {phrase}", errors)

    for phrase in (
        f"accepted_commit: {STABLE_MANIFEST_ACCEPTED_COMMIT}",
        f"artifact_digest: {SOURCE_ONLY_ARTIFACT_DIGEST}",
        "unresolved_items: []",
    ):
        require(phrase in manifest, f"Stable repository manifest provenance mismatch: {phrase}", errors)

    require(f"`{STABLE_MANIFEST_ACCEPTED_COMMIT}`" in provenance, "PROVENANCE.md stable accepted commit missing", errors)
    require(f"`{SOURCE_ONLY_ARTIFACT_DIGEST}`" in provenance, "PROVENANCE.md source-only artifact classification missing", errors)

    for placeholder in ("accepted_commit: UNRESOLVED", "artifact_digest: UNRESOLVED"):
        require(placeholder.lower() not in (manifest + provenance + register).lower(), f"Legacy unresolved provenance placeholder present: {placeholder}", errors)

    if errors:
        print(f"FAIL: {len(errors)} publication/provenance error(s)", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"PASS: EHCOsystem public publication identity (version {VERSION}, tag {TAG})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
