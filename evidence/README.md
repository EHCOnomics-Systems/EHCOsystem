# EHCOsystem Public Evidence

This directory contains the public evidence routes that support the EHCOsystem architecture and component records.

The public repository is organized **technology first, evidence second**: understand the system and component first, then use the evidence route for the proposition you want to inspect.

## Accepted Runtime / Full Flex

**EHCO AI-OS** is the realized Tier One Runtime with accepted standing **52/53** and accepted maturity **`REALIZED / COMPLETE_IN_ACCEPTED_SCOPE`**. `INSTANTIATED_EHCO_RUNTIME` owns Tier One Runtime authority and Runtime state.

The accepted **EHCO Full Flex Public Packet v1** is the selected public Runtime evidence identity represented by this repository:

```text
7F80C27D085AE871A00AED412C6F20EA9A76CB0677C93AEBA381CD1FD70EC8E5
```

The public repository publishes the [Full Flex public-safe record and evidence index](runtime/full-flex/v1/README.md), together with the accepted receipt and detached packet hash. The raw accepted packet remains in owning evidence custody because it contains internal source-routing metadata that is outside the public disclosure surface.

**[Start with the Runtime evidence page →](../runtime/README.md)**

## Language Model

The Language Model public evidence route includes:

- [Deterministic Capability Demonstration](../language-model/DETERMINISTIC-CAPABILITY-DEMONSTRATION.md)
- [Public Test Snapshot v1](../language-model/evidence/public-test-snapshot-v1/README.md) — seven exact fixture artifacts covering 62 cases
- [Qualification Test Index](../language-model/evidence/public-test-snapshot-v1/QUALIFICATION_TEST_INDEX_2026-08-24.md)

## Range Reactor

The Range Reactor public evidence route includes:

- [Operational Closure Evidence v1](../range-reactor/evidence/operational-closure-v1/README.md) — selected matched A/B result and 82/0 semantic closure
- [Public Capability Snapshot v1](../range-reactor/evidence/public-capability-snapshot-v1/README.md) — public-safe deterministic capability vectors

## Historical Public Evidence Companion

[`public-evidence-companion/v1/`](public-evidence-companion/v1/) contains immutable Packets 00–08. They preserve historical/event-time architecture, identity, observations, proof custody, manifests, receipts, and package closure.

These packets remain valid for the propositions and time windows they recorded. They provide deeper lineage behind the accepted architecture and evidence routes; they do not need to be reread to understand the public system at first contact.

## Evidence classes

Public material may represent controlled architecture, accepted artifact identity, public-safe evidence records, exact hashes and manifests, bounded fixtures, selected benchmark results, historical observations, and repository validation. Each route states the proposition and scope it supports.

Runtime authority and Runtime state remain owned by `INSTANTIATED_EHCO_RUNTIME`. Repository validation establishes integrity of the public representation for an exact revision; it does not replace the technical evidence that established an underlying system effect.

## Verify

Run:

```bash
python3 verification/verify_all_public.py
```

See [Public Repository Validation](../verification/README.md) for the canonical validation route.
