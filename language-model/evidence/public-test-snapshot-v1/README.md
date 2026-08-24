# EHCO Language Model Public Test Snapshot v1

## Purpose

This snapshot publishes a bounded selection of actual EHCOnomics Language Model repository test fixtures for technical inspection.

The files under `actual-tests/` are not rewritten examples or marketing demonstrations. Each is a byte-identical copy of a selected synthetic test fixture from the controlled Language Model test estate. At publication review, each public Git blob identity matched the corresponding controlled source artifact identity recorded in `MANIFEST.json`.

The snapshot contains 7 fixture artifacts and 62 explicit test cases covering lexical and morphological behavior, syntax and semantic composition, reference and context, ambiguity and withholding, fail-closed unsupported inputs, bounded mathematical language, an historical unseen-construction boundary, and a whole-path compositional evaluation fixture.

## Evidence class and proof ceiling

This is bounded repository test-artifact evidence. It establishes the identity and contents of the selected test fixtures and makes their inputs and expected dispositions publicly inspectable.

It is not an external benchmark, independent certification, proof of global language completeness, proof of equivalence to a frontier LLM, Runtime admission, Runtime authority, deployment evidence, production evidence, or current Runtime state.

The historical repository regression counts discussed elsewhere, including the 1,268 and later 1,278 checkpoints, are not created or independently proven by this snapshot. Those counts are a different repository-evidence claim. This snapshot exists so reviewers can inspect real test material rather than being asked to infer test design from a count alone.

## Historical fixture boundary

Several exact fixtures in this snapshot come from earlier zero-weight construction and evaluation stages that intentionally tested bounded capability and explicit failure or withholding boundaries. A `WITHHOLD`, `RETAIN_AMBIGUITY`, `CAPABILITY_FAILURE`, or `GENERALIZATION_NOT_ESTABLISHED` expectation is part of the test, not a publication error.

This snapshot is not a claim of current capability ceiling. These historical fixtures must not be read as the current capability ceiling of the Language Model. Later strengthening and qualification added further deterministic language, replay, structural, metamorphic, adversarial, conformance, resource-bound and service-boundary testing. A public-safe index of selected qualification test names and categories observed at the source-review date is provided in `QUALIFICATION_TEST_INDEX_2026-08-24.md`.

The historical whole-path fixture is not presented as a drop-in current regression case. Its expected dispositions belong to the evaluator lineage under which that fixture was created. Later evaluator strengthening changed candidate-resolution requirements, so the preserved historical fixture must not be read as a claim that the unchanged fixture produces the same result under the later evaluator.

The exact fixture copies retain their fixture-local schema and operation identifiers because removing those fields would alter the artifacts. Within this public snapshot those identifiers are frozen historical test metadata only. They are not private repository locators, current branch or pull-request state, active work-packet selection, Runtime authority, or current Runtime state.

## Why the complete harness is not published

The complete private test harness includes proprietary implementation imports, internal module paths, schemas, control objects, source-development locators and implementation surfaces that are outside the disclosure boundary of the public EHCOsystem repository.

For that reason, this snapshot publishes exact synthetic fixtures where the complete artifact is safe, and a bounded index where publishing the full executable harness would disclose protected implementation detail. This follows the repository's existing evidence-first diligence model: enough material to inspect the technical proposition without transferring the proprietary implementation.

## Files

- `MANIFEST.json` records fixture identity, case counts, scopes and proof ceilings.
- `actual-tests/` contains the exact selected test fixtures.
- `QUALIFICATION_TEST_INDEX_2026-08-24.md` records public-safe qualification test names and categories observed at the source-review date.

## Interpretation boundary

A test fixture is not a Runtime. A passing repository test is not Runtime admission. Test publication does not create authority, standing, deployment, release, consequence, persistence or Runtime truth. EHCO AI-OS Runtime authority and current Runtime state remain owned by the instantiated EHCO Runtime and its owning evidence.

Use of these materials is governed by the repository root `LICENSE`.
