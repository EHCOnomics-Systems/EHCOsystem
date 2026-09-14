# C1B OPA comparative proof

Status: **protocol preregistered; official one-shot result complete; independent external reproduction pending.**

The exact pre-result protocol remains permanently bound to public preregistration identity:

`8a1a05b4865eaefa716e77cbe669e819e7d6e5b3`

The nine files bound by `manifest.json` remain the frozen v1.0.0 comparison protocol. The official result does not mutate that preregistered protocol.

## Frozen operands

- EHCO: `EHCO-PUBLIC-PROOF-KERNEL-PREINTELLIGENCE-GATE-001`, accepted at Git identity `c208cb7cd002d016359f39aba1e3aef3f820befc`.
- Reference: Open Policy Agent `v1.20.2`, source commit `b2c26708e9d55645d7f837db495031f7e4152594`.
- Official reference asset: upstream `opa_linux_amd64_static`, SHA-256 `69da5179ee403d10fa11bab6cfb4ffb0d23dba5f9b682fa977db772a1da5670f`.
- OPA licensing: Apache-2.0. The reference binary is obtained from the official upstream release; EHCOsystem does not redistribute it.

## Frozen comparison policy

`opa-reference.rego` implements the reference-side decision semantics for the five shared synthetic fixtures using documented OPA policy evaluation. The policy digest remains bound by `manifest.json`.

Features that are not natively supplied by an operand are classified as `NOT_PROVIDED_WITH_REASON` or as harness-level observations; they are not fabricated as native capability.

## Official result

The one-shot official comparison was executed only after the preregistration identity above existed.

Official result SHA-256:

`0010b0f2f0369d9328d34e23d44e7117c038038ce4260a14cb51d0b1ad71e38b`

Result route:

[`results/`](results/)

All five planned cases were retained. Five were recorded, zero were omitted, zero had run failures, and every EHCO receipt verification exited `0`. The five recorded disposition pairs were:

- `C1B-VALID-001`: `PASS` / `PASS`
- `C1B-MISSING-PERMISSION-001`: `WITHHOLD` / `WITHHOLD`
- `C1B-ELIGIBILITY-001`: `WITHHOLD` / `WITHHOLD`
- `C1B-AMBIGUOUS-001`: `RETAIN_AMBIGUITY` / `RETAIN_AMBIGUITY`
- `C1B-UNSUPPORTED-001`: `UNSUPPORTED_REQUEST` / `UNSUPPORTED_REQUEST`

No official case was rerun to obtain a preferred result.

## Reproduction

Independent external reproduction is separately required. See:

[`../../../reproduction/INDEPENDENT-REPRODUCTION.md`](../../../reproduction/INDEPENDENT-REPRODUCTION.md)

The required independent reproduction receipt is not yet established.

## Scope boundary

This comparison is limited to the public synthetic proof proposition. It does not establish Tier One Runtime state, authority, participation, deployment, standing changes, proprietary implementation identity, independent certification, or universal superiority.
