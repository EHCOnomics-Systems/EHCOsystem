#!/usr/bin/env python3
"""Validate the canonical public claim registry and closeout representation invariants."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "assurance" / "PUBLIC-CLAIM-REGISTRY.json"
EXPECTED_PACKET_SHA256 = "7F80C27D085AE871A00AED412C6F20EA9A76CB0677C93AEBA381CD1FD70EC8E5"
EXPECTED_BASE = "2ee2eb0ac9cdf2c257a48460b8e83fda70b87952"
ERRORS: list[str] = []
CHECKS = 0


def checked(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        ERRORS.append(message)


def read(relative: str) -> str:
    path = ROOT / relative
    checked(path.is_file(), f"Required public file missing: {relative}")
    return path.read_text(encoding="utf-8-sig") if path.is_file() else ""


def main() -> int:
    checked(REGISTRY.is_file(), "Canonical public claim registry missing")
    try:
        registry = json.loads(REGISTRY.read_text(encoding="utf-8-sig"))
    except Exception as exc:
        ERRORS.append(f"Claim registry parse failure: {exc}")
        registry = {}

    checked(registry.get("schema") == "ehco.public.claim-registry.v1", "Claim registry schema mismatch")
    checked(registry.get("registry_version") == "1.1.0", "Claim registry version mismatch")
    checked(registry.get("published") == "2026-08-30", "Claim registry publication date mismatch")
    checked(registry.get("source_review_date") == "2026-08-30", "Claim registry source-review date mismatch")
    checked(registry.get("public_repository_base") == EXPECTED_BASE, "Claim registry accepted source-base mismatch")

    standing = registry.get("standing_interpretation", {})
    checked(standing.get("accepted_standing") == "52/53", "Standing interpretation mismatch")
    checked("numerical Runtime standing corridor" in str(standing.get("public_meaning", "")), "Standing interpretation is not bounded as a Runtime standing corridor")
    not_equivalent = standing.get("not_equivalent_to", [])
    for value in ["benchmark score", "percentage completion", "component maturity percentage", "deployment-state percentage", "public-release percentage"]:
        checked(value in not_equivalent, f"Standing non-equivalence missing: {value}")
    checked(standing.get("protected_denominator_mechanics") == "NOT_PUBLICLY_INFERRED_OR_EXPANDED", "Protected standing mechanics boundary missing")

    current = registry.get("current_runtime_evidence", {})
    checked(current.get("front_door") == "runtime/README.md", "Current Runtime front door mismatch")
    checked(current.get("packet_index") == "evidence/runtime/full-flex/v1/README.md", "Full Flex packet index mismatch")
    checked(current.get("packet_schema") == "EHCO_FULL_FLEX_PUBLIC_PACKET_V1", "Full Flex packet schema mismatch")
    checked(current.get("packet_sha256") == EXPECTED_PACKET_SHA256, "Full Flex packet hash mismatch")
    checked(current.get("runtime_maturity") == "REALIZED / COMPLETE_IN_ACCEPTED_SCOPE", "Runtime maturity mismatch")
    checked(current.get("accepted_standing") == "52/53", "Accepted standing mismatch")
    checked(current.get("docker_portability") == "PRIMARY_ACCESSIBLE_RUNTIME_PROJECTION", "Docker portability classification mismatch")
    checked("CURRENT_FULL_FLEX_FIRST" in str(current.get("precedence", "")), "Full Flex-first precedence missing")
    checked("HISTORICAL_EVENT_TIME_LINEAGE" in str(current.get("precedence", "")), "Historical packet lineage classification missing")

    claims = registry.get("claims", [])
    checked(isinstance(claims, list), "Claim registry claims must be a list")
    by_id = {item.get("claim_id"): item for item in claims if isinstance(item, dict)}
    required_claims = {
        "AIOS-RUNTIME-REALIZED": "realized Tier One Runtime",
        "AIOS-COMPLETE-ACCEPTED-SCOPE": "REALIZED / COMPLETE_IN_ACCEPTED_SCOPE",
        "AIOS-PORTABILITY-DEPLOYMENT-READY": "fully containerized, deployment-ready portable delivery form",
        "AIOS-LOCAL-RUNTIME-PROVEN": "self-hosted local Docker Runtime",
        "AIOS-LOCAL-DASHBOARD-PROVEN": "host port 8080",
        "AIOS-TIER1-MODEL-INDEPENDENT-OPERATION": "external-model seam disabled",
        "AIOS-PERFORMANCE-CHARACTERIZATION": "6.847-second",
        "RR-MATURE": "mature deterministic proof-carrying",
        "RR-PHYSICAL-QUALIFICATION": "physical service execution",
        "RR-PERFORMANCE": "58.458 ms median",
    }
    for claim_id, phrase in required_claims.items():
        checked(claim_id in by_id, f"Required public claim missing: {claim_id}")
        if claim_id in by_id:
            item = by_id[claim_id]
            checked(phrase in str(item.get("public_statement", "")), f"Required wording missing for {claim_id}: {phrase}")
            checked(item.get("status") == "ESTABLISHED", f"Claim status mismatch: {claim_id}")
            checked(bool(item.get("evidence_class")), f"Evidence class missing: {claim_id}")
            checked(bool(item.get("verification_method")), f"Verification method missing: {claim_id}")
            checked(bool(item.get("disclosure_ceiling")), f"Disclosure ceiling missing: {claim_id}")

    public_files = {
        "README.md": read("README.md"),
        "Start Here": read("getting-started/START-HERE.md"),
        "Technology Estate": read("architecture/EHCO-TECHNOLOGY-ESTATE.md"),
        "AI-OS System Card": read("architecture/EHCO-AI-OS-SYSTEM-CARD.md"),
        "Technical Diligence": read("TECHNICAL-DILIGENCE.md"),
        "Ecosystem Diligence": read("ECOSYSTEM-DILIGENCE.md"),
        "AI-OS Claim Matrix": read("assurance/CLAIM-EVIDENCE-MATRIX.md"),
        "Ecosystem Claim Matrix": read("assurance/ECOSYSTEM-CLAIM-EVIDENCE-MATRIX.md"),
        "Evidence README": read("evidence/README.md"),
        "Verification README": read("verification/README.md"),
    }

    for label, text in public_files.items():
        for forbidden in ["EHCOnomics-Systems/EHCO_AI-OS", "EHCOnomics-Systems/EHCO_Range_Reactor", "drive.google.com", "DESKTOP-", "C:\\", "Azure"]:
            checked(forbidden not in text, f"Protected locator/lineage token in {label}: {forbidden}")

    start_here = public_files["Start Here"]
    checked("Current EHCO AI-OS Runtime — start here" in start_here, "Start Here does not put current Runtime evidence first")
    checked("Benchmark scoring, percentage-completion measures" in start_here, "Start Here lacks bounded 52/53 interpretation")

    technical_diligence = public_files["Technical Diligence"]
    ecosystem_matrix = public_files["Ecosystem Claim Matrix"]
    for phrase in ["496,898,804-byte / 2,605,233-line", "6.847 seconds", "58.458 ms median", "110.213 ms p95", "213.075 ms maximum", "15.199 requests/second"]:
        checked(phrase in technical_diligence, f"Technical Diligence characterization wording missing: {phrase}")
        checked(phrase in ecosystem_matrix, f"Ecosystem matrix characterization wording missing: {phrase}")

    registry_text = json.dumps(registry, sort_keys=True)
    for forbidden in ["EHCOnomics-Systems/EHCO_AI-OS", "EHCOnomics-Systems/EHCO_Range_Reactor", "drive.google.com", "DESKTOP-", "C:\\\\", "Azure"]:
        checked(forbidden not in registry_text, f"Protected locator/lineage token in claim registry: {forbidden}")

    if ERRORS:
        print(f"EHCOsystem public claim-registry validation: FAIL ({len(ERRORS)} errors / {CHECKS} checks)")
        for error in ERRORS:
            print(f"- {error}")
        return 1

    print(f"EHCOsystem public claim-registry validation: PASS ({CHECKS} checks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
