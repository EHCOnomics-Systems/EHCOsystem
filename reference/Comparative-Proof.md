# Comparative Proof

## What the comparison asks
Under the frozen synthetic inputs, conditions, dispositions, and observables, what does the accepted EHCOsystem Public Proof Kernel and the frozen reference system each establish, permit, withhold, record, and make independently verifiable?

## Reference system
The reference is Open Policy Agent (OPA) v1.20.2 at source commit `b2c26708e9d55645d7f837db495031f7e4152594`, using the frozen Linux x86-64 static asset with SHA-256 `69da5179ee403d10fa11bab6cfb4ffb0d23dba5f9b682fa977db772a1da5670f`.

The frozen reference policy is published at [`comparison/c1b/v1/opa-reference.rego`](../comparison/c1b/v1/opa-reference.rego), and the frozen reference identity is recorded in [`reference-baseline.json`](../comparison/c1b/v1/reference-baseline.json).

## Fairness rules
The protocol is not designed to manufacture a winner. It uses materially equivalent synthetic requests and keeps different kinds of absence separate: native capability, protocol-level policy, harness-level observation, and not-provided-with-reason are not collapsed into one category.

All planned cases are retained, including EHCO failures, OPA advantages, ambiguity, unsupported requests, timeouts, and environment failures.

Review the frozen protocol in [`protocol.json`](../comparison/c1b/v1/protocol.json), the shared fixtures in [`shared-fixtures.json`](../comparison/c1b/v1/shared-fixtures.json), and the execution environment in [`environment.json`](../comparison/c1b/v1/environment.json).

## Preregistration
The exact pre-result public identity is:

`8a1a05b4865eaefa716e77cbe669e819e7d6e5b3`

The frozen protocol manifest SHA-256 is:

`440ae3a567f0d7db29a2c3348d0a7eb296ca5eece0b31a78fb9b58932efba357`

The preregistration manifest is [`comparison/c1b/v1/manifest.json`](../comparison/c1b/v1/manifest.json).

## Official result
The official result SHA-256 is:

`0010b0f2f0369d9328d34e23d44e7117c038038ce4260a14cb51d0b1ad71e38b`

Five cases were planned and all five were recorded. There were no omissions and no run failures. Every EHCO receipt verification exited `0`.

The recorded dispositions were:

- `PASS` / `PASS`
- `WITHHOLD` / `WITHHOLD`
- `WITHHOLD` / `WITHHOLD`
- `RETAIN_AMBIGUITY` / `RETAIN_AMBIGUITY`
- `UNSUPPORTED_REQUEST` / `UNSUPPORTED_REQUEST`

Read the [result index](../comparison/c1b/v1/results/README.md), [machine result](../comparison/c1b/v1/results/comparison-result.json), and [result manifest](../comparison/c1b/v1/results/result-manifest.json).

## Optional external corroboration
The clean public reproduction route is published in [`reproduction/INDEPENDENT-REPRODUCTION.md`](../reproduction/INDEPENDENT-REPRODUCTION.md). It is available to an independent reviewer using only public material. Public Launch Baseline v1 does not include a third-party reproduction receipt, so no third-party certification or external corroboration is claimed. A qualifying later reproduction would add a separate supplemental evidence class; it is not an unresolved validation or launch requirement.

Historical result artifacts retain the exact event-time state under which they were originally published. Any earlier event-time wording about external reproduction does not override the current accepted Baseline v1 state or convert optional corroboration into a present blocking gate.

## How to read the result
The comparison establishes bounded observed behavior under the frozen synthetic protocol. It does not establish universal superiority, production readiness, Tier One Runtime authority or state, deployment, proprietary same-code identity, or independent certification.
