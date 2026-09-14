# C1B OPA comparative proof preregistration candidate

Status: **prelaunch candidate**. No official comparative result exists.

This package freezes a proposed fair comparison between the accepted EHCOsystem Public Proof Kernel and Open Policy Agent (OPA) v1.20.2. It is designed to become a public preregistration **before** any official result run.

The comparison does not ask whether EHCO is universally better. It asks what each operand establishes, permits, withholds, records, and makes independently verifiable under the same frozen synthetic scenarios.

## Frozen operands

- EHCO: `EHCO-PUBLIC-PROOF-KERNEL-PREINTELLIGENCE-GATE-001`, accepted at Git identity `c208cb7cd002d016359f39aba1e3aef3f820befc`.
- Reference: Open Policy Agent `v1.20.2`, source commit `b2c26708e9d55645d7f837db495031f7e4152594`.
- Official reference asset for protocol v1.0.0: upstream `opa_linux_amd64_static`, SHA-256 `69da5179ee403d10fa11bab6cfb4ffb0d23dba5f9b682fa977db772a1da5670f`.
- OPA licensing: Apache-2.0. The reference binary is obtained from the official upstream release; EHCOsystem does not need to redistribute it.

## Frozen comparison policy

`opa-reference.rego` implements the reference-side decision semantics for the five shared synthetic fixtures using documented OPA policy evaluation. The policy digest is bound by `manifest.json`.

Features that are not natively supplied by an operand are classified as `NOT_PROVIDED_WITH_REASON` or as harness-level observations; they are not fabricated as native capability.

## Pre-preregistration qualification

Before this package may cross the public preregistration boundary, the exact candidate must pass:

1. manifest and package-integrity validation;
2. frozen OPA tag/commit/release-asset identity validation;
3. native OPA parsing of `opa-reference.rego`;
4. native OPA evaluation of every shared fixture as **qualification-only**, not as the official comparison result;
5. comparison-harness/failure-accounting checks;
6. disclosure qualification over the exact candidate plus proposed provider-visible ref and pull-request narrative.

The qualification mode is:

```text
python3 comparison/c1b/v1/run_comparison.py --opa /path/to/opa_linux_amd64_static --qualify-reference --qualification-out qualification.json
```

That qualification output is not an official comparative result.

## Official run boundary

An official comparison run is prohibited until the protocol is publicly preregistered at an exact immutable or provider-resolvable identity. The official run must bind that exact identity:

```text
python3 comparison/c1b/v1/run_comparison.py --opa /path/to/opa_linux_amd64_static --preregistration-identity <PUBLIC_PREREGISTRATION_IDENTITY> --nonce <FRESH_CHALLENGE> --output-dir comparison-results
```

All five planned cases must be retained. Failures, timeouts, ambiguity, unsupported cases, OPA advantages, and unfavorable EHCO outcomes may not be silently omitted or rerun into a preferred result.

## Scope boundary

This comparison is limited to the public synthetic proof proposition. It does not establish Tier One Runtime state, authority, participation, deployment, standing changes, proprietary implementation identity, independent certification, or universal superiority.
