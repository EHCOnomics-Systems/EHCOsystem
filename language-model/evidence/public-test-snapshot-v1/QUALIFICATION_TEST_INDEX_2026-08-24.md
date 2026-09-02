# EHCO Language Model Qualification Test Index

**Source-review date:** 2026-08-24  
**Evidence class:** bounded public index of controlled repository test source  
**Currentness:** dated exact-source review snapshot

This index records selected exact test names and qualification dimensions observed in the controlled EHCO Language Model source. The complete executable harness remains in controlled technical custody and this public index exposes the qualification structure at a reviewer-usable level.

## Deterministic replay and metamorphic qualification

Observed test names include:

- `test_identity_replay_qualifies_exact_canonical_document`
- `test_identity_replay_rejects_deterministic_contradiction`
- `test_identity_replay_withholds_missing_evidence`
- `test_explicit_pairwise_equivalence_qualifies_accepted_binding`
- `test_pairwise_missing_relation_is_withheld`
- `test_pairwise_source_anchored_transitivity_is_withheld`
- `test_pairwise_rejected_accepted_relation_rejects`
- `test_pairwise_binding_corruption_rejects`
- `test_verified_round_trip_qualifies`
- `test_round_trip_missing_is_withheld`
- `test_round_trip_binding_corruption_rejects`
- `test_aggregate_is_deterministic_and_strictly_replayable`
- `test_failure_frontier_contains_every_nonqualified_case`
- `test_all_qualified_cases_have_clean_bounded_frontier`
- `test_duplicate_case_identity_is_rejected`
- `test_schema_rejects_effect_promotion`
- `test_schema_rejects_global_completeness_promotion`

These tests exercise `QUALIFIED`, `WITHHELD` and `REJECTED` outcomes across missing evidence, relation loss, binding corruption, duplicate identity, effect-promotion attempts, and global-completeness-promotion attempts.

## Structural and property qualification

Observed test names include:

- `test_replay_witness_input_order_invariance_qualifies`
- `test_replay_case_set_drift_rejects`
- `test_s2_canonical_state_order_invariance_qualifies`
- `test_s2_strict_replay_rejects_noncanonical_provenance_order`
- `test_pairwise_preservation_qualifies_and_missing_support_withholds`
- `test_pairwise_rejected_relation_is_not_preserved`
- `test_round_trip_preservation_qualifies_and_carrier_drift_rejects`
- `test_s2_declared_extension_addition_qualifies`
- `test_s2_extension_binding_loss_rejects`
- `test_s2_semantic_payload_version_provenance_and_proof_lineage_drift_reject`

The inspected source exercises canonical ordering, provenance preservation, semantic-state drift, pairwise semantic preservation, round-trip preservation, extension-binding integrity, and proof-lineage drift.

## Full-range qualification dimensions

The inspected qualification source includes explicit dimensions for:

- text-encoding adversarial cases;
- mutation and fuzz failure-frontier cases;
- cross-caller semantic conformance;
- semantic injection and evidence poisoning;
- performance and resource bounds;
- bounded complexity and recursion.

Observed aggregate tests include:

- `test_campaign_replay_and_case_order_are_deterministic`
- `test_every_nonqualified_case_enters_failure_frontier`
- `test_rejected_case_dominates_aggregate_disposition`

These aggregate tests enforce deterministic campaign replay, explicit failure-frontier custody, disposition precedence, global-completeness bounding, and zero-effect qualification semantics.

## Deterministic component service boundary

Observed service-boundary tests include:

- `test_service_preserves_direct_engine_result_and_is_deterministic`
- `test_qualification_is_not_derived_from_semantic_disposition`
- `test_http_boundary_returns_same_component_response`
- `test_http_boundary_fails_closed_for_missing_engine_case_identity`
- `test_http_boundary_rejects_untyped_qualification_disposition`

These tests exercise deterministic replay through the component boundary, semantic-result/qualification separation, transport equivalence, identity validation, and typed qualification handling.

## Evidence scope

This index establishes selected source-reviewed test names and qualification dimensions. `actual-tests/` and `MANIFEST.json` establish the exact published fixture artifacts. The current Language Model architecture and maturity record is grounded through the owning controlled source and qualification estate.
