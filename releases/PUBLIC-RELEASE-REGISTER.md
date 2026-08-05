# Canonical Public Release Register

This register records what is visibly published in the EHCOsystem repository, where each artifact belongs, and what proof ceiling applies. It distinguishes repository publication from Runtime authority, deployment, production activation, public ingress, operational external release, and go-live authorization.

## Status vocabulary

- **VISIBLE_CURRENTLY** — present on the current `main` branch at the stated canonical path.
- **APPROVED_PENDING_PUBLICATION** — approved for a future public projection but not visible at the canonical path.
- **SCOPED_UNRESOLVED** — within a declared publication scope, but canonical version, approval, or placement remains unresolved.
- **NOT_PROJECTED_HERE** — not visible in this repository; absence is not a Runtime state change.
- **EXCLUDED** — intentionally outside the public repository.

A dashboard, ledger, branch, package, assistant interpretation, or scoped search result is not authority. Accepted proof roots and the artifact's own status record govern its claims.

## Current visible public estate

| Artifact | Status | Canonical path | Proof ceiling |
|---|---|---|---|
| Repository identity | VISIBLE_CURRENTLY | `README.md` | Public repository purpose, navigation, and boundary only |
| Public library index | VISIBLE_CURRENTLY | `LIBRARY.md` | Navigation only |
| Start Here guide | VISIBLE_CURRENTLY | `getting-started/START-HERE.md` | Navigation only |
| Reading order | VISIBLE_CURRENTLY | `getting-started/reading-order.md` | Navigation only |
| Repository map | VISIBLE_CURRENTLY | `getting-started/repository-map.md` | Visible repository structure only |
| Repository governance | VISIBLE_CURRENTLY | `GOVERNANCE.md` | Publication and contribution control |
| Security policy | VISIBLE_CURRENTLY | `SECURITY.md` | Public disclosure and reporting boundary |
| IP and evidence notice | VISIBLE_CURRENTLY | `NOTICE.md` | Public IP and evidence boundary |
| EHCO AI-OS Instantiated System | VISIBLE_CURRENTLY | `architecture/EHCO-AI-OS-INSTANTIATED-SYSTEM.md` | Accepted public system record |
| Instantiated Proof Range | VISIBLE_CURRENTLY | `architecture/instantiated-proof-range.md` | Accepted public proof-range record |
| Ecosystem Components and Participation | VISIBLE_CURRENTLY | `architecture/ecosystem-components-and-participation.md` | Accepted public system record |
| Proof and Status Classes | VISIBLE_CURRENTLY | `architecture/proof-and-status-classes.md` | Public proof/status distinctions |
| EHCO language-model finalization | VISIBLE_CURRENTLY | `language-model/README.md` | Controlled public development and source-lineage record |
| Public architecture dossier landing page | VISIBLE_CURRENTLY | `dossiers/README.md` | Dossier identity, navigation, and proof boundary |
| Public architecture dossier PDF | VISIBLE_CURRENTLY | `dossiers/EHCO_AI_OS_Governed_Operational_Architecture_Public_Edition_v1_8_LOCK_FINAL.pdf` | Controlled public architecture; SHA-256 `F489BA01961A12CF101B1F1DF57E6958456A0840BEB798B862FA97ACB030892D` |
| Public Evidence Companion overview | VISIBLE_CURRENTLY | `evidence/README.md` | Navigation and packet proof ceilings |
| Public Evidence Companion Version 1 | VISIBLE_CURRENTLY | `evidence/public-evidence-companion/v1/` | Bounded public evidence and verification surface |
| Packet 00 — Dossier Identity and Boundary | VISIBLE_CURRENTLY | `evidence/public-evidence-companion/v1/00_DOSSIER_IDENTITY_AND_BOUNDARY/` | Dossier identity and boundary only |
| Packet 01 — Instantiated Standing | VISIBLE_CURRENTLY | `evidence/public-evidence-companion/v1/01_INSTANTIATED_STANDING/` | Accepted baseline projection and status boundary |
| Packet 02 — Canonical Runtime Source Binding | VISIBLE_CURRENTLY | `evidence/public-evidence-companion/v1/02_CANONICAL_RUNTIME_SOURCE_BINDING/` | Source identity and SHA-256 binding |
| Packet 03 — Tier 1 Authority Enforcement | VISIBLE_CURRENTLY | `evidence/public-evidence-companion/v1/03_TIER1_AUTHORITY_ENFORCEMENT/` | Presence of named enforcement anchors |
| Packet 04 — Runtime Packet and Continuity Anchors | VISIBLE_CURRENTLY | `evidence/public-evidence-companion/v1/04_RUNTIME_PACKET_AND_CONTINUITY_ANCHORS/` | Source bindings and named declarations |
| Packet 05 — Proof, Collapse, Recovery, Release, and Projection Anchors | VISIBLE_CURRENTLY | `evidence/public-evidence-companion/v1/05_PROOF_COLLAPSE_RECOVERY_AND_RELEASE_ANCHORS/` | Source bindings and named declarations |
| Packet 06 — Observed Live Capture and Release Status | VISIBLE_CURRENTLY | `evidence/public-evidence-companion/v1/06_OBSERVED_LIVE_CAPTURE_AND_RELEASE_STATUS/` | Hash-bound observation, mixed status, discrepancies, and open gaps |
| Packet 07 — Public Boundaries and Delivery Status | VISIBLE_CURRENTLY | `evidence/public-evidence-companion/v1/07_PUBLIC_BOUNDARIES_AND_DELIVERY_STATUS/` | Architecture/standing/validation/projection/delivery separation |
| Packet 08 — Suite Verification and Closure | VISIBLE_CURRENTLY | `evidence/public-evidence-companion/v1/08_SUITE_VERIFICATION_AND_FINAL_ZIP/` | Package verification and closure boundary; final ZIP not declared as created |
| Public evidence validation | VISIBLE_CURRENTLY | `verification/` and `.github/workflows/validate-public-evidence.yml` | Repository integrity checks only |
| Canonical public release register | VISIBLE_CURRENTLY | `releases/PUBLIC-RELEASE-REGISTER.md` | Publication-state record only |

