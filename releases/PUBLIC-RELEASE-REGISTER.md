# Canonical Public Release Register

This register controls which EHCOsystem artifacts are approved for publication, which exact version is canonical, where each artifact belongs in the repository, and what proof ceiling it carries.

## Status values

- **Approved** — canonical public artifact confirmed.
- **Approved structure / files pending** — release structure is confirmed; canonical files still need to be copied from the approved source estate.
- **Metadata verification required** — artifact is intended for publication, but title, author, date, version, or URL still needs confirmation.
- **Content review required** — artifact may be public, but must be checked against the current architecture and disclosure boundary before publication.
- **Excluded** — not part of the public repository.

## First public release scope

| Artifact | Canonical version or state | Status | Public path | Proof ceiling | Notes |
|---|---|---|---|---|---|
| Repository identity | Current README | Approved | `README.md` | Public repository purpose and boundary | Already published. |
| Public library index | Current | Approved | `LIBRARY.md` | Navigation only | Already published. |
| Start Here guide | Current | Approved | `getting-started/START-HERE.md` | Navigation only | Already published. |
| Repository governance | Current | Approved | `GOVERNANCE.md` | Publication and contribution control | Already published. |
| Security policy | Current | Approved | `SECURITY.md` | Public disclosure and reporting boundary | Already published. |
| IP and evidence notice | Current | Approved | `NOTICE.md` | Public IP and evidence boundary | Already published. |
| Immutable Runtime baseline | Public baseline v1.0 | Approved | `architecture/runtime-baseline.md` | Controlled EHCO architecture | Current content exists at `docs/runtime-baseline.md`; move without changing substance. |
| Ecosystem governance discovery | Accepted public construct | Approved structure / files pending | `architecture/ecosystem-governance-discovery.md` | EHCO engineering finding and proposition | Must preserve the immutable Runtime baseline and the later discovery. |
| Proof classes | Accepted public distinctions | Approved structure / files pending | `architecture/proof-classes.md` | Public evidence and proof-state definitions | Must distinguish architecture, implementation, test definition, test execution, deployment, admission, standing, production, and release. |
| Public glossary | Accepted public terminology | Approved structure / files pending | `architecture/glossary.md` | Public definitions only | Must not expose proprietary implementation mechanics. |
| Public architecture dossier | EHCO AI-OS Governed Operational Architecture — Public Edition v1.8, July 2026 | Approved | `dossiers/EHCO_AI_OS_Governed_Operational_Architecture_Public_Edition_v1_8_LOCK_FINAL.pdf` | Controlled public architecture | Packet 00 records SHA-256 `F489BA01961A12CF101B1F1DF57E6958456A0840BEB798B862FA97ACB030892D`. |
| Dossier landing page | New publication index | Approved structure / files pending | `dossiers/README.md` | Navigation and proof boundary | Must identify version, date, hash, status, and what the dossier does not prove. |
| Public Evidence Companion | Version 1, packets 00–08 | Approved | `evidence/public-evidence-companion/v1/` | Bounded public evidence and verification surface | Preserve packet names, internal filenames, manifests, receipts, hashes, verification results, and boundary records exactly. |
| Public Evidence Companion overview | Current | Approved | `evidence/README.md` | Navigation and packet proof ceilings | Already published. |
| Packet 00 — Dossier Identity and Boundary | Approved packet | Approved structure / files pending | `evidence/public-evidence-companion/v1/00_DOSSIER_IDENTITY_AND_BOUNDARY/` | Dossier identity and boundary only | No authority, standing, Runtime-truth, deployment, or release effect. |
| Packet 01 — Instantiated Standing | Approved packet | Approved structure / files pending | `evidence/public-evidence-companion/v1/01_INSTANTIATED_STANDING/` | Accepted baseline projection and status boundary | Does not instantiate, promote, demote, deploy, release, or authorize Runtime. |
| Packet 02 — Canonical Runtime Source Binding | Approved packet | Approved structure / files pending | `evidence/public-evidence-companion/v1/02_CANONICAL_RUNTIME_SOURCE_BINDING/` | Source identity and SHA-256 binding | Does not disclose source code or claim live observation. |
| Packet 03 — Tier 1 Authority Enforcement | Approved packet | Approved structure / files pending | `evidence/public-evidence-companion/v1/03_TIER1_AUTHORITY_ENFORCEMENT/` | Presence of named enforcement anchors | Does not execute Runtime or authorize release. |
| Packet 04 — Runtime Packet and Continuity Anchors | Approved packet | Approved structure / files pending | `evidence/public-evidence-companion/v1/04_RUNTIME_PACKET_AND_CONTINUITY_ANCHORS/` | Source bindings and named declarations | No live execution, end-to-end behavioral proof, persistence/restart validation, recovery validation, or complete source disclosure. |
| Packet 05 — Proof, Collapse, Recovery, Release, and Projection Anchors | Approved packet | Approved structure / files pending | `evidence/public-evidence-companion/v1/05_PROOF_COLLAPSE_RECOVERY_AND_RELEASE_ANCHORS/` | Source bindings and named declarations | No live execution, proof-admission validation, named mechanism test results, production authorization, or complete source disclosure. |
| Packet 06 — Observed Live Capture and Release Status | Approved packet | Approved structure / files pending | `evidence/public-evidence-companion/v1/06_OBSERVED_LIVE_CAPTURE_AND_RELEASE_STATUS/` | Hash-bound observation, mixed status, discrepancies, and open gaps | External release and production activation are not granted. |
| Packet 07 — Public Boundaries and Delivery Status | Approved packet | Approved structure / files pending | `evidence/public-evidence-companion/v1/07_PUBLIC_BOUNDARIES_AND_DELIVERY_STATUS/` | Architecture/standing/validation/projection/delivery separation | Does not authorize public ingress, release, activation, go-live, or Kubernetes realization. |
| Packet 08 — Suite Verification and Final ZIP | Approved packet | Approved structure / files pending | `evidence/public-evidence-companion/v1/08_SUITE_VERIFICATION_AND_FINAL_ZIP/` | Package verification and closure boundary | Runtime implementation source excluded; bounded verification tooling permitted; secret-indicator scan recorded as pass with zero findings. |
| Controlled review policy | New public policy | Approved structure / files pending | `verification/controlled-review-policy.md` | Review process only | Must describe review classes without exposing protected implementation. |
| EHCO Insights series index | Cornerstone instantiation series | Metadata verification required | `references/ehco-insights/instantiated-governance-series.md` | Public authorship and intellectual lineage | Verify exact title, author, publication date, update date, and stable URL for every article before publication. |
| External source index | Accepted external primary sources | Approved structure / files pending | `references/external/external-sources.md` | External facts, incidents, definitions, standards, and legislation | Separate external fact from EHCO interpretation. |
| Constitutional Instantiation paper | Accepted construct, public edition pending | Content review required | `papers/constitutional-instantiation-of-ai-governance/` | EHCO architecture, engineering findings, propositions, and public evidence | Complete public-safe edition before release. No private source locators. |
| Public architecture diagram | First diagram pending | Content review required | `diagrams/` | Conceptual public architecture only | Must not expose protected topology or implementation mechanics. |
| Release notes | First release | Approved structure / files pending | `release-notes/2026-08-initial-public-release.md` | Release history only | Must list exactly what was added and what remains pending. |

