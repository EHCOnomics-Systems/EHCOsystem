---
title: EHCO AI-OS Technical Diligence — Start Here
version: 1.1
status: public-diligence-navigation
published: 2026-08-28
maintainer: EHCOnomics
evidence_class: navigation-and-bounded-technical-summary
evidence_scope: focused Tier One public evidence route
supersedes: version 1.0
---

# EHCO AI-OS Technical Diligence — Start Here

This page is the shortest public route to EHCO AI-OS implementation anchors and observed evidence.

## Technical claim

EHCO AI-OS separates intelligence capability from the authority and standing under which an action or state acquires governed operational consequence. The public evidence exposes bounded authority admission, packet and continuity evaluation, proof and range evaluation, recovery quarantine, and release/freeze gating records.

## 1. Observed run — Packet 06

Open:

- [`OBSERVED_LIVE_CAPTURE.json`](evidence/public-evidence-companion/v1/06_OBSERVED_LIVE_CAPTURE_AND_RELEASE_STATUS/06A_OBSERVED_LIVE_CAPTURE/OBSERVED_LIVE_CAPTURE.json)
- raw [`api_chat_probe.json`](evidence/public-evidence-companion/v1/06_OBSERVED_LIVE_CAPTURE_AND_RELEASE_STATUS/06A_OBSERVED_LIVE_CAPTURE/raw/api_chat_probe.json)
- [`DISCREPANCY_AND_GAP_REGISTER.json`](evidence/public-evidence-companion/v1/06_OBSERVED_LIVE_CAPTURE_AND_RELEASE_STATUS/06C_DISCREPANCY_AND_GAP_REGISTER/DISCREPANCY_AND_GAP_REGISTER.json)

Packet 06 preserves a hash-bound `local_live` capture containing:

- three observed Compose service rows and three healthy rows;
- authority admission recorded as admitted;
- packet, continuity, range, and proof status recorded as valid;
- recovery quarantine active under a bounded recovery scope;
- a release gate returning `bounded_release` while closure/readiness/freeze remain governed by their own conditions; and
- a configured LLM that remained idle during the captured authority/proof/range/quarantine/release-gate sequence.

The capture therefore provides a direct public example of governed state evaluation proceeding through the recorded control path with the configured language model idle.

## 2. Implementation anchors — Packet 03

Open [`TIER1_AUTHORITY_ENFORCEMENT.json`](evidence/public-evidence-companion/v1/03_TIER1_AUTHORITY_ENFORCEMENT/TIER1_AUTHORITY_ENFORCEMENT.json).

Packet 03 binds exact source identities and named enforcement anchors including:

- `enforce_startup_authority`
- `evaluate_runtime_admission`
- `force_fail_closed_packet`
- `apply_runtime_admission`
- `validate_authority_manifest`
- `_build_release_gate`
- `evaluate_freeze_gate`

It records source hashes and declaration matches for the identified artifacts. Pair Packet 03's source/anchor evidence with Packet 06's observed capture for a two-class view of implementation identity and observed behavior.

## 3. Recorded evidence lanes

Packet 06 retains three direct discrepancy records:

1. `D06-001` — external-freeze readiness value versus derived-verdict divergence;
2. `D06-002` — `ehco1_authority.py` hash divergence inside the bound record set;
3. `D06-003` — live-capture classification versus a freeze reason containing `deployment_evidence_not_live_capture`.

The capture also identifies five additional behavioral evidence lanes for controlled qualification:

1. invalid admission;
2. manifest-mismatch fail-closed behavior;
3. missing-proof adversarial control;
4. discrete public-projection denial; and
5. process restart, persisted-state recovery, and re-admission.

This register gives reviewers a precise map of observed evidence and follow-on qualification targets.

## 4. Public and controlled diligence surfaces

The public repository provides architecture, exact bounded implementation anchors, source hashes, observed execution records, discrepancies, manifests, receipts, and proof scopes.

Controlled diligence can extend that public route through exact source/revision identity, hashes or digests, reviewer-selected safe tests, witnessed build/execution, and written verification findings. Protected implementation, schemas, credentials, topology and operational access remain in controlled custody.

## 5. Reviewer path

1. Packet 06 observed capture and raw probe;
2. Packet 03 source identities and enforcement anchors;
3. Packet 06 discrepancy/gap register;
4. [Runtime, Repository, and Test-Estate Boundary](architecture/runtime-repository-and-test-estate-boundary.md);
5. [Public Claim → Evidence Matrix](assurance/CLAIM-EVIDENCE-MATRIX.md);
6. [Public Evidence Companion](evidence/README.md); and
7. broader EHCOsystem architecture.

## Evidence scope

This page routes reviewers to existing public records. Each linked artifact retains its own evidence class, time boundary, status and scope.
