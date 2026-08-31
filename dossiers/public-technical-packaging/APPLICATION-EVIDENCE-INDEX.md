# EHCOsystem Public Application & Evidence Index v1.0

**Evidence class:** public review index / provenance routing  
**Public package baseline:** `77b9d82e0e1bb63d932bd0c62ed98e6dfc32e4f5`  
**Review date:** 2026-08-31  
**Accepted numerical standing represented:** 52/53

## Purpose

This index gives a reviewer one bounded route from a public EHCOsystem component or proposition to the source/evidence domain that owns the exact fact, the accepted public evidence route, and the repository-side validator that checks the public representation.

This file is an index, not independent technical evidence. `EHCOnomics-Systems/EHCOsystem` remains a public projection/diligence surface. Direct owning repositories establish exact implementation state; owning technical evidence establishes physical effects; `INSTANTIATED_EHCO_RUNTIME` owns Tier One Runtime facts and current Runtime state.

## Currentness vocabulary

- `CURRENT` — current for the public package at the review date.
- `HISTORICAL` — valid evidence of a bounded past state, not presented as current state.
- `SUPERSEDED` — retained for lineage but replaced by a later public representation.
- `NOT_REVALIDATED` — previously represented but currentness was not re-established for this package.

Currentness is separate from maturity, lifecycle state, Runtime status, acceptance, and historical validity.

## Principal application/component index

| Public component / proposition | Owning source or evidence domain | Exact accepted owning revision / identity | Public evidence route | Public validator | Currentness | Public ceiling |
|---|---|---|---|---|---|---|
| EHCO AI-OS — Tier One Runtime identity and accepted 52/53 standing projection | `INSTANTIATED_EHCO_RUNTIME` for current Runtime facts; `EHCOnomics-Systems/EHCO_AI-OS` is source/control repository, not instantiated authority | Current Runtime state: Runtime-owned; exact source revision is `NOT_ESTABLISHED_IN_PUBLIC_PACKAGE` | `runtime/README.md`; `evidence/runtime/full-flex/v1/README.md`; `assurance/PUBLIC-CLAIM-REGISTRY.json` | `verification/validate_current_runtime_evidence.py`; `verification/validate_public_claim_registry.py` | `CURRENT` public projection | Realized Tier One identity, accepted maturity/standing projection, and published evidence relationships; public Git does not become Runtime authority. |
| EHCO Full Flex Public Packet v1 | Owning Windows/Docker host evidence for physical effects; public exact-byte custody in `EHCOsystem` | Packet SHA-256 `7F80C27D085AE871A00AED412C6F20EA9A76CB0677C93AEBA381CD1FD70EC8E5` | `evidence/runtime/full-flex/v1/EHCO_FULL_FLEX_PUBLIC_PACKET_V1.json` | `verification/validate_current_runtime_evidence.py` | `CURRENT` | Exact public packet identity and public representation; physical Runtime execution remains established by owning execution evidence. |
| EHCO Range Reactor — mature deterministic range/reasoning component | `EHCOnomics-Systems/EHCO_Range_Reactor` | Accepted operational-closure owner revision `eae888b784620ed37ed7d6704bcd91dedcf92936`; benchmark source `e72b2a29e52878d300b44f0286259466352f73cc` | `range-reactor/README.md`; `range-reactor/evidence/public-capability-snapshot-v1/README.md`; `range-reactor/evidence/operational-closure-v1/README.md` | `verification/validate_public_range_reactor_snapshot.py`; `verification/validate_public_range_reactor_operational_closure.py` | `CURRENT` for selected published evidence | Mature bounded capability; matched A/B applies only to selected benchmark; semantic closure applies only to selected current corpus; no universal correctness or Tier One Runtime participation claim. |
| EHCO Language Model — deterministic computational-language component | `EHCOnomics-Systems/ehco_Language-Model_v1` | Exact accepted owning revision is `NOT_ESTABLISHED_IN_PUBLIC_PACKAGE` | `language-model/evidence/public-test-snapshot-v1/README.md`; `architecture/EHCO-TECHNOLOGY-ESTATE.md` | `verification/validate_public_lm_test_snapshot.py` | `CURRENT` public test snapshot; exact private source currentness separately owned | Seven exact public fixtures / 62 cases and public maturity representation; public snapshot is not the full controlled implementation or qualification estate. |
| EHCO RAG — governed retrieval/evidence component | `EHCOnomics-Systems/ehco_RAG` | `NOT_ESTABLISHED_IN_PUBLIC_PACKAGE` | `architecture/EHCO-TECHNOLOGY-ESTATE.md`; `assurance/ECOSYSTEM-CLAIM-EVIDENCE-MATRIX.md` | General repository validation only | `CURRENT` public maturity representation | Governed retrieval/context/source-custody/provenance role and public maturity representation; no public claim of completed production realization or Runtime participation. |
| EHCO Prime — relationship/assistant-coordination service | Owning repository identity is not established by the current public package | `NOT_ESTABLISHED_IN_PUBLIC_PACKAGE` | `architecture/EHCO-TECHNOLOGY-ESTATE.md`; `assurance/ECOSYSTEM-CLAIM-EVIDENCE-MATRIX.md` | General repository validation only | `CURRENT` public maturity representation | Public role/maturity only; exact implementation state remains with its owning source. |
| EHCO Agent Connect — registry/discovery/compatibility coordination service | Owning repository identity is not established by the current public package | `NOT_ESTABLISHED_IN_PUBLIC_PACKAGE` | `architecture/EHCO-TECHNOLOGY-ESTATE.md`; `assurance/ECOSYSTEM-CLAIM-EVIDENCE-MATRIX.md` | General repository validation only | `CURRENT` public maturity representation | Public role/maturity only; no automatic Runtime participation, binding, or invocation claim. |
| EHCO Dashboard — Tier Three projection baseline | Tier One current state remains Runtime-owned; Dashboard is a projection/interface surface | Captured operating-state source identity is not published as an owning Git revision | `README.md`; `architecture/EHCO-AI-OS-SYSTEM-CARD.md`; `runtime/README.md` | `verification/validate_public_evidence.py`; `verification/validate_public_claim_registry.py` | `CURRENT` accepted public projection baseline; dated captures are historical observations | Tier Three projection and bounded local captured-state relationship; Dashboard does not own Runtime truth. |
| Historical Public Evidence Companion Packets 00–08 | Historical event-time evidence lineage | Immutable packet identities/manifests in public evidence estate | `evidence/README.md` | `verification/validate_public_evidence.py` | `HISTORICAL` | Historical/event-time evidence only; Full Flex is the current first public Runtime evidence route. |

