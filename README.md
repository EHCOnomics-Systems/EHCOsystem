# EHCOsystem

**Public architecture, evidence, provenance, research, verification, and publication repository for EHCO AI-OS and the EHCOsystem.**

EHCO AI-OS is the realized Tier 1 Runtime of the EHCOsystem. Its accepted standing baseline is **52/53**. The Runtime governs authority, standing, recognized state, transition, consequence, persistence, recovery, withholding, release, closure, and Runtime truth.

This GitHub repository is not the Runtime. It does not hold Runtime authority or authoritative Runtime state, and repository publication, commits, workflows, packets, manifests, tests, or public visibility do not independently create, promote, demote, calculate, revoke, or alter Runtime standing.

## Technical diligence

If you are evaluating the differentiated technical work, start with **[Technical Diligence — Start Here](TECHNICAL-DILIGENCE.md)** rather than reading the repository front to back.

The shortest public diligence path is:

1. **Packet 06 — observed behavior:** a hash-bound `local_live` capture records authority admission, packet/continuity/range/proof state, recovery quarantine, and bounded release/freeze gating. The raw capture records the configured LLM as **not invoked and not used** in that bounded run.
2. **Packet 03 — implementation anchors:** exact source identities and named enforcement functions for authority admission, fail-closed behavior, manifest validation, release-gate construction, and freeze-gate evaluation.
3. **Packet 06 gap register — evidence limits:** three direct unresolved discrepancies and five behavioral lanes not directly observed are retained explicitly rather than represented as passes.

The public repository intentionally excludes the complete proprietary Runtime implementation. Qualified technical diligence is evidence-first: it may use exact source/revision identities, hashes or digests, bounded execution records, reviewer-selected safe test cases, witnessed build or execution, written verification findings, and—only where materially necessary and specifically authorized—narrow supervised inspection that does not transfer the proprietary implementation.

See also [Public Documentation and Evidence Provenance](PROVENANCE.md) for the distinction among explanatory/AI-assisted material, architecture, hash-bound evidence, observations, and repository verification tooling.

## Runtime, repository, and test-estate boundary

Controlled private repositories and their runtime-support folders contain bounded source, test, compatibility, packaging, deployment-support, and evidence-generation artifacts used to exercise and reproduce specified EHCO behavior. Those repositories, folders, and files are not the Runtime and are not authority locations.

File identity does not establish Runtime identity. A named declaration does not establish executed enforcement. A passing build or test does not establish Runtime admission. A repository or evidence packet does not replace Runtime-originated state, consequence, persistence, or proof.

Read the controlling boundary before interpreting source-binding or capture packets:

- [Runtime, Repository, and Test-Estate Boundary](architecture/runtime-repository-and-test-estate-boundary.md)

## Public evidence

The Public Evidence Companion preserves the identity, integrity, provenance, observations, discrepancies, proof ceilings, and status boundaries of Packets 00-08.

- Packet 02 binds a packet-time set of runtime-support test and source artifacts to exact hashes. Its historical title does not make those artifacts or their repository the Runtime.
- Packets 03-05 establish bounded artifact identity and named declarations or anchors unless a packet expressly records executed behavior.
- Packet 06 is a hash-preserved historical test and observation capture. Its integrity `PASS` is not a universal behavioral `PASS` and is not current Runtime state.

The accepted 52/53 baseline is an EHCOnomics-controlled operational standing record projected through the public evidence estate. Independent third-party certification is not claimed unless an identified public record expressly states it.

## General reading path

For broader architecture, governance, and publication context:

1. [Runtime, Repository, and Test-Estate Boundary](architecture/runtime-repository-and-test-estate-boundary.md)
2. [Canonical Public Dossier](dossiers/README.md)
3. [EHCO AI-OS Instantiated System](architecture/EHCO-AI-OS-INSTANTIATED-SYSTEM.md)
4. [EHCO AI-OS Public System Card](architecture/EHCO-AI-OS-SYSTEM-CARD.md)
5. [Governed Runtime Architecture](architecture/GOVERNED-RUNTIME-ARCHITECTURE.md)
6. [System Invariants](architecture/SYSTEM-INVARIANTS.md)
7. [Instantiated Proof Range](architecture/instantiated-proof-range.md)
8. [Public Evidence Companion](evidence/README.md)
9. [Proof and Status Classes](architecture/proof-and-status-classes.md)
10. [EHCO Language-Model System Boundary](language-model/README.md)
11. [EHCOsystem Library](LIBRARY.md)

## Canonical public record

- **System description:** EHCO AI-OS Governed Operational Architecture - Public Edition v1.8
- **Accepted Runtime standing:** 52/53
- **Public evidence:** Public Evidence Companion, Packets 00-08, and the canonical dossier PDF
- **Validation:** bounded repository-integrity and semantic-boundary checks
- **Release control:** canonical public release register, manifests, SHA-256 checksums, and automated validation

Runtime realization remains distinct from production hosting, environment-specific deployment, public ingress, commercial activation, operational external release, and go-live authorization. Those states must be established by their own governing evidence and authorization.

## Publication and use

- [Repository Governance](GOVERNANCE.md)
- [Security and Responsible Disclosure](SECURITY.md)
- [Proprietary Public Inspection License](LICENSE)
- [Notice](NOTICE.md)
- [Public Documentation and Evidence Provenance](PROVENANCE.md)

Proprietary implementation mechanics, private control anchors, credentials, active endpoints, confidential proof records, and production infrastructure remain outside this public repository except where an approved hash-preserved evidence record expressly retains a bounded historical capture attribute.

Copyright (c) 2026 EHCOnomics. All rights reserved.
