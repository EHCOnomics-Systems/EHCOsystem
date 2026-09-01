# EHCO Range Reactor Operational Closure Evidence v1

## Established selected-scope result

EHCO Range Reactor has an accepted physical matched A/B result for `RR-EXPLORATION-AB-001` on the selected `rr-independent-obligation-permutation-n6-v1` workload:

- **14.304307x wall-clock improvement**;
- **14.208722x CPU-time improvement**;
- **94.755854% benchmark-defined Python peak-allocation reduction** (`tracemalloc`);
- **96.729688% state-work reduction**, from **1,957** states to **64**;
- **90.184049% transition-work reduction**, from **1,956** transitions to **192**; and
- **720 histories preserved** in both modes.

The controlled measurement used **2 warm-up pairs** and **10 measured pairs**. The measured result applies to this selected benchmark workload.

## Semantic closure

The accepted selected semantic closure corpus records **82 passed / 0 failed** with deterministic replay digest `collapse-certificate-58a1e724b8acb571891d3c52`.

Together, the selected benchmark and semantic-closure result show deterministic reduction with preserved selected-workload semantics and an inspectable replay/integrity route.

## Container/service qualification

A separate accepted container/service qualification establishes Range Reactor operation through a containerized internal HTTP service, including private-network operation, capability execution, fail-closed transport handling, timeout/unavailability behavior, restart recovery, temporary portability, and AI-OS fail-closed fallback.

## Public integrity route

[`PUBLIC_RESULT.json`](PUBLIC_RESULT.json) is the public-safe machine-readable result. It preserves the selected workload identity, measurement configuration, measured values, selected semantic-closure result, and public-safe integrity hashes without publishing private repository names, private source revisions, private evidence-receipt locators, or internal development topology.

Public integrity anchors retained in the result include:

- workload SHA-256 `44ad414852b2b23bc64cc415c8a433878d08da0698f17446f28c6ffdfa1ed8f6`;
- physical result SHA-256 `C6B7DAB276DCB620CC17C4D7F7B1E8B0EE45D53F6B64E574F55D7CC7ADBF2ED2`;
- result-payload SHA-256 `6cca258517425c8d3723c036b8bf36d7ccb5f09991054b4f4bacf75a6f7dc697`; and
- continuation-manifest SHA-256 `083BA279EBE5456B8C874E087C6FEBD9624BB52D1FC2FFB48DFB410F6DB7E232`.

## Review route

Run:

```bash
python3 verification/validate_public_range_reactor_operational_closure.py
```

or use the canonical complete public validation route:

```bash
python3 verification/verify_all_public.py
```

The validator confirms this public result record. The accepted technical evidence remains the evidence that established the measured result; repository validation does not regenerate it.
