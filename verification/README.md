# Public Repository Validation

This directory contains repository-side validation tooling for the canonical public dossier, historical Public Evidence Companion, current Full Flex Runtime evidence route, Instantiated AI architecture, EHCOsystem technology-estate architecture, navigation, maturity representation, evidence matrices, canonical public claim registry, component evidence snapshots, Range Reactor operational closure, disclosure controls and publication identity.

## Run the complete public verification route

From repository root:

```bash
python3 verification/verify_all_public.py
```

`verify_all_public.py` is an orchestrator. It runs the existing specialized validators in the stable order below, stops at the first failure, identifies the failing validation class, and preserves the evidence boundary of each underlying check. Specialized validators retain their own logic. Runtime, implementation, physical-execution, authority, standing, deployment, and release evidence remain established by their applicable owning evidence domains.

The successful terminal result is `PASS ALL (7/7)`.

## Run validators individually

```bash
python3 verification/validate_public_evidence.py
python3 verification/validate_public_claim_registry.py
python3 verification/validate_current_runtime_evidence.py
python3 verification/validate_public_lm_test_snapshot.py
python3 verification/validate_public_range_reactor_snapshot.py
python3 verification/validate_public_range_reactor_operational_closure.py
python3 verification/validate_release_identity.py
```

## Failure interpretation

A failed validator establishes a failure of that public repository/package check for the checkout being tested. Owning implementation state, owning physical evidence, and `INSTANTIATED_EHCO_RUNTIME` standing remain determined by their respective owning evidence domains; a repository/package check carries its own bounded evidence class.

Use the failing label/path reported by `verify_all_public.py` as the first inspection route:

| Orchestrator label | Inspection surface |
|---|---|
| `PUBLIC_REPOSITORY_INTEGRITY` | `validate_public_evidence.py`; public architecture/navigation/evidence integrity |
| `PUBLIC_CLAIM_REGISTRY` | `assurance/PUBLIC-CLAIM-REGISTRY.json`; `validate_public_claim_registry.py` |
| `CURRENT_RUNTIME_PUBLIC_EVIDENCE` | `runtime/README.md`; `evidence/runtime/full-flex/v1/`; `validate_current_runtime_evidence.py` |
| `LANGUAGE_MODEL_PUBLIC_SNAPSHOT` | `language-model/evidence/public-test-snapshot-v1/`; `validate_public_lm_test_snapshot.py` |
| `RANGE_REACTOR_CAPABILITY_SNAPSHOT` | `range-reactor/evidence/public-capability-snapshot-v1/`; `validate_public_range_reactor_snapshot.py` |
| `RANGE_REACTOR_OPERATIONAL_CLOSURE` | `range-reactor/evidence/operational-closure-v1/`; `validate_public_range_reactor_operational_closure.py` |
| `REGISTERED_RELEASE_IDENTITY` | registered public provenance surfaces; `validate_release_identity.py` |

For component/source ownership and currentness routing, see `dossiers/public-technical-packaging/APPLICATION-EVIDENCE-INDEX.md`.

## Current Runtime evidence validation

`validate_current_runtime_evidence.py` verifies the Full Flex-first public Runtime evidence relationship, including:

- `runtime/README.md` as the current public Runtime front door;
- schema `EHCO_FULL_FLEX_PUBLIC_PACKET_V1` and packet SHA-256 `7F80C27D085AE871A00AED412C6F20EA9A76CB0677C93AEBA381CD1FD70EC8E5`;
- accepted maturity `REALIZED / COMPLETE_IN_ACCEPTED_SCOPE` and standing **52/53**;
- `EHCO_DOCKER_PORTABILITY` as `PRIMARY_ACCESSIBLE_RUNTIME_PROJECTION`;
- Full Flex before historical Packet 06 in the public review order;
- detached packet-hash identity;
- historical Public Evidence Companion classification; and
- exact packet-byte SHA-256/schema verification when the byte-identical JSON is present.

The exact Full Flex packet JSON is present in canonical public Git custody and is verified against its accepted SHA-256. Physical Runtime execution remains established by its owning execution evidence.

## Repository and evidence integrity

