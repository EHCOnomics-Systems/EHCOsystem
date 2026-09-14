# Public Repository Validation

EHCOsystem uses one canonical public-repository verification entrypoint:

```bash
python3 verification/verify_all_public.py
```

The orchestrator runs the complete required validator set in a stable order:

1. public repository integrity and disclosure boundaries;
2. pre-publication disclosure-gate synthetic regression behavior;
3. canonical public claim registry;
4. bounded executable Public Proof Kernel;
5. accepted Runtime / Full Flex public representation;
6. Language Model public snapshot;
7. Range Reactor capability snapshot;
8. Range Reactor operational-closure public result;
9. registered public release identity; and
10. SOW-10 Public Launch candidate bindings, including C1B frozen-protocol integrity, result-manifest closure, launch threat/failure coverage, machine verification discovery, baseline candidate cross-bindings, public reproduction contract state, and required public routes.

The required GitHub workflow runs this same entrypoint, so local reviewer instructions and repository CI describe the same validation surface.

## Pre-publication disclosure gate

Repository validation after a push is not the confidentiality boundary. For normal publisher transports, the candidate must be qualified before GitHub receives it.

Install the clone-local pre-push guard once:

```text
python verification/install_publication_guard.py
```

The installed hook calls `verification/pre_publication_gate.py` for each pushed candidate ref. The gate compares the exact candidate to accepted public `main` and scans:

- every newly reachable Git blob, including transient content later removed from the final tree;
- commit messages;
- provider-visible ref names;
- repository paths;
- high-confidence secret indicators; and
- provider-facing metadata files supplied explicitly with `--metadata-file`.

The gate does not echo matched protected values. It reports rule classes only. Successful local execution can write `.git/ehco-publication-clearance.json`, which remains outside the public tree and binds the exact candidate SHA/tree. Any candidate mutation requires a fresh clearance.

Opaque archive and office-container additions fail closed rather than being treated as inspected public material.

For provider-facing narrative that is not part of the Git candidate, place the proposed title/body/release text in a local file and run:

```text
python verification/pre_publication_gate.py --base origin/main --candidate HEAD --ref-name CANDIDATE_PUBLIC_REF --metadata-file LOCAL_METADATA_FILE --receipt .git/ehco-publication-clearance.json
```

Use public-safe placeholders such as `CANDIDATE_PUBLIC_REF` and `LOCAL_METADATA_FILE`; do not put protected identifiers into shell history merely to test the gate.

## Bounded executable Public Proof Kernel

`proof/public-kernel/v1/` is an intentionally public, standard-library-only, offline, model-free proof/reference implementation of one synthetic pre-intelligence gating proposition. It is not the Tier One Runtime and does not reproduce proprietary implementation source.

Run the candidate-specific validation:

```text
python3 verification/validate_public_proof_kernel.py
```

The validator exercises five official governed-disposition fixtures plus fixture, protocol, artifact, receipt, and nonce tamper/replay controls. The proof emits nonce-bound machine-readable receipts and preserves `PASS`, `WITHHOLD`, `RETAIN_AMBIGUITY`, `UNSUPPORTED_REQUEST`, and integrity/protocol failure semantics without promoting the result into Runtime authority, standing, deployment, Language Model qualification, or Range Reactor qualification.

The proof package's manifest binds exact public proof bytes by SHA-256 but intentionally does not embed its own final Git commit SHA. Final launch-checkpoint identity is a separate later acceptance binding.

## SOW-10 Public Launch candidate bindings

`verification/validate_public_launch_candidate.py` is the canonical launch-candidate integrity layer. It does not create Public Launch Baseline acceptance. It validates the currently published candidate state by requiring:

