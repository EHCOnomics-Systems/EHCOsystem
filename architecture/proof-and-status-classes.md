---
title: Proof and Status Classes
version: 1.3
status: accepted-public-record
published: 2026-08-25
maintainer: EHCOnomics
evidence_class: controlled-ehco-proof-record
supersedes: version 1.2
---

# Proof and Status Classes

The EHCOsystem keeps Runtime, component identity, Runtime participation, artifact, declaration, test, observation, deployment, evidence, publication, and release states distinct. No class may be promoted into another without an applicable governing record.

## Runtime classes

### Runtime realized
EHCO AI-OS exists as the realized Tier One Runtime. Runtime realization is not created by a repository, source folder, build, test, packet, container, dashboard, or public document.

### Runtime standing
The accepted standing baseline is **52/53**. Standing changes only through the applicable Runtime authority and proof path.

### Runtime participant / admitted relationship
A downstream governed component, person, service, or operation is Runtime-participating only for a scoped relationship established by the governing admission/binding evidence. Persistent component identity alone does not establish participation.

### Runtime evidenced
A Runtime-originated record establishes authoritative operational state, consequence, persistence, release, revocation, recovery, or another governed effect within its scope.

## Artifact and evidence classes

### Artifact identified
An exact file, folder snapshot, manifest, image, package, or document is identified by path, revision, hash, byte count, or another declared identity control.

### Declaration present
A named class, function, route, rule, manifest entry, or control declaration is present in an identified artifact. Presence is not executed enforcement.

### Build or test verified
A bounded build, test, lint, typing, compatibility, security, image, or workflow result has been verified for the stated artifact revision and environment. A passing result is not Runtime admission or universal behavioral proof.

### Behavior observed
A bounded capture or test records behavior for identified inputs, versions, environment, and time. Historical observation is not current Runtime state unless a governing Runtime-originated record binds it.

### Packet integrity verified
A packet's declared files, manifests, hashes, receipts, and closure conditions match. Packet-integrity `PASS` does not convert mixed evidence, unresolved discrepancies, or unobserved lanes into behavioral passes.

### Publicly evidenced
A public-safe dossier, packet, manifest, receipt, capture, or verification record establishes the stated public proof range and no more.

### Independently validated
An identified third party has performed and published an applicable validation under a stated method and scope. Independent validation is not inferred from EHCOnomics-controlled records.

## Delivery classes

### Deployment supported
Artifacts or mechanics support deployment into a defined environment. This does not automatically establish production activation, public ingress, operational external release, or go-live.

### Production activated
A production environment has been expressly authorized and activated under its own governing record.

### Public ingress authorized
External access has been expressly authorized under its own security and release controls.

### Operationally released
A system or service has been expressly authorized for external operational use.

### Public artifact released
A document or evidence artifact has been published through the canonical public record with its applicable identity, integrity, and proof ceiling. Public artifact release is not Runtime release.

## Controlled vocabulary

- **PROVEN** - established within an expressly identified proof scope.
- **BOUND_BY_PRIOR_PROOF** - preserved by an accepted proof root.
- **VISIBLE_CURRENTLY** - present in the current public repository.
- **SCOPED_UNRESOLVED** - unresolved within the stated packet, test, capture, or publication scope.
- **NOT_PROJECTED_HERE** - not represented by the current public source.
- **SOURCE_UNAVAILABLE** - the required source cannot be inspected in the stated scope.
- **CONTRADICTED_BY_VALID_PROOF** - displaced by an accepted contradiction proof.

## Related material

- [Runtime, Repository, and Test-Estate Boundary](runtime-repository-and-test-estate-boundary.md)
- [System Invariants](SYSTEM-INVARIANTS.md)
- [Instantiated Proof Range](instantiated-proof-range.md)
- [Public Evidence Companion](../evidence/README.md)

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.3 | 2026-08-25 | Separated persistent component identity from scoped Runtime-participant/admitted relationships. |
| 1.2 | 2026-08-05 | Added explicit Runtime, artifact, declaration, test, observation, packet-integrity, independent-validation, and delivery classes. |
| 1.1 | 2026-08-05 | Added deployment/release separation and packet-time provenance boundaries. |
| 1.0 | 2026-08-04 | Initial public proof and status classes. |
