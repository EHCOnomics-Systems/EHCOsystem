# Verify EHCOsystem

This is the canonical human-readable verification front door for the EHCOsystem public technical publication candidate.

## What can be verified here

EHCOsystem separates three evidence domains:

1. **Public repository verification** checks the integrity and coherence of the public representation for an exact repository revision.
2. **Executable public proof** lets a reviewer cause fresh, bounded, synthetic computation using the accepted Public Proof Kernel.
3. **Comparative public proof** uses a preregistered protocol to compare the bounded public proof proposition against a frozen external reference. The selected reference is Open Policy Agent (OPA) v1.20.2.

None of these surfaces creates Tier One Runtime authority, changes accepted numerical standing 52/53, proves production deployment, or transfers proprietary implementation source.

## Canonical verifier

Run:

```text
python3 verification/verify_all_public.py
```

Machine-readable discovery:

`verification/EHCO_PUBLIC_VERIFICATION_MANIFEST.json`

## Executable public proof

Accepted proof identity:

`c208cb7cd002d016359f39aba1e3aef3f820befc`

Proof family:

`EHCO-PUBLIC-PROOF-KERNEL-PREINTELLIGENCE-GATE-001`

Public path:

`proof/public-kernel/v1/`

The proof is deliberately synthetic, offline, standard-library-only, model-free, and bounded to its published proposition.

## Comparative proof

Protocol:

`EHCO-C1B-OPA-PUBLIC-PROOF-COMPARISON-001`

Public preregistration identity:

`8a1a05b4865eaefa716e77cbe669e819e7d6e5b3`

Reference:

- Open Policy Agent v1.20.2
- source commit `b2c26708e9d55645d7f837db495031f7e4152594`
- official Linux x86-64 static asset SHA-256 `69da5179ee403d10fa11bab6cfb4ffb0d23dba5f9b682fa977db772a1da5670f`

Official one-shot result SHA-256:

`0010b0f2f0369d9328d34e23d44e7117c038038ce4260a14cb51d0b1ad71e38b`

Result route:

`comparison/c1b/v1/results/`

All five planned cases were recorded with zero omissions and zero run failures. All five produced `MATCHED_DISPOSITION`, and every EHCO public-proof receipt verification exited `0`.

This is a bounded synthetic result, not universal superiority and not independent certification.

## Independent reproduction

Instructions:

`reproduction/INDEPENDENT-REPRODUCTION.md`

The mandatory independent external reproduction receipt is **not yet established**.

## Direct public routes

- Public claims: `assurance/PUBLIC-CLAIM-REGISTRY.json`
- Claim/evidence matrix: `assurance/ECOSYSTEM-CLAIM-EVIDENCE-MATRIX.md`
- Public proof: `proof/public-kernel/v1/`
- Comparative protocol/result: `comparison/c1b/v1/`
- Verification guide: `verification/README.md`
- Reader reference: `reference/Home.md`
- Technical diligence: `ECOSYSTEM-DILIGENCE.md`
- Security / responsible disclosure: `SECURITY.md`
- Citation metadata: `CITATION.cff`
- Launch-baseline candidate manifest: `PUBLIC_LAUNCH_BASELINE.json`

## Public / proprietary boundary

The public verifier and proof harness operate only on intentionally public material. They are not the proprietary EHCO evaluator, are not the Tier One Runtime, and are not independent third-party certification.

Private implementation source, private repository/source topology, private control routing, credentials, privileged endpoints, and protected operational topology remain outside this public verification route.

## Launch state

`EHCO_PUBLIC_LAUNCH_BASELINE_V1_ACCEPTED` has **not** been issued. Independent reproduction, final launch qualification, provider checkpoint, and acceptance remain separate gates.
