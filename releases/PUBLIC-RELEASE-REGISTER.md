# Canonical Public Release Register

This register records canonical public artifact identity, visibility, and proof ceiling for the `EHCOsystem` repository. Shared Runtime/repository interpretation is maintained in the [Runtime, Repository, and Test-Estate Boundary](../architecture/runtime-repository-and-test-estate-boundary.md); this register remains focused on publication state.

## Status vocabulary

- **VISIBLE_CURRENTLY** - present on the current `main` branch at the stated path.
- **APPROVED_PENDING_PUBLICATION** - approved for a future public projection but not visible at the canonical path.
- **SCOPED_UNRESOLVED** - unresolved within a declared packet, capture, test, or publication scope.
- **NOT_PROJECTED_HERE** - not visible in this repository; absence is not a Runtime state change.
- **EXCLUDED** - intentionally outside the public repository.

## Canonical public release identity

- Version: `1.0.0`
- Tag: `v1.0.0-public`
- Release title: `EHCOsystem Public Architecture and Evidence Baseline v1.0.0`

These values define the canonical identity of the first public EHCOsystem architecture and evidence baseline. This register does not by itself assert that the tag or GitHub Release has been published. The GitHub Releases surface determines live publication state.

## Current visible public estate

| Artifact | Status | Canonical path | Proof ceiling |
|---|---|---|---|
| Repository identity and front door | VISIBLE_CURRENTLY | `README.md` | Public purpose, estate orientation, evidence/diligence navigation, and canonical boundary linkage |
| EHCOnomics Technology Estate | VISIBLE_CURRENTLY | `architecture/EHCO-TECHNOLOGY-ESTATE.md` | Controlled technology-estate architecture and bounded source/evidence representation |
| Ecosystem Components and Runtime Relationships | VISIBLE_CURRENTLY | `architecture/ecosystem-components-and-participation.md` | Component identity and scoped Runtime-relationship architecture |
| Ecosystem Claim → Evidence Matrix | VISIBLE_CURRENTLY | `assurance/ECOSYSTEM-CLAIM-EVIDENCE-MATRIX.md` | Claim/evidence navigation; inherits cited/reviewed source proof ceilings |
| Ecosystem Technical Diligence | VISIBLE_CURRENTLY | `ECOSYSTEM-DILIGENCE.md` | Navigation and bounded source/evidence review method only |
| Runtime/repository/test-estate boundary | VISIBLE_CURRENTLY | `architecture/runtime-repository-and-test-estate-boundary.md` | Controlling public interpretation boundary |
| Public library | VISIBLE_CURRENTLY | `LIBRARY.md` | Navigation only |
| Start Here | VISIBLE_CURRENTLY | `getting-started/START-HERE.md` | Navigation only |
| Reading order | VISIBLE_CURRENTLY | `getting-started/reading-order.md` | Navigation only |
| Repository map | VISIBLE_CURRENTLY | `getting-started/repository-map.md` | Visible repository structure only |
| Repository governance | VISIBLE_CURRENTLY | `GOVERNANCE.md` | Publication and contribution control |
| Security policy | VISIBLE_CURRENTLY | `SECURITY.md` | Public disclosure and reporting boundary |
| Proprietary license | VISIBLE_CURRENTLY | `LICENSE` | Repository-use permissions and restrictions |
| Notice | VISIBLE_CURRENTLY | `NOTICE.md` | Public purpose, evidence, IP, and implementation boundary |
| EHCO AI-OS Instantiated System | VISIBLE_CURRENTLY | `architecture/EHCO-AI-OS-INSTANTIATED-SYSTEM.md` | Accepted controlled public system record |
| EHCO AI-OS Public System Card | VISIBLE_CURRENTLY | `architecture/EHCO-AI-OS-SYSTEM-CARD.md` | Accepted explanatory public architecture; not Runtime proof |
| EHCO AI-OS Governed Runtime Architecture | VISIBLE_CURRENTLY | `architecture/GOVERNED-RUNTIME-ARCHITECTURE.md` | Accepted conceptual public architecture; not an implementation map or Runtime proof |
| EHCO AI-OS Public System Invariants | VISIBLE_CURRENTLY | `architecture/SYSTEM-INVARIANTS.md` | Canonical public invariant reference |
| Instantiated Proof Range | VISIBLE_CURRENTLY | `architecture/instantiated-proof-range.md` | Accepted public proof-range record |
| Proof and Status Classes | VISIBLE_CURRENTLY | `architecture/proof-and-status-classes.md` | Public proof/status vocabulary |
| EHCO Language Model | VISIBLE_CURRENTLY | `language-model/README.md` | Controlled component architecture/source representation and public-test routing |
| Language Model Public Test Snapshot v1 | VISIBLE_CURRENTLY | `language-model/evidence/public-test-snapshot-v1/` | Selected exact test-artifact identity and public test design |
| Public assurance index | VISIBLE_CURRENTLY | `assurance/README.md` | Assurance navigation only |
| EHCO AI-OS Claim → Evidence Matrix | VISIBLE_CURRENTLY | `assurance/CLAIM-EVIDENCE-MATRIX.md` | Maps selected AI-OS claims to existing public sources/proof ceilings |
| Public dossier landing page | VISIBLE_CURRENTLY | `dossiers/README.md` | Dossier identity, navigation, and proof boundary |
| Public dossier PDF | VISIBLE_CURRENTLY | `dossiers/EHCO_AI_OS_Governed_Operational_Architecture_Public_Edition_v1_8_LOCK_FINAL.pdf` | Controlled public architecture; SHA-256 `F489BA01961A12CF101B1F1DF57E6958456A0840BEB798B862FA97ACB030892D` |
| Public Evidence Companion overview | VISIBLE_CURRENTLY | `evidence/README.md` | Navigation and packet-specific interpretation |
| Public Evidence Companion Version 1 | VISIBLE_CURRENTLY | `evidence/public-evidence-companion/v1/` | Hash-preserved bounded evidence and verification surface |
| Public validation | VISIBLE_CURRENTLY | `verification/` and `.github/workflows/validate-public-evidence.yml` | Repository integrity and semantic-boundary checks only |
| Public release register | VISIBLE_CURRENTLY | `releases/PUBLIC-RELEASE-REGISTER.md` | Publication-state record only |