- byte-for-byte SHA-256 closure of all nine files in the C1B preregistration manifest;
- the exact preregistration identity `8a1a05b4865eaefa716e77cbe669e819e7d6e5b3` and manifest SHA-256 `440ae3a567f0d7db29a2c3348d0a7eb296ca5eece0b31a78fb9b58932efba357`;
- the exact official one-shot result SHA-256 `0010b0f2f0369d9328d34e23d44e7117c038038ce4260a14cb51d0b1ad71e38b`;
- closure of every file published by the C1B result manifest, with five planned / five recorded cases, zero omissions, zero recorded run failures, and no preferred-result rerun;
- launch-level threat/failure coverage for static replay, artifact/fixture substitution, post-result protocol drift, hidden dependency, reference-baseline drift, asymmetric comparative configuration, selective omission, integrity bypass, and claim-scope inflation;
- canonical-verifier Git-blob identity and machine-route consistency;
- Public Launch Baseline candidate cross-bindings to the verification-discovery and launch-threat-model digests; and
- independent external reproduction remaining `NOT_ESTABLISHED` until an owning third-party receipt is received and validated.

Run it directly with:

```text
python3 verification/validate_public_launch_candidate.py
```

The launch validator is also child 10 of `verification/verify_all_public.py`, so the repository workflow cannot report canonical success while those launch bindings are inconsistent.

## What validation establishes

A successful run establishes that the checked-out public repository is internally coherent for its exact revision: required files and links are present, public/private disclosure boundaries hold, selected public evidence records match their expected identities, component and Runtime terminology is consistent, and the reader-facing representation satisfies the repository's public validation rules.

Repository validation qualifies the **public representation**. The Public Proof Kernel additionally provides fresh bounded computation for its exact synthetic protocol. The C1B launch-candidate validator verifies published protocol/result/binding integrity. None of those layers reopens or replaces the owning evidence that established Runtime operation, Full Flex, Range Reactor performance/semantic closure, Language Model artifact/release/staging state, deployment, authority, standing, or Runtime participation.

The public validation surface also enforces **durable public semantics** for the intended repository resting state: active reader-facing language must preserve evidence ownership, lifecycle dimensions, Runtime identity/authority separation, accepted evidence meaning, and historical/event-time scope without creating avoidable live-currentness obligations.

## Accepted Runtime / Full Flex

`validate_current_runtime_evidence.py` retains its established filename and machine-facing status vocabulary while verifying the accepted Full Flex-first public Runtime route, accepted Runtime maturity `REALIZED / COMPLETE_IN_ACCEPTED_SCOPE`, standing **52/53**, `EHCO_DOCKER_PORTABILITY` as `PRIMARY_ACCESSIBLE_RUNTIME_PROJECTION`, the accepted Full Flex packet SHA-256 `7F80C27D085AE871A00AED412C6F20EA9A76CB0677C93AEBA381CD1FD70EC8E5`, public-safe packet identity/receipt custody, and the historical classification of the Public Evidence Companion.

It also protects reader-facing semantics by rejecting residual Full Flex “synthesis” language and wording that assigns Tier One Runtime authority/state ownership to EHCO AI-OS instead of `INSTANTIATED_EHCO_RUNTIME`.

## Language Model

`validate_public_lm_test_snapshot.py` verifies the established seven-fixture / 62-case public snapshot. The accepted public component record and deterministic capability demonstration are presentation surfaces for already-established accepted Language Model capabilities; they do not create a new maturity or lifecycle proof program.

## Range Reactor

`validate_public_range_reactor_snapshot.py` verifies the synthetic capability snapshot.

`validate_public_range_reactor_operational_closure.py` verifies the accepted selected-scope public operational-closure result, including **14.304307x** wall-clock improvement, **14.208722x** CPU-time improvement, **94.755854%** benchmark-defined Python peak-allocation reduction, **1,957 → 64** states, **1,956 → 192** transitions, **720 → 720** histories, and **82 passed / 0 failed** selected semantic closure. Public validation verifies the public-safe result record and its integrity fields; private owning-source topology remains outside the public tree.

## Acceptance governance

Pull-request acceptance uses the exact candidate plus the repository and organization protections that apply at review time, including repository validation, CodeQL, and the EHCO Assistant Operation Gate. Accepted numerical standing remains **52/53** unless separately changed by its owning authority.

The current result-publication candidate does not issue `EHCO_PUBLIC_LAUNCH_BASELINE_V1_ACCEPTED`. Independent external reproduction remains separately required; discovery/reconstruction, final exact-candidate qualification, launch checkpoint, broader distribution, and end-to-end public-loop closure remain downstream SOW gates.
