#!/usr/bin/env python3
"""Validate the current EHCO AI-OS Runtime public-evidence route."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PACKET_SCHEMA = "EHCO_FULL_FLEX_PUBLIC_PACKET_V1"
EXPECTED_PACKET_SHA256 = "7F80C27D085AE871A00AED412C6F20EA9A76CB0677C93AEBA381CD1FD70EC8E5"
EXPECTED_ZIP_SHA256 = "DBF984B55731B5EA53C4D7F2A24F8CF4C0C4207E355EB8E6B1170113509F6B94"
EXPECTED_STANDING = "52/53"
EXPECTED_MATURITY = "REALIZED / COMPLETE_IN_ACCEPTED_SCOPE"
EXPECTED_PORTABILITY = "PRIMARY_ACCESSIBLE_RUNTIME_PROJECTION"

ERRORS: list[str] = []
CHECKS = 0


def checked(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        ERRORS.append(message)


def read(relative: str) -> str:
    path = ROOT / relative
    checked(path.is_file(), f"Required current Runtime evidence file missing: {relative}")
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
    root_readme = read("README.md")
    runtime_readme = read("runtime/README.md")
    evidence_readme = read("evidence/README.md")
    packet_index = read("evidence/runtime/full-flex/v1/README.md")
    detached_sha = read("evidence/runtime/full-flex/v1/EHCO_FULL_FLEX_PUBLIC_PACKET_V1.sha256").strip()
    diligence = read("TECHNICAL-DILIGENCE.md")
    release_register = read("releases/PUBLIC-RELEASE-REGISTER.md")
    public_record = load_json("evidence/runtime/full-flex/v1/PUBLIC_SAFE_RECORD.json")
    receipt = load_json("evidence/runtime/full-flex/v1/PACKET_RECEIPT.json")
    registry = load_json("assurance/PUBLIC-CLAIM-REGISTRY.json")

    raw_packet = ROOT / "evidence" / "runtime" / "full-flex" / "v1" / "EHCO_FULL_FLEX_PUBLIC_PACKET_V1.json"
    checked(not raw_packet.exists(), "Raw Full Flex packet must not remain in the current public tree")

    checked("EHCO AI-OS" in root_readme, "Root README does not identify EHCO AI-OS")
    checked("runtime/README.md" in root_readme, "Root README does not route to Runtime front door")
    checked("Full Flex" in root_readme, "Root README does not name Full Flex")

    checked(EXPECTED_MATURITY in runtime_readme, "Runtime front door maturity mismatch")
    checked(EXPECTED_STANDING in runtime_readme, "Runtime front door standing mismatch")
    checked(EXPECTED_PORTABILITY in runtime_readme, "Runtime front door portability classification mismatch")
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
    checked("CURRENT_PUBLIC_EVIDENCE_IDENTITY" in release_register, "Release register lacks current public evidence identity class")
    checked("Historical Public Evidence Companion Packets 00–08" in release_register, "Release register lacks historical companion classification")
    checked("Full Flex" in evidence_readme, "Evidence README lacks Full Flex route")

    public_combined = "\n".join([root_readme, runtime_readme, evidence_readme, packet_index, diligence, release_register, json.dumps(public_record), json.dumps(registry)])
    checked("1FydQKUNfpQ7oZrgpLDlqRHxFM_f1mFv5uq_akploL38" not in public_combined, "Private Drive control identifier exposed in current Runtime public surfaces")

    if ERRORS:
        print(f"EHCOsystem current Runtime evidence validation: FAIL ({len(ERRORS)} errors / {CHECKS} checks)")
        for error in ERRORS:
            print(f"- {error}")
        return 1

    print(f"EHCOsystem current Runtime evidence validation: PASS ({CHECKS} checks) [PUBLIC_SAFE_ACCEPTED_PACKET_IDENTITY]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
