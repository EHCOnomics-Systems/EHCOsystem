---
title: EHCO AI-OS Public Claim-Evidence Matrix
version: 2.0
status: accepted-public-assurance-reference
published: 2026-09-01
maintainer: EHCOnomics
evidence_class: public-assurance-mapping
evidence_scope: Tier One public claim-to-evidence relationships
---

# EHCO AI-OS Public Claim → Evidence Matrix

Accepted EHCO AI-OS standing is **52/53**, with accepted Runtime maturity **`REALIZED / COMPLETE_IN_ACCEPTED_SCOPE`**.

For current public interpretation, begin with [EHCO AI-OS Runtime — Current Public Evidence](../runtime/README.md), the [Full Flex evidence index](../evidence/runtime/full-flex/v1/README.md), and the [Canonical Public Claim Registry](PUBLIC-CLAIM-REGISTRY.json).

| Public proposition | Evidence class | Public source | Verification method | Evidence scope |
|---|---|---|---|---|
| EHCO AI-OS is the realized **Tier One Runtime** with accepted standing **52/53** and accepted maturity `REALIZED / COMPLETE_IN_ACCEPTED_SCOPE`. | Accepted Runtime/standing representation | [Runtime](../runtime/README.md); [Instantiated System](../architecture/EHCO-AI-OS-INSTANTIATED-SYSTEM.md) | `validate_current_runtime_evidence.py` | Tier One identity, accepted maturity, and standing representation |
| `EHCO_DOCKER_PORTABILITY` is the `PRIMARY_ACCESSIBLE_RUNTIME_PROJECTION` and fully containerized, deployment-ready portable delivery form of the established hardened Runtime/root-image lineage. | Accepted Docker/host technical evidence + controlled architecture | [Runtime](../runtime/README.md); [Technical Diligence](../TECHNICAL-DILIGENCE.md) | `validate_current_runtime_evidence.py` | Runtime-projection lineage and portability |
| EHCO AI-OS has physically operated as a self-hosted local Docker Runtime with Dashboard, Runtime bridge, worker service, networking, persistent Runtime/proof/data surfaces, health behavior, and hardened image identity. | Accepted physical execution evidence | [Runtime](../runtime/README.md); [Technical Diligence](../TECHNICAL-DILIGENCE.md) | Review current public-safe route and accepted evidence relationship | Self-hosted local Docker operating posture |
| EHCO Full Flex Public Packet v1 is the accepted current Runtime evidence identity, bound to SHA-256 `7F80C27D085AE871A00AED412C6F20EA9A76CB0677C93AEBA381CD1FD70EC8E5`. | Accepted packet identity + public-safe current record | [Full Flex](../evidence/runtime/full-flex/v1/README.md); [Public-Safe Record](../evidence/runtime/full-flex/v1/PUBLIC_SAFE_RECORD.json) | `validate_current_runtime_evidence.py` | Accepted packet identity and current public-safe representation |
| Historical Public Evidence Companion Packets 00–08 retain their recorded event-time propositions and cryptographic identity. | Hash-preserved historical evidence | [Public Evidence](../evidence/README.md); [Historical Packets](../evidence/public-evidence-companion/v1/) | Public repository integrity validator | Historical event-time evidence and package lineage |
| Runtime engineering characterization recorded a **496,898,804-byte / 2,605,233-line** activity ledger request at **6.847 seconds** and identified whole-ledger reading before the accepted bounded reverse-tail reader repair. | Historical engineering characterization + accepted repair lineage | [Technical Diligence](../TECHNICAL-DILIGENCE.md) | Inspect the bounded historical characterization | Historical workload, mechanism diagnosis, and repair relationship |
| The public `EHCOsystem` repository owns public architecture, public-safe evidence representation, verification, and publication source state. | Repository governance and validation | [README](../README.md); [Verification](../verification/README.md) | `python3 verification/verify_all_public.py` | Exact public repository revision |
| Downstream component capability and Tier One Runtime participation are separate governed dimensions. | Controlled architecture | [Components and Runtime Relationships](../architecture/ecosystem-components-and-participation.md) | Architecture review | Component/Runtime relationship semantics |
| Evidence supports governed technical conclusions within its evidence class; authoritative Runtime state and consequence remain owned by the instantiated Runtime. | Controlled architecture and evidence ownership | [System Invariants](../architecture/SYSTEM-INVARIANTS.md); [Runtime Boundary](../architecture/runtime-repository-and-test-estate-boundary.md) | Inspect ownership records | Evidence/authority relationship |

## Interpretation

The matrix routes public claims to the evidence class that supports them. The accepted Full Flex identity is preserved through its hash, receipt, and public-safe record; raw packet bytes carrying internal source-routing metadata remain outside the current public tree. Repository verification checks the public representation for an exact revision and does not regenerate Runtime or physical execution evidence.
