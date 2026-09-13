# EHCOsystem Public Proof Kernel — Pre-Intelligence Gate v1

This directory contains a deliberately **public, bounded, synthetic proof kernel** for the EHCOsystem public-launch program.

It demonstrates one narrow proposition: under the frozen synthetic protocol, declared proof-relevant governing conditions are evaluated **before** a deterministic intelligence placeholder may execute; invalid, missing, ambiguous, unsupported, or integrity-invalid cases do not invoke the placeholder; and each run emits a nonce-bound machine-readable receipt.

## What this is

- an intentionally public proof/reference implementation;
- standard-library-only Python;
- offline;
- model-free;
- deterministic for material output under the same frozen input and nonce;
- inspectable without any private EHCOnomics repository, Drive record, credential, endpoint, or unpublished intervention.

## What this is not

This proof kernel is **not** the Tier One EHCO Runtime. It does not simulate or assert Runtime standing, authority, admission, binding, invocation, participation, or current Runtime state. Its synthetic labels are proof-only conditions and are not private Runtime schema fields.

It does not requalify EHCO AI-OS, the EHCO Language Model, EHCO Range Reactor, deployment, production, or accepted standing **52/53**. It does not show that proprietary EHCO implementation source uses the same code or internal mechanics. It is not independent certification and it is not a universal superiority claim.

## Run a fresh proof

From the repository root:

```text
python3 proof/public-kernel/v1/kernel.py --fixture PK-VALID-001 --nonce REVIEWER_CHALLENGE --receipt-out receipt.json
python3 proof/public-kernel/v1/verify_receipt.py --receipt receipt.json --expected-nonce REVIEWER_CHALLENGE
```

Use your own unpredictable nonce for a real fresh-run challenge.

Official synthetic fixture families are defined in `fixtures.json`:

- `PK-VALID-001` -> `PASS`, placeholder invoked exactly once.
- `PK-MISSING-PERMISSION-001` -> `WITHHOLD`, placeholder not invoked.
- `PK-ELIGIBILITY-NOT-SATISFIED-001` -> `WITHHOLD`, placeholder not invoked.
- `PK-AMBIGUOUS-001` -> `RETAIN_AMBIGUITY`, placeholder not invoked.
- `PK-UNSUPPORTED-001` -> `UNSUPPORTED_REQUEST`, placeholder not invoked.

The repository validator also exercises fixture, protocol, artifact, receipt, and nonce tamper/replay controls.

## Integrity model

`public-proof-manifest.json` binds the exact protocol, kernel, verifier, environment, fixture, claim/test, and threat-control files by SHA-256. The tracked manifest intentionally does **not** contain its own final Git commit SHA. Final public-launch Git/tag/Release identity is a separate later acceptance binding.

A mutation to the exact public candidate requires a new pre-publication clearance before provider publication.

## Evidence class

`FRESH_EXECUTABLE_PUBLIC_PROOF_OF_BOUNDED_PUBLIC_KERNEL`

This evidence class remains separate from accepted historical technical evidence, comparative proof, independent reproduction evidence, public/social evidence, and Runtime-owned evidence.

## Validation

Run the candidate-specific validator:

```text
python3 verification/validate_public_proof_kernel.py
```

Run the complete canonical public repository validation:

```text
python3 verification/verify_all_public.py
```

The candidate is not `EHCO_PUBLIC_LAUNCH_BASELINE_V1_ACCEPTED`. Comparative preregistration/results, machine-resolution, Wiki/reference, independent external reproduction, discovery/reconstruction, launch checkpoint, distribution, and end-to-end loop closure remain later SOW gates.
