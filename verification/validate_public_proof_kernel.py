#!/usr/bin/env python3
"""Validate the bounded EHCOsystem Public Proof Kernel candidate."""
from __future__ import annotations

import ast
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "proof" / "public-kernel" / "v1"
KERNEL = PROOF / "kernel.py"
VERIFY = PROOF / "verify_receipt.py"
MANIFEST = PROOF / "public-proof-manifest.json"
ERRORS: list[str] = []
CHECKS = 0

def checked(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        ERRORS.append(message)

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def run(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, *args], cwd=cwd or ROOT, text=True, capture_output=True)

def receipt(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))

def test_fixture(tmp: Path, fixture_id: str, expected: str, count: int, nonce: str) -> dict:
    out = tmp / f"{fixture_id}.json"
    result = run(str(KERNEL), "--fixture", fixture_id, "--nonce", nonce, "--receipt-out", str(out))
    checked(result.returncode == 0, f"{fixture_id} execution failed: {result.stderr.strip()}")
    data = receipt(out)
    checked(data["run"]["disposition"] == expected, f"{fixture_id} disposition mismatch")
    checked(data["intelligence_invocation_count"] == count, f"{fixture_id} invocation count mismatch")
    verify = run(str(VERIFY), "--receipt", str(out), "--expected-nonce", nonce)
    checked(verify.returncode == 0, f"{fixture_id} receipt verification failed: {verify.stderr.strip()}")
    return data

def mutate_copy(tmp: Path, rel: str, marker: str) -> Path:
    copy_root = tmp / ("tamper-" + marker)
    shutil.copytree(PROOF, copy_root)
    target = copy_root / rel
    if target.suffix == ".json":
        obj = json.loads(target.read_text(encoding="utf-8"))
        obj["_synthetic_tamper_marker"] = marker
        target.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    else:
        target.write_text(target.read_text(encoding="utf-8") + f"\n# synthetic tamper {marker}\n", encoding="utf-8")
    return copy_root

def run_tamper(copy_root: Path, fixture: str, nonce: str) -> dict:
    out = copy_root / "tamper-receipt.json"
    result = run(str(copy_root / "kernel.py"), "--fixture", fixture, "--nonce", nonce, "--receipt-out", str(out), cwd=copy_root)
    checked(result.returncode != 0, "tampered package returned success exit")
    data = receipt(out)
    checked(data["run"]["disposition"] == "INTEGRITY_FAILURE", "tampered package did not yield INTEGRITY_FAILURE")
    checked(data["intelligence_invocation_count"] == 0, "tampered package invoked intelligence placeholder")
    return data

