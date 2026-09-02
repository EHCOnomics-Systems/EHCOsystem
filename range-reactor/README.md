---
title: EHCO Range Reactor
version: 2.1
status: current-public-component-record
published: 2026-09-01
maintainer: EHCOnomics
evidence_class: public-component-capability-and-operational-closure-record
evidence_scope: mature deterministic range/reasoning capability and selected public-safe operational result
---

# EHCO Range Reactor

The **EHCO Range Reactor** is EHCOnomics' mature deterministic **proof-carrying implication, reachability, range, and reasoning system** within the shared EHCOsystem technology spine.

## What it does

Range Reactor provides bounded deterministic reasoning across implication and reachability, typed range evaluation, semantic result identity, deterministic replay, contradiction/remainder/frontier preservation, and finite semantic reduction with retained concrete-history witness custody.

Its accepted capability includes:

- executable deterministic reference semantics;
- typed query, event, proof, result, standing, and reduction contracts;
- canonical content-addressed identity and deterministic replay;
- contradiction, remainder, and frontier preservation;
- possible-versus-inevitable reachability distinctions;
- finite semantic quotient/reduction with retained witness fibers;
- independent verification of proposed reductions;
- service and container interfaces; and
- interoperable governed reasoning relationships with other EHCO technologies.

## Selected operational result

For the accepted `RR-EXPLORATION-AB-001` selected workload, the matched physical A/B result records:

- **14.304307x wall-clock improvement**;
- **14.208722x CPU-time improvement**;
- **94.755854% benchmark-defined Python peak-allocation reduction**;
- **96.729688% state-work reduction**, from **1,957** states to **64**;
- **90.184049% transition-work reduction**, from **1,956** transitions to **192**; and
- **720 histories preserved** in both modes.

The selected semantic-closure corpus records **82 passed / 0 failed** with deterministic replay.

The benchmark and semantic corpus define the scope of those measured results. Range Reactor's mature component capability is broader than one benchmark, while the numerical measurements remain attached to the selected workload that produced them.

## Public evidence

- **[Operational Closure Evidence v1](evidence/operational-closure-v1/README.md)** — the selected matched A/B result, selected semantic closure, public-safe integrity hashes, and accepted container/service qualification summary.
- **[Public Capability Snapshot v1](evidence/public-capability-snapshot-v1/README.md)** — eight public-safe synthetic capability vectors covering deterministic replay, contradiction/frontier preservation, modal distinction, reduction witness custody, independent verification, source-sensitive identity, and grounded proof custody.

## EHCOsystem relationship

Range Reactor supplies deterministic range/reasoning computation as a downstream governed component. Component capability maturity remains distinct from Tier One Runtime authority and Runtime participation. **EHCO AI-OS** remains the Tier One Runtime identity, and `INSTANTIATED_EHCO_RUNTIME` owns Tier One Runtime authority and Runtime state. No Tier One Runtime participation relationship is implied by the component capability or selected operational result.

## Verify

Run the complete public verification route:

```bash
python3 verification/verify_all_public.py
```

or the dedicated operational-closure validator:

```bash
python3 verification/validate_public_range_reactor_operational_closure.py
```

Use of these materials is governed by the repository root `LICENSE`.