## Packet register

| Packet | Status | Proof ceiling |
|---|---|---|
| 00 - Dossier Identity and Boundary | VISIBLE_CURRENTLY | Exact dossier identity and boundary only |
| 01 - Instantiated Standing | VISIBLE_CURRENTLY | Bounded projection of the accepted 52/53 standing record; packet authority and standing effects are `NONE` |
| 02 - Canonical Runtime Source Binding | VISIBLE_CURRENTLY | Packet-time runtime-support test/source-artifact identity, integrity, and SHA-256 provenance; not a Runtime repository, Runtime implementation, authority location, or current Runtime state |
| 03 - Tier 1 Authority Enforcement | VISIBLE_CURRENTLY | Exact artifact identity and named declaration/anchor presence; declaration presence is not executed enforcement |
| 04 - Runtime Packet and Continuity Anchors | VISIBLE_CURRENTLY | Artifact bindings and named declarations within the packet ceiling |
| 05 - Proof, Collapse, Recovery, Release, and Projection Anchors | VISIBLE_CURRENTLY | Artifact bindings and named declarations within the packet ceiling |
| 06 - Observed Live Capture and Release Status | VISIBLE_CURRENTLY | Hash-preserved historical bounded test/observation capture; integrity `PASS` is not universal behavioral `PASS`; current Runtime state is NOT_PROJECTED_HERE |
| 07 - Public Boundaries and Delivery Status | VISIBLE_CURRENTLY | Architecture, standing, validation, projection, and delivery separation |
| 08 - Suite Verification and Closure | VISIBLE_CURRENTLY | Package identity, manifest, receipt, and closure verification only |

Packets 00-08 remain byte-preserved. Current packet interpretation is controlled by `evidence/README.md` and the canonical boundary record; packet bytes are not rewritten to update historical terminology.

## Evidence package identity

The canonical dossier is intentionally present in two byte-identical locations:

1. `dossiers/EHCO_AI_OS_Governed_Operational_Architecture_Public_Edition_v1_8_LOCK_FINAL.pdf`
2. `evidence/public-evidence-companion/v1/00_DOSSIER_IDENTITY_AND_BOUNDARY/source_document/EHCO_AI_OS_Governed_Operational_Architecture_Public_Edition_v1_8_LOCK_FINAL.pdf`

Both retain SHA-256:

```text
F489BA01961A12CF101B1F1DF57E6958456A0840BEB798B862FA97ACB030892D
```

## Not currently projected

Moving private source/workstream state, current Runtime state beyond approved public records, and production/public-ingress/go-live state remain outside this publication register unless separately established and approved for projection.

## Required release checks

Before an artifact becomes **VISIBLE_CURRENTLY**, confirm accepted authority/version, correct evidence class/proof ceiling, disclosure safety, preserved identity/integrity where applicable, correct navigation/licensing, and successful repository validation.

Public artifact visibility is a publication state. Runtime, deployment, operational release, and standing effects remain separate governed dimensions.
