#!/usr/bin/env python3
"""Validate the canonical EHCOsystem public release identity documents."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
RELEASE_VERSION = "1.0.0"
RELEASE_TAG = "v1.0.0-public"
RELEASE_TITLE = "EHCOsystem Public Architecture and Evidence Baseline v1.0.0"

DOCUMENTS = [
    "getting-started/repository-map.md",
    "releases/PUBLIC-RELEASE-REGISTER.md",
]

REQUIRED_STATEMENTS = [
    f"Version: `{RELEASE_VERSION}`",
    f"Tag: `{RELEASE_TAG}`",
    f"Release title: `{RELEASE_TITLE}`",
    "The GitHub Releases surface determines live publication state.",
]

OBSOLETE_STATEMENTS = [
    "No tagged GitHub Release is currently declared",
    "No tag or GitHub Release is currently declared",
]


def main() -> int:
    errors: list[str] = []
    checks = 0

    for relative in DOCUMENTS:
        path = REPO_ROOT / relative
        checks += 1
        if not path.is_file():
            errors.append(f"Missing release identity document: {relative}")
            continue

        text = path.read_text(encoding="utf-8-sig")
        for statement in REQUIRED_STATEMENTS:
            checks += 1
            if statement not in text:
                errors.append(f"Release identity missing from {relative}: {statement}")

        for statement in OBSOLETE_STATEMENTS:
            checks += 1
            if statement.lower() in text.lower():
                errors.append(f"Obsolete release-state wording in {relative}: {statement}")

    if errors:
        print(
            f"FAIL: {len(errors)} release identity error(s) across {checks} checks",
            file=sys.stderr,
        )
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "PASS: EHCOsystem canonical public release identity "
        f"({checks} checks, version {RELEASE_VERSION}, tag {RELEASE_TAG})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