## Claim-class routing

For machine-readable public propositions, use `assurance/PUBLIC-CLAIM-REGISTRY.json`. Its current registered classes include:

- EHCO AI-OS realized Runtime identity, accepted-scope maturity, Docker portability, local operation, Dashboard relationship, model-independent Tier One lineage, and historical performance characterization;
- Range Reactor mature capability, physical qualification, historical diagnostic performance, matched exploration-time A/B collapse performance, and selected semantic closure.

The registry is a public proposition layer. Claim-specific technical propositions retain their applicable evidence owner and evidence class.

## Verification route

Run the complete public validation sequence with:

```bash
python3 verification/verify_all_public.py
```

The orchestrator reports the exact specialized validator that fails. A failed public check establishes a repository/package validation failure for that check; it does not by itself demote owning implementation, physical-effect, or Runtime state.

## Failure inspection map

| Failure class | First inspection surface |
|---|---|
| General repository, navigation, disclosure, architecture, evidence integrity | `verification/validate_public_evidence.py` and `verification/README.md` |
| Claim-registry/current public proposition mismatch | `assurance/PUBLIC-CLAIM-REGISTRY.json` and `verification/validate_public_claim_registry.py` |
| Full Flex packet/hash/current Runtime evidence-route mismatch | `runtime/README.md`, `evidence/runtime/full-flex/v1/`, `verification/validate_current_runtime_evidence.py` |
| Language Model public snapshot mismatch | `language-model/evidence/public-test-snapshot-v1/` and `verification/validate_public_lm_test_snapshot.py` |
| Range Reactor capability mismatch | `range-reactor/evidence/public-capability-snapshot-v1/` and `verification/validate_public_range_reactor_snapshot.py` |
| Range Reactor operational-closure mismatch | `range-reactor/evidence/operational-closure-v1/` and `verification/validate_public_range_reactor_operational_closure.py` |
| Registered release/provenance identity mismatch | `verification/validate_release_identity.py` and its referenced public provenance surfaces |

## Nonclaims

This index does not establish deployment, production activation, GitHub Release materialization, Tier One Runtime admission/binding/invocation, Runtime participation, authority changes, standing changes, universal correctness, or automatic successor activation.
