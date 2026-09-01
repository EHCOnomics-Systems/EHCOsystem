# Public Repository Validation

EHCOsystem uses one canonical public-repository verification entrypoint:

```bash
python3 verification/verify_all_public.py
```

The orchestrator runs the complete required validator set in a stable order:

1. public repository integrity and disclosure boundaries;
2. canonical public claim registry;
3. accepted Runtime / Full Flex public representation;
4. Language Model public snapshot;
5. Range Reactor capability snapshot;
6. Range Reactor operational-closure public result; and
7. registered public release identity.

The required GitHub workflow runs this same entrypoint, so local reviewer instructions and repository CI describe the same validation surface.

## What validation establishes

A successful run establishes that the checked-out public repository is internally coherent for its exact revision: required files and links are present, public/private disclosure boundaries hold, selected public evidence records match their expected identities, component and Runtime terminology is consistent, and the reader-facing representation satisfies the repository's public validation rules.

Repository validation qualifies the **public representation**. It does not reopen or replace the owning evidence that established Runtime operation, Full Flex, Range Reactor performance/semantic closure, Language Model artifact/release/staging state, deployment, authority, standing, or Runtime participation.

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
