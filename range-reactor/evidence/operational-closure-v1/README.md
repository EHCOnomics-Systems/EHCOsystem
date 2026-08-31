# EHCO Range Reactor Operational Closure Evidence v1

## What this publishes

This public packet projects the accepted Range Reactor operational-closure evidence from the direct owning repository into EHCOsystem's public evidence surface. It is a bounded public projection, not a copy of controlled implementation source or private execution logs.

The owning Range Reactor evidence is accepted at `eae888b784620ed37ed7d6704bcd91dedcf92936`, bound to benchmark/source revision `e72b2a29e52878d300b44f0286259466352f73cc`.

## Established selected-benchmark result

For `RR-EXPLORATION-AB-001` on the selected `rr-independent-obligation-permutation-n6-v1` workload, the established physical A/B result is:

- **14.304307x wall-clock speedup**;
- **14.208722x CPU-time speedup**;
- **94.755854% peak Python-allocation reduction** (`tracemalloc`, not RSS);
- **14.304307x throughput gain**;
- **96.729688% state-work reduction**, from 1,957 states to 64;
- **90.184049% transition-work reduction**, from 1,956 transitions to 192; and
- **720 histories preserved in both modes**, with semantic equivalence `PROVEN_EQUAL_FOR_SELECTED_BENCHMARK_PROJECTION`.

The controlled measurement used 2 warm-up pairs and 10 measured pairs. These figures apply to this selected benchmark projection; they are not a universal Range Reactor speedup claim.

## Physical execution and real-world qualification context

The accepted benchmark is **physical local execution evidence**, not simulation-only or CI-only evidence. The matched A/B was executed through the owning Windows/Docker estate in a local Docker/Linux environment using CPython 3.11.16, with exact benchmark source bound to `e72b2a29e52878d300b44f0286259466352f73cc` and the retained physical result file independently hashed.

Range Reactor also has a separate, earlier **real-world container/service qualification** bound to owning source revision `149314be7c4302d66bd93ac112e062292a2e815b` and immutable local qualification image `sha256:f69cd78902d2a8b97e4f70f86b779159dac394c9d43ddcb81611a76897055c0a`. That qualification exercised the software as a containerized internal HTTP service and recorded PASS for source/static contract, build identity, private-network health, capability execution, fail-closed transport handling, timeout/unavailability behavior, restart recovery, temporary portability, and AI-OS fail-closed fallback. Diagnostic service performance was also collected, but it had no acceptance threshold and is not substituted for the later exploration-algorithm A/B result.

Together, these evidence classes show a progression from deterministic source semantics and controlled semantic verification to physical performance measurement and bounded real-world container/service behavior. They do **not** establish production deployment, registry release, Tier One Runtime admission, Runtime participation/binding/invocation, or a canonical Runtime receipt.

## Semantic closure

The accepted closure receipt records **82 selected current tests passed and 0 failed**, with deterministic replay digest `collapse-certificate-58a1e724b8acb571891d3c52`. This supports the bounded selected semantic corpus represented by the owning evidence. It does not establish universal or unbounded correctness.

A generic scalar prediction-versus-ground-truth "foresight accuracy percentage" remains `NOT_ESTABLISHED_FOR_DEVELOPMENT`; the accepted evidence instead establishes the selected semantic-equivalence and preservation claims represented by the corpus.

## Provenance

`PUBLIC_RESULT.json` binds this projection to:

- owning accepted RR commit `eae888b784620ed37ed7d6704bcd91dedcf92936`;
- benchmark source `e72b2a29e52878d300b44f0286259466352f73cc`;
- owning evidence receipt Git blob `42d7e0d448a59b82d15eade58e11d8de9407f7f2`;
- physical benchmark file SHA-256 `C6B7DAB276DCB620CC17C4D7F7B1E8B0EE45D53F6B64E574F55D7CC7ADBF2ED2`; and
- benchmark internal-result SHA-256 `6cca258517425c8d3723c036b8bf36d7ccb5f09991054b4f4bacf75a6f7dc697`.

The physical-file hash and internal-result hash are separate evidence identities and are intentionally preserved as such.

## Evidence boundary

This public packet does not publish controlled Range Reactor implementation mechanics, raw semantic test logs, private host filesystem paths, credentials, active endpoints, or production infrastructure. It creates no Tier One Runtime admission, participation, binding, invocation, deployment, release, authority, standing, or successor effect. Accepted numerical standing remains **52/53**.
