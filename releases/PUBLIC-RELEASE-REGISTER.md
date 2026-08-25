# Canonical Public Release Register

This register records public artifact identity, revision visibility, and proof ceiling for `EHCOsystem`. Shared Runtime/repository interpretation is maintained in the [Runtime, Repository, and Test-Estate Boundary](../architecture/runtime-repository-and-test-estate-boundary.md); this register remains focused on publication state.

## Status vocabulary

- **PRESENT_IN_REVISION** - present at the stated path in the Git revision containing this register. When that revision is canonical `main`, this is canonical repository visibility.
- **APPROVED_PENDING_PUBLICATION** - approved for a future public projection but not present in the revision being interpreted.
- **SCOPED_UNRESOLVED** - unresolved within a declared packet, capture, test, or publication scope.
- **NOT_PROJECTED_HERE** - not represented by the revision or record being interpreted; absence is not a Runtime state change.
- **EXCLUDED** - intentionally outside the public repository.

## Canonical public release identity

- Version: `1.0.0`
- Tag: `v1.0.0-public`
- Release title: `EHCOsystem Public Architecture and Evidence Baseline v1.0.0`

These values define the canonical identity of the first public EHCOsystem architecture and evidence baseline. This register does not by itself assert that the tag or GitHub Release has been published. The GitHub Releases surface determines live publication state.

## Public estate in this revision

| Artifact | Status | Canonical path | Proof ceiling |
|---|---|---|---|
| Repository identity and front door | PRESENT_IN_REVISION | `README.md` | Public purpose, estate orientation, evidence/diligence navigation, and canonical boundary linkage |
| EHCOnomics Technology Estate | PRESENT_IN_REVISION | `architecture/EHCO-TECHNOLOGY-ESTATE.md` | Controlled technology-estate architecture and bounded source/evidence representation |
| Ecosystem Components and Runtime Relationships | PRESENT_IN_REVISION | `architecture/ecosystem-components-and-participation.md` | Component identity and scoped Runtime-relationship architecture |
| Ecosystem Claim → Evidence Matrix | PRESENT_IN_REVISION | `assurance/ECOSYSTEM-CLAIM-EVIDENCE-MATRIX.md` | Claim/evidence navigation; inherits cited/reviewed source proof ceilings |
| Ecosystem Technical Diligence | PRESENT_IN_REVISION | `ECOSYSTEM-DILIGENCE.md` | Navigation and bounded source/evidence review method only |
| Runtime/repository/test-estate boundary | PRESENT_IN_REVISION | `architecture/runtime-repository-and-test-estate-boundary.md` | Controlling public interpretation boundary |
| Public library | PRESENT_IN_REVISION | `LIBRARY.md` | Navigation only |
| Start Here | PRESENT_IN_REVISION | `getting-started/START-HERE.md` | Navigation only |
| Reading order | PRESENT_IN_REVISION | `getting-started/reading-order.md` | Navigation only |
| Repository map | PRESENT_IN_REVISION | `getting-started/repository-map.md` | Visible repository structure only |
| Repository governance | PRESENT_IN_REVISION | `GOVERNANCE.md` | Publication and contribution control |
| Security policy | PRESENT_IN_REVISION | `SECURITY.md` | Public disclosure and reporting boundary |
| Proprietary license | PRESENT_IN_REVISION | `LICENSE` | Repository-use permissions and restrictions |
| Notice | PRESENT_IN_REVISION | `NOTICE.md` | Public purpose, evidence, IP, and implementation boundary |
| EHCO AI-OS Instantiated System | PRESENT_IN_REVISION | `architecture/EHCO-AI-OS-INSTANTIATED-SYSTEM.md` | Accepted controlled public system record |
| EHCO AI-OS Public System Card | PRESENT_IN_REVISION | `architecture/EHCO-AI-OS-SYSTEM-CARD.md` | Accepted explanatory public architecture; not Runtime proof |
| EHCO AI-OS Governed Runtime Architecture | PRESENT_IN_REVISION | `architecture/GOVERNED-RUNTIME-ARCHITECTURE.md` | Accepted conceptual public architecture; not an implementation map or Runtime proof |
| EHCO AI-OS Public System Invariants | PRESENT_IN_REVISION | `architecture/SYSTEM-INVARIANTS.md` | Canonical public invariant reference |
| Instantiated Proof Range | PRESENT_IN_REVISION | `architecture/instantiated-proof-range.md` | Accepted public proof-range record |
| Proof and Status Classes | PRESENT_IN_REVISION | `architecture/proof-and-status-classes.md` | Public proof/status vocabulary |
| EHCO Language Model | PRESENT_IN_REVISION | `language-model/README.md` | Controlled component architecture/source representation and public-test routing |
| Language Model Public Test Snapshot v1 | PRESENT_IN_REVISION | `language-model/evidence/public-test-snapshot-v1/` | Selected exact test-artifact identity and public test design |
| Public assurance index | PRESENT_IN_REVISION | `assurance/README.md` | Assurance navigation only |
| EHCO AI-OS Claim → Evidence Matrix | PRESENT_IN_REVISION | `assurance/CLAIM-EVIDENCE-MATRIX.md` | Maps selected AI-OS claims to existing public sources/proof ceilings |
| Public dossier landing page | PRESENT_IN_REVISION | `dossiers/README.md` | Dossier identity, navigation, and proof boundary |
| Public dossier PDF | PRESENT_IN_REVISION | `dossiers/EHCO_AI_OS_Governed_Operational_Architecture_Public_Edition_v1_8_LOCK_FINAL.pdf` | Controlled public architecture; SHA-256 `F489BA01961A12CF101B1F1DF57E6958456A0840BEB798B862FA97ACB030892D` |
| Public Evidence Companion overview | PRESENT_IN_REVISION | `evidence/README.md` | Navigation and packet-specific interpretation |
| Public Evidence Companion Version 1 | PRESENT_IN_REVISION | `evidence/public-evidence-companion/v1/` | Hash-preserved bounded evidence and verification surface |
| Public validation | PRESENT_IN_REVISION | `verification/` and `.github/workflows/validate-public-evidence.yml` | Repository integrity and semantic-boundary checks only |
| Public release register | PRESENT_IN_REVISION | `releases/PUBLIC-RELEASE-REGISTER.md` | Publication-state record only |

