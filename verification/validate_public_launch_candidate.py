#!/usr/bin/env python3
"""Validate EHCO-PUB-SOW-010 launch bindings without originating acceptance."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREREG_ID = "8a1a05b4865eaefa716e77cbe669e819e7d6e5b3"
PREREG_MANIFEST_SHA256 = "440ae3a567f0d7db29a2c3348d0a7eb296ca5eece0b31a78fb9b58932efba357"
RESULT_SHA256 = "0010b0f2f0369d9328d34e23d44e7117c038038ce4260a14cb51d0b1ad71e38b"
RESULT_MANIFEST_SHA256 = "a961891144ff43cf1772bc9bef775eaa723347ec276892a31bcf64a73cffd35c"
C1_ID = "c208cb7cd002d016359f39aba1e3aef3f820befc"
BASELINE_REVISION = "666634a271b2254fdefa8076dcb8f960ff2e9e4b"
PROVIDER_TAG = "v1.0.0-public"
PROVIDER_RELEASE_ID = 388874688
PROVIDER_RELEASE_TITLE = "EHCOsystem Public Architecture and Evidence Baseline v1.0.0"
PROVIDER_PUBLICATION_TIMESTAMP = "2026-09-15T04:51:05Z"
PUBLICATION_DATE = "2026-09-15"

EXPECTED_CHILD_VALIDATORS = [
    ("PUBLIC_REPOSITORY_INTEGRITY", "verification/validate_public_evidence.py"),
    ("PREPUBLICATION_DISCLOSURE_GATE", "verification/validate_pre_publication_gate.py"),
    ("PUBLIC_CLAIM_REGISTRY", "verification/validate_public_claim_registry.py"),
    ("PUBLIC_PROOF_KERNEL", "verification/validate_public_proof_kernel.py"),
    ("CURRENT_RUNTIME_PUBLIC_EVIDENCE", "verification/validate_current_runtime_evidence.py"),
    ("LANGUAGE_MODEL_PUBLIC_SNAPSHOT", "verification/validate_public_lm_test_snapshot.py"),
    ("RANGE_REACTOR_CAPABILITY_SNAPSHOT", "verification/validate_public_range_reactor_snapshot.py"),
    ("RANGE_REACTOR_OPERATIONAL_CLOSURE", "verification/validate_public_range_reactor_operational_closure.py"),
    ("REGISTERED_RELEASE_IDENTITY", "verification/validate_release_identity.py"),
    ("PUBLIC_LAUNCH_CANDIDATE_BINDINGS", "verification/validate_public_launch_candidate.py"),
]

VALID_SOW10_OPERATION_IDS = {
    "EHCOSYSTEM-SOW010-LAUNCH-INTEGRITY-REMEDIATION-001",
    "EHCOSYSTEM-SOW010-WORKSTREAM-L-RECONSTRUCTION-001",
    "EHCOSYSTEM-SOW010-WORKSTREAM-O-PUBLIC-DISTRIBUTION-001",
}


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


def _resolve_local_ref(root_schema: dict, ref: str) -> dict:
    if not ref.startswith("#/"):
        fail(f"C1D receipt schema uses unsupported non-local reference {ref!r}")
    current = root_schema
    for token in ref[2:].split("/"):
        token = token.replace("~1", "/").replace("~0", "~")
        if not isinstance(current, dict) or token not in current:
            fail(f"C1D receipt schema reference cannot be resolved: {ref!r}")
        current = current[token]
    if not isinstance(current, dict):
        fail(f"C1D receipt schema reference does not resolve to an object: {ref!r}")
    return current


def _validate_schema_value(value, schema: dict, root_schema: dict, path: str = "$") -> None:
    if "$ref" in schema:
        _validate_schema_value(value, _resolve_local_ref(root_schema, schema["$ref"]), root_schema, path)
        return
    if "const" in schema and value != schema["const"]:
        fail(f"C1D receipt {path}: expected constant {schema['const']!r}, got {value!r}")
    if "enum" in schema and value not in schema["enum"]:
        fail(f"C1D receipt {path}: value {value!r} is not in {schema['enum']!r}")
    expected_type = schema.get("type")
    if expected_type == "object":
        if not isinstance(value, dict):
            fail(f"C1D receipt {path}: expected object")
        properties = schema.get("properties", {})
        for required in schema.get("required", []):
            if required not in value:
                fail(f"C1D receipt {path}: missing required property {required!r}")
        if schema.get("additionalProperties") is False:
            unexpected = sorted(set(value) - set(properties))
            if unexpected:
                fail(f"C1D receipt {path}: unexpected properties {unexpected!r}")
        for key, child in value.items():
            if key in properties:
                _validate_schema_value(child, properties[key], root_schema, f"{path}.{key}")
        return
    if expected_type == "array":
        if not isinstance(value, list):
            fail(f"C1D receipt {path}: expected array")
        if len(value) < schema.get("minItems", 0):
            fail(f"C1D receipt {path}: fewer than {schema['minItems']} items")
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, item in enumerate(value):
                _validate_schema_value(item, item_schema, root_schema, f"{path}[{index}]")
        return
    if expected_type == "string":
        if not isinstance(value, str):
            fail(f"C1D receipt {path}: expected string")
        if len(value) < schema.get("minLength", 0):
            fail(f"C1D receipt {path}: shorter than minimum length {schema['minLength']}")
        pattern = schema.get("pattern")
        if pattern is not None and re.search(pattern, value) is None:
            fail(f"C1D receipt {path}: value does not match required pattern")
        return
    if expected_type == "integer":
        if not isinstance(value, int) or isinstance(value, bool):
            fail(f"C1D receipt {path}: expected integer")
        minimum = schema.get("minimum")
        if minimum is not None and value < minimum:
            fail(f"C1D receipt {path}: value is below minimum {minimum}")
        return
    if expected_type == "boolean":
        if not isinstance(value, bool):
            fail(f"C1D receipt {path}: expected boolean")
        return


def validate_reproduction_receipt(receipt_path: Path, receipt_schema: dict) -> None:
    try:
        raw_text = receipt_path.read_text(encoding="utf-8")
    except OSError as exc:
        fail(f"cannot read C1D receipt {receipt_path}: {exc}")
    try:
        receipt = json.loads(raw_text, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(f"non-standard JSON constant {value!r}")))
    except (json.JSONDecodeError, ValueError) as exc:
        fail(f"invalid C1D receipt JSON {receipt_path}: {exc}")
    _validate_schema_value(receipt, receipt_schema, receipt_schema)
    claimed = receipt.get("receipt_sha256")
    payload = dict(receipt)
    payload.pop("receipt_sha256", None)
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")
    actual = hashlib.sha256(canonical).hexdigest()
    require_equal(claimed, actual, "C1D receipt canonical self-hash")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate SOW-10 launch bindings and optionally a returned C1D reproduction receipt.")
    parser.add_argument("--reproduction-receipt", type=Path, help="Optional path to a C1D receipt to validate structurally and verify its canonical SHA-256 self-hash.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
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
    required_threats = {"STATIC_REPLAY", "ARTIFACT_OR_FIXTURE_SUBSTITUTION", "POST_RESULT_PROTOCOL_DRIFT", "HIDDEN_DEPENDENCY", "REFERENCE_BASELINE_DRIFT", "ASYMMETRIC_COMPARATIVE_CONFIGURATION", "SELECTIVE_RESULT_OMISSION", "INTEGRITY_BYPASS", "CLAIM_SCOPE_INFLATION"}
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
    require_equal(canonical.get("child_validator_count"), len(EXPECTED_CHILD_VALIDATORS), "canonical child validator count")
    children = canonical.get("child_validators")
    if not isinstance(children, list):
        fail("verification discovery does not enumerate canonical child validators")
    require_equal(len(children), len(EXPECTED_CHILD_VALIDATORS), "enumerated child validator count")
    for index, ((expected_id, expected_path), item) in enumerate(zip(EXPECTED_CHILD_VALIDATORS, children)):
        if not isinstance(item, dict):
            fail(f"child validator entry {index} is not an object")
        require_equal(item.get("id"), expected_id, f"child validator {index} id")
        require_equal(item.get("path"), expected_path, f"child validator {expected_id} path")
        require_equal(item.get("git_blob_sha"), git_blob_sha(expected_path), f"child validator {expected_id} Git blob")

    routes = discovery.get("machine_routes", {})
    for key, path in {
        "claim_evidence_matrix": "assurance/ECOSYSTEM-CLAIM-EVIDENCE-MATRIX.md",
        "claim_registry": "assurance/PUBLIC-CLAIM-REGISTRY.json",
        "comparative_protocol_manifest": prereg_path,
        "comparative_result_manifest": result_manifest_path,
        "executable_proof_manifest": "proof/public-kernel/v1/public-proof-manifest.json",
        "independent_reproduction_instructions": "reproduction/INDEPENDENT-REPRODUCTION.md",
        "launch_baseline_manifest": "PUBLIC_LAUNCH_BASELINE.json",
        "launch_threat_model": threat_path,
        "reader_reference": "reference/Home.md",
        "launch_acceptance_receipt": "EHCO_PUBLIC_LAUNCH_BASELINE_V1_ACCEPTED.json",
    }.items():
        require_equal(routes.get(key), path, f"machine route {key}")
        read(path)

    baseline = load("PUBLIC_LAUNCH_BASELINE.json")
    require_equal(baseline.get("schema"), "EHCO_PUBLIC_LAUNCH_BASELINE_MANIFEST_V1", "launch baseline schema")
    require_equal(baseline.get("status"), "EHCO_PUBLIC_LAUNCH_BASELINE_V1_ACCEPTED", "launch baseline acceptance state")
    require_equal(baseline.get("final_git_commit"), BASELINE_REVISION, "final Git binding")
    provider = baseline.get("provider_publication_identity", {})
    require_equal(provider.get("tag"), PROVIDER_TAG, "provider checkpoint tag")
    require_equal(provider.get("release_id"), PROVIDER_RELEASE_ID, "provider Release id")
    require_equal(provider.get("release_title"), PROVIDER_RELEASE_TITLE, "provider Release title")
    require_equal(provider.get("published_at"), PROVIDER_PUBLICATION_TIMESTAMP, "provider publication timestamp")
    require_equal(baseline.get("publication_date"), PUBLICATION_DATE, "launch baseline publication date")
    require_equal(baseline.get("acceptance_receipt"), "EHCO_PUBLIC_LAUNCH_BASELINE_V1_ACCEPTED.json", "acceptance receipt route")
    require_equal(baseline.get("independent_reproduction", {}).get("receipt_identity"), "NOT_ESTABLISHED", "baseline C1D state")
    require_equal(baseline.get("independent_reproduction", {}).get("classification"), "OPTIONAL_SUPPLEMENTAL_EVIDENCE", "baseline C1D classification")
    require_equal(baseline.get("independent_reproduction", {}).get("required"), False, "baseline C1D required flag")
    require_equal(baseline.get("comparative_proof", {}).get("preregistration_identity"), PREREG_ID, "baseline C1B preregistration identity")
    require_equal(baseline.get("comparative_proof", {}).get("candidate_manifest_sha256"), PREREG_MANIFEST_SHA256, "baseline C1B preregistration manifest")
    require_equal(baseline.get("comparative_proof", {}).get("official_result_sha256"), RESULT_SHA256, "baseline C1B result")
    require_equal(baseline.get("comparative_proof", {}).get("official_result_manifest_identity", {}).get("sha256"), RESULT_MANIFEST_SHA256, "baseline C1B result manifest")
    require_equal(baseline.get("public_verifier", {}).get("discovery_manifest"), discovery_path, "baseline discovery path")
    require_equal(baseline.get("public_verifier", {}).get("discovery_manifest_sha256"), sha256(discovery_path), "baseline discovery SHA-256")
    require_equal(baseline.get("launch_threat_model", {}).get("path"), threat_path, "baseline threat-model path")
    require_equal(baseline.get("launch_threat_model", {}).get("sha256"), sha256(threat_path), "baseline threat-model SHA-256")

    acceptance = load("EHCO_PUBLIC_LAUNCH_BASELINE_V1_ACCEPTED.json")
    require_equal(acceptance.get("schema"), "EHCO_PUBLIC_LAUNCH_BASELINE_ACCEPTANCE_RECEIPT_V1", "acceptance receipt schema")
    require_equal(acceptance.get("receipt_id"), "EHCO_PUBLIC_LAUNCH_BASELINE_V1_ACCEPTED", "acceptance receipt id")
    require_equal(acceptance.get("status"), "EHCO_PUBLIC_LAUNCH_BASELINE_V1_ACCEPTED", "acceptance receipt state")
    require_equal(acceptance.get("accepted_baseline_revision"), BASELINE_REVISION, "acceptance baseline revision")
    require_equal(acceptance.get("provider_checkpoint", {}).get("tag"), PROVIDER_TAG, "acceptance provider tag")
    require_equal(acceptance.get("provider_checkpoint", {}).get("tag_resolved_revision"), BASELINE_REVISION, "acceptance provider tag revision")
    require_equal(acceptance.get("provider_checkpoint", {}).get("release_id"), PROVIDER_RELEASE_ID, "acceptance Release id")
    require_equal(acceptance.get("provider_checkpoint", {}).get("release_title"), PROVIDER_RELEASE_TITLE, "acceptance Release title")
    require_equal(acceptance.get("provider_checkpoint", {}).get("published_at"), PROVIDER_PUBLICATION_TIMESTAMP, "acceptance provider timestamp")
    require_equal(acceptance.get("independent_reproduction", {}).get("status"), "NOT_ESTABLISHED", "acceptance C1D state")
    require_equal(acceptance.get("independent_reproduction", {}).get("classification"), "OPTIONAL_SUPPLEMENTAL_EVIDENCE", "acceptance C1D classification")
    require_equal(acceptance.get("independent_reproduction", {}).get("blocks_acceptance"), False, "acceptance C1D blocking flag")
    require_equal(acceptance.get("accepted_numerical_standing"), "52/53", "acceptance standing")
    for effect in ("runtime_effect", "deployment_effect", "authority_effect", "standing_effect", "proprietary_source_transfer_effect"):
        require_equal(acceptance.get(effect), "NONE", f"acceptance {effect}")

    citation = read("CITATION.cff").decode("utf-8")
    if 'version: "1.0.0"' not in citation:
        fail("launch citation identity must be version 1.0.0")
    if 'date-released: "2026-09-15"' not in citation:
        fail("launch citation metadata must bind publication date 2026-09-15")

    for required in ["VERIFY.md", "CITATION.cff", "reference/Home.md", ".github/ISSUE_TEMPLATE/technical-challenge.yml", "EHCO_PUBLIC_LAUNCH_BASELINE_V1_ACCEPTED.json"]:
        read(required)

    operation = read("ehco.operation.yaml").decode("utf-8")
    if not any(operation_id in operation for operation_id in VALID_SOW10_OPERATION_IDS):
        fail("public operation projection is not a recognized SOW-10 launch operation")

    print("PASS SOW-10 public launch acceptance receipt bindings")
    print(f"baseline_revision={BASELINE_REVISION}")
    print(f"provider_tag={PROVIDER_TAG}")
    print(f"provider_release_id={PROVIDER_RELEASE_ID}")
    print(f"preregistration_identity={PREREG_ID}")
    print(f"official_result_sha256={RESULT_SHA256}")
    print("independent_external_reproduction=NOT_ESTABLISHED")
    print("public_launch_baseline_v1=EHCO_PUBLIC_LAUNCH_BASELINE_V1_ACCEPTED")

    if args.reproduction_receipt is not None:
        validate_reproduction_receipt(args.reproduction_receipt, receipt_schema)
        print(f"PASS C1D reproduction receipt structure_and_self_hash={args.reproduction_receipt}")
        print("c1d_acceptance=NOT_ESTABLISHED_BY_STRUCTURAL_RECEIPT_VALIDATION")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, KeyError, TypeError) as exc:
        print(f"FAIL SOW-10 public launch acceptance receipt bindings: {exc}", file=sys.stderr)
        raise SystemExit(1)
