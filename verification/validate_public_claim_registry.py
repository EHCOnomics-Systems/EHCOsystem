#!/usr/bin/env python3
"""Validate the canonical public claim registry and current public evidence synchronization."""
from __future__ import annotations
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "assurance" / "PUBLIC-CLAIM-REGISTRY.json"
EXPECTED_PACKET_SHA256 = "7F80C27D085AE871A00AED412C6F20EA9A76CB0677C93AEBA381CD1FD70EC8E5"
EXPECTED_BASE = "451ccd2603debcb0691893b7fd262fdbfbc89cc3"
ERRORS: list[str] = []
CHECKS = 0

def checked(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition: ERRORS.append(message)

def read(relative: str) -> str:
    path = ROOT / relative
    checked(path.is_file(), f"Required public file missing: {relative}")
    return path.read_text(encoding="utf-8-sig") if path.is_file() else ""

def main() -> int:
    checked(REGISTRY.is_file(), "Canonical public claim registry missing")
    try: registry = json.loads(REGISTRY.read_text(encoding="utf-8-sig"))
    except Exception as exc:
        ERRORS.append(f"Claim registry parse failure: {exc}"); registry = {}
    checked(registry.get("schema") == "ehco.public.claim-registry.v1", "Claim registry schema mismatch")
    checked(registry.get("registry_version") == "1.2.0", "Claim registry version mismatch")
    checked(registry.get("published") == "2026-08-31", "Claim registry publication date mismatch")
    checked(registry.get("source_review_date") == "2026-08-31", "Claim registry source-review date mismatch")
    checked(registry.get("public_repository_base") == EXPECTED_BASE, "Claim registry accepted source-base mismatch")
    standing = registry.get("standing_interpretation", {})
    checked(standing.get("accepted_standing") == "52/53", "Standing interpretation mismatch")
    checked("numerical Runtime standing corridor" in str(standing.get("public_meaning", "")), "Standing interpretation is not bounded as a Runtime standing corridor")
    for value in ["benchmark score", "percentage completion", "component maturity percentage", "deployment-state percentage", "public-release percentage"]:
        checked(value in standing.get("not_equivalent_to", []), f"Standing non-equivalence missing: {value}")
    checked(standing.get("protected_denominator_mechanics") == "NOT_PUBLICLY_INFERRED_OR_EXPANDED", "Protected standing mechanics boundary missing")
    current = registry.get("current_runtime_evidence", {})
    for key, value in {
        "front_door":"runtime/README.md", "packet_index":"evidence/runtime/full-flex/v1/README.md",
        "packet_schema":"EHCO_FULL_FLEX_PUBLIC_PACKET_V1", "packet_sha256":EXPECTED_PACKET_SHA256,
        "runtime_maturity":"REALIZED / COMPLETE_IN_ACCEPTED_SCOPE", "accepted_standing":"52/53",
        "docker_portability":"PRIMARY_ACCESSIBLE_RUNTIME_PROJECTION", "exact_byte_publication":"PUBLISHED_EXACT_BYTES_HASH_VERIFIED"
    }.items(): checked(current.get(key) == value, f"Current Runtime evidence mismatch: {key}")
    checked("CURRENT_FULL_FLEX_FIRST" in str(current.get("precedence", "")), "Full Flex-first precedence missing")
    checked("HISTORICAL_EVENT_TIME_LINEAGE" in str(current.get("precedence", "")), "Historical packet lineage classification missing")
    claims = registry.get("claims", [])
    checked(isinstance(claims, list), "Claim registry claims must be a list")
    by_id = {item.get("claim_id"): item for item in claims if isinstance(item, dict)}
    required_claims = {
        "AIOS-RUNTIME-REALIZED":"realized Tier One Runtime", "AIOS-COMPLETE-ACCEPTED-SCOPE":"REALIZED / COMPLETE_IN_ACCEPTED_SCOPE",
        "AIOS-PORTABILITY-DEPLOYMENT-READY":"fully containerized, deployment-ready portable delivery form", "AIOS-LOCAL-RUNTIME-PROVEN":"self-hosted local Docker Runtime",
        "AIOS-LOCAL-DASHBOARD-PROVEN":"host port 8080", "AIOS-TIER1-MODEL-INDEPENDENT-OPERATION":"external-model seam disabled",
        "AIOS-PERFORMANCE-CHARACTERIZATION":"6.847-second", "RR-MATURE":"mature deterministic proof-carrying",
        "RR-PHYSICAL-QUALIFICATION":"physical service execution", "RR-PERFORMANCE":"58.458 ms median",
        "RR-MATCHED-AB-COLLAPSE-PERFORMANCE":"14.304307x wall-clock speedup", "RR-SEMANTIC-CLOSURE":"82 passed and 0 failed"
    }
    for claim_id, phrase in required_claims.items():
        checked(claim_id in by_id, f"Required public claim missing: {claim_id}")
        if claim_id in by_id:
            item = by_id[claim_id]
            checked(phrase in str(item.get("public_statement", "")), f"Required wording missing for {claim_id}: {phrase}")
            checked(item.get("status") == "ESTABLISHED", f"Claim status mismatch: {claim_id}")
            for field in ["evidence_class", "verification_method", "disclosure_ceiling"]: checked(bool(item.get(field)), f"{field} missing: {claim_id}")
    rr_ab = by_id.get("RR-MATCHED-AB-COLLAPSE-PERFORMANCE", {})
    checked("matched benchmark only" in str(rr_ab.get("disclosure_ceiling", "")), "RR matched A/B claim lacks selected-benchmark ceiling")
    checked("2 warm-up pairs and 10 measured pairs" in str(rr_ab.get("disclosure_ceiling", "")), "RR matched A/B measurement count missing")
    rr_semantic = by_id.get("RR-SEMANTIC-CLOSURE", {})
    checked("SELECTED_CURRENT_SEMANTIC_CORPUS_ONLY" in str(rr_semantic.get("disclosure_ceiling", "")), "RR semantic closure lacks selected-corpus ceiling")
    checked("universal or unbounded correctness are not established" in str(rr_semantic.get("disclosure_ceiling", "")), "RR semantic closure universal nonclaim missing")
    public_files = {label: read(path) for label, path in {
        "README.md":"README.md", "Start Here":"getting-started/START-HERE.md", "Technology Estate":"architecture/EHCO-TECHNOLOGY-ESTATE.md",
        "AI-OS System Card":"architecture/EHCO-AI-OS-SYSTEM-CARD.md", "Technical Diligence":"TECHNICAL-DILIGENCE.md", "Ecosystem Diligence":"ECOSYSTEM-DILIGENCE.md",
        "AI-OS Claim Matrix":"assurance/CLAIM-EVIDENCE-MATRIX.md", "Ecosystem Claim Matrix":"assurance/ECOSYSTEM-CLAIM-EVIDENCE-MATRIX.md",
        "Evidence README":"evidence/README.md", "Verification README":"verification/README.md", "Range Reactor README":"range-reactor/README.md"}.items()}
    for label, text in public_files.items():
        for forbidden in ["EHCOnomics-Systems/EHCO_AI-OS", "EHCOnomics-Systems/EHCO_Range_Reactor", "drive.google.com", "DESKTOP-", "C:\\", "Azure"]:
            checked(forbidden not in text, f"Protected locator/lineage token in {label}: {forbidden}")
    checked("Current EHCO AI-OS Runtime — start here" in public_files["Start Here"], "Start Here does not put current Runtime evidence first")
    checked("Benchmark scoring, percentage-completion measures" in public_files["Start Here"], "Start Here lacks bounded 52/53 interpretation")
    for phrase in ["496,898,804-byte / 2,605,233-line", "6.847 seconds", "58.458 ms median", "110.213 ms p95", "213.075 ms maximum", "15.199 requests/second"]:
        checked(phrase in public_files["Technical Diligence"], f"Technical Diligence characterization wording missing: {phrase}")
        checked(phrase in public_files["Ecosystem Claim Matrix"], f"Ecosystem matrix characterization wording missing: {phrase}")
    checked("operational-closure-v1" in public_files["README.md"], "Root README does not expose RR operational closure")
    checked("operational-closure-v1" in public_files["Range Reactor README"], "Range Reactor README does not expose operational closure")
    checked("validate_public_range_reactor_operational_closure.py" in public_files["Verification README"], "Verification README does not register RR operational-closure validator")
    registry_text = json.dumps(registry, sort_keys=True)
    for forbidden in ["EHCOnomics-Systems/EHCO_AI-OS", "EHCOnomics-Systems/EHCO_Range_Reactor", "drive.google.com", "DESKTOP-", "C:\\\\", "Azure"]:
        checked(forbidden not in registry_text, f"Protected locator/lineage token in claim registry: {forbidden}")
    if ERRORS:
        print(f"EHCOsystem public claim-registry validation: FAIL ({len(ERRORS)} errors / {CHECKS} checks)")
        for error in ERRORS: print(f"- {error}")
        return 1
    print(f"EHCOsystem public claim-registry validation: PASS ({CHECKS} checks)")
    return 0
if __name__ == "__main__": raise SystemExit(main())
