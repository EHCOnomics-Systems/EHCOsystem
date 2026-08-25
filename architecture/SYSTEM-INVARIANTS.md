---
title: EHCO AI-OS Public System Invariants
version: 1.1
status: accepted-public-reference
published: 2026-08-25
maintainer: EHCOnomics
evidence_class: controlled-ehco-architecture
proof_ceiling: public invariant reference; not implementation evidence or Runtime proof
supersedes: version 1.0
---

# EHCO AI-OS Public System Invariants

## Purpose

These invariants are the canonical concise public interpretation controls for the EHCOsystem. The accepted standing baseline remains **52/53**.

## Runtime and authority

### 1. Runtime != repository
A repository can preserve source, evidence, documentation, tests, manifests, and release history without becoming the Runtime.

### 2. Capability != authority
A component's technical ability to perform work does not independently establish authority for that work to acquire governed Runtime consequence.

### 3. Component identity != Runtime participation
Persistent Tier Two software identities are downstream governed components. Runtime participation is a separate scoped relationship established only by applicable Runtime evidence.

### 4. Participation != Tier One authority
A model, agent, application, service, or other component may participate within governed scope without becoming the source of Tier One Runtime authority.

### 5. Proposal != commit
A proposed change, generated plan, model output, or draft does not become an accepted system change merely because it has been produced.

### 6. Code generation != Runtime execution
Generated or stored code is an artifact until execution is established within the applicable operational context.

### 7. Package completion != Runtime realization
A package, build, image, or deployment-support artifact can be complete without becoming the realized Runtime.

## Evidence and proof

### 8. Claim != proof
A claim asserts or represents. Proof is bounded to the conditions, evidence, scope, authority, and operational state under which the claim can stand.

### 9. Evidence != authority
Evidence can support a governed determination without becoming the authority that makes the determination.

### 10. Artifact identity != Runtime identity
An exact path, hash, revision, package, file set, or manifest can identify an artifact without identifying the Runtime itself.

### 11. File presence != execution
The existence of a source file, declaration, rule, schema, or control artifact does not prove that the corresponding behavior executed.

### 12. Declaration != enforcement
A declared control establishes presence within its evidence scope. It does not, by itself, prove enforcement.

### 13. Test success != Runtime admission
A passing test can establish bounded test behavior. It does not independently establish Runtime participation, authority, standing, or universal behavioral correctness.

### 14. Packet integrity != universal behavioral proof
A packet can be complete and hash-valid while containing bounded observations, scoped discrepancies, or lanes that were not directly observed.

### 15. Ledger != authority
A ledger can preserve evidence and history without automatically acquiring Runtime authority.

### 16. Dashboard != Runtime truth
A dashboard or projection can display governed information without becoming authoritative Runtime state.

## State and standing

### 17. Scope miss != state change
Failure to retrieve or observe something within a bounded scope does not independently establish that underlying Runtime state changed.

### 18. Missing retrieval != contradiction
Failure to retrieve an applicable source or record is not itself evidence that the source or record is false.

### 19. Non-observation != demotion
A bounded test or capture that does not observe a lane does not independently demote accepted Runtime standing.

### 20. Local artifact status != global Runtime state
The status of a local file, test environment, package, repository, or capture does not automatically establish global Runtime state.

### 21. Typed status != numerical standing
Descriptive status classes do not replace the accepted numerical standing baseline.

### 22. Repository activity does not change standing
A commit, pull request, workflow result, documentation change, or publication event does not independently calculate, promote, demote, revoke, or alter Runtime standing.

The accepted standing baseline remains **52/53** unless changed by the applicable Runtime authority and proof path.

## Projection and publication

### 23. Projection != authority
Public views, reports, models, dashboards, and repository documents can make governed information visible without acquiring the authority of the system they describe.

### 24. Public artifact release != Runtime release
Publishing a document, dossier, evidence packet, or repository release is a publication event. It is not equivalent to operational Runtime release.

### 25. Runtime realization != production activation
A realized Runtime is distinct from environment-specific hosting, public ingress, operational external release, commercial activation, and go-live authorization.

## Interpretation rule

When two public records appear to differ, identify the governed object, source owner, evidence class, proof ceiling, relevant time/scope, and whether the apparent conflict is actually a scope difference. A scope difference should not be promoted into a Runtime contradiction without applicable proof.

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.1 | 2026-08-25 | Added the component-identity/Runtime-participation invariant and reconciled persistent Tier Two terminology. |
| 1.0 | 2026-08-08 | Initial accepted public invariant reference. |
