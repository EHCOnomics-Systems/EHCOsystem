#!/usr/bin/env python3
"""Verify an EHCOsystem Public Proof Kernel run receipt from the exact proof checkout."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "public-proof-manifest.json"

def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")

def digest_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()

def digest_file(path: Path) -> str:
    return digest_bytes(path.read_bytes())

def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))

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

def fail(message: str) -> int:
    print(f"FAIL receipt verification: {message}", file=sys.stderr)
    return 1

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", required=True)
    parser.add_argument("--expected-nonce", required=True)
    args = parser.parse_args()

    try:
        manifest = load_json(MANIFEST)
        receipt = load_json(Path(args.receipt))
        fixtures = load_json(ROOT / "fixtures.json")
    except Exception:
        return fail("required JSON could not be parsed")

    if manifest.get("schema") != "EHCO_PUBLIC_PROOF_MANIFEST_V1":
        return fail("manifest schema mismatch")

    for item in manifest.get("files", []):
        path = ROOT / item["path"]
        if not path.is_file() or digest_file(path) != item["sha256"]:
            return fail("proof package integrity mismatch")

    if receipt.get("schema") != "EHCO_PUBLIC_PROOF_RUN_RECEIPT_V1":
        return fail("receipt schema mismatch")
    if receipt.get("receipt_content_digest") != receipt_digest(receipt):
        return fail("receipt content digest mismatch")

    manifest_digest = digest_file(MANIFEST)
    if receipt.get("manifest_digest") != manifest_digest:
        return fail("manifest digest mismatch")
    if receipt.get("proof_family_id") != manifest.get("proof_family_id"):
        return fail("proof family mismatch")

    challenge = receipt.get("challenge", {})
    expected_nonce_digest = digest_bytes(args.expected_nonce.encode("utf-8"))
    if challenge.get("nonce_digest") != expected_nonce_digest:
        return fail("challenge nonce mismatch")

    artifact = receipt.get("artifact_identity", {})
    environment = receipt.get("environment_identity", {})
    fixture_entry = (receipt.get("fixtures") or [{}])[0]
    run = receipt.get("run", {})
    output = receipt.get("placeholder_output")
    output_digest = digest_bytes(canonical_bytes(output)) if output is not None else None
    if receipt.get("output_digest") != output_digest:
        return fail("placeholder output digest mismatch")

    fixture_id = fixture_entry.get("fixture_id")
    fixture = next((f for f in fixtures.get("fixtures", []) if f.get("fixture_id") == fixture_id), None)
    if fixture is None:
        if run.get("disposition") != "UNSUPPORTED_REQUEST":
            return fail("unknown fixture did not yield unsupported disposition")
        fixture_digest = "NOT_ESTABLISHED"
    else:
        fixture_digest = digest_bytes(canonical_bytes(fixture))
        if fixture_entry.get("selected_fixture_digest") != fixture_digest:
            return fail("selected fixture digest mismatch")
        if run.get("disposition") != fixture.get("expected_disposition"):
            return fail("disposition does not match frozen fixture expectation")

    expected_run_id = make_run_id(
        manifest_digest=manifest_digest,
        protocol_digest=digest_file(ROOT / "protocol.json"),
        artifact_digest=digest_file(ROOT / "kernel.py"),
        environment_digest=digest_file(ROOT / "environment.json"),
        fixture_digest=fixture_digest,
        nonce_digest=expected_nonce_digest,
        disposition=run.get("disposition"),
        output_digest=output_digest,
    )
    if run.get("run_id") != expected_run_id:
        return fail("run identity mismatch")

    count = receipt.get("intelligence_invocation_count")
    invoked = receipt.get("intelligence_invoked")
    if run.get("disposition") == "PASS":
        if count != 1 or invoked is not True or output is None:
            return fail("PASS invocation semantics invalid")
    else:
        if count != 0 or invoked is not False or output is not None:
            return fail("non-PASS invocation semantics invalid")

    print(f"PASS receipt verification fixture={fixture_id} disposition={run.get('disposition')}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
