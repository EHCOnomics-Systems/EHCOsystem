---
title: EHCO AI-OS Public Claim-Evidence Matrix
version: 1.0
status: accepted-public-assurance-reference
published: 2026-08-08
maintainer: EHCOnomics
evidence_class: public-assurance-mapping
proof_ceiling: maps public claims to existing public sources and their existing proof ceilings; creates no new Runtime proof
---

# EHCO AI-OS Public Claim → Evidence Matrix

## Purpose

This matrix binds selected public EHCO AI-OS claims to the public records that support them and states the proof ceiling that applies to each relationship.

The matrix does not create a new proof class. It does not convert architecture, repository records, packet integrity, declarations, tests, captures, dashboards, ledgers, or assistant output into Runtime authority or Runtime-originated proof.

Accepted EHCO AI-OS standing remains **52/53**.

## Matrix

| Public claim | Governed object | Claim / evidence class | Public source | Verification method | Proof ceiling / non-claim |
|---|---|---|---|---|---|
| EHCO AI-OS is the realized Tier 1 Runtime with accepted standing **52/53**. | EHCO AI-OS Runtime standing | Controlled EHCO architecture + controlled operational standing projection | `architecture/EHCO-AI-OS-INSTANTIATED-SYSTEM.md`; `architecture/instantiated-proof-range.md`; Public Evidence Companion Packet 01 | Read accepted public system/proof records; verify Packet 01 through repository validation | Public projection of the accepted standing record. Repository publication does not create, recalculate, promote, demote, revoke, or replace standing. |
| The public `EHCOsystem` repository is not the Runtime and does not hold Runtime authority or authoritative Runtime state. | Runtime/repository boundary | Controlled EHCO architecture | `architecture/runtime-repository-and-test-estate-boundary.md`; `README.md`; `GOVERNANCE.md` | Read controlling boundary and repository governance; run semantic-boundary validation | Establishes the accepted public interpretation boundary. It does not locate or expose Runtime implementation or authority. |
| File, repository, package, or artifact identity is not Runtime identity. | Artifact identity versus Runtime identity | Controlled architecture + artifact identity/provenance | `architecture/runtime-repository-and-test-estate-boundary.md`; `architecture/instantiated-proof-range.md`; Packet 02 | Verify packet manifests/hashes and read proof-range classification | Exact identity/integrity/provenance of captured artifacts only; not Runtime identity, authority location, or current Runtime state. |
| A named declaration or anchor is not executed enforcement. | Declaration/enforcement distinction | Controlled architecture + declaration/anchor presence | `architecture/instantiated-proof-range.md`; Packets 03–05 | Verify exact artifact bindings and declaration presence under packet manifests | Presence of named constructs only unless execution is expressly recorded. Does not prove universal enforcement, Runtime admission, or consequence. |
| A passing build or test is not Runtime admission. | Test evidence versus Runtime participation | Controlled architecture + bounded test/observation | `architecture/instantiated-proof-range.md`; `evidence/README.md`; Packet 06 | Review exact test/capture scope and packet integrity; preserve observation bounds | Establishes behavior only for identified inputs/environment/version/time. Does not independently establish Runtime admission or universal behavior. |
| Packet-integrity `PASS` is not universal behavioral `PASS`. | Evidence-package integrity | Hash-preserved historical evidence | `evidence/README.md`; Packet 06; Packet 08 | Run repository manifest/hash/suite-closure validation | Proves package integrity within the declared manifest. Does not prove universal Runtime behavior or current Runtime state. |
| Packet 06 is a historical bounded capture, not a projection of current Runtime state. | Historical observation | Bounded test or observation | `evidence/README.md`; Packet 06; `releases/PUBLIC-RELEASE-REGISTER.md` | Review capture scope/time and current interpretation records | Historical bounded observation only. Discrepancies/unobserved lanes remain scoped to that capture and do not independently establish current Runtime defect or standing change. |
| Scope miss, missing retrieval, or non-observation does not independently change Runtime state or standing. | State/standing interpretation | Controlled EHCO architecture | `architecture/SYSTEM-INVARIANTS.md`; `architecture/runtime-repository-and-test-estate-boundary.md` | Read accepted invariant/boundary records | Interpretation rule only. It does not suppress valid contradictory Runtime-originated proof if such proof exists. |
| Evidence is not authority; ledger and dashboard projections do not become Runtime truth merely by recording or displaying information. | Evidence/projection boundary | Controlled EHCO architecture | `architecture/EHCO-AI-OS-SYSTEM-CARD.md`; `architecture/SYSTEM-INVARIANTS.md` | Read accepted public architecture/invariants | Architectural distinction. Does not assert that every ledger/dashboard implementation is correct or secure. |
| Tier 2 governed execution and Tier 3 projection do not independently acquire Tier 1 Runtime authority. | Tier relationships | Controlled EHCO architecture | `architecture/EHCO-AI-OS-SYSTEM-CARD.md`; `architecture/GOVERNED-RUNTIME-ARCHITECTURE.md` | Read accepted public architecture | Conceptual public architecture only; not an implementation map, source disclosure, or Runtime execution trace. |
| Runtime realization is distinct from production activation, public ingress, operational external release, commercial activation, and go-live. | Runtime realization versus deployment/release states | Controlled architecture + release boundary | `README.md`; `architecture/SYSTEM-INVARIANTS.md`; `releases/PUBLIC-RELEASE-REGISTER.md`; Packet 07; Packet 08 | Read public release boundary and packet non-authorization records | Does not establish any current production/deployment/release state unless a separately applicable governing record does so. |
| The public evidence estate does not claim independent third-party certification absent a specifically identified third-party record. | Independent validation | Public governance/proof boundary | `GOVERNANCE.md`; `architecture/instantiated-proof-range.md`; `releases/PUBLIC-RELEASE-REGISTER.md` | Inspect public register and proof classifications for an identified independent record | No independent certification is inferred from EHCOnomics-controlled evidence, automated validation, or repository publication. |
| Repository validation establishes bounded repository integrity and semantic-boundary compliance for the checked commit. | Public repository validation | Repository-side validation evidence | `verification/README.md`; `.github/workflows/validate-public-evidence.yml` | Run `python3 verification/validate_public_evidence.py` and `python3 verification/validate_release_identity.py` via GitHub Actions | Does not execute the Runtime, create standing, prove production security, authorize deployment/release, or constitute independent certification. |

## Reading the matrix

A row is not a substitute for its cited source. Where the claim concerns Runtime standing, current Runtime state, authoritative consequence, persistence, recovery, release, revocation, or Runtime truth, the applicable Runtime-originated evidence remains the controlling proof class.

A later accepted source may supersede an earlier interpretation. Scope differences must not be promoted into contradictions without applicable proof.

## Public/private boundary

This matrix intentionally references public canonical paths and public packet identifiers only. It does not expose private source roots, private repository names, private revisions, internal schemas, protected control paths, privileged endpoints, production topology, credentials, or private proof records.
