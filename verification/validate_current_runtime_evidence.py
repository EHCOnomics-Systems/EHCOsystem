#!/usr/bin/env python3
"""Validate the current EHCO AI-OS Runtime public-evidence front door."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PACKET_SCHEMA = "EHCO_FULL_FLEX_PUBLIC_PACKET_V1"
EXPECTED_PACKET_SHA256 = "7F80C27D085AE871A00AED412C6F20EA9A76CB0677C93AEBA381CD1FD70EC8E5"
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


def main() -> int:
    root_readme = read("README.md")
    runtime_readme = read("runtime/README.md")
    evidence_readme = read("evidence/README.md")
    packet_index = read("evidence/runtime/full-flex/v1/README.md")
    detached_sha = read("evidence/runtime/full-flex/v1/EHCO_FULL_FLEX_PUBLIC_PACKET_V1.sha256").strip()
    diligence = read("TECHNICAL-DILIGENCE.md")
    release_register = read("releases/PUBLIC-RELEASE-REGISTER.md")

    registry_path = ROOT / "assurance" / "PUBLIC-CLAIM-REGISTRY.json"
    checked(registry_path.is_file(), "Canonical public claim registry missing")
    try:
        registry = json.loads(registry_path.read_text(encoding="utf-8-sig"))
    except Exception as exc:
        ERRORS.append(f"Claim registry parse failure: {exc}")
        registry = {}

    for label, text in {
        "README.md": root_readme,
        "runtime/README.md": runtime_readme,
        "evidence/README.md": evidence_readme,
        "Full Flex evidence index": packet_index,
        "TECHNICAL-DILIGENCE.md": diligence,
        "PUBLIC-RELEASE-REGISTER.md": release_register,
    }.items():
        checked(EXPECTED_PACKET_SHA256 in text or label == "README.md", f"Current Full Flex packet hash missing from {label}")

    checked("Current EHCO AI-OS Runtime evidence — start here" in root_readme, "Root README does not expose current Runtime evidence first")
    checked("runtime/README.md" in root_readme, "Root README does not route to Runtime front door")
    checked("Full Flex" in root_readme, "Root README does not name Full Flex current evidence")

    checked("canonical first public evidence route" in runtime_readme, "Runtime front door does not establish current-evidence precedence")
    checked(EXPECTED_MATURITY in runtime_readme, "Runtime front door maturity mismatch")
    checked(EXPECTED_STANDING in runtime_readme, "Runtime front door standing mismatch")
    checked(EXPECTED_PORTABILITY in runtime_readme, "Runtime front door portability classification mismatch")
    checked("Packet 06 is a historical bounded observation window" in runtime_readme, "Runtime front door does not preserve Packet 06 historical classification")
    checked("Full Flex packet" in runtime_readme, "Runtime front door does not identify Full Flex current packet")

    checked(EXPECTED_PACKET_SCHEMA in packet_index, "Full Flex evidence index schema mismatch")
    checked("historical/event-time evidence" in packet_index, "Full Flex evidence index does not preserve historical packet lineage")
    checked("../../../../runtime/README.md" in packet_index, "Full Flex index Runtime-front-door link mismatch")
    checked("../../../public-evidence-companion/v1/" in packet_index, "Full Flex index historical companion link mismatch")

    expected_sha_line = f"{EXPECTED_PACKET_SHA256}  EHCO_FULL_FLEX_PUBLIC_PACKET_V1.json"
    checked(detached_sha == expected_sha_line, "Detached Full Flex SHA-256 identity mismatch")

    checked("## 1. Current Runtime evidence — Full Flex first" in diligence, "Technical Diligence does not place Full Flex first")
    checked("## 3. Historical observed run — Packet 06" in diligence, "Technical Diligence does not classify Packet 06 as historical")
    full_flex_pos = diligence.find("## 1. Current Runtime evidence — Full Flex first")
    packet06_pos = diligence.find("## 3. Historical observed run — Packet 06")
    checked(full_flex_pos >= 0 and packet06_pos > full_flex_pos, "Technical Diligence reviewer order does not place current Full Flex before Packet 06")

    current = registry.get("current_runtime_evidence", {}) if isinstance(registry, dict) else {}
    checked(current.get("front_door") == "runtime/README.md", "Claim registry current Runtime front door mismatch")
    checked(current.get("packet_index") == "evidence/runtime/full-flex/v1/README.md", "Claim registry Full Flex index mismatch")
    checked(current.get("packet_schema") == EXPECTED_PACKET_SCHEMA, "Claim registry Full Flex schema mismatch")
    checked(current.get("packet_sha256") == EXPECTED_PACKET_SHA256, "Claim registry Full Flex packet hash mismatch")
    checked(current.get("runtime_maturity") == EXPECTED_MATURITY, "Claim registry Runtime maturity mismatch")
    checked(current.get("accepted_standing") == EXPECTED_STANDING, "Claim registry accepted standing mismatch")
    checked(current.get("docker_portability") == EXPECTED_PORTABILITY, "Claim registry portability classification mismatch")
    checked("CURRENT_FULL_FLEX_FIRST" in str(current.get("precedence", "")), "Claim registry precedence does not place current Full Flex first")
    checked("HISTORICAL_EVENT_TIME_LINEAGE" in str(current.get("precedence", "")), "Claim registry precedence does not preserve historical packet lineage")

    checked("CURRENT_PUBLIC_EVIDENCE_IDENTITY" in release_register, "Release register lacks current public evidence identity class")
    checked("Historical Public Evidence Companion Packets 00–08" in release_register, "Release register lacks historical companion classification")

    packet_path = ROOT / "evidence" / "runtime" / "full-flex" / "v1" / "EHCO_FULL_FLEX_PUBLIC_PACKET_V1.json"
    if packet_path.exists():
        digest = hashlib.sha256(packet_path.read_bytes()).hexdigest().upper()
        checked(digest == EXPECTED_PACKET_SHA256, f"Published Full Flex packet SHA-256 mismatch: {digest}")
        try:
            packet = json.loads(packet_path.read_text(encoding="utf-8-sig"))
        except Exception as exc:
            ERRORS.append(f"Published Full Flex packet JSON parse failure: {exc}")
            packet = {}
        checked(packet.get("schema") == EXPECTED_PACKET_SCHEMA, "Published Full Flex packet schema mismatch")
    else:
        checked("exact packet JSON is inserted here only when the byte-identical owning-host artifact is available" in packet_index, "Absent packet bytes are not explicitly protected by exact-byte custody language")

    if ERRORS:
        print(f"EHCOsystem current Runtime evidence validation: FAIL ({len(ERRORS)} errors / {CHECKS} checks)")
        for error in ERRORS:
            print(f"- {error}")
        return 1

    publication = "BYTE_EXACT_PACKET_PRESENT" if packet_path.exists() else "IDENTITY_AND_PRECEDENCE_PRESENT_EXACT_BYTES_PENDING"
    print(f"EHCOsystem current Runtime evidence validation: PASS ({CHECKS} checks) [{publication}]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