## Packet register

| Packet | Status | Proof ceiling |
|---|---|---|
| 00 - Dossier Identity and Boundary | PRESENT_IN_REVISION | Exact dossier identity and boundary only |
| 01 - Instantiated Standing | PRESENT_IN_REVISION | Bounded projection of the accepted 52/53 standing record; packet authority and standing effects are `NONE` |
| 02 - Canonical Runtime Source Binding | PRESENT_IN_REVISION | Packet-time runtime-support test/source-artifact identity, integrity, and SHA-256 provenance; not a Runtime repository, Runtime implementation, authority location, or current Runtime state |
| 03 - Tier 1 Authority Enforcement | PRESENT_IN_REVISION | Exact artifact identity and named declaration/anchor presence; declaration presence is not executed enforcement |
| 04 - Runtime Packet and Continuity Anchors | PRESENT_IN_REVISION | Artifact bindings and named declarations within the packet ceiling |
| 05 - Proof, Collapse, Recovery, Release, and Projection Anchors | PRESENT_IN_REVISION | Artifact bindings and named declarations within the packet ceiling |
| 06 - Observed Live Capture and Release Status | PRESENT_IN_REVISION | Hash-preserved historical bounded test/observation capture; integrity `PASS` is not universal behavioral `PASS`; current Runtime state is NOT_PROJECTED_HERE |
| 07 - Public Boundaries and Delivery Status | PRESENT_IN_REVISION | Architecture, standing, validation, projection, and delivery separation |
| 08 - Suite Verification and Closure | PRESENT_IN_REVISION | Package identity, manifest, receipt, and closure verification only |

Packets 00-08 remain byte-preserved. Current packet interpretation is controlled by `evidence/README.md` and the canonical boundary record; packet bytes are not rewritten to update historical terminology.

## Evidence package identity

The canonical dossier is intentionally present in two byte-identical locations:

1. `dossiers/EHCO_AI_OS_Governed_Operational_Architecture_Public_Edition_v1_8_LOCK_FINAL.pdf`
2. `evidence/public-evidence-companion/v1/00_DOSSIER_IDENTITY_AND_BOUNDARY/source_document/EHCO_AI_OS_Governed_Operational_Architecture_Public_Edition_v1_8_LOCK_FINAL.pdf`

Both retain SHA-256:

```text
F489BA01961A12CF101B1F1DF57E6958456A0840BEB798B862FA97ACB030892D
```

## Live publication interpretation

Revision presence, canonical-main visibility, and GitHub Release publication are separate publication facts. The GitHub repository/branch surface determines revision and canonical-main visibility; the GitHub Releases surface determines live Release publication state.

Moving private source/workstream state, current Runtime state beyond approved public records, and production/public-ingress/go-live state remain outside this publication register unless separately established and approved for projection.

## Required release checks

Before a revision is accepted into canonical `main`, confirm accepted authority/version, correct evidence class/proof ceiling, disclosure safety, preserved identity/integrity where applicable, correct navigation/licensing, and successful repository validation.

Public artifact visibility is a publication state. Runtime, deployment, operational release, and standing effects remain separate governed dimensions.
