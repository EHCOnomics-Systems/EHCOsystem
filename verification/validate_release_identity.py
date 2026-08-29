#!/usr/bin/env python3
"""Validate the canonical EHCOsystem public release identity and provenance semantics."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
RELEASE_VERSION = "1.0.0"
RELEASE_TAG = "v1.0.0-public"
RELEASE_TITLE = "EHCOsystem Public Architecture and Evidence Baseline v1.0.0"
STABLE_MANIFEST_ACCEPTED_COMMIT = "eff9301e7c5ddfc0759ee0d7e3c026ad28c5670c"
SOURCE_ONLY_ARTIFACT_DIGEST = "NOT_APPLICABLE_SOURCE_ONLY_PUBLIC_PROJECTION_NO_SEPARATE_BUILD_ARTIFACT"

RELEASE_DOCUMENTS = [
    "getting-started/repository-map.md",
    "releases/PUBLIC-RELEASE-REGISTER.md",
]

RELEASE_REQUIRED_STATEMENTS = [
    f"Version: `{RELEASE_VERSION}`",
    f"Tag: `{RELEASE_TAG}`",
    f"Release title: `{RELEASE_TITLE}`",
    "The GitHub Releases surface determines live publication state.",
]

PROVENANCE_REQUIRED = {
    "ehco.repository.yaml": [
        f"accepted_commit: {STABLE_MANIFEST_ACCEPTED_COMMIT}",
        f"artifact_digest: {SOURCE_ONLY_ARTIFACT_DIGEST}",
        "unresolved_items: []",
    ],
    "PROVENANCE.md": [
        f"`{STABLE_MANIFEST_ACCEPTED_COMMIT}`",
        f"`{SOURCE_ONLY_ARTIFACT_DIGEST}`",
        "it is not an alias for current `main`",
        "Registered release identity and live provider publication are distinct publication states.",
    ],
    "releases/PUBLIC-RELEASE-REGISTER.md": [
        f"`provenance.accepted_commit` identifies the commit that accepted the stable `ehco.repository.yaml` boundary represented by the file, not current `main`;",
        f"`{STABLE_MANIFEST_ACCEPTED_COMMIT}`",
        f"`provenance.artifact_digest` is `{SOURCE_ONLY_ARTIFACT_DIGEST}`",
        "The registered release identity above remains distinct from provider publication.",
    ],
}

OBSOLETE_STATEMENTS = [
    "No tagged GitHub Release is currently declared",
    "No tag or GitHub Release is currently declared",
    "accepted_commit: UNRESOLVED",
    "artifact_digest: UNRESOLVED",
    "Define non-circular acceptance semantics before populating provenance.accepted_commit or artifact_digest.",
]


def read(relative: str, errors: list[str]) -> str:
    path = REPO_ROOT / relative
    if not path.is_file():
        errors.append(f"Missing release/provenance document: {relative}")
        return ""
    return path.read_text(encoding="utf-8-sig")


def main() -> int:
    errors: list[str] = []
    checks = 0
    loaded: dict[str, str] = {}

    for relative in sorted(set(RELEASE_DOCUMENTS) | set(PROVENANCE_REQUIRED)):
        checks += 1
        loaded[relative] = read(relative, errors)

    for relative in RELEASE_DOCUMENTS:
        text = loaded.get(relative, "")
        for statement in RELEASE_REQUIRED_STATEMENTS:
            checks += 1
            if statement not in text:
                errors.append(f"Release identity missing from {relative}: {statement}")

    for relative, statements in PROVENANCE_REQUIRED.items():
        text = loaded.get(relative, "")
        for statement in statements:
            checks += 1
            if statement not in text:
                errors.append(f"Provenance invariant missing from {relative}: {statement}")

    for relative, text in loaded.items():
        for statement in OBSOLETE_STATEMENTS:
            checks += 1
            if statement.lower() in text.lower():
                errors.append(f"Obsolete release/provenance wording in {relative}: {statement}")

    if errors:
        print(
            f"FAIL: {len(errors)} release/provenance error(s) across {checks} checks",
            file=sys.stderr,
        )
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "PASS: EHCOsystem canonical public release identity and non-circular provenance "
        f"({checks} checks, version {RELEASE_VERSION}, tag {RELEASE_TAG})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
