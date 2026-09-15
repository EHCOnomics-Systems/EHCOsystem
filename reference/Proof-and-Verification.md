# Proof and Verification

EHCOsystem separates repository checks, executable proof, comparative proof, evidence ownership, and independent reproduction. They answer different questions and should not be treated as interchangeable evidence.

## Start with the canonical verifier

Use [`VERIFY.md`](../VERIFY.md) for the public verification front door, or run:

`python3 verification/verify_all_public.py`

The verifier itself is at [`verification/verify_all_public.py`](../verification/verify_all_public.py), with supporting documentation in [verification/README.md](../verification/README.md).

## Executable public proof

The accepted bounded Public Proof Kernel is identified by `c208cb7cd002d016359f39aba1e3aef3f820befc` and proof family `EHCO-PUBLIC-PROOF-KERNEL-PREINTELLIGENCE-GATE-001`.

It is a public-safe synthetic proof mechanism. It is not proprietary EHCO implementation source and it is not the Tier One Runtime.

Review the proof package at [proof/public-kernel/v1/](../proof/public-kernel/v1/README.md).

## Comparative proof

The preregistered comparison protocol is `EHCO-C1B-OPA-PUBLIC-PROOF-COMPARISON-001`, bound to pre-result public identity `8a1a05b4865eaefa716e77cbe669e819e7d6e5b3`.

The official one-shot comparison is complete. The machine result SHA-256 is `0010b0f2f0369d9328d34e23d44e7117c038038ce4260a14cb51d0b1ad71e38b`, with the public evidence under [comparison/c1b/v1/results/](../comparison/c1b/v1/results/README.md).

Use [Comparative Proof](Comparative-Proof.md) for the protocol, fairness rules, official result, and interpretation limits.

## Independent reproduction

[`reproduction/INDEPENDENT-REPRODUCTION.md`](../reproduction/INDEPENDENT-REPRODUCTION.md) defines the clean external reproduction procedure. An independent external reproduction receipt has not yet been established.

## Evidence reading guide

Read every public proposition through four questions:

1. **What exact claim is being made?** Use the [public claim registry](../assurance/PUBLIC-CLAIM-REGISTRY.json).
2. **Which evidence domain owns it?** Use the [claim-to-evidence matrix](../assurance/ECOSYSTEM-CLAIM-EVIDENCE-MATRIX.md).
3. **What can the public verifier actually establish?** Repository validation establishes coherence of the public repository and intentionally public proof objects.
4. **What does the evidence not establish?** Public proof does not by itself create Runtime authority, Runtime state, deployment, standing changes, or proprietary same-code identity.

The Public Proof Kernel and comparative protocol establish only their bounded published propositions. None of these artifacts reissues or replaces the evidence that owns Runtime or component state.
