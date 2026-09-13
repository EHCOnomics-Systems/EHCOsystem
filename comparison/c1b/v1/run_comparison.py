#!/usr/bin/env python3
"""Frozen C1B EHCO/OPA comparison harness.

This public harness is protocol machinery, not an official result by itself.
An official result exists only when invoked after a public preregistration
identity has been resolved and supplied to this program.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[2]
FIXTURES = HERE / "shared-fixtures.json"
PROTOCOL = HERE / "protocol.json"
ENVIRONMENT = HERE / "environment.json"
REFERENCE = HERE / "reference-baseline.json"
REGO = HERE / "opa-reference.rego"
EHCO_KERNEL = REPO_ROOT / "proof/public-kernel/v1/kernel.py"
EHCO_VERIFY = REPO_ROOT / "proof/public-kernel/v1/verify_receipt.py"

PROVES = [
    "The bounded observed behavior of the two frozen operands under the published synthetic comparison protocol.",
    "Whether every published shared case produced the recorded public-safe dispositions and evidence under the recorded environment.",
]
DOES_NOT_PROVE = [
    "Universal superiority of EHCO over OPA or any other system.",
    "Current Tier One Runtime state, authority, admission, binding, invocation, or participation.",
    "Any change to accepted numerical standing 52/53.",
    "Production deployment or independent certification.",
    "That proprietary EHCO implementation source uses the same code or mechanics as the public proof kernel.",
]

def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())

def run_process(argv: list[str], *, timeout: int) -> dict[str, Any]:
    try:
        cp = subprocess.run(
            argv,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
        )
        return {
            "status": "COMPLETED",
            "exit_status": cp.returncode,
            "stdout": cp.stdout.decode("utf-8", errors="replace"),
            "stderr": cp.stderr.decode("utf-8", errors="replace"),
        }
    except subprocess.TimeoutExpired as exc:
        return {
            "status": "TIMEOUT",
            "exit_status": None,
            "stdout": (exc.stdout or b"").decode("utf-8", errors="replace"),
            "stderr": (exc.stderr or b"").decode("utf-8", errors="replace"),
        }

def extract_opa_value(stdout: str) -> dict[str, Any]:
    payload = json.loads(stdout)
    return payload["result"][0]["expressions"][0]["value"]

def normalize_opa_disposition(value: dict[str, Any]) -> str:
    disposition = value.get("disposition")
    if not isinstance(disposition, str):
        raise ValueError("OPA result has no string disposition")
    return disposition

def qualify_reference(opa: Path, timeout: int) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    check = run_process([str(opa), "check", str(REGO)], timeout=timeout)
    checks.append({
        "check": "OPA_NATIVE_PARSE",
        "status": "PASS" if check["status"] == "COMPLETED" and check["exit_status"] == 0 else "FAIL",
        "exit_status": check["exit_status"],
        "stdout_sha256": sha256_bytes(check["stdout"].encode()),
        "stderr_sha256": sha256_bytes(check["stderr"].encode()),
    })
    fixtures = load_json(FIXTURES)["fixtures"]
    with tempfile.TemporaryDirectory(prefix="ehco-c1b-qualify-") as tmp:
        t = Path(tmp)
        for fixture in fixtures:
            inp = t / f"{fixture['fixture_id']}.json"
            inp.write_text(json.dumps(fixture["request"], sort_keys=True) + "\n", encoding="utf-8")
            result = run_process(
                [
                    str(opa), "eval", "--format=json", "--data", str(REGO),
                    "--input", str(inp), "data.ehco_c1b.reference.result",
                ],
                timeout=timeout,
            )
            status = "FAIL"
            observed = None
            if result["status"] == "COMPLETED" and result["exit_status"] == 0:
                try:
                    observed = normalize_opa_disposition(extract_opa_value(result["stdout"]))
                    expected = "PASS" if fixture["expected_class"] == "PERMIT" else fixture["expected_class"]
                    status = "PASS" if observed == expected else "FAIL"
                except Exception:
                    status = "FAIL"
            checks.append({
                "check": "OPA_NATIVE_FIXTURE_EVAL",
                "fixture_id": fixture["fixture_id"],
                "status": status,
                "observed_disposition": observed,
                "exit_status": result["exit_status"],
                "stdout_sha256": sha256_bytes(result["stdout"].encode()),
                "stderr_sha256": sha256_bytes(result["stderr"].encode()),
            })
    return {
        "schema": "EHCO_C1B_REFERENCE_QUALIFICATION_V1",
        "opa_binary_sha256": sha256_file(opa),
        "policy_sha256": sha256_file(REGO),
        "checks": checks,
        "pass": all(item["status"] == "PASS" for item in checks),
        "official_comparative_result": False,
    }

def run_official(args: argparse.Namespace) -> int:
    if not args.preregistration_identity:
        print("Official run requires --preregistration-identity", file=sys.stderr)
        return 2
    protocol = load_json(PROTOCOL)
    environment = load_json(ENVIRONMENT)
    reference = load_json(REFERENCE)
    fixtures = load_json(FIXTURES)["fixtures"]
    expected_opa_digest = reference["official_release_asset"]["sha256"]
    observed_opa_digest = sha256_file(args.opa)
    if observed_opa_digest != expected_opa_digest:
        print("OPA binary digest mismatch", file=sys.stderr)
        return 2

    outdir = args.output_dir
    outdir.mkdir(parents=True, exist_ok=True)
    cases = []
    failures = []

    for fixture in fixtures:
        fixture_id = fixture["fixture_id"]
        source_fixture_id = fixture["source_fixture_id"]
        nonce = f"{args.nonce}:{fixture_id}"
        ehco_receipt = outdir / f"{fixture_id}.ehco.json"
        reference_input = outdir / f"{fixture_id}.opa-input.json"
        reference_raw = outdir / f"{fixture_id}.opa-raw.json"
        reference_input.write_text(json.dumps(fixture["request"], indent=2, sort_keys=True) + "\n", encoding="utf-8")

        ehco_run = run_process(
            [
                sys.executable, str(EHCO_KERNEL), "--fixture", source_fixture_id,
                "--nonce", nonce, "--receipt-out", str(ehco_receipt),
            ],
            timeout=args.timeout,
        )
        ehco_verify = run_process(
            [
                sys.executable, str(EHCO_VERIFY), "--receipt", str(ehco_receipt),
                "--expected-nonce", nonce,
            ],
            timeout=args.timeout,
        ) if ehco_receipt.is_file() else {
            "status": "NOT_RUN", "exit_status": None, "stdout": "", "stderr": ""
        }

        opa_run = run_process(
            [
                str(args.opa), "eval", "--format=json", "--data", str(REGO),
                "--input", str(reference_input), "data.ehco_c1b.reference.result",
            ],
            timeout=args.timeout,
        )
        reference_raw.write_text(opa_run["stdout"], encoding="utf-8")

        ehco_disp = None
        if ehco_receipt.is_file():
            try:
                ehco_disp = load_json(ehco_receipt)["run"]["disposition"]
            except Exception:
                pass
        opa_disp = None
        if opa_run["status"] == "COMPLETED" and opa_run["exit_status"] == 0:
            try:
                opa_disp = normalize_opa_disposition(extract_opa_value(opa_run["stdout"]))
            except Exception:
                pass

        if ehco_disp is None or opa_disp is None or ehco_verify["exit_status"] != 0:
            classification = "RUN_FAILURE"
            failures.append(fixture_id)
        elif ehco_disp == opa_disp:
            classification = "MATCHED_DISPOSITION"
        else:
            classification = "DIFFERENT_DISPOSITION"

        cases.append({
            "fixture_id": fixture_id,
            "source_fixture_id": source_fixture_id,
            "ehco": {
                "status": ehco_run["status"],
                "disposition": ehco_disp,
                "exit_status": ehco_run["exit_status"],
                "receipt_verification_exit_status": ehco_verify["exit_status"],
                "output_sha256": sha256_file(ehco_receipt) if ehco_receipt.is_file() else None,
            },
            "reference": {
                "status": opa_run["status"],
                "disposition": opa_disp,
                "exit_status": opa_run["exit_status"],
                "output_sha256": sha256_file(reference_raw),
            },
            "classification": classification,
            "raw_output_identities": {
                "ehco_receipt": ehco_receipt.name if ehco_receipt.is_file() else None,
                "opa_raw": reference_raw.name,
                "opa_input": reference_input.name,
            },
            "notes": [],
        })

    manifest_digest = sha256_file(HERE / "manifest.json")
    result = {
        "schema": "EHCO_C1B_RESULT_V1",
        "protocol_id": protocol["protocol_id"],
        "protocol_version": protocol["protocol_version"],
        "preregistration_identity": args.preregistration_identity,
        "preregistration_manifest_sha256": manifest_digest,
        "ehco_artifact_identity": protocol["ehco_operand"],
        "reference_baseline_identity": reference,
        "fixture_set_identity": {
            "path": "comparison/c1b/v1/shared-fixtures.json",
            "sha256": sha256_file(FIXTURES),
        },
        "environment_identity_ehco": environment["ehco"],
        "environment_identity_reference": environment["reference"],
        "cases": cases,
        "failure_and_omission_accounting": {
            "planned_cases": len(fixtures),
            "recorded_cases": len(cases),
            "run_failure_fixture_ids": failures,
            "omitted_fixture_ids": [],
        },
        "bounded_interpretation": (
            "Measured facts are limited to the frozen protocol and may not be generalized "
            "to universal superiority, production readiness, Runtime authority, or certification."
        ),
        "what_this_proves": PROVES,
        "what_this_does_not_prove": DOES_NOT_PROVE,
    }
    result_path = outdir / "comparison-result.json"
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result_path)
    return 0 if not failures else 1

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--opa", type=Path, required=True)
    parser.add_argument("--qualify-reference", action="store_true")
    parser.add_argument("--qualification-out", type=Path)
    parser.add_argument("--preregistration-identity")
    parser.add_argument("--nonce")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--timeout", type=int, default=30)
    args = parser.parse_args()

    if args.qualify_reference:
        payload = qualify_reference(args.opa, args.timeout)
        target = args.qualification_out
        if target is None:
            print(json.dumps(payload, indent=2, sort_keys=True))
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            print(target)
        return 0 if payload["pass"] else 1

    if not args.nonce or args.output_dir is None:
        parser.error("official run requires --nonce and --output-dir")
    return run_official(args)

if __name__ == "__main__":
    raise SystemExit(main())
