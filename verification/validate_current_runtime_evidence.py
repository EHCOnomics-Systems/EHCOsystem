#!/usr/bin/env python3
"""Validate the accepted EHCO AI-OS Runtime public-evidence route and durable public semantics."""

from __future__ import annotations

import json
from pathlib import Path

from public_disclosure_policy import find_disclosure_violations, run_synthetic_policy_self_test

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PACKET_SCHEMA = "EHCO_FULL_FLEX_PUBLIC_PACKET_V1"
EXPECTED_PACKET_SHA256 = "7F80C27D085AE871A00AED412C6F20EA9A76CB0677C93AEBA381CD1FD70EC8E5"
EXPECTED_ZIP_SHA256 = "DBF984B55731B5EA53C4D7F2A24F8CF4C0C4207E355EB8E6B1170113509F6B94"
EXPECTED_STANDING = "52/53"
EXPECTED_MATURITY = "REALIZED / COMPLETE_IN_ACCEPTED_SCOPE"
EXPECTED_PORTABILITY = "PRIMARY_ACCESSIBLE_RUNTIME_PROJECTION"
EXPECTED_RUNTIME_FRONT_DOOR_TITLE = "EHCO AI-OS Runtime — Accepted Public Evidence"
RUNTIME_AUTHORITY_OWNER = "INSTANTIATED_EHCO_RUNTIME"

ERRORS: list[str] = []
CHECKS = 0