## Presentation and investor material

| Artifact | Current state | Status | Decision |
|---|---|---|---|
| Approved investor deck | Approved investor release exists | Content review required | Publish only if expressly intended for unrestricted public release. Investor-shareable is not automatically equivalent to public-repository approved. |
| Instantiation technical note | Public/share source exists | Content review required | Candidate for `papers/` after current-architecture and disclosure audit. |
| Public Evidence Companion Investor Guide | Controlled investor edition exists | Content review required | May be adapted into a public evidence guide; do not publish investor-only framing without review. |
| Standards advancement strategy | Controlled investor edition exists | Content review required | Publish only a separately approved public edition. |
| IP and technology portfolio | Controlled investor edition exists | Excluded from first release | Not required for the technical public release and may expose commercial positioning. |
| Financial, tax, debt, management records | Internal/controlled | Excluded | Never publish in this repository. |

## Website and public channels

The first release must include verified links to:

- the official EHCOnomics website;
- EHCO Insights;
- the five cornerstone instantiation articles;
- the public GitHub repository;
- approved public social or media channels where relevant.

Website articles establish public chronology, authorship, and explanatory lineage. They do not constitute independent validation of EHCO technical claims.

## Required release checks

Before an artifact changes to **Approved**, confirm:

1. **Canonical authority** — exact accepted version and approving source.
2. **Accuracy** — alignment with the current immutable baseline and later ecosystem findings.
3. **Disclosure safety** — no damaging proprietary, security-sensitive, personal, customer, financial, or infrastructure disclosure.
4. **Proof ceiling** — explicit statement of what the artifact establishes and does not establish.
5. **Integrity** — hash, manifest, filename, and package structure preserved where applicable.
6. **Presentation** — clean title, version, date, context, and navigation.
7. **Linkage** — related architecture, evidence, papers, articles, and diagrams connected.

## Control rule

No draft, duplicate, superseded, investor-only, internal, or private implementation artifact enters the public repository merely because it is shareable or exists in a release folder. Publication requires an explicit entry in this register and an approved status.