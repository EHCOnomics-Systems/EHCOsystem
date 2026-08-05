# Repository Governance

## Purpose

This repository publishes approved public architecture, evidence, provenance, research, verification, and publication materials of the EHCOsystem.

EHCO AI-OS is the realized Tier 1 Runtime. This repository is not the Runtime and does not govern Runtime authority, standing, authoritative state, transition, consequence, persistence, recovery, withholding, release, closure, or Runtime truth.

## Controlling boundary

All public material must conform to the [Runtime, Repository, and Test-Estate Boundary](architecture/runtime-repository-and-test-estate-boundary.md).

The following distinctions are mandatory:

- repository is not Runtime;
- file identity is not Runtime identity;
- declaration presence is not executed enforcement;
- build or test success is not Runtime admission;
- packet integrity is not universal behavioral proof;
- historical observation is not current Runtime state;
- public visibility is not Runtime authority;
- scope miss is not state change.

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

Changes to the accepted public standing and architecture records require explicit EHCOnomics approval. The applicable records are hash-bound or version-controlled public baselines; Git repository mutability must not be described as physical immutability.

Later research, testing, development, deployment, and ecosystem findings remain distinguishable from accepted Runtime standing. A dashboard, ledger, branch, package, assistant interpretation, repository status, or scoped search result does not independently change accepted standing or Runtime truth.

## Validation

Every pull request and every push to `main` must run the repository validation workflow. Validation confirms bounded repository integrity and current semantic-boundary compliance. It does not create authority, standing, deployment, production activation, operational release, or go-live authorization.

## Licensing

Repository use is governed by the root [LICENSE](LICENSE). Public availability grants only the rights expressly stated there.

## Contact

Questions concerning publication, review, licensing, security, or use should be directed through an official EHCOnomics contact channel.