def checked(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        ERRORS.append(message)


def read(relative: str) -> str:
    path = ROOT / relative
    checked(path.is_file(), f"Required Runtime/public-semantics file missing: {relative}")
    return path.read_text(encoding="utf-8-sig") if path.is_file() else ""


def load_json(relative: str) -> dict:
    text = read(relative)
    try:
        value = json.loads(text)
    except Exception as exc:
        ERRORS.append(f"JSON parse failure for {relative}: {exc}")
        return {}
    checked(isinstance(value, dict), f"JSON object expected: {relative}")
    return value if isinstance(value, dict) else {}


def main() -> int:
    try:
        run_synthetic_policy_self_test()
        checked(True, "Public disclosure policy synthetic self-test failed")
    except AssertionError as exc:
        checked(False, f"Public disclosure policy synthetic self-test failed: {exc}")

    root_readme = read("README.md")
    runtime_readme = read("runtime/README.md")
    evidence_readme = read("evidence/README.md")
    packet_index = read("evidence/runtime/full-flex/v1/README.md")
    detached_sha = read("evidence/runtime/full-flex/v1/EHCO_FULL_FLEX_PUBLIC_PACKET_V1.sha256").strip()
    diligence = read("TECHNICAL-DILIGENCE.md")
    ecosystem_diligence = read("ECOSYSTEM-DILIGENCE.md")
    release_register = read("releases/PUBLIC-RELEASE-REGISTER.md")
    notice = read("NOTICE.md")
    start_here = read("getting-started/START-HERE.md")
    reading_order = read("getting-started/reading-order.md")
    library = read("LIBRARY.md")
    instantiated_ai = read("architecture/INSTANTIATED-AI.md")
    technology_estate = read("architecture/EHCO-TECHNOLOGY-ESTATE.md")
    system_card = read("architecture/EHCO-AI-OS-SYSTEM-CARD.md")
    instantiated_system = read("architecture/EHCO-AI-OS-INSTANTIATED-SYSTEM.md")
    governed_runtime = read("architecture/GOVERNED-RUNTIME-ARCHITECTURE.md")
    proof_range = read("architecture/instantiated-proof-range.md")
    runtime_boundary = read("architecture/runtime-repository-and-test-estate-boundary.md")
    diagrams = read("architecture/diagrams/README.md")
    claim_matrix = read("assurance/CLAIM-EVIDENCE-MATRIX.md")
    public_record = load_json("evidence/runtime/full-flex/v1/PUBLIC_SAFE_RECORD.json")
    receipt = load_json("evidence/runtime/full-flex/v1/PACKET_RECEIPT.json")
    registry = load_json("assurance/PUBLIC-CLAIM-REGISTRY.json")

    raw_packet = ROOT / "evidence" / "runtime" / "full-flex" / "v1" / "EHCO_FULL_FLEX_PUBLIC_PACKET_V1.json"
    checked(not raw_packet.exists(), "Raw Full Flex packet must not remain in the public tree")

    checked("EHCO AI-OS" in root_readme, "Root README does not identify EHCO AI-OS")
    checked("runtime/README.md" in root_readme, "Root README does not route to Runtime front door")
    checked("Full Flex" in root_readme, "Root README does not name Full Flex")

    checked(EXPECTED_RUNTIME_FRONT_DOOR_TITLE in runtime_readme, "Runtime front door title is not resting-state durable")
    checked(EXPECTED_MATURITY in runtime_readme, "Runtime front door maturity mismatch")
    checked(EXPECTED_STANDING in runtime_readme, "Runtime front door standing mismatch")
    checked(EXPECTED_PORTABILITY in runtime_readme, "Runtime front door portability classification mismatch")
    checked(RUNTIME_AUTHORITY_OWNER in runtime_readme, "Runtime front door does not identify the Runtime authority/state owner")
    checked("public-safe" in runtime_readme.lower(), "Runtime front door does not describe the public-safe Full Flex route")

    checked(EXPECTED_PACKET_SCHEMA in packet_index, "Full Flex evidence index schema mismatch")
    checked(EXPECTED_PACKET_SHA256 in packet_index, "Full Flex evidence index packet hash mismatch")
    checked(EXPECTED_ZIP_SHA256 in packet_index, "Full Flex evidence index ZIP hash mismatch")
    checked("PUBLIC_SAFE_RECORD.json" in packet_index, "Full Flex evidence index does not expose public-safe record")
    checked("historical/event-time evidence" in packet_index, "Full Flex index does not preserve historical packet lineage")

    expected_sha_line = f"{EXPECTED_PACKET_SHA256}  EHCO_FULL_FLEX_PUBLIC_PACKET_V1.json"
    checked(detached_sha == expected_sha_line, "Detached accepted Full Flex packet identity mismatch")

    accepted_packet = public_record.get("accepted_packet", {})
    checked(public_record.get("schema") == "EHCO_FULL_FLEX_PUBLIC_SAFE_RECORD_V1", "Full Flex public-safe record schema mismatch")
    checked(accepted_packet.get("schema") == EXPECTED_PACKET_SCHEMA, "Full Flex public-safe accepted schema mismatch")
    checked(accepted_packet.get("sha256") == EXPECTED_PACKET_SHA256, "Full Flex public-safe accepted packet hash mismatch")
    checked(accepted_packet.get("clean_package_zip_sha256") == EXPECTED_ZIP_SHA256, "Full Flex public-safe ZIP hash mismatch")
    runtime = public_record.get("runtime", {})
    checked(runtime.get("maturity") == EXPECTED_MATURITY, "Full Flex public-safe Runtime maturity mismatch")
    checked(runtime.get("accepted_standing") == EXPECTED_STANDING, "Full Flex public-safe standing mismatch")
    checked(public_record.get("portable_delivery", {}).get("classification") == EXPECTED_PORTABILITY, "Full Flex public-safe portability mismatch")
    checked(public_record.get("public_custody", {}).get("raw_packet_bytes") == "WITHHELD_FROM_CURRENT_PUBLIC_TREE_TO_PROTECT_INTERNAL_SOURCE_ROUTING_METADATA", "Full Flex public-safe raw-byte custody mismatch")

    checked(receipt.get("packet_sha256") == EXPECTED_PACKET_SHA256, "Full Flex receipt packet hash mismatch")
    checked(receipt.get("runtime_standing") == EXPECTED_STANDING, "Full Flex receipt standing mismatch")
    checked(receipt.get("docker_portability") == EXPECTED_PORTABILITY, "Full Flex receipt portability mismatch")

    current = registry.get("current_runtime_evidence", {})
    checked(current.get("front_door") == "runtime/README.md", "Claim registry Runtime front door mismatch")
    checked(current.get("packet_index") == "evidence/runtime/full-flex/v1/README.md", "Claim registry Full Flex index mismatch")
    checked(current.get("public_safe_record") == "evidence/runtime/full-flex/v1/PUBLIC_SAFE_RECORD.json", "Claim registry public-safe record mismatch")
    checked(current.get("packet_schema") == EXPECTED_PACKET_SCHEMA, "Claim registry Full Flex schema mismatch")
    checked(current.get("packet_sha256") == EXPECTED_PACKET_SHA256, "Claim registry Full Flex packet hash mismatch")
    checked(current.get("runtime_maturity") == EXPECTED_MATURITY, "Claim registry Runtime maturity mismatch")
    checked(current.get("accepted_standing") == EXPECTED_STANDING, "Claim registry accepted standing mismatch")
    checked(current.get("docker_portability") == EXPECTED_PORTABILITY, "Claim registry portability mismatch")
    checked(current.get("public_custody") == "ACCEPTED_PACKET_HASH_AND_RECEIPT_WITH_PUBLIC_SAFE_RECORD", "Claim registry public custody mismatch")

    checked("Full Flex" in diligence, "Technical Diligence does not retain Full Flex route")
    checked("CURRENT_PUBLIC_EVIDENCE_IDENTITY" in release_register, "Release register lacks selected public evidence identity class")
    checked("Historical Public Evidence Companion Packets 00–08" in release_register, "Release register lacks historical companion classification")
    checked("Full Flex" in evidence_readme, "Evidence README lacks Full Flex route")

    reader_semantics = "\n".join(
        [
            root_readme,
            runtime_readme,
            evidence_readme,
            packet_index,
            diligence,
            ecosystem_diligence,
            notice,
            start_here,
            reading_order,
            library,
            instantiated_ai,
            technology_estate,
            system_card,
            instantiated_system,
            governed_runtime,
            proof_range,
            runtime_boundary,
            diagrams,
            claim_matrix,
        ]
    )
    forbidden_reader_phrases = {
        "current public evidence projection and synthesis": "Residual Full Flex synthesis wording remains",
        "current public capability-and-evidence synthesis": "Residual Full Flex capability-synthesis wording remains",
        "public synthesis role": "Residual Full Flex synthesis-role wording remains",
        "EHCO AI-OS owns the governing Runtime relationships": "EHCO AI-OS is still presented as the Runtime authority owner",
        "EHCO AI-OS owns:\n\n- admission and standing": "EHCO AI-OS authority-owner collapse remains in Tier One relationship prose",
        "exact packet-byte insertion awaits lawful byte custody": "Stale Full Flex exact-byte custody wording remains",
        "scoped Runtime participation relationship are independently tracked": "Language Model Runtime participation is still implied without owning evidence",
        "EHCO AI-OS Runtime — Current Public Evidence": "Volatile Runtime front-door label remains in active reader-facing prose",
    }
    lower_reader_semantics = reader_semantics.lower()
    for phrase, message in forbidden_reader_phrases.items():
        checked(phrase.lower() not in lower_reader_semantics, message)

    checked(RUNTIME_AUTHORITY_OWNER in root_readme, "Root README does not separate Runtime identity from authority/state ownership")
    checked(RUNTIME_AUTHORITY_OWNER in instantiated_ai, "Instantiated AI page does not identify Runtime authority/state owner")
    checked(RUNTIME_AUTHORITY_OWNER in technology_estate, "Technology Estate does not identify Runtime authority/state owner")
    checked(RUNTIME_AUTHORITY_OWNER in diagrams, "Architecture diagrams do not identify Runtime authority/state owner")

    disclosure_inputs = {
        "Runtime reader surfaces": reader_semantics,
        "Release register": release_register,
        "Runtime public-safe record": json.dumps(public_record, sort_keys=True),
        "Public claim registry": json.dumps(registry, sort_keys=True),
    }
    for source, text in disclosure_inputs.items():
        violations = find_disclosure_violations(text, source)
        checked(not violations, f"Protected source/topology information exposed in {source}")

    if ERRORS:
        print(f"EHCOsystem accepted Runtime evidence validation: FAIL ({len(ERRORS)} errors / {CHECKS} checks)")
        for error in ERRORS:
            print(f"- {error}")
        return 1

    print(f"EHCOsystem accepted Runtime evidence validation: PASS ({CHECKS} checks) [PUBLIC_SAFE_ACCEPTED_PACKET_IDENTITY / DURABLE_PUBLIC_SEMANTICS]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