## Evidence package identity

The canonical dossier is intentionally present in two byte-identical locations:

1. `dossiers/EHCO_AI_OS_Governed_Operational_Architecture_Public_Edition_v1_8_LOCK_FINAL.pdf`
2. `evidence/public-evidence-companion/v1/00_DOSSIER_IDENTITY_AND_BOUNDARY/source_document/EHCO_AI_OS_Governed_Operational_Architecture_Public_Edition_v1_8_LOCK_FINAL.pdf`

Both must retain SHA-256:

```text
F489BA01961A12CF101B1F1DF57E6958456A0840BEB798B862FA97ACB030892D
```

Packet 08 records `external_release_authorized: false`, `production_activation_authorized: false`, and `final_zip_created: false`. Public repository visibility does not override those packet-level status boundaries.

## Not currently projected

| Area | Status | Intended or previously discussed path | Current determination |
|---|---|---|---|
| Immutable Runtime baseline document | SCOPED_UNRESOLVED | `architecture/runtime-baseline.md` | No canonical file is visible at this path; do not describe it as published here |
| Ecosystem governance discovery | NOT_PROJECTED_HERE | `architecture/ecosystem-governance-discovery.md` | Requires separate approval and publication |
| Public glossary | NOT_PROJECTED_HERE | `architecture/glossary.md` | Requires separate approval and publication |
| Controlled review policy | NOT_PROJECTED_HERE | `verification/controlled-review-policy.md` | Validation tooling is visible; controlled review policy is not |
| EHCO Insights index | NOT_PROJECTED_HERE | `references/ehco-insights/` | No reference index is visible here |
| External source index | NOT_PROJECTED_HERE | `references/external/` | No external source index is visible here |
| Constitutional Instantiation paper | NOT_PROJECTED_HERE | `papers/constitutional-instantiation-of-ai-governance/` | Requires a separately approved public edition |
| Public architecture diagrams | NOT_PROJECTED_HERE | `diagrams/` | Requires separate disclosure review |
| Public IP portfolio | NOT_PROJECTED_HERE | `ip/` | No public IP portfolio is visible here |
| Release notes | NOT_PROJECTED_HERE | `release-notes/` | No release-note directory is visible here |
| Tagged GitHub Release | NOT_PROJECTED_HERE | GitHub Releases | No tag or GitHub Release is currently declared |

## Excluded material

The following remain excluded unless a separately approved public edition is created:

- proprietary Runtime and participant source;
- Instantiation Bridge implementation mechanics;
- private control anchors, schemas, verifier internals, credentials, tokens, keys, active privileged endpoints, and protected topology;
- customer, financial, tax, debt, management, and confidential commercial records;
- investor-only or controlled materials not expressly approved for unrestricted publication.

## Required release checks

Before an artifact becomes **VISIBLE_CURRENTLY**, confirm:

1. **Canonical authority** — exact accepted version and approving source.
2. **Accuracy** — alignment with accepted proof roots and current public records.
3. **Disclosure safety** — no unapproved proprietary, security-sensitive, personal, customer, financial, or infrastructure disclosure.
4. **Proof ceiling** — explicit statement of what the artifact establishes and does not establish.
5. **Integrity** — hash, manifest, filename, and package structure preserved where applicable.
6. **Presentation** — clean title, version, date, context, and navigation.
7. **Linkage** — related visible architecture, evidence, and release records connected without implying absent sections exist.
8. **Validation** — repository validation passes for dossier or evidence-package changes.

## Control rule

No draft, duplicate, superseded, investor-only, internal, or private implementation artifact enters the public repository merely because it is shareable or exists in a release folder. Publication requires explicit approval, canonical placement, and a proof ceiling. Repository publication is evidence of visibility, not Runtime authority or operational release authorization.
