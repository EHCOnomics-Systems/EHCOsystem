# Repository Governance

## Purpose

This repository publishes approved public architecture, evidence, provenance, research, verification and publication materials for **EHCOsystem, EHCOnomics' Instantiated AI ecosystem**.

**EHCO AI-OS is the realized Tier One Runtime foundation and system identity.** Tier One Runtime authority and Runtime state are owned by `INSTANTIATED_EHCO_RUNTIME`. The public repository owns the public architecture/evidence representation.

## Controlling architecture

Public material follows the [Runtime, Repository, and Test-Estate Boundary](architecture/runtime-repository-and-test-estate-boundary.md) and [System Invariants](architecture/SYSTEM-INVARIANTS.md).

Publication preserves explicit ownership across component identity, Runtime participation, evidence, authority, artifact identity, Runtime identity, projection and Runtime state.

## Publication control

Public material enters the repository through a governed publication path that establishes:

- public-release approval;
- accepted source or evidence lineage;
- disclosure classification;
- evidence class and scope;
- security, confidentiality, personal-information and intellectual-property review;
- canonical repository path and integrity controls; and
- repository validation coverage.

### Pre-publication disclosure boundary

GitHub is the destination after disclosure qualification, not the first place disclosure qualification occurs.

The normal publication path is:

`PRIVATE/LOCAL WORK -> PUBLICATION CANDIDATE -> PRE-PUBLICATION DISCLOSURE GATE -> PUBLIC GITHUB REF/METADATA -> REQUIRED CI/REVIEW -> MERGE -> PUBLIC READBACK`

Before a candidate is pushed to this public repository, `verification/pre_publication_gate.py` scans the Git objects newly reachable from that candidate relative to accepted public `main`. This includes commit messages, path names, new blob content, objects introduced and later removed inside the candidate history, and the provider-visible ref name. Provider-facing narrative such as a pull-request body or release text is scanned separately before publication.

The gate uses structural public-policy checks and synthetic fixtures. It does not embed the protected private identifiers it is intended to exclude. Clearance is bound to the exact candidate SHA/tree and must be regenerated after any candidate change.

Post-push GitHub validation remains mandatory defense in depth. It is not treated as the confidentiality boundary because a public branch or pull-request object is already provider-visible by the time ordinary CI executes.

## Evidence classes

1. **Controlled EHCO architecture** — accepted architectural position.
2. **Controlled operational standing** — EHCOnomics-controlled standing record projected publicly.
3. **Artifact identity and provenance** — exact identity, revision, path, hash, manifest or packet-time binding.
4. **Declaration or anchor presence** — named construct presence in an identified artifact.
5. **Bounded test or observation** — behavior recorded for identified inputs, source, environment, method and time.
6. **Runtime-originated evidence** — authoritative Runtime state, consequence, persistence, release, revocation, recovery or proof record.
7. **External fact or incident** — documented event or requirement from an external primary source.
8. **EHCO analysis or proposition** — engineering conclusion advanced by EHCOnomics.
9. **Independent validation** — identified third-party validation under a stated method and scope.
10. **Hash-preserved historical evidence** — approved historical capture retained byte-for-byte with cryptographic identity.

## Hash-preserved evidence

Packets 00-08 remain hash-preserved Version 1 evidence. Historical paths, source labels, container names, local ports, revisions and similar capture attributes retain their packet-time meaning. Accepted interpretation is supplied through the active architecture and evidence landing records; historical packet wording remains scoped to its event time.

## Contribution policy

Public issues and corrections are welcome through the repository's public issue channels. Implementation contributions are managed through EHCOnomics' controlled development estate. Public publication focuses on architecture, evidence, verification, provenance and diligence material.

## Protected publication classes

Proprietary Runtime/component source, private source locators, protected schemas, credentials, privileged endpoints, production topology, control internals and private proof records remain under controlled custody. Public publication uses approved abstractions, exact safe evidence artifacts and public-safe source relationships.

## Change control

Accepted public architecture and standing records move through explicit EHCOnomics change control. Repository mutability, Runtime standing and Runtime state each retain their own governing owner and evidence class.

## Validation

Every pull request and every branch push runs repository validation. Acceptance also uses the repository and organization rulesets and their required status/review conditions applicable to the exact candidate at review time.

Local publisher transports must satisfy the pre-publication disclosure gate before GitHub receives the candidate. The GitHub-hosted copy of that gate is a regression/detection layer and does not retroactively make an unsafe public push confidential.

## Licensing

Repository use is governed by the root [LICENSE](LICENSE).

## Contact

Questions concerning publication, review, licensing, security or use can be directed through an official EHCOnomics contact channel.
