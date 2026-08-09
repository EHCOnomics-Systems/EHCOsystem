# Canonical Public Release Register

This register records what is visibly published in the `EHCOsystem` repository and the proof ceiling of each public artifact.

The repository is not the EHCO AI-OS Runtime. Repository publication, commits, workflows, manifests, packets, tests, and release records do not hold Runtime authority or independently create, promote, demote, calculate, revoke, or alter Runtime standing.

## Status vocabulary

- **VISIBLE_CURRENTLY** - present on the current `main` branch at the stated path.
- **APPROVED_PENDING_PUBLICATION** - approved for a future public projection but not visible at the canonical path.
- **SCOPED_UNRESOLVED** - unresolved within a declared packet, capture, test, or publication scope.
- **NOT_PROJECTED_HERE** - not visible in this repository; absence is not a Runtime state change.
- **EXCLUDED** - intentionally outside the public repository.

A dashboard, ledger, branch, package, repository, assistant interpretation, or scoped search result is not authority. Claims remain bound to accepted proof roots and the artifact's own proof ceiling.

## Canonical public release identity

- Version: `1.0.0`
- Tag: `v1.0.0-public`
- Release title: `EHCOsystem Public Architecture and Evidence Baseline v1.0.0`

These values define the canonical identity of the first public EHCOsystem architecture and evidence baseline. This register does not by itself assert that the tag or GitHub Release has been published. The GitHub Releases surface determines live publication state.

## Current visible public estate

| Artifact | Status | Canonical path | Proof ceiling |
|---|---|---|---|
| Repository identity | VISIBLE_CURRENTLY | `README.md` | Public purpose, navigation, and boundary only |
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
| EHCO AI-OS Public System Card | VISIBLE_CURRENTLY | `architecture/EHCO-AI-OS-SYSTEM-CARD.md` | Accepted controlled public architecture; explanatory synthesis only, not Runtime proof |
| EHCO AI-OS Governed Runtime Architecture | VISIBLE_CURRENTLY | `architecture/GOVERNED-RUNTIME-ARCHITECTURE.md` | Accepted conceptual public architecture; not an implementation map or Runtime proof |
| EHCO AI-OS Public System Invariants | VISIBLE_CURRENTLY | `architecture/SYSTEM-INVARIANTS.md` | Accepted public invariant reference; not implementation evidence or Runtime proof |
| Instantiated Proof Range | VISIBLE_CURRENTLY | `architecture/instantiated-proof-range.md` | Accepted public proof-range record |
| Ecosystem Components and Participation | VISIBLE_CURRENTLY | `architecture/ecosystem-components-and-participation.md` | Accepted public component record |
| Proof and Status Classes | VISIBLE_CURRENTLY | `architecture/proof-and-status-classes.md` | Public proof/status distinctions |
| Language-model system boundary | VISIBLE_CURRENTLY | `language-model/README.md` | Stable public system relationship only |
| Public assurance index | VISIBLE_CURRENTLY | `assurance/README.md` | Assurance navigation only; no Runtime authority or proof effect |
| Public Claim → Evidence Matrix | VISIBLE_CURRENTLY | `assurance/CLAIM-EVIDENCE-MATRIX.md` | Maps selected public claims to existing public sources and proof ceilings; creates no new Runtime proof |
| Public dossier landing page | VISIBLE_CURRENTLY | `dossiers/README.md` | Dossier identity, navigation, and proof boundary |
| Public dossier PDF | VISIBLE_CURRENTLY | `dossiers/EHCO_AI_OS_Governed_Operational_Architecture_Public_Edition_v1_8_LOCK_FINAL.pdf` | Controlled public architecture; SHA-256 `F489BA01961A12CF101B1F1DF57E6958456A0840BEB798B862FA97ACB030892D` |
| Public Evidence Companion overview | VISIBLE_CURRENTLY | `evidence/README.md` | Navigation and current packet interpretation |
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

Packets 00-08 remain byte-preserved. Current interpretation is controlled by `evidence/README.md` and `architecture/runtime-repository-and-test-estate-boundary.md`; packet bytes are not rewritten to update historical terminology.

## Evidence package identity

The canonical dossier is intentionally present in two byte-identical locations:

1. `dossiers/EHCO_AI_OS_Governed_Operational_Architecture_Public_Edition_v1_8_LOCK_FINAL.pdf`
2. `evidence/public-evidence-companion/v1/00_DOSSIER_IDENTITY_AND_BOUNDARY/source_document/EHCO_AI_OS_Governed_Operational_Architecture_Public_Edition_v1_8_LOCK_FINAL.pdf`

Both retain SHA-256:

```text
F489BA01961A12CF101B1F1DF57E6958456A0840BEB798B862FA97ACB030892D
```

Packet 06 preserves direct discrepancies and not-directly-observed lanes as **SCOPED_UNRESOLVED** within its historical capture. Packet 08 preserves `external_release_authorized: false`, `production_activation_authorized: false`, and `final_zip_created: false` for that suite. Public visibility does not override packet-level status boundaries.

## Independent validation boundary

The accepted 52/53 standing baseline is an EHCOnomics-controlled operational standing record. The repository establishes the identity, integrity, provenance, scope, and declared proof ceilings of its controlled public artifacts. Independent third-party certification is not claimed unless an identified record expressly states it.

## Not currently projected

| Area | Status | Current determination |
|---|---|---|
| Moving private language-model workstream state | NOT_PROJECTED_HERE | Exact private commits, pull requests, gaps, activation decisions, and next-operation controls are intentionally not mirrored |
| Current private test/source-estate state | NOT_PROJECTED_HERE | Public packets preserve approved packet-time artifact provenance only |
| Current Runtime state beyond approved public records | NOT_PROJECTED_HERE | Repository and packets are not Runtime authority or live Runtime projection |
| Production activation, public ingress, operational external release, and go-live | NOT_PROJECTED_HERE | Each requires its own governing evidence and authorization |

## Excluded material

The following remain excluded unless a separately approved public edition is created:

- proprietary Runtime and participant implementation mechanics;
- protected Instantiation Bridge mechanics, private schemas, verifier internals, credentials, keys, tokens, active privileged endpoints, and production topology;
- moving private development ledgers and workstream controls;
- customer, personal, financial, tax, debt, management, investor-only, and confidential commercial records.

## Required release checks

Before an artifact becomes **VISIBLE_CURRENTLY**, confirm:

1. accepted authority and exact approved version;
2. alignment with the Runtime/repository/test-estate boundary;
3. accurate evidence class, status, and proof ceiling;
4. no unapproved proprietary, security-sensitive, personal, customer, financial, or infrastructure disclosure;
5. preserved hash, manifest, filename, and package structure where applicable;
6. correct presentation, navigation, licensing, and linkage;
7. successful repository validation.

Repository publication is evidence of visibility, not Runtime authority or operational release authorization.
