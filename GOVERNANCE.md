# Repository Governance

## Purpose

This repository publishes approved public architecture, evidence, provenance, research, verification, and publication materials for **EHCOsystem, EHCOnomics' Instantiated AI ecosystem**.

**EHCO AI-OS is the realized Tier One Runtime foundation.** This repository is a public technical representation and evidence surface; it does not hold Runtime authority or authoritative Runtime state.

## Controlling boundary

All public material must conform to the [Runtime, Repository, and Test-Estate Boundary](architecture/runtime-repository-and-test-estate-boundary.md) and the canonical [System Invariants](architecture/SYSTEM-INVARIANTS.md).

Publication must preserve the distinctions material to the claim being made, including component identity versus scoped Runtime participation, evidence versus authority, artifact identity versus Runtime identity, and public projection versus Runtime truth. Shared invariant language should be linked rather than repeatedly restated across public pages.

## Publication control

Material may be added only when it is:

- expressly approved for public release;
- derived from an accepted public architecture, evidence source, or controlled publication record;
- stripped of unapproved implementation detail and active infrastructure information;
- classified accurately by evidence class, status, and proof ceiling;
- reviewed for security, confidentiality, personal information, and intellectual-property exposure;
- placed at its canonical repository path with identity and integrity controls preserved;
- consistent with the Runtime/repository/test-estate boundary;
- covered by the repository validation workflow.

## Evidence classes

Public claims must identify one or more applicable classes:

1. **Controlled EHCO architecture** - an accepted EHCO architectural position.
2. **Controlled operational standing** - an EHCOnomics-controlled standing record projected publicly with its proof ceiling.
3. **Artifact identity and provenance** - exact identity, revision, path, hash, manifest, or packet-time binding.
4. **Declaration or anchor presence** - presence of a named construct in an identified artifact, without an implied execution claim.
5. **Bounded test or observation** - behavior recorded for identified inputs, versions, environment, and time.
6. **Runtime-originated evidence** - authoritative Runtime state, consequence, persistence, release, revocation, recovery, or proof record.
7. **External fact or incident** - a documented event or requirement from an external primary source.
8. **EHCO analysis or proposition** - an engineering conclusion advanced by EHCOnomics.
9. **Independent validation** - an identified third-party validation under a published method and scope.
10. **Hash-preserved historical evidence** - an approved historical capture retained byte-for-byte where alteration would break declared cryptographic identity.

No class may be represented as another. EHCOnomics-controlled evidence is not described as independent certification unless a specific third-party record supports that description.

## Hash-preserved evidence

Packets 00-08 remain hash-preserved Version 1 evidence. Historical paths, source labels, container names, local ports, revisions, and similar attributes may remain inside those packets only under their applicable disclosure policy and proof ceiling.

Retention preserves packet identity; it does not make the attribute current Runtime truth, an active endpoint, a current authority location, or deployment authorization. Current interpretation is provided by the repository boundary records without rewriting packet bytes.

## Contribution policy

Public issues and corrections may be submitted. External implementation contributions are not currently accepted because this repository is documentation- and evidence-focused and is not an open-source implementation distribution.

Proposed changes must not introduce:

- a statement that a repository, folder, file set, container, workflow, or packet is the Runtime;
- unapproved private repository names or internal control locators;
- credentials, secrets, privileged endpoints, protected topology, or current deployment details;
- unsupported claims of independent certification, universal proof, exclusivity, or production completion;
- semantic promotion of packet integrity into behavioral, Runtime, deployment, or release proof.

## Change control

Changes to accepted public architecture and standing records require explicit EHCOnomics approval. Git repository mutability must not be described as physical immutability, and repository activity does not independently alter Runtime standing or Runtime truth.

## Validation

Every pull request and every push to `main` must run the repository validation workflow. Before acceptance, the then-current repository and organization rulesets must also be re-read and every applicable required check must be satisfied on the exact candidate relationship. Bypass capability is not acceptance evidence.

Validation confirms bounded repository integrity and current semantic-boundary compliance. It does not create authority, standing, deployment, production activation, operational release, or go-live authorization.

## Licensing

Repository use is governed by the root [LICENSE](LICENSE). Public availability grants only the rights expressly stated there.

## Contact

Questions concerning publication, review, licensing, security, or use should be directed through an official EHCOnomics contact channel.
