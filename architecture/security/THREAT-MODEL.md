---
title: EHCO AI-OS Public Threat Model
version: 1.0
status: accepted-public-security-reference
published: 2026-08-08
maintainer: EHCOnomics
evidence_class: controlled-ehco-architecture
proof_ceiling: public threat classes, security objectives, and mitigation categories only; not an implementation map or security certification
---

# EHCO AI-OS Public Threat Model

## Scope

This document describes public threat classes against the architectural distinctions already published for EHCO AI-OS.

It intentionally does **not** disclose private source, internal detection logic, protected enforcement mechanics, control thresholds, private schemas, privileged APIs, production topology, credentials, recovery internals, or exploit-enabling bypass sequences.

The accepted EHCO AI-OS standing remains **52/53**. This threat model does not calculate or alter standing and does not constitute Runtime-originated proof or independent security certification.

## Protected architectural properties

The public EHCO architecture seeks to preserve the following distinctions:

- Runtime authority remains distinct from repository state, model output, tools, execution capability, dashboards, ledgers, packets, and other projections.
- Participation or capability does not independently create Tier 1 authority.
- Artifact identity does not become Runtime identity.
- Declaration presence does not become executed enforcement.
- Bounded test success does not become Runtime admission or universal behavioral proof.
- Evidence remains bounded to its source, scope, time, evidence class, and proof ceiling.
- Projection remains subordinate to the owning evidence and Runtime relationships.
- Missing retrieval, scope miss, or non-observation does not silently become a Runtime state change.
- Runtime realization remains distinct from production activation, public ingress, operational external release, commercial activation, and go-live.

## Threat classes

### Authority impersonation

A component, model, tool, repository artifact, credential-bearing process, or projection may be represented as if it independently holds authority it does not possess.

**Security objective:** preserve the distinction between capability, participation, delegated scope, and Tier 1 Runtime authority.

**Public mitigation categories:** explicit tier boundaries; standing/authority separation; proof-class discipline; controlled interpretation records.

### Scope expansion

A participant may be treated as authorized beyond the bounded role or context under which it was admitted or evaluated.

**Security objective:** prevent technical capability, discovered capability, or changed context from silently expanding governing scope.

**Public mitigation categories:** bounded participation; explicit scope relationships; renewed governance interpretation when material conditions differ; withholding where applicable governing conditions are not established.

### Projection confusion

A dashboard, ledger, report, repository document, model output, or public evidence artifact may be mistaken for authoritative Runtime state or Runtime truth.

**Security objective:** prevent representations of state from acquiring the authority of the state they represent.

**Public mitigation categories:** Tier 3 projection boundary; source ownership; proof ceilings; explicit non-claims in public records.

### Evidence promotion

Artifact hashes, declarations, tests, captures, packet integrity, or other bounded evidence may be promoted into a stronger proof class than the evidence supports.

**Security objective:** keep every claim within its applicable evidence class and proof ceiling.

**Public mitigation categories:** claim/evidence mapping; packet-specific proof ceilings; status classes; repository semantic-boundary validation.

### Stale-state substitution

Historical captures or packet-time artifact records may be interpreted as current Runtime state, current topology, or current authority location.

**Security objective:** prevent historical evidence from silently becoming current operational truth.

**Public mitigation categories:** historical-capture classification; `NOT_PROJECTED_HERE` for current Runtime state where appropriate; public Runtime/repository/test-estate boundary records.

### Non-observation promotion

Missing retrieval, an unobserved lane, or a scoped test miss may be interpreted as a contradiction, defect, demotion, or authoritative state transition.

**Security objective:** preserve the distinction between absence of observation and evidence of state change.

**Public mitigation categories:** scope discipline; explicit `SCOPED_UNRESOLVED` status where applicable; system invariants governing scope miss and non-observation.

### Continuity degradation

Changes in participants, context, evidence, or system conditions may cause previously recognized relationships to be misapplied, lost, or reconstructed incorrectly.

**Security objective:** preserve meaningful continuity of recognized relationships and evidence across change without treating stale context as current authority.

**Public mitigation categories:** continuity as a distinct Runtime concern; bounded state/evidence relationships; correction, recovery, withholding, and release as separate governing concerns.

### Publication leakage

Public documentation, evidence, pull requests, issues, workflows, or release materials may accidentally expose protected implementation details or operational infrastructure.

**Security objective:** maintain a public architecture and assurance surface without exposing private implementation or increasing attack surface unnecessarily.

**Public mitigation categories:** publication governance; responsible-disclosure rules; secret and semantic-boundary checks; code ownership; review templates; proof-ceiling review; explicit exclusion of private source, schemas, control paths, credentials, active endpoints, and topology.

### Supply-chain drift in repository automation

Mutable third-party workflow references or unreviewed automation changes may alter repository validation behavior over time.

**Security objective:** keep repository-side validation dependencies reviewable and intentionally version-bound.

**Public mitigation categories:** immutable action pinning; least-privilege workflow permissions; explicit validation workflows; exact-head pull-request checks.

## Trust boundaries

The public model distinguishes at least these conceptual boundaries:

1. **Runtime authority boundary** — separates Tier 1 Runtime authority from downstream participants, tools, models, repositories, evidence stores, and projections.
2. **Execution boundary** — separates bounded execution capability from the authority for actions to acquire governed consequence.
3. **Projection boundary** — separates visible representations from Runtime truth and authoritative state.
4. **Evidence boundary** — separates artifact identity, declarations, tests, observations, and package integrity from stronger Runtime-originated proof classes.
5. **Publication boundary** — separates public architecture/evidence from protected implementation and operational infrastructure.

These are conceptual public boundaries, not network zones or internal service maps.

## Security non-claims

This document does not claim:

- that every implementation or deployment is secure;
- that repository validation is equivalent to Runtime security validation;
- that public threat coverage is exhaustive;
- that protected mitigations are implemented by any particular private mechanism;
- that no undisclosed threat exists;
- that accepted standing 52/53 is an independent third-party security certification.

## Related public records

- [EHCO AI-OS Public System Card](../EHCO-AI-OS-SYSTEM-CARD.md)
- [Governed Runtime Architecture](../GOVERNED-RUNTIME-ARCHITECTURE.md)
- [System Invariants](../SYSTEM-INVARIANTS.md)
- [Runtime, Repository, and Test-Estate Boundary](../runtime-repository-and-test-estate-boundary.md)
- [Public Claim → Evidence Matrix](../../assurance/CLAIM-EVIDENCE-MATRIX.md)
- [Security and Responsible Disclosure](../../SECURITY.md)
