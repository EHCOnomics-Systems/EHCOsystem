#!/usr/bin/env python3
"""Validate the accepted public Range Reactor operational-closure projection."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "range-reactor" / "evidence" / "operational-closure-v1" / "PUBLIC_RESULT.json"
README = ROOT / "range-reactor" / "evidence" / "operational-closure-v1" / "README.md"
ERRORS: list[str] = []
CHECKS = 0


def checked(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        ERRORS.append(message)


def main() -> int:
    checked(RESULT.is_file(), "RR operational-closure PUBLIC_RESULT.json missing")
    checked(README.is_file(), "RR operational-closure README missing")
    try:
        result = json.loads(RESULT.read_text(encoding="utf-8-sig"))
    except Exception as exc:
        ERRORS.append(f"RR operational-closure result parse failure: {exc}")
        result = {}

    checked(result.get("schema") == "EHCO_RR_PUBLIC_OPERATIONAL_CLOSURE_RESULT_V1", "RR result schema mismatch")
    checked(result.get("evidence_class") == "PUBLIC_PROJECTION_OF_ACCEPTED_OWNING_EVIDENCE", "RR evidence class mismatch")
    checked(result.get("owning_accepted_commit") == "eae888b784620ed37ed7d6704bcd91dedcf92936", "RR owning accepted commit mismatch")
    checked(result.get("benchmark_source_commit") == "e72b2a29e52878d300b44f0286259466352f73cc", "RR benchmark source commit mismatch")
    checked(result.get("owning_evidence_receipt_blob") == "42d7e0d448a59b82d15eade58e11d8de9407f7f2", "RR owning receipt blob mismatch")

    benchmark = result.get("benchmark", {})
    expected = {
        "contract": "RR-EXPLORATION-AB-001",
        "workload_id": "rr-independent-obligation-permutation-n6-v1",
        "workload_sha256": "44ad414852b2b23bc64cc415c8a433878d08da0698f17446f28c6ffdfa1ed8f6",
        "execution_evidence_class": "PHYSICAL_DOCKER_LINUX_EXECUTION_ON_OWNING_WINDOWS_DOCKER_ESTATE",
        "execution_python": "CPython 3.11.16",
        "wall_clock_speedup_x": 14.304307,
        "cpu_time_speedup_x": 14.208722,
        "memory_reduction_percent": 94.755854,
        "throughput_gain_x": 14.304307,
        "state_work_reduction_percent": 96.729688,
        "transition_work_reduction_percent": 90.184049,
        "literal_states": 1957,
        "reduced_states": 64,
        "literal_transitions": 1956,
        "reduced_transitions": 192,
        "literal_histories": 720,
        "reduced_histories": 720,
        "semantic_equivalence": "PROVEN_EQUAL_FOR_SELECTED_BENCHMARK_PROJECTION",
        "measurement_pairs": 10,
        "warmup_pairs": 2,
        "memory_metric_class": "PYTHON_TRACEMALLOC_PEAK_BYTES",
        "owning_host_file_sha256": "C6B7DAB276DCB620CC17C4D7F7B1E8B0EE45D53F6B64E574F55D7CC7ADBF2ED2",
        "internal_result_sha256": "6cca258517425c8d3723c036b8bf36d7ccb5f09991054b4f4bacf75a6f7dc697",
    }
    for key, value in expected.items():
        checked(benchmark.get(key) == value, f"RR benchmark field mismatch: {key}")

    service = result.get("real_world_service_qualification", {})
    checked(service.get("evidence_class") == "SEPARATE_HISTORICAL_PHYSICAL_CONTAINER_SERVICE_QUALIFICATION", "RR service qualification evidence class mismatch")
    checked(service.get("qualification_id") == "RR-REALWORLD-QUALIFY-001", "RR service qualification id mismatch")
    checked(service.get("source_revision") == "149314be7c4302d66bd93ac112e062292a2e815b", "RR service qualification source revision mismatch")
    checked(service.get("runtime_eligibility_admission_binding") == "NOT_ESTABLISHED", "RR service qualification Runtime nonclaim missing")
    checked(service.get("production_registry_custody_deployment_rollback") == "NOT_ESTABLISHED", "RR production nonclaim missing")
    checked(service.get("registry_published") is False, "RR registry publication nonclaim mismatch")

    semantic = result.get("semantic_closure", {})
    checked(semantic.get("selected_current_tests_passed") == 82, "RR semantic pass count mismatch")
    checked(semantic.get("selected_current_tests_failed") == 0, "RR semantic fail count mismatch")
    checked(semantic.get("deterministic_replay_digest") == "collapse-certificate-58a1e724b8acb571891d3c52", "RR deterministic replay digest mismatch")
    checked(semantic.get("continuation_manifest_sha256") == "083BA279EBE5456B8C874E087C6FEBD9624BB52D1FC2FFB48DFB410F6DB7E232", "RR continuation manifest hash mismatch")
    checked(semantic.get("claim_ceiling") == "SELECTED_CURRENT_SEMANTIC_CORPUS_ONLY", "RR semantic claim ceiling mismatch")

    boundary = result.get("claim_boundary", {})
    checked(boundary.get("generic_scalar_foresight_accuracy_percent") == "NOT_ESTABLISHED_FOR_DEVELOPMENT", "RR generic foresight-accuracy nonclaim missing")
    checked(boundary.get("universal_or_unbounded_correctness") is False, "RR universal/unbounded correctness nonclaim missing")
    for key in ["runtime_effect", "deployment_effect", "release_effect", "authority_effect", "standing_effect"]:
        checked(boundary.get(key) == "NONE", f"RR effect ceiling mismatch: {key}")
    checked(boundary.get("runtime_participation") == "NOT_ESTABLISHED", "RR Runtime participation nonclaim missing")
    checked(result.get("accepted_numerical_standing") == "52/53", "RR accepted standing mismatch")

    readme = README.read_text(encoding="utf-8-sig") if README.is_file() else ""
    for phrase in [
        "14.304307",
        "14.208722",
        "94.755854",
        "1,957",
        "64",
        "1,956",
        "192",
        "720",
        "82",
        "0",
        "selected benchmark",
        "not a universal Range Reactor speedup",
        "NOT_ESTABLISHED_FOR_DEVELOPMENT",
    ]:
        checked(phrase in readme, f"RR operational-closure README missing bounded representation: {phrase}")

    if ERRORS:
        print(f"EHCOsystem RR operational-closure validation: FAIL ({len(ERRORS)} errors / {CHECKS} checks)")
        for error in ERRORS:
            print(f"- {error}")
        return 1

    print(f"EHCOsystem RR operational-closure validation: PASS ({CHECKS} checks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
