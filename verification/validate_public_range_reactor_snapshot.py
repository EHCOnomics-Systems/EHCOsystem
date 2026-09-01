#!/usr/bin/env python3
"""Validate the EHCO Range Reactor public capability snapshot and current public representation."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RR_ROOT = ROOT / "range-reactor"
SNAPSHOT = RR_ROOT / "evidence" / "public-capability-snapshot-v1"
MANIFEST = SNAPSHOT / "MANIFEST.json"
VECTORS = SNAPSHOT / "capability-vectors.json"
EXPECTED_SOURCE_REVISION = "2ab887e1e82c2c5422223fbd862b288c8c63ee27"
EXPECTED_VECTOR_SHA256 = "612389A01DA53688CCB0276D0633A3CEA757517DAC736615D089D597424762D1"
EXPECTED_CAPABILITIES = {
    "deterministic_replay",
    "contradiction_preservation",
    "frontier_preservation",
    "possible_vs_inevitable",
    "collapse_with_witness_fibers",
    "independent_collapse_verification",
    "source_mutation_identity_sensitivity",
    "proof_custody_and_grounded_discharge",
}
PUBLIC_SURFACES = [
    "README.md",
    "LIBRARY.md",
    "ECOSYSTEM-DILIGENCE.md",
    "getting-started/START-HERE.md",
    "architecture/EHCO-TECHNOLOGY-ESTATE.md",
    "architecture/ecosystem-components-and-participation.md",
    "architecture/diagrams/README.md",
    "assurance/ECOSYSTEM-CLAIM-EVIDENCE-MATRIX.md",
    "verification/README.md",
    "range-reactor/README.md",
    "range-reactor/evidence/public-capability-snapshot-v1/README.md",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def read_text(relative: str) -> str:
    path = ROOT / relative
    require(path.is_file(), f"missing Range Reactor public surface: {relative}")
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict[str, object]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise SystemExit(f"unable to read Range Reactor public JSON {path}: {exc}") from exc
    require(isinstance(value, dict), f"Range Reactor public JSON must be an object: {path}")
    return value


def validate_snapshot() -> None:
    manifest = load_json(MANIFEST)
    vectors = load_json(VECTORS)
    require(manifest.get("schema") == "EHCO_PUBLIC_RANGE_REACTOR_CAPABILITY_SNAPSHOT_MANIFEST_V1", "RR manifest schema drift")
    require(manifest.get("snapshot_id") == "EHCO-RR-PUBLIC-CAPABILITY-SNAPSHOT-V1", "RR snapshot identity drift")
    require(manifest.get("owning_source_revision") == EXPECTED_SOURCE_REVISION, "RR accepted source-review revision drift")
    require(manifest.get("evidence_class") == "SOURCE_REVIEWED_SYNTHETIC_CAPABILITY_EVIDENCE", "RR evidence class drift")
    require(manifest.get("fixture_count") == 1 and manifest.get("case_count") == 8, "RR manifest count drift")
    raw = VECTORS.read_bytes()
    require(hashlib.sha256(raw).hexdigest().upper() == EXPECTED_VECTOR_SHA256, "RR capability vector SHA-256 drift")
    cases = vectors.get("cases")
    require(isinstance(cases, list) and len(cases) == 8, "RR capability vector count drift")
    capabilities = {case.get("capability") for case in cases if isinstance(case, dict)}
    require(capabilities == EXPECTED_CAPABILITIES, "RR capability category drift")
    ids = [case.get("id") for case in cases if isinstance(case, dict)]
    require(ids == [f"RR-PUB-{index:03d}" for index in range(1, 9)], "RR public vector identity drift")
    fixtures = manifest.get("fixtures")
    require(isinstance(fixtures, list) and len(fixtures) == 1, "RR fixture manifest structure drift")
    entry = fixtures[0]
    require(isinstance(entry, dict), "RR fixture manifest entry invalid")
    require(entry.get("path") == "capability-vectors.json", "RR fixture path drift")
    require(entry.get("sha256") == EXPECTED_VECTOR_SHA256, "RR manifest fixture hash drift")


def validate_public_representation() -> None:
    texts = {relative: read_text(relative) for relative in PUBLIC_SURFACES}
    combined = "\n".join(texts.values())

    required = {
        "README.md": ["mature deterministic proof-carrying implication", "Public Capability Snapshot v1", "14.304307x"],
        "range-reactor/README.md": ["proof-carrying implication, reachability, range, and reasoning system", "14.304307x wall-clock improvement", "82 passed / 0 failed", "Public Capability Snapshot v1"],
        "architecture/EHCO-TECHNOLOGY-ESTATE.md": ["mature deterministic proof-carrying implication, reachability, range, and reasoning system", "14.304307x wall-clock improvement"],
        "architecture/ecosystem-components-and-participation.md": ["mature deterministic proof-carrying implication, reachability, range, and reasoning", "14.304307x wall-clock"],
        "assurance/ECOSYSTEM-CLAIM-EVIDENCE-MATRIX.md": ["EHCO Range Reactor", "14.304307x wall", "82 passed / 0 failed"],
        "verification/README.md": ["validate_public_range_reactor_snapshot.py", "Range Reactor capability snapshot"],
        "LIBRARY.md": ["Public Capability Snapshot v1"],
        "getting-started/START-HERE.md": ["EHCO Range Reactor", "14.304307x wall-clock improvement"],
    }
    for relative, phrases in required.items():
        for phrase in phrases:
            require(phrase in texts[relative], f"Range Reactor public representation missing in {relative}: {phrase}")

    controlled_locator = re.compile(r"\bEHCOnomics-Systems/EHCO_Range_Reactor\b", re.IGNORECASE)
    require(controlled_locator.search(combined) is None, "controlled Range Reactor repository locator present in reader-facing public text")
    require("refs/heads/" not in combined, "Range Reactor branch choreography present in public representation")

    for phrase in (
        "Range Reactor is a Runtime participant",
        "Range Reactor is production deployed",
        "Range Reactor is Runtime-admitted",
        "Range Reactor owns Runtime authority",
    ):
        require(phrase not in combined, f"Range Reactor lifecycle/authority overclaim detected: {phrase}")


def validate_disclosure_boundary() -> None:
    combined = "\n".join((MANIFEST.read_text(encoding="utf-8"), VECTORS.read_text(encoding="utf-8"), read_text("range-reactor/evidence/public-capability-snapshot-v1/README.md")))
    require("EHCOnomics-Systems/" not in combined, "controlled repository locator detected in RR snapshot")
    for marker in ("BEGIN PRIVATE KEY", "api_key=", "password=", "github_pat_"):
        require(marker not in combined, f"RR snapshot disclosure marker detected: {marker}")


def main() -> None:
    validate_snapshot()
    validate_public_representation()
    validate_disclosure_boundary()
    print("public Range Reactor capability snapshot validation: PASS (8 vectors)")


if __name__ == "__main__":
    main()