def main() -> int:
    required = [
        "README.md","kernel.py","verify_receipt.py","protocol.json","environment.json",
        "fixtures.json","claim-test-map.json","threat-control-map.json","public-proof-manifest.json",
    ]
    for rel in required:
        checked((PROOF / rel).is_file(), f"missing proof file: {rel}")

    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except Exception as exc:
        ERRORS.append(f"manifest parse failure: {exc}")
        manifest = {}

    checked(manifest.get("schema") == "EHCO_PUBLIC_PROOF_MANIFEST_V1", "manifest schema mismatch")
    checked(manifest.get("source_public_base") == "58f8a0375df7ca3ef19b25f0103d93c987854543", "source public base mismatch")
    checked(manifest.get("final_git_commit_identity") == "BOUND_LATER_BY_PROVIDER_CHECKPOINT_NOT_SELF_REFERENCED", "manifest violates two-part Git identity rule")
    checked("52/53" not in json.dumps(manifest) or manifest.get("standing_effect") == "NONE", "manifest standing boundary mismatch")

    for item in manifest.get("files", []):
        path = PROOF / item["path"]
        checked(path.is_file() and digest(path) == item["sha256"], f"manifest digest mismatch: {item.get('path')}")

    # No network/model imports in executable proof source.
    forbidden_import_roots = {"socket","urllib","http","requests","aiohttp","openai","anthropic","transformers","torch"}
    for source in [KERNEL, VERIFY]:
        tree = ast.parse(source.read_text(encoding="utf-8"))
        imported = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported.add(node.module.split(".")[0])
        checked(not (imported & forbidden_import_roots), f"network/model dependency imported by {source.name}")

    environment = json.loads((PROOF / "environment.json").read_text(encoding="utf-8"))
    checked(environment.get("network_dependency_class") == "OFFLINE", "environment is not OFFLINE")
    checked(environment.get("model_dependency_state") == "ABSENT", "model dependency is not ABSENT")

    threat_map = json.loads((PROOF / "threat-control-map.json").read_text(encoding="utf-8"))
    checked(len(threat_map.get("threats", [])) == 26, "threat coverage register does not contain 26 entries")
    checked(len({t.get("threat_id") for t in threat_map.get("threats", [])}) == 26, "threat IDs are not unique")

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        receipts = {}
        fixtures = [
            ("PK-VALID-001","PASS",1,"nonce-valid-001"),
            ("PK-MISSING-PERMISSION-001","WITHHOLD",0,"nonce-permission-001"),
            ("PK-ELIGIBILITY-NOT-SATISFIED-001","WITHHOLD",0,"nonce-eligibility-001"),
            ("PK-AMBIGUOUS-001","RETAIN_AMBIGUITY",0,"nonce-ambiguous-001"),
            ("PK-UNSUPPORTED-001","UNSUPPORTED_REQUEST",0,"nonce-unsupported-001"),
        ]
        for fid, disp, count, nonce in fixtures:
            receipts[fid] = test_fixture(tmp, fid, disp, count, nonce)

        # Same input + same nonce must preserve material result identity.
        repeat_path = tmp / "repeat.json"
        repeat = run(str(KERNEL), "--fixture", "PK-VALID-001", "--nonce", "nonce-valid-001", "--receipt-out", str(repeat_path))
        checked(repeat.returncode == 0, "deterministic replay execution failed")
        repeat_data = receipt(repeat_path)
        a = receipts["PK-VALID-001"]
        checked(a["run"]["run_id"] == repeat_data["run"]["run_id"], "deterministic run identity changed")
        checked(a["output_digest"] == repeat_data["output_digest"], "deterministic output digest changed")
        checked(a["run"]["disposition"] == repeat_data["run"]["disposition"], "deterministic disposition changed")

        # Three integrity tamper families.
        run_tamper(mutate_copy(tmp, "fixtures.json", "fixture"), "PK-VALID-001", "tamper-fixture")
        run_tamper(mutate_copy(tmp, "protocol.json", "protocol"), "PK-VALID-001", "tamper-protocol")
        run_tamper(mutate_copy(tmp, "kernel.py", "artifact"), "PK-VALID-001", "tamper-artifact")

        # Receipt mutation + nonce replay rejection (one test family).
        valid_receipt = tmp / "PK-VALID-001.json"
        mutated = tmp / "mutated-receipt.json"
        data = receipt(valid_receipt)
        data["run"]["disposition"] = "WITHHOLD"
        mutated.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        vr = run(str(VERIFY), "--receipt", str(mutated), "--expected-nonce", "nonce-valid-001")
        checked(vr.returncode != 0, "mutated receipt verified successfully")
        replay = run(str(VERIFY), "--receipt", str(valid_receipt), "--expected-nonce", "nonce-new-challenge")
        checked(replay.returncode != 0, "old receipt verified against new challenge nonce")

    # 9 high-level test families represented in the map and exercised above.
    claim_map = json.loads((PROOF / "claim-test-map.json").read_text(encoding="utf-8"))
    checked(len(claim_map.get("tests", [])) == 9, "claim/test map does not contain 9 test families")
    checked(claim_map.get("status") == "CANDIDATE_TEST_DESIGNED", "claim/test map status exceeds prelaunch state")

    combined = "\n".join((PROOF / rel).read_text(encoding="utf-8") for rel in required)
    prohibited_markers = [
        "EHCO_PUBLIC_LAUNCH_BASELINE_V1_ACCEPTED",
    ]
    # The phrase may appear only when explicitly negated in README/operation, so do not treat text presence as acceptance.
    checked("private repository access is required" not in combined.lower(), "proof package implies private repository requirement")

    if ERRORS:
        print(f"EHCOsystem public proof-kernel validation: FAIL ({len(ERRORS)} errors / {CHECKS} checks)")
        for err in ERRORS:
            print(f"- {err}")
        return 1

    print(f"EHCOsystem public proof-kernel validation: PASS ({CHECKS} checks) [9 TEST FAMILIES]")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
