---
title: EHCO AI-OS Public Claim-Evidence Matrix
version: 1.2
status: accepted-public-assurance-reference
published: 2026-08-28
maintainer: EHCOnomics
evidence_class: public-assurance-mapping
evidence_scope: Tier One public claim-to-evidence relationships
supersedes: version 1.1
---

# EHCO AI-OS Public Claim → Evidence Matrix

Accepted EHCO AI-OS standing is **52/53**.

| Public proposition | Governed object | Evidence class | Public source | Verification method | Evidence scope |
|---|---|---|---|---|---|
| EHCO AI-OS is the realized **Tier One Runtime** with accepted standing **52/53**. | EHCO AI-OS Runtime standing | Controlled architecture + operational standing projection | `architecture/EHCO-AI-OS-INSTANTIATED-SYSTEM.md`; `architecture/instantiated-proof-range.md`; Packet 01 | Inspect accepted public system/proof records and verify Packet 01 | Tier One Runtime identity and accepted standing projection |
| The public `EHCOsystem` repository owns public architecture, evidence, provenance, verification and publication. | Public repository | Controlled architecture + repository governance | `architecture/runtime-repository-and-test-estate-boundary.md`; `GOVERNANCE.md` | Inspect boundary and governance records | Public technical representation and evidence custody |
| Persistent downstream component identity and scoped Runtime participation are separately governed dimensions. | Component / Runtime relationship | Controlled architecture | `architecture/ecosystem-components-and-participation.md`; `architecture/SYSTEM-INVARIANTS.md` | Inspect component and invariant records | Persistent component identity and Runtime relationship semantics |
| Artifact identity/provenance establishes exact source, path, revision, hash and manifest relationships. | Artifact identity | Artifact identity/provenance | `architecture/instantiated-proof-range.md`; Packet 02 | Verify packet manifests and hashes | Exact captured artifact identity and provenance |
| Declaration/anchor evidence establishes named construct presence in identified artifacts. | Declaration presence | Declaration/anchor presence | `architecture/instantiated-proof-range.md`; Packets 03–05 | Verify exact artifact bindings and declaration presence | Named construct presence |
| Bounded build/test evidence establishes behavior for identified source, inputs, environment and time. | Test evidence | Bounded test/observation | `architecture/instantiated-proof-range.md`; `evidence/README.md`; Packet 06 | Inspect test/capture scope and packet integrity | Bounded observed behavior |
| Packet-integrity `PASS` establishes declared package integrity. | Evidence package | Hash-preserved evidence | `evidence/README.md`; Packets 06 and 08 | Run manifest/hash/suite-closure validation | Package identity, integrity and closure |
| Packet 06 records a historical bounded local-live observation window. | Historical observation | Bounded observation | `evidence/README.md`; Packet 06 | Inspect capture scope, time, observations and discrepancy register | Historical captured behavior and evidence lanes |
| Scope findings retain the scope and time of their originating record. | Evidence interpretation | Controlled architecture | `architecture/SYSTEM-INVARIANTS.md`; boundary record | Inspect scope and evidence-owner fields | Scope/currentness discipline |
| Evidence supports governed determinations; authority owners issue authoritative state and consequence. | Evidence / authority | Controlled architecture | System Card; System Invariants | Inspect architecture and ownership map | Evidence/authority relationship |
| Downstream components own their capabilities; Tier Three owns projection; EHCO AI-OS owns Tier One Runtime authority. | System roles | Controlled architecture | System Card; Runtime Architecture; Component map | Inspect current public architecture | Computational ownership |
| Runtime realization, production activation, public ingress and operational release are independently governed lifecycle dimensions. | Lifecycle relationships | Controlled architecture + release control | System Invariants; Public Release Register | Inspect lifecycle and publication records | Lifecycle-state separation |
| Independent validation is established by an identified third-party record with stated method and scope. | Independent validation | Independent validation | Governance; proof records | Inspect identified third-party validation records | Third-party validation class |
| Repository validation establishes public repository integrity and semantic alignment for the checked revision. | Repository validation | Repository-side validation | `verification/README.md`; validation workflow | Run repository validators and GitHub checks | Checked repository revision |

## Reading the matrix

Each row identifies the proposition, owner, evidence class and scope that establish it. Runtime-originated records remain the controlling evidence class for Runtime state, consequence, persistence, recovery, release and proof.

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.2 | 2026-08-28 | Recast the matrix as affirmative ownership and evidence-scope relationships. |
| 1.1 | 2026-08-26 | Reconciled current tier/component terminology. |