`validate_public_evidence.py` verifies canonical dossier identity, Packets 00–08 structure/manifests/hashes/suite closure, JSON syntax, internal links, repository residue, high-confidence credential indicators, architecture/navigation relationships, Runtime/component/Tier Three terminology, Docker portability classification, Dashboard representation, current public maturity language, component snapshot relationships and claim/evidence matrix structure.

It also preserves the required **Language Model capability-based advanced near-final maturation representation** while active reader-facing maturity prose remains bounded to public capability representation. Internal Language Model stage/unit/program mechanics stay within their owning controlled sources.

Hash-preserved Packets 00–08 and exact component fixture artifacts retain their accepted bytes.

## Canonical public claim-registry validation

`validate_public_claim_registry.py` verifies the current machine-readable claim layer and first-contact public surfaces. It checks:

- registry publication/source-review currentness for the August 31 synchronization;
- realized EHCO AI-OS standing **52/53** and `REALIZED / COMPLETE_IN_ACCEPTED_SCOPE` maturity;
- bounded interpretation of 52/53 as a numerical Runtime standing corridor;
- Full Flex-first current evidence precedence and completed exact-byte publication status;
- `EHCO_DOCKER_PORTABILITY` deployment-ready portable-delivery representation;
- self-hosted local Docker Runtime and Dashboard port-8080 representation;
- Tier One external-model-disabled operating lineage;
- the bounded 6.847-second large-ledger historical Runtime characterization and accepted repair sequence;
- Range Reactor mature capability and historical physical diagnostic performance;
- separate Range Reactor matched A/B collapse-performance and selected semantic-closure claims;
- root, Range Reactor and verification navigation synchronization;
- public/private locator disclosure boundaries; and
- required claim/evidence fields and disclosure ceilings.

Protected standing denominator mechanics remain within their owning governed sources, and repository validation remains a source/repository evidence class distinct from Runtime-originated proof.

## Language Model snapshot validation

`validate_public_lm_test_snapshot.py` verifies seven exact fixture artifacts / 62 cases, manifest identities, JSON structure and public evidence metadata.

## Range Reactor capability validation

`validate_public_range_reactor_snapshot.py` verifies the dedicated Range Reactor component/evidence route, eight synthetic capability vectors, manifest/source-review identity, fixture SHA-256, public navigation/claim presence, disclosure boundaries, evidence ceilings, and mature-capability representation. Deployment, production activation and Runtime participation remain separately owned dimensions.

## Range Reactor operational-closure validation

`validate_public_range_reactor_operational_closure.py` verifies the accepted `range-reactor/evidence/operational-closure-v1/` projection as one bounded evidence unit. It pins:

- accepted owning-evidence and benchmark-source identities;
- workload SHA-256 and owning/internal result hashes;
- 2 warm-up pairs and 10 measured pairs;
- **14.304307x** wall-clock and **14.208722x** CPU-time speedup;
- **94.755854%** Python peak-allocation reduction;
- **1,957 → 64** states and **1,956 → 192** transitions;
- **720 → 720** histories;
- **82 passed / 0 failed** selected semantic closure;
- deterministic replay and continuation-manifest identity;
- the selected-benchmark and selected-current-corpus claim ceilings; and
- bounded claim ceilings for universal/unbounded correctness, generic scalar foresight accuracy, Tier One Runtime participation, deployment, release, authority and standing effects.

The historical real-world container/service qualification remains a separate evidence class and its diagnostic service timings stay separate from the matched A/B result.

## Release identity and provenance validation

`validate_release_identity.py` verifies the registered public release identity and stable repository-level provenance semantics. Registered release identity remains distinct from live GitHub Release materialization; provider surfaces establish the latter when such objects exist.

## Acceptance governance

Repository validation is one acceptance input. Pull-request acceptance uses the current repository and organization rulesets, exact candidate relationship, required status checks, code-scanning conditions and review conditions.

## Validation evidence

A successful repository validation establishes checked repository integrity, disclosure, architecture, currentness, publication identity and public-representation conditions for that exact revision. Claim-specific technical propositions retain their applicable evidence owner and class. Physical execution remains owned by Docker/host or Runtime evidence as applicable.
