#!/usr/bin/env python3
"""Validate SOW-008 canonical public claims and representation invariants."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "assurance" / "PUBLIC-CLAIM-REGISTRY.json"

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
    checked(registry.get("registry_version") == "1.0.0", "Claim registry version mismatch")
    checked(registry.get("source_review_date") == "2026-08-29", "Claim registry source-review date mismatch")

    claims = registry.get("claims", [])
    checked(isinstance(claims, list), "Claim registry claims must be a list")
    by_id = {
        item.get("claim_id"): item
        for item in claims
        if isinstance(item, dict) and isinstance(item.get("claim_id"), str)
    }

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
            statement = str(by_id[claim_id].get("public_statement", ""))
            checked(phrase in statement, f"Required public claim wording missing for {claim_id}: {phrase}")
            checked(by_id[claim_id].get("status") == "ESTABLISHED", f"Claim status mismatch: {claim_id}")
            checked(bool(by_id[claim_id].get("evidence_class")), f"Evidence class missing: {claim_id}")
            checked(bool(by_id[claim_id].get("verification_method")), f"Verification method missing: {claim_id}")
            checked(bool(by_id[claim_id].get("disclosure_ceiling")), f"Disclosure ceiling missing: {claim_id}")

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

    readme = public_files["README.md"]
    system_card = public_files["AI-OS System Card"]
    technology = public_files["Technology Estate"]
    technical_diligence = public_files["Technical Diligence"]
    ecosystem_matrix = public_files["Ecosystem Claim Matrix"]

    for label, text in public_files.items():
        checked("EHCOnomics-Systems/EHCO_AI-OS" not in text, f"Protected AI-OS source locator in {label}")
        checked("EHCOnomics-Systems/EHCO_Range_Reactor" not in text, f"Protected Range Reactor source locator in {label}")
        checked("drive.google.com" not in text, f"Drive locator in {label}")
        checked("DESKTOP-" not in text, f"Private host identifier in {label}")
        checked("C:\\" not in text, f"Private host path in {label}")
        checked("Azure" not in text, f"Private cloud-provider lineage name in {label}")

    required_readme = [
        "EHCO AI-OS is the realized Tier One Runtime",
        "fully containerized, deployment-ready portable delivery form",
        "self-hosted local Docker Runtime",
        "host port 8080",
        "assurance/PUBLIC-CLAIM-REGISTRY.json",
    ]
    for phrase in required_readme:
        checked(phrase in readme, f"README final-closeout representation missing: {phrase}")

    checked(readme.count("operating local EHCO Docker Runtime") >= 2, "README local Dashboard-origin captions incomplete")
    checked(system_card.count("operating local EHCO Docker Runtime") >= 6, "System Card local Dashboard-origin captions incomplete")

    for phrase in [
        "fully containerized, deployment-ready portable delivery form",
        "self-hosted local Docker Runtime",
        "host port 8080",
    ]:
        checked(phrase in technology, f"Technology Estate final-closeout representation missing: {phrase}")

    for phrase in [
        "496,898,804-byte / 2,605,233-line",
        "6.847 seconds",
        "58.458 ms median",
        "110.213 ms p95",
        "213.075 ms maximum",
        "15.199 requests/second",
        "separate workloads",
    ]:
        checked(phrase in technical_diligence, f"Technical Diligence characterization wording missing: {phrase}")
        checked(phrase in ecosystem_matrix or phrase == "separate workloads", f"Ecosystem matrix characterization wording missing: {phrase}")

    registry_text = json.dumps(registry, sort_keys=True)
    for forbidden in [
        "EHCOnomics-Systems/EHCO_AI-OS",
        "EHCOnomics-Systems/EHCO_Range_Reactor",
        "drive.google.com",
        "DESKTOP-",
        "C:\\\\",
        "Azure",
    ]:
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
