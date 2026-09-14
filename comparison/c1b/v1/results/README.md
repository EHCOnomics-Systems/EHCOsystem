# C1B official comparative result

Status: **official one-shot result complete; public result-publication candidate; independent external reproduction pending.**

## Exact bindings

- Protocol: `EHCO-C1B-OPA-PUBLIC-PROOF-COMPARISON-001` v1.0.0
- Public preregistration identity: `8a1a05b4865eaefa716e77cbe669e819e7d6e5b3`
- Frozen C1B manifest SHA-256: `440ae3a567f0d7db29a2c3348d0a7eb296ca5eece0b31a78fb9b58932efba357`
- Accepted EHCO Public Proof Kernel identity: `c208cb7cd002d016359f39aba1e3aef3f820befc`
- OPA v1.20.2 official static asset SHA-256: `69da5179ee403d10fa11bab6cfb4ffb0d23dba5f9b682fa977db772a1da5670f`
- Official result SHA-256: `0010b0f2f0369d9328d34e23d44e7117c038038ce4260a14cb51d0b1ad71e38b`
- Public result manifest SHA-256: `a961891144ff43cf1772bc9bef775eaa723347ec276892a31bcf64a73cffd35c`
- Raw owning run-context SHA-256: `68e16581945a3e282735dc7d21a7d85ab69558daad37b18a6be9ead1ad3ecfb7`

The raw owning run-context is retained outside the public tree because the repository disclosure policy structurally classifies one local context value as a private host locator. `official-run-context-public.json` is a derived public-safe representation bound to those exact source bytes by SHA-256. No official case was rerun.

## Results

| Fixture | EHCO | OPA | Classification |
| --- | --- | --- | --- |
| `C1B-VALID-001` | `PASS` | `PASS` | `MATCHED_DISPOSITION` |
| `C1B-MISSING-PERMISSION-001` | `WITHHOLD` | `WITHHOLD` | `MATCHED_DISPOSITION` |
| `C1B-ELIGIBILITY-001` | `WITHHOLD` | `WITHHOLD` | `MATCHED_DISPOSITION` |
| `C1B-AMBIGUOUS-001` | `RETAIN_AMBIGUITY` | `RETAIN_AMBIGUITY` | `MATCHED_DISPOSITION` |
| `C1B-UNSUPPORTED-001` | `UNSUPPORTED_REQUEST` | `UNSUPPORTED_REQUEST` | `MATCHED_DISPOSITION` |

Five cases were planned and five were recorded. There were zero omitted cases and zero run-failure cases. Every EHCO public-proof receipt verification exited `0`.

## Public evidence

- Machine result: [`comparison-result.json`](comparison-result.json)
- Result manifest: [`result-manifest.json`](result-manifest.json)
- Public-safe execution context: [`official-run-context-public.json`](official-run-context-public.json)
- Official run exit record: [`official-run-exit.json`](official-run-exit.json)
- Per-case EHCO receipts, OPA inputs, and OPA raw outputs are retained in this directory.

## Interpretation boundary

This result establishes only the bounded observed behavior of the two frozen public operands under the preregistered synthetic protocol. It does **not** establish universal superiority, production readiness, independent certification, proprietary same-code identity, Tier One Runtime state or authority, deployment, participation, or any change to accepted numerical standing 52/53.

Independent external reproduction is a separate mandatory gate and is not yet established.
