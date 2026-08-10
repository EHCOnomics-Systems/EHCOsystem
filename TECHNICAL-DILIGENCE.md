---
title: EHCO AI-OS Technical Diligence — Start Here
version: 1.0
status: public-diligence-navigation
published: 2026-08-10
maintainer: EHCOnomics
evidence_class: navigation-and-bounded-technical-summary
proof_ceiling: navigation and source-bound summary only; underlying records retain their own proof ceilings
---

# Technical Diligence — Start Here

This page is the shortest public route to the technically differentiated EHCO AI-OS material. It is intended for reviewers who want to inspect implementation anchors and observed behavior before reading the broader architecture estate.

## Technical claim

EHCO AI-OS separates model or tool capability from the authority for an action or state to acquire governed operational consequence. The public evidence exposes a bounded enforcement path for authority admission, packet and continuity evaluation, proof and range evaluation, quarantine, and release/freeze gating.

The public repository does not disclose the complete proprietary Runtime implementation. It does expose exact bounded implementation anchors, source hashes, observed execution records, discrepancies, and proof ceilings so a reviewer can distinguish declarations from observations.

## 1. Start with the observed run — Packet 06

Open:

- [`OBSERVED_LIVE_CAPTURE.json`](evidence/public-evidence-companion/v1/06_OBSERVED_LIVE_CAPTURE_AND_RELEASE_STATUS/06A_OBSERVED_LIVE_CAPTURE/OBSERVED_LIVE_CAPTURE.json)
- raw [`api_chat_probe.json`](evidence/public-evidence-companion/v1/06_OBSERVED_LIVE_CAPTURE_AND_RELEASE_STATUS/06A_OBSERVED_LIVE_CAPTURE/raw/api_chat_probe.json)
- [`DISCREPANCY_AND_GAP_REGISTER.json`](evidence/public-evidence-companion/v1/06_OBSERVED_LIVE_CAPTURE_AND_RELEASE_STATUS/06C_DISCREPANCY_AND_GAP_REGISTER/DISCREPANCY_AND_GAP_REGISTER.json)

Packet 06 preserves a hash-bound `local_live` capture. Within that capture, the public records show:

- three observed Compose service rows and three healthy rows;
- authority admission recorded as admitted;
- packet, continuity, range, and proof status recorded as valid;
- recovery quarantine active under a bounded recovery scope;
- a release gate returning `bounded_release` while withholding closure, readiness language, and freeze;
- the raw packet records `llm_configured: true`, `llm_invoked: false`, and `llm_used: false`.

That last point is important for diligence: in this bounded run, the recorded authority/proof/range/quarantine/release-gate state was produced while the configured LLM was not invoked or used.

Packet 06 is not represented as universal behavioral proof or current Runtime state. Its own record states that a negative-control suite was not executed.

## 2. Then inspect the implementation anchors — Packet 03

Open:

- [`TIER1_AUTHORITY_ENFORCEMENT.json`](evidence/public-evidence-companion/v1/03_TIER1_AUTHORITY_ENFORCEMENT/TIER1_AUTHORITY_ENFORCEMENT.json)

Packet 03 binds exact source identities and named enforcement anchors, including:

- `enforce_startup_authority`
- `evaluate_runtime_admission`
- `force_fail_closed_packet`
- `apply_runtime_admission`
- `validate_authority_manifest`
- `_build_release_gate`
- `evaluate_freeze_gate`

The packet includes source hashes and declaration matches. Its boundary is explicit: it proves sealed artifact identity and the presence of named declarations; it does not by itself claim live execution. Pair Packet 03 with Packet 06 rather than treating either record as sufficient alone.

## 3. What the public evidence currently does not close

Packet 06 openly retains three direct unresolved discrepancies:

1. `D06-001` — external-freeze readiness value versus derived verdict divergence;
2. `D06-002` — `ehco1_authority.py` hash divergence inside the bound record set;
3. `D06-003` — live-capture classification versus a freeze reason containing `deployment_evidence_not_live_capture`.

It also lists five behavioral lanes that were not directly observed:

1. invalid admission;
2. manifest-mismatch fail-closed behavior;
3. missing-proof negative control;
4. discrete public-projection denial;
5. process restart, persisted-state recovery, and re-admission.

These are presented as open evidence lanes, not as passes and not as evidence of failure.

## 4. What is public and what is private

This repository is a public architecture, evidence, provenance, verification, and publication surface. Complete proprietary Runtime implementation, protected control mechanics, credentials, active production infrastructure, and confidential proof material are intentionally excluded.

For qualified technical diligence, EHCOnomics can provide controlled access to additional Runtime source and verification material under the applicable diligence process. The public evidence should be used to identify the exact implementation and behavioral questions to inspect in that private review.

## 5. Suggested reviewer path

For a technical review, use this order:

1. Packet 06 observed capture and raw probe;
2. Packet 03 source identities and enforcement anchors;
3. Packet 06 discrepancy and gap register;
4. [Runtime, Repository, and Test-Estate Boundary](architecture/runtime-repository-and-test-estate-boundary.md);
5. [Public Claim → Evidence Matrix](assurance/CLAIM-EVIDENCE-MATRIX.md);
6. [Public Evidence Companion](evidence/README.md);
7. broader architecture only as needed.

## Interpretation boundary

This page does not create Runtime state, authority, proof, release, deployment, or standing. It summarizes and routes to existing public records. Each linked artifact retains its own evidence class, time boundary, status, and proof ceiling.
