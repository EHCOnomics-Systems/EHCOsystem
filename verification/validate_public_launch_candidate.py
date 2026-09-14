#!/usr/bin/env python3
"""Validate EHCO-PUB-SOW-010 launch-candidate bindings without creating acceptance."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREREG_ID = "8a1a05b4865eaefa716e77cbe669e819e7d6e5b3"
PREREG_MANIFEST_SHA256 = "440ae3a567f0d7db29a2c3348d0a7eb296ca5eece0b31a78fb9b58932efba357"
RESULT_SHA256 = "0010b0f2f0369d9328d34e23d44e7117c038038ce4260a14cb51d0b1ad71e38b"
RESULT_MANIFEST_SHA256 = "a961891144ff43cf1772bc9bef775eaa723347ec276892a31bcf64a73cffd35c"
C1_ID = "c208cb7cd002d016359f39aba1e3aef3f820befc"

def fail(message: str) -> None:
    raise AssertionError(message)

def read(path: str) -> bytes:
    target = ROOT / path
    if not target.is_file():
        fail(f"missing required file: {path}")
    return target.read_bytes()

def load(path: str) -> dict:
    try:
        return json.loads(read(path))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON {path}: {exc}")
    raise AssertionError("unreachable")

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def sha256(path: str) -> str:
    return sha256_bytes(read(path))

def git_blob_sha(path: str) -> str:
    data = read(path)
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()

def require_equal(actual, expected, label: str) -> None:
    if actual != expected:
        fail(f"{label}: expected {expected!r}, got {actual!r}")

def main() -> int:
    prereg_path = "comparison/c1b/v1/manifest.json"
    require_equal(sha256(prereg_path), PREREG_MANIFEST_SHA256, "C1B preregistration manifest SHA-256")
    prereg = load(prereg_path)
    require_equal(prereg.get("schema"), "EHCO_C1B_PREREGISTRATION_MANIFEST_V1", "C1B preregistration schema")
    require_equal(prereg.get("protocol_id"), "EHCO-C1B-OPA-PUBLIC-PROOF-COMPARISON-001", "C1B protocol id")
    require_equal(prereg.get("protocol_version"), "1.0.0", "C1B protocol version")
    files = prereg.get("files")
    if not isinstance(files, list) or len(files) != 9:
        fail("C1B preregistration must bind exactly nine files")
    for item in files:
        require_equal(sha256(item["path"]), item["sha256"], f"preregistered file {item['path']}")

    result_manifest_path = "comparison/c1b/v1/results/result-manifest.json"
    require_equal(sha256(result_manifest_path), RESULT_MANIFEST_SHA256, "C1B result manifest SHA-256")
    result_manifest = load(result_manifest_path)
    require_equal(result_manifest.get("schema"), "EHCO_C1B_PUBLIC_RESULT_MANIFEST_V1", "C1B result manifest schema")
    require_equal(result_manifest.get("accepted_c1_identity"), C1_ID, "accepted C1 identity")
    require_equal(result_manifest.get("preregistration_identity"), PREREG_ID, "C1B preregistration identity")
    require_equal(result_manifest.get("preregistration_manifest_sha256"), PREREG_MANIFEST_SHA256, "C1B preregistration manifest binding")
    require_equal(result_manifest.get("planned_cases"), 5, "C1B planned case count")
    require_equal(result_manifest.get("recorded_cases"), 5, "C1B recorded case count")
    require_equal(result_manifest.get("omitted_fixture_ids"), [], "C1B omitted fixture list")
    require_equal(result_manifest.get("run_failure_fixture_ids"), [], "C1B run-failure fixture list")
    require_equal(result_manifest.get("official_run_retry_performed"), False, "C1B preferred-result rerun flag")
    official = result_manifest.get("official_result", {})
    require_equal(official.get("sha256"), RESULT_SHA256, "C1B official result binding")
    require_equal(sha256(official["path"]), RESULT_SHA256, "C1B official result file SHA-256")
    for item in result_manifest.get("published_result_files", []):
        data = read(item["path"])
        require_equal(len(data), item["size"], f"published result size {item['path']}")
        require_equal(sha256_bytes(data), item["sha256"], f"published result SHA-256 {item['path']}")

    threat_path = "assurance/PUBLIC_LAUNCH_THREAT_MODEL.json"
    threat = load(threat_path)
    require_equal(threat.get("schema"), "EHCO_PUBLIC_LAUNCH_THREAT_MODEL_V1", "launch threat-model schema")
    require_equal(threat.get("frozen_c1b_preregistration_identity"), PREREG_ID, "threat-model C1B preregistration identity")
    require_equal(threat.get("official_c1b_result_sha256"), RESULT_SHA256, "threat-model C1B result identity")
    require_equal(threat.get("independent_external_reproduction_status"), "NOT_ESTABLISHED", "threat-model C1D state")
    required_threats = {
        "STATIC_REPLAY",
        "ARTIFACT_OR_FIXTURE_SUBSTITUTION",
        "POST_RESULT_PROTOCOL_DRIFT",
        "HIDDEN_DEPENDENCY",
        "REFERENCE_BASELINE_DRIFT",
        "ASYMMETRIC_COMPARATIVE_CONFIGURATION",
        "SELECTIVE_RESULT_OMISSION",
        "INTEGRITY_BYPASS",
        "CLAIM_SCOPE_INFLATION",
    }
    observed = {item.get("id") for item in threat.get("threats", []) if item.get("status") in {"CONTROLLED", "DISCLOSED_LIMITATION"}}
    missing = sorted(required_threats - observed)
    if missing:
        fail(f"launch threat model missing required threats: {', '.join(missing)}")

    receipt_schema = load("reproduction/INDEPENDENT_REPRODUCTION_RECEIPT.schema.json")
    require_equal(receipt_schema.get("$id"), "EHCO_INDEPENDENT_REPRODUCTION_RECEIPT_V1", "C1D receipt schema id")
    prereg_const = receipt_schema.get("properties", {}).get("public_preregistration_identity", {}).get("const")
    require_equal(prereg_const, PREREG_ID, "C1D schema preregistration binding")

    discovery_path = "verification/EHCO_PUBLIC_VERIFICATION_MANIFEST.json"
    discovery = load(discovery_path)
    require_equal(discovery.get("schema"), "EHCO_PUBLIC_VERIFICATION_MANIFEST_V1", "verification discovery schema")
    require_equal(discovery.get("comparative_proof", {}).get("preregistration_identity"), PREREG_ID, "discovery C1B preregistration identity")
    require_equal(discovery.get("comparative_proof", {}).get("preregistration_manifest_sha256"), PREREG_MANIFEST_SHA256, "discovery C1B prereg manifest")
    require_equal(discovery.get("comparative_proof", {}).get("official_result_sha256"), RESULT_SHA256, "discovery C1B result")
    require_equal(discovery.get("comparative_proof", {}).get("public_result_manifest_sha256"), RESULT_MANIFEST_SHA256, "discovery result manifest")
    require_equal(discovery.get("comparative_proof", {}).get("independent_external_reproduction_status"), "NOT_ESTABLISHED", "discovery C1D state")
    canonical = discovery.get("canonical_verifier", {})
    require_equal(canonical.get("path"), "verification/verify_all_public.py", "canonical verifier path")
    require_equal(canonical.get("execution_command"), "python3 verification/verify_all_public.py", "canonical verifier command")
    require_equal(canonical.get("git_blob_sha"), git_blob_sha("verification/verify_all_public.py"), "canonical verifier Git blob")
    if canonical.get("child_validator_count", 0) < 10:
        fail("canonical verifier does not include launch-candidate validation")
    routes = discovery.get("machine_routes", {})
    for key, path in {
        "comparative_protocol_manifest": prereg_path,
        "comparative_result_manifest": result_manifest_path,
        "independent_reproduction_instructions": "reproduction/INDEPENDENT-REPRODUCTION.md",
        "launch_baseline_manifest": "PUBLIC_LAUNCH_BASELINE.json",
        "launch_threat_model": threat_path,
    }.items():
        require_equal(routes.get(key), path, f"machine route {key}")
        read(path)

    baseline = load("PUBLIC_LAUNCH_BASELINE.json")
    require_equal(baseline.get("schema"), "EHCO_PUBLIC_LAUNCH_BASELINE_MANIFEST_V1", "launch baseline schema")
    require_equal(baseline.get("status"), "RESULT_PUBLICATION_CANDIDATE_NOT_ACCEPTED", "launch baseline acceptance state")
    require_equal(baseline.get("final_git_commit"), "BOUND_BY_FINAL_ACCEPTANCE_CHECKPOINT_AFTER_COMMIT", "final Git binding state")
    require_equal(baseline.get("provider_publication_identity"), "PENDING_FINAL_PROVIDER_TAG_OR_RELEASE_CHECKPOINT", "provider checkpoint state")
    require_equal(baseline.get("independent_reproduction", {}).get("receipt_identity"), "NOT_ESTABLISHED", "baseline C1D state")
    require_equal(baseline.get("comparative_proof", {}).get("preregistration_identity"), PREREG_ID, "baseline C1B preregistration identity")
    require_equal(baseline.get("comparative_proof", {}).get("candidate_manifest_sha256"), PREREG_MANIFEST_SHA256, "baseline C1B preregistration manifest")
    require_equal(baseline.get("comparative_proof", {}).get("official_result_sha256"), RESULT_SHA256, "baseline C1B result")
    require_equal(baseline.get("comparative_proof", {}).get("official_result_manifest_identity", {}).get("sha256"), RESULT_MANIFEST_SHA256, "baseline C1B result manifest")
    require_equal(baseline.get("public_verifier", {}).get("discovery_manifest"), discovery_path, "baseline discovery path")
    require_equal(baseline.get("public_verifier", {}).get("discovery_manifest_sha256"), sha256(discovery_path), "baseline discovery SHA-256")
    require_equal(baseline.get("launch_threat_model", {}).get("path"), threat_path, "baseline threat-model path")
    require_equal(baseline.get("launch_threat_model", {}).get("sha256"), sha256(threat_path), "baseline threat-model SHA-256")

    for required in [
        "VERIFY.md",
        "CITATION.cff",
        "reference/Home.md",
        ".github/ISSUE_TEMPLATE/technical-challenge.yml",
    ]:
        read(required)

    operation = read("ehco.operation.yaml").decode("utf-8")
    if "EHCOSYSTEM-SOW010-LAUNCH-INTEGRITY-REMEDIATION-001" not in operation:
        fail("public operation projection is not the SOW-10 launch-integrity remediation operation")

    print("PASS SOW-10 public launch candidate bindings")
    print(f"preregistration_identity={PREREG_ID}")
    print(f"official_result_sha256={RESULT_SHA256}")
    print("independent_external_reproduction=NOT_ESTABLISHED")
    print("public_launch_baseline_v1=NOT_ACCEPTED")
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"FAIL SOW-10 public launch candidate bindings: {exc}", file=sys.stderr)
        raise SystemExit(1)
