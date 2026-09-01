#!/usr/bin/env python3
"""Validate canonical public claims and resting-state presentation boundaries."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "assurance" / "PUBLIC-CLAIM-REGISTRY.json"
EXPECTED_PACKET_SHA256 = "7F80C27D085AE871A00AED412C6F20EA9A76CB0677C93AEBA381CD1FD70EC8E5"
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
    checked(registry.get("registry_version") == "1.3.0", "Claim registry version mismatch")
    checked(registry.get("published") == "2026-09-01", "Claim registry publication date mismatch")
    checked(registry.get("source_review_date") == "2026-09-01", "Claim registry source-review date mismatch")

    standing = registry.get("standing_interpretation", {})
    checked(standing.get("accepted_standing") == "52/53", "Standing interpretation mismatch")
    checked("numerical Runtime standing corridor" in str(standing.get("public_meaning", "")), "Standing interpretation is not bounded as a Runtime standing corridor")

    current = registry.get("current_runtime_evidence", {})
    expected_current = {
        "front_door": "runtime/README.md",
        "packet_index": "evidence/runtime/full-flex/v1/README.md",
        "public_safe_record": "evidence/runtime/full-flex/v1/PUBLIC_SAFE_RECORD.json",
        "packet_schema": "EHCO_FULL_FLEX_PUBLIC_PACKET_V1",
        "packet_sha256": EXPECTED_PACKET_SHA256,
        "runtime_maturity": "REALIZED / COMPLETE_IN_ACCEPTED_SCOPE",
        "accepted_standing": "52/53",
        "docker_portability": "PRIMARY_ACCESSIBLE_RUNTIME_PROJECTION",
        "public_custody": "ACCEPTED_PACKET_HASH_AND_RECEIPT_WITH_PUBLIC_SAFE_RECORD",
        "raw_packet_publication": "WITHHELD_FROM_CURRENT_PUBLIC_TREE_TO_PROTECT_INTERNAL_SOURCE_ROUTING_METADATA",
    }
    for key, value in expected_current.items():
        checked(current.get(key) == value, f"Current Runtime evidence mismatch: {key}")

    claims = registry.get("claims", [])
    checked(isinstance(claims, list), "Claim registry claims must be a list")
    by_id = {item.get("claim_id"): item for item in claims if isinstance(item, dict)}
    required_claims = {
        "AIOS-RUNTIME-REALIZED": "realized Tier One Runtime",
        "AIOS-COMPLETE-ACCEPTED-SCOPE": "REALIZED / COMPLETE_IN_ACCEPTED_SCOPE",
        "AIOS-PORTABILITY-DEPLOYMENT-READY": "fully containerized, deployment-ready portable delivery form",
        "AIOS-LOCAL-RUNTIME-PROVEN": "self-hosted local Docker Runtime",
        "LM-MATURE-DETERMINISTIC-COMPUTATIONAL-LANGUAGE": "mature deterministic computational-language system",
        "LM-ARTIFACT-RELEASE-STAGING-ESTABLISHED": "governed staging execution and verification established",
        "RR-MATURE": "mature deterministic proof-carrying",
        "RR-MATCHED-AB-COLLAPSE-PERFORMANCE": "14.304307x wall-clock improvement",
        "RR-SEMANTIC-CLOSURE": "82 passed and 0 failed",
    }
    for claim_id, phrase in required_claims.items():
        checked(claim_id in by_id, f"Required public claim missing: {claim_id}")
        if claim_id in by_id:
            item = by_id[claim_id]
            checked(phrase in str(item.get("public_statement", "")), f"Required wording missing for {claim_id}: {phrase}")
            checked(item.get("status") == "ESTABLISHED", f"Claim status mismatch: {claim_id}")
            for field in ["evidence_class", "verification_method", "disclosure_ceiling"]:
                checked(bool(item.get(field)), f"{field} missing: {claim_id}")

    public_files = {
        "README.md": read("README.md"),
        "Start Here": read("getting-started/START-HERE.md"),
        "Technology Estate": read("architecture/EHCO-TECHNOLOGY-ESTATE.md"),
        "Language Model": read("language-model/README.md"),
        "LM Demonstration": read("language-model/DETERMINISTIC-CAPABILITY-DEMONSTRATION.md"),
        "Runtime": read("runtime/README.md"),
        "Full Flex": read("evidence/runtime/full-flex/v1/README.md"),
        "Range Reactor": read("range-reactor/README.md"),
        "RR Operational Closure": read("range-reactor/evidence/operational-closure-v1/README.md"),
        "Verification": read("verification/README.md"),
    }

    checked("Instantiated AI" in public_files["README.md"], "Root README does not expose Instantiated AI")
    checked("DETERMINISTIC-CAPABILITY-DEMONSTRATION.md" in public_files["Language Model"], "Language Model page does not route to deterministic capability demonstration")
    checked("14.304307x" in public_files["Range Reactor"], "Range Reactor page does not expose selected operational result")
    checked("PUBLIC_SAFE_RECORD.json" in public_files["Full Flex"], "Full Flex page does not route to public-safe record")
    checked("verify_all_public.py" in public_files["Verification"], "Verification README does not expose unified validator")

    combined = "\n".join(public_files.values()) + "\n" + json.dumps(registry, sort_keys=True)
    forbidden = [
        "EHCOnomics-Systems/EHCO_AI-OS",
        "EHCOnomics-Systems/EHCO_Range_Reactor",
        "EHCOnomics-Systems/ehco_Language-Model_v1",
        "drive.google.com",
        "1FydQKUNfpQ7oZrgpLDlqRHxFM_f1mFv5uq_akploL38",
        "DESKTOP-",
        "C:\\",
    ]
    for value in forbidden:
        checked(value not in combined, f"Protected locator/topology token in active public representation: {value}")

    checked("advanced near-final" not in combined.lower(), "Obsolete advanced-near-final wording remains active")
    checked("current selected lifecycle frontier is governed staging" not in combined.lower(), "Stale Language Model staging-frontier wording remains active")

    if ERRORS:
        print(f"EHCOsystem public claim-registry validation: FAIL ({len(ERRORS)} errors / {CHECKS} checks)")
        for error in ERRORS:
            print(f"- {error}")
        return 1

    print(f"EHCOsystem public claim-registry validation: PASS ({CHECKS} checks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
