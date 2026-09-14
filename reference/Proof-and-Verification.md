# Proof and Verification

EHCOsystem separates repository checks, executable proof, comparative proof, and independent reproduction. They answer different questions and should not be treated as interchangeable evidence.

## Repository validation
Run:

`python3 verification/verify_all_public.py`

This checks the public repository representation for the exact checkout being reviewed.

## Executable public proof
The accepted bounded Public Proof Kernel is identified by `c208cb7cd002d016359f39aba1e3aef3f820befc` and proof family `EHCO-PUBLIC-PROOF-KERNEL-PREINTELLIGENCE-GATE-001`.

It is a public-safe synthetic proof mechanism. It is not proprietary EHCO implementation source and it is not the Tier One Runtime.

## Comparative proof
The preregistered comparison protocol is `EHCO-C1B-OPA-PUBLIC-PROOF-COMPARISON-001`, bound to pre-result public identity `8a1a05b4865eaefa716e77cbe669e819e7d6e5b3`.

The official one-shot comparison is complete. The machine result SHA-256 is `0010b0f2f0369d9328d34e23d44e7117c038038ce4260a14cb51d0b1ad71e38b`, with the public evidence under `comparison/c1b/v1/results/`.

All five planned cases were recorded. There were no omissions and no run-failure cases. The result is limited to the frozen synthetic protocol and does not support a universal-superiority claim.

## Independent reproduction
`reproduction/INDEPENDENT-REPRODUCTION.md` defines the clean external reproduction procedure. An independent external reproduction receipt has not yet been established.

## What each layer proves
Repository validation establishes coherence of the public repository. The Public Proof Kernel and comparative protocol establish only their bounded published propositions. None of these artifacts reissues or replaces the evidence that owns Runtime or component state.
