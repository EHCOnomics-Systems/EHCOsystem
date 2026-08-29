#!/usr/bin/env python3
"""Validate the EHCO Language Model public test snapshot.

This validator confirms the public snapshot's file identity, JSON structure,
case counts, disclosure boundary, and affirmative evidence-scope language.
The snapshot's evidence class and owning-source relationships remain explicit.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / "language-model" / "evidence" / "public-test-snapshot-v1"
MANIFEST = SNAPSHOT / "MANIFEST.json"
README = SNAPSHOT / "README.md"
INDEX = SNAPSHOT / "QUALIFICATION_TEST_INDEX_2026-08-24.md"

EXPECTED: dict[str, tuple[str, int]] = {
    "actual-tests/LM_ZW_CAP_SLICE_001_LEXICAL_MORPHOLOGY.json": (
        "c30b4a522963e5d63dec4d2171b33ce570bbc411",
        8,
    ),
    "actual-tests/LM_ZW_CAP_SLICE_002_SYNTAX_COMPOSITION.json": (
        "cc0a690dc57dfb5c44123c6668d2c9c1eb1b2fbb",
        11,
    ),
    "actual-tests/LM_ZW_CAP_SLICE_003_REFERENCE_CONTEXT.json": (
        "501e73dad98927165cba83e00d361b770b44afdf",
        11,
    ),
    "actual-tests/LM_ZW_CAP_SLICE_004_AMBIGUITY_WITHHOLDING.json": (
        "263f4bcf505d3f99c5f16918fdef8406456be775",
        9,
    ),
    "actual-tests/LM_ZW_CAP_SLICE_008_UNSEEN_CONSTRUCTIONS.json": (
        "30d063bc4a44acab532102f4dfa2288376badd0e",
        7,
    ),
    "actual-tests/LM_ZW_CAP_SLICE_012_MATHEMATICAL_LANGUAGE.json": (
        "535695ec27b5324e974f704b6a7edcc7b3ffc793",
        10,
    ),
    "actual-tests/LM_ZW_WHOLE_PATH_COMPOSITIONAL_EVAL_001.json": (
        "caaac9e61724b75090b8e40876685bc353e5a47a",
        6,
    ),
}


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise SystemExit(f"unable to read public LM snapshot JSON {path}: {exc}") from exc


def validate_manifest() -> None:
    manifest = load_json(MANIFEST)
    require(isinstance(manifest, dict), "LM snapshot manifest must be an object")
    manifest = dict(manifest)
    require(
        manifest.get("schema") == "EHCO_PUBLIC_LANGUAGE_MODEL_TEST_SNAPSHOT_MANIFEST_V1",
        "LM snapshot manifest schema drift",
    )
    require(manifest.get("fixture_count") == len(EXPECTED), "LM fixture count drift")
    require(
        manifest.get("case_count") == sum(item[1] for item in EXPECTED.values()),
        "LM aggregate case count drift",
    )
    fixtures = manifest.get("fixtures")
    require(isinstance(fixtures, list), "LM snapshot fixtures must be a list")
    listed = {
        entry.get("path"): (entry.get("git_blob_sha1"), entry.get("case_count"))
        for entry in fixtures
        if isinstance(entry, dict)
    }
    require(listed == EXPECTED, "LM snapshot manifest fixture identity drift")


def validate_fixtures() -> None:
    total_cases = 0
    for relative, (expected_blob, expected_cases) in EXPECTED.items():
        path = SNAPSHOT / relative
        require(path.is_file(), f"missing public LM fixture: {relative}")
        raw = path.read_bytes()
        require(
            git_blob_sha1(raw) == expected_blob,
            f"public LM fixture byte identity drift: {relative}",
        )
        document = load_json(path)
        require(isinstance(document, dict), f"LM fixture must be an object: {relative}")
        cases = document.get("cases")
        require(isinstance(cases, list), f"LM fixture cases must be a list: {relative}")
        require(len(cases) == expected_cases, f"LM fixture case count drift: {relative}")
        total_cases += len(cases)
    require(total_cases == 62, "LM public snapshot aggregate case count must remain 62")


def validate_public_boundary() -> None:
    required_files = (README, INDEX, MANIFEST, *(SNAPSHOT / path for path in EXPECTED))
    text_parts: list[str] = []
    for path in required_files:
        require(path.is_file(), f"missing public LM snapshot file: {path.relative_to(ROOT)}")
        text_parts.append(path.read_text(encoding="utf-8"))
    combined = "\n".join(text_parts)

    sensitive_markers = (
        "BEGIN PRIVATE KEY",
        "api_key=",
        "password=",
    )
    for needle in sensitive_markers:
        require(needle not in combined, f"public LM disclosure boundary marker detected: {needle}")

    # The public snapshot remains self-contained with respect to controlled source repositories.
    organization_repository_locator = re.compile(
        r"\bEHCOnomics-Systems/[A-Za-z0-9_.-]+\b",
        re.IGNORECASE,
    )
    require(
        organization_repository_locator.search(combined) is None,
        "controlled-source repository locator detected in public LM snapshot",
    )

    readme = README.read_text(encoding="utf-8")
    for statement in (
        "exact repository test-artifact evidence",
        "The broader Language Model maturity record is grounded in the current controlled source and qualification estate.",
        "This snapshot provides a public inspection window into that larger system.",
        "The historical whole-path fixture retains the evaluator semantics under which its expected dispositions were recorded.",
        "**Tier One Runtime authority and current Runtime state:** instantiated EHCO Runtime evidence.",
    ):
        require(statement in readme, f"LM snapshot README missing evidence-scope statement: {statement}")


def main() -> None:
    validate_manifest()
    validate_fixtures()
    validate_public_boundary()
    print("public LM test snapshot validation: PASS (7 fixtures, 62 cases)")


if __name__ == "__main__":
    main()
