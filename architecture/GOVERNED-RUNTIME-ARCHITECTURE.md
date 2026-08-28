---
title: EHCO AI-OS Governed Runtime Architecture
version: 1.1
status: accepted-public-reference
published: 2026-08-25
maintainer: EHCOnomics
evidence_class: controlled-ehco-architecture
proof_ceiling: conceptual public architecture; not an implementation map or Runtime proof
supersedes: version 1.0
---

# EHCO AI-OS Governed Runtime Architecture

## Scope

This document describes the public conceptual architecture of EHCO AI-OS and its relationships with downstream governed components and Tier Three projections. It is a conceptual architecture, not an implementation sequence or deployment topology.

The accepted EHCO AI-OS standing baseline remains **52/53**.

## Architectural objective

EHCO AI-OS is the **realized Tier One Runtime** of the EHCOsystem. The architecture keeps identity, component capability, Runtime participation, authority, scope, state, consequence, continuity, evidence, and projection from collapsing into one another.

Models can infer. Tools and applications can execute. Repositories can preserve artifacts. Dashboards can project status. Downstream governed components can own substantial computational and domain capability. Those capabilities remain distinct from the Tier One relationships through which authority and authoritative Runtime consequence acquire operational meaning.

## Conceptual model

```text
DOWNSTREAM GOVERNED COMPONENTS
language / range / retrieval / memory / coordination / research / applications
          |
          | scoped Runtime relationship where established
          v
GOVERNING CONDITIONS
identity / admission / authority / scope / context
          |
          v
TIER ONE — EHCO AI-OS RUNTIME
recognized state / lawful transition / consequence
continuity / persistence / withholding / release / recovery / proof
          |
          +----------------------+
          |                      |
          v                      v
GOVERNED WORK               TIER THREE
scoped execution            projection / reporting
and component effects       dashboards / public views
          |                      |
          +----------+-----------+
                     |
                     v
              EVIDENCE RECORDS
       bounded by source and proof ceiling
```

The arrows describe conceptual relationships only. They do not reveal internal services, ordering guarantees, private APIs, or protected control mechanics.

## Tier One — Runtime Authority

Tier One owns the governing relationships for admission and standing, authority and scope, recognized Runtime state, lawful transition and consequence, persistence and continuity, withholding/release, correction/recovery, and Runtime-originated proof.

## Downstream governed components

Persistent Tier Two software identities are downstream governed components. They can own computational language, reasoning/range, retrieval/evidence, memory/continuity, relationship, coordination, research, and domain-application capability.

A component may exist, be developed, be packaged, be realized as an application/service, or execute locally without that fact alone establishing EHCO Runtime participation. Where a Runtime corridor is established, participation is a separate scoped relationship owned by the instantiated Runtime and applicable Runtime evidence.

## Tier Three — Projection

Tier Three exposes governed information through interfaces, dashboards, reports, metrics, and public-safe views. Projection can report or explain governed information without becoming the component, evidence source, or Runtime relationship that owns the underlying state.

## Proof and evidence

EHCO public records keep evidence classes distinct. Architecture, artifact identity, declarations, tests, bounded observations, build/artifact evidence, deployment evidence, and Runtime-originated evidence establish different propositions.

The canonical public invariant vocabulary is maintained in [System Invariants](SYSTEM-INVARIANTS.md), and the detailed repository/Runtime/test-estate distinction is maintained in the [Runtime, Repository, and Test-Estate Boundary](runtime-repository-and-test-estate-boundary.md).

## Change and continuity

Continuity concerns preservation of recognized relationships, evidence, state, and governing context across change. The implementation mechanics that realize continuity remain outside the public repository.

## Public/private boundary

Security and disclosure controls are maintained in [Security and Responsible Disclosure](../SECURITY.md) and [Repository Governance](../GOVERNANCE.md). This conceptual record intentionally omits protected implementation mechanics, private topology, credentials, and operational access detail.

## Related material

- [EHCOnomics Technology Estate](EHCO-TECHNOLOGY-ESTATE.md)
- [EHCO AI-OS Public System Card](EHCO-AI-OS-SYSTEM-CARD.md)
- [System Invariants](SYSTEM-INVARIANTS.md)
- [EHCO AI-OS Instantiated System](EHCO-AI-OS-INSTANTIATED-SYSTEM.md)
- [Ecosystem Components and Runtime Relationships](ecosystem-components-and-participation.md)
- [Runtime, Repository, and Test-Estate Boundary](runtime-repository-and-test-estate-boundary.md)
- [Public Evidence Companion](../evidence/README.md)

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.1 | 2026-08-25 | Reconciled persistent component identity with scoped Runtime participation and centralized duplicate boundary/security language. |
| 1.0 | 2026-08-08 | Initial accepted conceptual Runtime architecture. |
