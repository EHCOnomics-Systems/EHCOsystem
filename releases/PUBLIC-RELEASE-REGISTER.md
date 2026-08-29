# Canonical Public Publication Register

This register records public source visibility, artifact identity and evidence scope for `EHCOsystem`.

## Publication vocabulary

- **PRESENT_IN_REVISION** — present in the stated Git revision.
- **REGISTERED_RELEASE_IDENTITY** — declared release identity reserved for publication lifecycle use.
- **HASH_PRESERVED_EVIDENCE** — byte-preserved evidence with cryptographic identity.
- **CURRENT_RUNTIME_EVIDENCE_REQUIRED** — current Runtime evidence owns the proposition.

## Registered public release identity

- Version: `1.0.0`
- Tag: `v1.0.0-public`
- Release title: `EHCOsystem Public Architecture and Evidence Baseline v1.0.0`

Canonical `main` is the active public source stream. The GitHub Releases surface determines live publication state. The registered release identity is tracked as a separate publication-lifecycle record.

## Repository provenance basis

The stable repository manifest uses non-circular provenance semantics:

- `provenance.accepted_commit` identifies the commit that accepted the stable `ehco.repository.yaml` boundary represented by the file, not current `main`;
- the current stable manifest baseline was accepted by `eff9301e7c5ddfc0759ee0d7e3c026ad28c5670c`;
- `artifact_identifier` is `public-repository`;
- `provenance.artifact_digest` is `NOT_APPLICABLE_SOURCE_ONLY_PUBLIC_PROJECTION_NO_SEPARATE_BUILD_ARTIFACT` because the public repository is a source-only projection and no separately built repository artifact is defined.

Hash-bound dossiers, evidence packets, Dashboard derivatives, Language Model fixtures and Range Reactor evidence retain their own artifact identities and are not substituted into the repository-level provenance field.

The registered release identity above remains distinct from provider publication. Live materialization is established by the provider-owned Git tag and GitHub Release surfaces when those objects exist.

## Public estate in the current revision

| Artifact | Status | Canonical path | Evidence scope |
|---|---|---|---|
| Repository identity and front door | PRESENT_IN_REVISION | `README.md` | Category-to-ecosystem orientation and current maturity |
| Instantiated AI | PRESENT_IN_REVISION | `architecture/INSTANTIATED-AI.md` | Category architecture |
| EHCOsystem Technology Estate | PRESENT_IN_REVISION | `architecture/EHCO-TECHNOLOGY-ESTATE.md` | Ecosystem architecture and source-grounded maturity |
| Public Architecture Diagrams | PRESENT_IN_REVISION | `architecture/diagrams/README.md` | Public explanatory relationships |
| Ecosystem Components and Runtime Relationships | PRESENT_IN_REVISION | `architecture/ecosystem-components-and-participation.md` | Component identity, maturity and Runtime relationships |
| Ecosystem Claim → Evidence Matrix | PRESENT_IN_REVISION | `assurance/ECOSYSTEM-CLAIM-EVIDENCE-MATRIX.md` | Claim/evidence navigation |
| Ecosystem Technical Diligence | PRESENT_IN_REVISION | `ECOSYSTEM-DILIGENCE.md` | Reviewer evidence route |
| Runtime/Repository/Test-Estate Boundary | PRESENT_IN_REVISION | `architecture/runtime-repository-and-test-estate-boundary.md` | Evidence-domain ownership |
| EHCO AI-OS Instantiated System | PRESENT_IN_REVISION | `architecture/EHCO-AI-OS-INSTANTIATED-SYSTEM.md` | Tier One public system record |
| EHCO AI-OS Public System Card | PRESENT_IN_REVISION | `architecture/EHCO-AI-OS-SYSTEM-CARD.md` | Tier One public synthesis |
| Governed Runtime Architecture | PRESENT_IN_REVISION | `architecture/GOVERNED-RUNTIME-ARCHITECTURE.md` | Conceptual Runtime architecture |
| System Invariants | PRESENT_IN_REVISION | `architecture/SYSTEM-INVARIANTS.md` | Canonical separation principles |
| Instantiated Proof Range | PRESENT_IN_REVISION | `architecture/instantiated-proof-range.md` | Proof/evidence classes |
| EHCO Language Model | PRESENT_IN_REVISION | `language-model/README.md` | Deterministic language architecture and current maturity |
| Language Model Public Test Snapshot v1 | PRESENT_IN_REVISION | `language-model/evidence/public-test-snapshot-v1/` | Seven exact fixtures / 62 cases and qualification index |
| Public dossier PDF | HASH_PRESERVED_EVIDENCE | `dossiers/EHCO_AI_OS_Governed_Operational_Architecture_Public_Edition_v1_8_LOCK_FINAL.pdf` | Controlled public architecture; SHA-256 `F489BA01961A12CF101B1F1DF57E6958456A0840BEB798B862FA97ACB030892D` |
| Public Evidence Companion Version 1 | HASH_PRESERVED_EVIDENCE | `evidence/public-evidence-companion/v1/` | Packets 00-08 and their packet-specific evidence classes |
| Public validation | PRESENT_IN_REVISION | `verification/` | Repository integrity and public-representation validation |

## Packet register

| Packet | Status | Evidence scope |
|---|---|---|
| 00 — Dossier Identity and Boundary | HASH_PRESERVED_EVIDENCE | Exact dossier identity |
| 01 — Instantiated Standing | HASH_PRESERVED_EVIDENCE | Accepted 52/53 standing projection |
| 02 — Canonical Runtime Source Binding | HASH_PRESERVED_EVIDENCE | Packet-time source/artifact identity and provenance |
| 03 — Tier One Authority Enforcement | HASH_PRESERVED_EVIDENCE | Artifact identity and named authority constructs |
| 04 — Runtime Packet and Continuity Anchors | HASH_PRESERVED_EVIDENCE | Artifact bindings and continuity constructs |
| 05 — Proof, Collapse, Recovery, Release and Projection Anchors | HASH_PRESERVED_EVIDENCE | Artifact bindings and named proof/recovery/release constructs |
| 06 — Observed Live Capture and Release Status | HASH_PRESERVED_EVIDENCE | Historical bounded test/observation capture |
| 07 — Public Boundaries and Delivery Status | HASH_PRESERVED_EVIDENCE | Architecture, standing, validation, projection and delivery relationships |
| 08 — Suite Verification and Closure | HASH_PRESERVED_EVIDENCE | Package identity, manifests, receipts and closure |

## Evidence package identity

The canonical dossier appears in two byte-identical locations and retains SHA-256:

```text
F489BA01961A12CF101B1F1DF57E6958456A0840BEB798B862FA97ACB030892D
```

## Publication lifecycle

Revision visibility, canonical-main publication, stable repository provenance and registered release identity are tracked as separate publication records. Live GitHub release materialization is established by the provider release surface. Current Runtime state remains owned by current Runtime evidence.
