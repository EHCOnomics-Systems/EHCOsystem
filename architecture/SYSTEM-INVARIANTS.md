---
title: EHCO AI-OS Public System Invariants
version: 1.3
status: accepted-public-reference
published: 2026-09-01
maintainer: EHCOnomics
evidence_class: controlled-ehco-architecture
evidence_scope: canonical public separation principles
supersedes: version 1.2
---

# EHCO AI-OS Public System Invariants

The accepted standing baseline is **52/53**.

## Runtime and authority

### 1. Runtime authority has an explicit owner
`INSTANTIATED_EHCO_RUNTIME` owns Tier One Runtime authority and Runtime state.

### 2. Capability and authority are separate dimensions
A component's technical capability describes the work it can perform. Authority describes the governing basis under which work can acquire Runtime consequence.

### 3. Component identity and Runtime participation are separate dimensions
Persistent Tier Two software identities are downstream governed components. Runtime participation is scoped to an applicable Runtime corridor and owning Runtime evidence.

### 4. Tier One authority remains centralized
EHCO AI-OS is the Tier One Runtime system identity. Models, agents, applications and services operate under the governing Runtime relationships owned by `INSTANTIATED_EHCO_RUNTIME`.

### 5. Proposals follow an acceptance lifecycle
Generated plans, model output, drafts and proposed changes move through their applicable review, acceptance and commit controls.

### 6. Code artifacts and execution evidence have separate custody
Source/code identity is established by source evidence. Execution is established by execution evidence.

### 7. Package completion and Runtime realization are separate lifecycle states
Packages, builds, images and deployment-support artifacts retain their own completion state. Runtime realization retains its Runtime evidence state.

## Evidence and proof

### 8. Claims map to proof
A claim states a proposition. Proof binds that proposition to evidence, scope, authority, time and operational state.

### 9. Evidence supports governed determination
Evidence provides the basis for a determination. The designated authority owner issues the governed determination.

### 10. Artifact identity identifies artifacts
Paths, hashes, revisions, packages, file sets and manifests identify the artifacts they bind.

### 11. Execution is established by execution evidence
Source presence and declaration presence are source facts. Execution records establish executed behavior.

### 12. Enforcement is established by enforcement evidence
Declarations identify control constructs. Enforcement records establish their executed effect.

### 13. Tests establish bounded behavior
A passing test establishes behavior for the identified source, inputs, environment, method and time.

### 14. Packet integrity establishes package integrity
Manifest and hash verification establishes the identity and integrity of the declared packet contents.

### 15. Ledgers preserve evidence and history
Ledger authority remains explicit in the governing architecture.

### 16. Dashboards project governed information
Dashboard state carries the evidence/source relationship of the information it displays.

## State and standing

### 17. Scope findings remain scope-specific
Retrieval and observation results retain their stated scope and time.

### 18. Retrieval state and source truth are independently evaluated
Source authority and applicability are established through their governing evidence chain.

### 19. Unobserved lanes retain their owning evidence state
New evidence can extend, supersede or contradict that state through the applicable proof path.

### 20. Local artifact state and global Runtime state have separate owners
Repository, package, test and capture state remain source/evidence facts; Runtime state remains Runtime-owned.

### 21. Typed status and numerical standing are separate dimensions
Typed lifecycle/status labels describe their governed object. Numerical standing remains the accepted Runtime standing measure.

### 22. Runtime authority owns standing transitions
The accepted standing baseline remains **52/53** until an applicable Runtime authority and proof path establishes a transition.

## Projection and publication

### 23. Projections present governed information
Public views, reports, models and dashboards carry source/evidence attribution alongside their projected state.

### 24. Public artifact release is a publication lifecycle
Documents, dossiers, evidence packets and repository releases follow their own publication controls.

### 25. Runtime realization and production activation are independent lifecycle dimensions
Environment hosting, public ingress, operational external release, commercial activation and go-live each retain their own governing record.

## Interpretation rule

When two records differ, identify the governed object, source owner, evidence class, time/scope, and lifecycle dimension. This resolves scope differences and identifies any genuine superseding or contradictory proof.

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.3 | 2026-09-01 | Separated EHCO AI-OS Runtime system identity from `INSTANTIATED_EHCO_RUNTIME` authority/state ownership in the canonical invariants. |
| 1.2 | 2026-08-28 | Recast the canonical invariants as affirmative ownership, lifecycle and evidence principles. |
| 1.1 | 2026-08-25 | Added the component-identity/Runtime-participation invariant. |
