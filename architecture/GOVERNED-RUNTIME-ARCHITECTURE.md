---
title: EHCO AI-OS Governed Runtime Architecture
version: 1.0
status: accepted-public-reference
published: 2026-08-08
maintainer: EHCOnomics
evidence_class: controlled-ehco-architecture
proof_ceiling: conceptual public architecture; not an implementation map or Runtime proof
---

# EHCO AI-OS Governed Runtime Architecture

## Scope

This document describes the public conceptual architecture of governed participation in EHCO AI-OS.

It is **not** an implementation sequence, network diagram, deployment topology, source map, private schema, control-flow trace, or operational access guide.

The accepted EHCO AI-OS standing baseline remains **52/53**. Nothing in this document changes Runtime standing or authority.

## Architectural objective

EHCO AI-OS is designed around a distinction between systems that **represent** operational reality and a Runtime that establishes and maintains the governing conditions under which participation has operational meaning.

Models can infer. Tools can execute. Identity systems can identify. Repositories can preserve artifacts. Dashboards can project status. Ledgers can preserve records.

None of those capabilities, by themselves, establish the complete Runtime authority relationship.

The governed Runtime architecture exists to keep identity, participation, authority, scope, state, consequence, continuity, evidence, and projection from collapsing into one another.

## Conceptual model

The following is a public conceptual model, not a literal internal processing pipeline:

```text
PARTICIPANTS AND CAPABILITIES
          |
          v
GOVERNING CONDITIONS
identity / participation / authority / scope / context
          |
          v
TIER 1 — RUNTIME AUTHORITY
recognized state / lawful transition / consequence
withholding / release / continuity / recovery / proof
          |
          +----------------------+
          |                      |
          v                      v
TIER 2 — EXECUTION         TIER 3 — PROJECTION
bounded participation      visibility / reporting
and operational work       dashboards / public views
          |                      |
          +----------+-----------+
                     |
                     v
              EVIDENCE RECORDS
       bounded by source and proof ceiling
```

The arrows describe conceptual relationships only. They do not reveal internal services, ordering guarantees, implementation components, private APIs, or control mechanics.

## Standing Baseline

EHCOnomics publicly describes a Standing Baseline as a continuously maintained foundation for the operational conditions under which people, systems, processes, services, and intelligent participants operate.

A Standing Baseline is not merely an aggregation of data.

Its role is to preserve the relationships needed to determine what participation means as conditions change, including:

- who or what is participating;
- which relationships are recognized;
- what authority and scope apply;
- what state is recognized;
- which consequences may acquire operational effect;
- what evidence can support a claim;
- how continuity is maintained across change.

The public architecture treats this maintained baseline as distinct from repeatedly reconstructing operational reality through inference alone.

## Tier 1 — Runtime Authority

Tier 1 is the authoritative Runtime layer.

Public EHCO records assign Tier 1 responsibility for:

- admission and standing;
- authority and scope;
- recognized Runtime state;
- lawful transition and consequence;
- persistence and continuity;
- withholding and release;
- correction, closure, and recovery;
- Runtime truth and Runtime-originated proof.

A downstream component can participate in these relationships without acquiring Tier 1 authority itself.

## Tier 2 — Governed Execution

Tier 2 is the execution domain for governed participants and applications.

A Tier 2 participant can carry out bounded work when the applicable Runtime relationships permit that participation.

Execution capability is therefore kept distinct from authority.

Technical ability to perform an action does not, by itself, establish the governing authority for that action to acquire operational consequence.

## Tier 3 — Projection

Tier 3 exposes governed information through projections such as interfaces, dashboards, reports, metrics, and public-safe views.

Projection is useful precisely because it makes operational information legible.

It remains subordinate to the owning evidence and Runtime relationships.

A projection can report state without creating state. It can display standing without calculating or changing standing. It can preserve visibility without becoming Runtime truth.

## Models and intelligent participants

Language models, agents, retrieval systems, and other intelligent components participate as bounded capabilities.

Their outputs can contribute interpretation, inference, retrieval, coordination, or execution within assigned roles.

They do not independently create:

- Tier 1 authority;
- Runtime standing;
- authoritative Runtime state;
- lawful consequence;
- persistence;
- release authority;
- Runtime truth.

This separation is central to the public EHCO distinction between intelligence and operational authority.

## Proof and evidence

EHCO public records separate evidence from authority.

Evidence can support a claim only within its applicable source identity, integrity controls, scope, observation conditions, and proof ceiling.

Examples of bounded public evidence include:

- artifact hashes;
- manifests;
- declared controls;
- test results;
- bounded captures;
- receipts;
- dossier statements;
- release records.

No single evidence type should impersonate another proof class.

A hash can establish integrity without establishing authority. A test can establish bounded behavior without establishing Runtime admission. A dashboard can project status without becoming Runtime truth.

## Change and continuity

A governed Runtime must preserve meaningful distinctions as participants and conditions change.

The public architecture therefore treats continuity as more than data retention. Continuity concerns the preservation of recognized relationships, evidence, state, and governing context across change.

The implementation mechanics that realize continuity remain outside the public repository.

## Withholding and uncertainty

Where a governing condition is not established, the public architecture does not permit missing information to be silently promoted into authority or proof.

This supports several public rules:

- missing retrieval is not contradiction;
- scope miss is not state change;
- non-observation is not demotion;
- assistant output is not technical evidence;
- public projection is not Runtime truth.

These rules prevent absence, uncertainty, or projection error from being mistaken for an authoritative Runtime transition.

## Public/private boundary

This document intentionally exposes **architectural properties**, not **attack surface**.

It does not publish:

- private source;
- internal control paths;
- private repository structure;
- exact internal schemas;
- privileged APIs;
- internal service identifiers;
- production network topology;
- decision thresholds;
- secret material;
- protected recovery procedures;
- exploit-relevant failure conditions.

The public architecture should remain sufficient to understand what EHCO AI-OS claims to govern without revealing how protected implementation mechanisms are constructed.

## Related material

- [EHCO AI-OS Public System Card](EHCO-AI-OS-SYSTEM-CARD.md)
- [System Invariants](SYSTEM-INVARIANTS.md)
- [EHCO AI-OS Instantiated System](EHCO-AI-OS-INSTANTIATED-SYSTEM.md)
- [Runtime, Repository, and Test-Estate Boundary](runtime-repository-and-test-estate-boundary.md)
- [Proof and Status Classes](proof-and-status-classes.md)
- [Public Evidence Companion](../evidence/README.md)
