---
title: Proof and Status Classes
version: 1.4
status: accepted-public-record
published: 2026-08-28
maintainer: EHCOnomics
evidence_class: controlled-ehco-proof-record
supersedes: version 1.3
---

# Proof and Status Classes

EHCOsystem tracks Runtime, component identity, Runtime participation, artifact, declaration, test, observation, deployment, evidence, publication and release states as explicit independent classes.

## Runtime classes

### Runtime realized
EHCO AI-OS exists as the realized Tier One Runtime.

### Runtime standing
The accepted standing baseline is **52/53**. Standing transitions are established through the applicable Runtime authority and proof path.

### Runtime participant / admitted relationship
A downstream governed component, person, service or operation participates through a scoped relationship established by governing admission/binding evidence.

### Runtime evidenced
Runtime-originated records establish authoritative operational state, consequence, persistence, release, revocation, recovery and other governed effects within their scope.

## Artifact and evidence classes

### Artifact identified
An exact file, folder snapshot, manifest, image, package or document is identified by path, revision, hash, byte count or another declared identity control.

### Declaration present
A named class, function, route, rule, manifest entry or control declaration is present in an identified artifact.

### Build or test verified
A bounded build, test, lint, typing, compatibility, security, image or workflow result is verified for the stated artifact revision, inputs, method and environment.

### Behavior observed
A bounded capture or test records behavior for identified inputs, versions, environment and time.

### Packet integrity verified
A packet's declared files, manifests, hashes, receipts and closure conditions match their declared identity.

### Publicly evidenced
A public-safe dossier, packet, manifest, receipt, capture or verification record establishes its stated public evidence scope.

### Independently validated
An identified third party performs and publishes an applicable validation under a stated method and scope.

## Delivery classes

### Deployment supported
Artifacts and mechanics support deployment into a defined environment.

### Production activated
A production environment is expressly authorized and activated under its governing record.

### Public ingress authorized
External access is expressly authorized under its security and release controls.

### Operationally released
A system or service is expressly authorized for external operational use.

### Public artifact released
A document or evidence artifact is published through the canonical public record with applicable identity, integrity and evidence scope.

## Controlled vocabulary

- **PROVEN** — established within an expressly identified proof scope.
- **BOUND_BY_PRIOR_PROOF** — preserved by an accepted proof root.
- **PRESENT_IN_REVISION** — present in the Git revision being interpreted.
- **CURRENT_RUNTIME_EVIDENCE_REQUIRED** — current Runtime evidence owns the proposition.
- **SOURCE_REVIEW_REQUIRED** — owning source review establishes the proposition.
- **CONTRADICTED_BY_VALID_PROOF** — displaced by accepted contradiction proof.

## Related material

- [Runtime, Repository, and Test-Estate Boundary](runtime-repository-and-test-estate-boundary.md)
- [System Invariants](SYSTEM-INVARIANTS.md)
- [Instantiated Proof Range](instantiated-proof-range.md)
- [Public Evidence Companion](../evidence/README.md)

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.4 | 2026-08-28 | Recast evidence and lifecycle classes as affirmative state definitions. |
| 1.3 | 2026-08-25 | Separated persistent component identity from scoped Runtime relationships. |
