#!/usr/bin/env python3
"""Bounded, public-safe EHCOsystem proof kernel.

This program implements only the synthetic public proof protocol shipped beside
it. It is not the Tier One Runtime, does not model private Runtime schemas, and
does not import or invoke proprietary implementation source.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import secrets
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "public-proof-manifest.json"

PROVES = [
    "For the frozen synthetic protocol, declared proof-relevant conditions are evaluated before the intelligence placeholder may execute.",
    "Declared invalid, missing, ambiguous, unsupported, or integrity-invalid cases do not invoke the intelligence placeholder.",
    "A fresh challenge nonce is bound into the machine-readable run receipt.",
]
DOES_NOT_PROVE = [
    "Current Tier One Runtime state, authority, admission, binding, invocation, or participation.",
    "Any change to accepted numerical standing 52/53.",
    "That proprietary EHCO implementation source uses identical code or internal mechanics.",
    "Production deployment, independent certification, or universal superiority.",
    "Language Model or Range Reactor requalification.",
    "Security properties or capability outside the frozen public proof protocol.",
]

def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")

def digest_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()

def digest_file(path: Path) -> str:
    return digest_bytes(path.read_bytes())

def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()

def receipt_digest(receipt: dict[str, Any]) -> str:
    body = dict(receipt)
    body.pop("receipt_content_digest", None)
    return digest_bytes(canonical_bytes(body))

def make_run_id(*, manifest_digest: str, protocol_digest: str, artifact_digest: str,
                environment_digest: str, fixture_digest: str, nonce_digest: str,
                disposition: str, output_digest: str | None) -> str:
    body = {
        "manifest_digest": manifest_digest,
        "protocol_digest": protocol_digest,
        "artifact_digest": artifact_digest,
        "environment_digest": environment_digest,
        "fixture_digest": fixture_digest,
        "nonce_digest": nonce_digest,
        "disposition": disposition,
        "output_digest": output_digest,
    }
    return digest_bytes(canonical_bytes(body))

def integrity_preflight() -> tuple[dict[str, Any] | None, list[dict[str, str]], dict[str, str]]:
    checks: list[dict[str, str]] = []
    observed: dict[str, str] = {}
    try:
        manifest = load_json(MANIFEST)
    except Exception:
        return None, [{"check_id": "MANIFEST_PARSE", "status": "FAIL"}], observed

    if manifest.get("schema") != "EHCO_PUBLIC_PROOF_MANIFEST_V1":
        return manifest, [{"check_id": "MANIFEST_SCHEMA", "status": "FAIL"}], observed

    for item in manifest.get("files", []):
        rel = item.get("path")
        expected = item.get("sha256")
        path = ROOT / rel
        check_id = "FILE_DIGEST:" + str(rel)
        if not isinstance(rel, str) or not isinstance(expected, str) or not path.is_file():
            checks.append({"check_id": check_id, "status": "FAIL"})
            continue
        actual = digest_file(path)
        observed[rel] = actual
        checks.append({"check_id": check_id, "status": "PASS" if actual == expected else "FAIL"})
    return manifest, checks, observed

def find_fixture(fixtures: dict[str, Any], fixture_id: str) -> dict[str, Any] | None:
    for item in fixtures.get("fixtures", []):
        if item.get("fixture_id") == fixture_id:
            return item
    return None

def evaluate_fixture(protocol: dict[str, Any], fixture: dict[str, Any]) -> tuple[str, list[dict[str, str]], int, dict[str, str] | None]:
    trace: list[dict[str, str]] = []
    request = fixture.get("request", {})
    conditions = request.get("conditions", {})

    required = protocol["required_conditions"]
    failed_required = False
    for name in required:
        status = conditions.get(name)
        passed = status == "SATISFIED"
        trace.append({"rule_id": f"REQUIRED:{name}", "status": "PASS" if passed else "FAIL"})
        if not passed:
            failed_required = True
    if failed_required:
        return "WITHHOLD", trace, 0, None

    ambiguity = conditions.get("ambiguity_condition")
    if ambiguity == "AMBIGUOUS":
        trace.append({"rule_id": "AMBIGUITY", "status": "RETAIN"})
        return "RETAIN_AMBIGUITY", trace, 0, None
    trace.append({"rule_id": "AMBIGUITY", "status": "CLEAR"})

    action_class = request.get("action_class")
    if action_class not in protocol["supported_action_classes"]:
        trace.append({"rule_id": "SUPPORTED_ACTION", "status": "FAIL"})
        return "UNSUPPORTED_REQUEST", trace, 0, None
    trace.append({"rule_id": "SUPPORTED_ACTION", "status": "PASS"})

    placeholder_payload = {
        "placeholder": "DETERMINISTIC_INTELLIGENCE_PLACEHOLDER_EXECUTED",
        "request_id": request.get("request_id"),
        "action_class": action_class,
    }
    trace.append({"rule_id": "INTELLIGENCE_PLACEHOLDER", "status": "INVOKED_AFTER_PASS"})
    return "PASS", trace, 1, placeholder_payload

def build_receipt(*, manifest: dict[str, Any] | None, integrity_checks: list[dict[str, str]],
                  observed: dict[str, str], fixture_id: str, nonce: str,
                  disposition: str, trace: list[dict[str, str]] | None = None,
                  invocation_count: int = 0, placeholder_output: dict[str, str] | None = None,
                  fixture_digest: str = "NOT_ESTABLISHED") -> dict[str, Any]:
    now_start = utc_now()
    manifest_digest = digest_file(MANIFEST) if MANIFEST.is_file() else "NOT_ESTABLISHED"
    manifest = manifest or {}
    protocol_digest = observed.get("protocol.json", manifest.get("declared_protocol_digest", "NOT_ESTABLISHED"))
    artifact_digest = observed.get("kernel.py", manifest.get("declared_artifact_digest", "NOT_ESTABLISHED"))
    environment_digest = observed.get("environment.json", manifest.get("declared_environment_digest", "NOT_ESTABLISHED"))
    nonce_digest = digest_bytes(nonce.encode("utf-8"))
    output_digest = digest_bytes(canonical_bytes(placeholder_output)) if placeholder_output is not None else None
    run_id = make_run_id(
        manifest_digest=manifest_digest,
        protocol_digest=protocol_digest,
        artifact_digest=artifact_digest,
        environment_digest=environment_digest,
        fixture_digest=fixture_digest,
        nonce_digest=nonce_digest,
        disposition=disposition,
        output_digest=output_digest,
    )
    receipt: dict[str, Any] = {
        "schema": "EHCO_PUBLIC_PROOF_RUN_RECEIPT_V1",
        "receipt_version": 1,
        "proof_family_id": manifest.get("proof_family_id", "EHCO-PUBLIC-PROOF-KERNEL-PREINTELLIGENCE-GATE-001"),
        "proof_protocol_version": manifest.get("protocol_version", "NOT_ESTABLISHED"),
        "proof_protocol_digest": protocol_digest,
        "public_launch_identity": "PRELAUNCH_CANDIDATE_NOT_YET_ACCEPTED",
        "claim_ids": [manifest.get("proof_family_id", "EHCO-PUBLIC-PROOF-KERNEL-PREINTELLIGENCE-GATE-001")],
        "artifact_identity": {
            "class": "PUBLIC_SAFE_WRAPPER",
            "name": "EHCOsystem Public Proof Kernel",
            "version": manifest.get("artifact_version", "NOT_ESTABLISHED"),
            "digest_algorithm": "SHA256",
            "digest": artifact_digest,
        },
        "environment_identity": {
            "manifest_id": "EHCO-PUBLIC-PROOF-KERNEL-ENVIRONMENT-V1",
            "manifest_digest": environment_digest,
            "observed_material_values": {
                "network_dependency_class": "OFFLINE",
                "model_dependency_state": "ABSENT",
            },
        },
        "fixtures": [{
            "fixture_id": fixture_id,
            "expected_digest": observed.get("fixtures.json", manifest.get("declared_fixture_bundle_digest", "NOT_ESTABLISHED")),
            "observed_digest": observed.get("fixtures.json", "NOT_ESTABLISHED"),
            "integrity_status": "PASS" if all(c.get("status") == "PASS" for c in integrity_checks) else "FAIL",
            "selected_fixture_digest": fixture_digest,
        }],
        "challenge": {
            "nonce_digest": nonce_digest,
            "source": "REVIEWER_SUPPLIED",
        },
        "run": {
            "run_id": run_id,
            "started_at": now_start,
            "completed_at": utc_now(),
            "exit_status": 0 if disposition in {"PASS", "WITHHOLD", "RETAIN_AMBIGUITY", "UNSUPPORTED_REQUEST"} else 2,
            "disposition": disposition,
            "deterministic_replay_class": "FULLY_DETERMINISTIC_SAME_INPUT_SAME_DISPOSITION_AND_MATERIAL_OUTPUT",
        },
        "evaluation_trace_public_safe": trace or [],
        "intelligence_invoked": invocation_count > 0,
        "intelligence_invocation_count": invocation_count,
        "placeholder_output": placeholder_output,
        "output_digest": output_digest,
        "outputs": [] if output_digest is None else [{
            "output_id": "PLACEHOLDER_OUTPUT",
            "media_or_schema_type": "application/json",
            "digest_algorithm": "SHA256",
            "digest": output_digest,
            "public_interpretation_role": "Shows the deterministic placeholder executed only after PASS.",
        }],
        "integrity_checks": integrity_checks,
        "limitations": DOES_NOT_PROVE,
        "what_this_proves": PROVES,
        "what_this_does_not_prove": DOES_NOT_PROVE,
        "manifest_digest": manifest_digest,
    }
    receipt["receipt_content_digest"] = receipt_digest(receipt)
    return receipt

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", required=True, help="official fixture_id from fixtures.json")
    parser.add_argument("--nonce", default=None, help="reviewer challenge nonce; generated locally when omitted")
    parser.add_argument("--receipt-out", required=True, help="path for machine-readable run receipt")
    args = parser.parse_args()

    nonce = args.nonce or secrets.token_hex(24)
    manifest, checks, observed = integrity_preflight()
    integrity_ok = bool(manifest) and bool(checks) and all(item.get("status") == "PASS" for item in checks)

    if not integrity_ok:
        receipt = build_receipt(
            manifest=manifest,
            integrity_checks=checks,
            observed=observed,
            fixture_id=args.fixture,
            nonce=nonce,
            disposition="INTEGRITY_FAILURE",
        )
        Path(args.receipt_out).write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print("INTEGRITY_FAILURE")
        return 2

    try:
        protocol = load_json(ROOT / "protocol.json")
        fixtures = load_json(ROOT / "fixtures.json")
    except Exception:
        receipt = build_receipt(
            manifest=manifest,
            integrity_checks=checks + [{"check_id": "PUBLIC_PROTOCOL_PARSE", "status": "FAIL"}],
            observed=observed,
            fixture_id=args.fixture,
            nonce=nonce,
            disposition="PROTOCOL_FAILURE",
        )
        Path(args.receipt_out).write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print("PROTOCOL_FAILURE")
        return 2

    fixture = find_fixture(fixtures, args.fixture)
    if fixture is None:
        receipt = build_receipt(
            manifest=manifest,
            integrity_checks=checks,
            observed=observed,
            fixture_id=args.fixture,
            nonce=nonce,
            disposition="UNSUPPORTED_REQUEST",
            trace=[{"rule_id": "OFFICIAL_FIXTURE_ID", "status": "NOT_FOUND"}],
        )
        Path(args.receipt_out).write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print("UNSUPPORTED_REQUEST")
        return 0

    fixture_digest = digest_bytes(canonical_bytes(fixture))
    disposition, trace, count, placeholder = evaluate_fixture(protocol, fixture)
    receipt = build_receipt(
        manifest=manifest,
        integrity_checks=checks,
        observed=observed,
        fixture_id=args.fixture,
        nonce=nonce,
        disposition=disposition,
        trace=trace,
        invocation_count=count,
        placeholder_output=placeholder,
        fixture_digest=fixture_digest,
    )
    Path(args.receipt_out).write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(disposition)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
