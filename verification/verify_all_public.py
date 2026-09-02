#!/usr/bin/env python3
"""Run the canonical EHCOsystem public repository validators in a stable order.

This is a repository-quality orchestration surface. It does not replace or
promote the evidence class of any specialized validator.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

VALIDATORS = [
    ("PUBLIC_REPOSITORY_INTEGRITY", "verification/validate_public_evidence.py"),
    ("PUBLIC_CLAIM_REGISTRY", "verification/validate_public_claim_registry.py"),
    ("CURRENT_RUNTIME_PUBLIC_EVIDENCE", "verification/validate_current_runtime_evidence.py"),
    ("LANGUAGE_MODEL_PUBLIC_SNAPSHOT", "verification/validate_public_lm_test_snapshot.py"),
    ("RANGE_REACTOR_CAPABILITY_SNAPSHOT", "verification/validate_public_range_reactor_snapshot.py"),
    ("RANGE_REACTOR_OPERATIONAL_CLOSURE", "verification/validate_public_range_reactor_operational_closure.py"),
    ("REGISTERED_RELEASE_IDENTITY", "verification/validate_release_identity.py"),
]


def main() -> int:
    print("EHCOsystem public repository verification")
    print(f"repository_root={ROOT}\n")

    for label, relative_path in VALIDATORS:
        script = ROOT / relative_path
        if not script.is_file():
            print(f"FAIL [{label}] missing validator: {relative_path}", file=sys.stderr)
            return 2

        print(f"RUN  [{label}] {relative_path}")
        result = subprocess.run([sys.executable, str(script)], cwd=ROOT)
        if result.returncode != 0:
            print(f"FAIL [{label}] returncode={result.returncode}", file=sys.stderr)
            return result.returncode
        print(f"PASS [{label}]\n")

    print(f"PASS ALL ({len(VALIDATORS)}/{len(VALIDATORS)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
