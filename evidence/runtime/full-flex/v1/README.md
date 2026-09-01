# EHCO Full Flex Public Packet v1 — Accepted Runtime Evidence Index

This directory is the canonical public evidence route for the accepted **EHCO Full Flex Public Packet v1** and the accepted EHCO AI-OS Runtime representation carried by this repository.

## Accepted packet identity

- Schema: `EHCO_FULL_FLEX_PUBLIC_PACKET_V1`
- Established: `2026-08-30`
- Packet SHA-256: `7F80C27D085AE871A00AED412C6F20EA9A76CB0677C93AEBA381CD1FD70EC8E5`
- Clean package ZIP SHA-256: `DBF984B55731B5EA53C4D7F2A24F8CF4C0C4207E355EB8E6B1170113509F6B94`
- Runtime maturity represented: `REALIZED / COMPLETE_IN_ACCEPTED_SCOPE`
- Accepted standing represented: `52/53`
- Docker portability class represented: `PRIMARY_ACCESSIBLE_RUNTIME_PROJECTION`

The accepted packet identity remains unchanged. The public repository publishes a **public-safe Full Flex record** rather than the raw packet bytes because the accepted raw packet contains internal source-routing metadata that is outside the public disclosure surface.

Public custody is therefore:

- [`PUBLIC_SAFE_RECORD.json`](PUBLIC_SAFE_RECORD.json) — public-safe Runtime record bound to the accepted packet identity;
- [`PACKET_RECEIPT.json`](PACKET_RECEIPT.json) — accepted packet receipt;
- [`EHCO_FULL_FLEX_PUBLIC_PACKET_V1.sha256`](EHCO_FULL_FLEX_PUBLIC_PACKET_V1.sha256) — detached accepted packet identity.

The raw packet remains the accepted evidence object in its owning custody. Removing its public copy does not alter its hash, receipt, establishment, or technical result.

## What Full Flex establishes publicly

Full Flex records the established EHCO AI-OS Runtime posture together with its deployment-ready Docker portability and supporting technical relationships: physically operated local Docker Runtime behavior, Dashboard/bridge/worker relationships, persistent Runtime/proof/data surfaces, Docker networking, hardened image identity, operating independence, engineering-scale Runtime characterization, Range Reactor qualification/performance, public claim bindings, and artifact integrity.

For the reader-facing Runtime route, start with [EHCO AI-OS Runtime — Accepted Public Evidence](../../../../runtime/README.md).

## Historical evidence relationship

The existing [`public-evidence-companion/v1`](../../../public-evidence-companion/v1/) Packets 00–08 remain immutable historical/event-time evidence. They preserve the propositions and observations recorded at their event time.

The accepted Full Flex route is the primary public Runtime evidence route for the established baseline; the historical companion remains the deeper event-time lineage behind it. Any later Runtime-state proposition remains owned by applicable Runtime evidence.

## Evidence ownership

- `INSTANTIATED_EHCO_RUNTIME` owns Tier One Runtime authority and Runtime state.
- Owning technical evidence established the physical Runtime and Full Flex result.
- This public repository publishes the public-safe representation and integrity route.

## Verify

Run:

```bash
python3 verification/validate_current_runtime_evidence.py
```

or the canonical complete public validation route:

```bash
python3 verification/verify_all_public.py
```
