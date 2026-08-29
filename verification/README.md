# Public Repository Validation

This directory contains repository-side validation tooling for the canonical public dossier, Public Evidence Companion, Instantiated AI architecture, EHCOsystem technology-estate architecture, diagrams, navigation, maturity representation, evidence matrices, public Language Model snapshot, public Range Reactor capability snapshot, disclosure controls and publication identity.

## Run locally

```bash
python3 verification/validate_public_evidence.py
python3 verification/validate_public_lm_test_snapshot.py
python3 verification/validate_public_range_reactor_snapshot.py
python3 verification/validate_release_identity.py
```

## Repository and evidence integrity

`validate_public_evidence.py` verifies:

- canonical dossier identity and SHA-256;
- Packets 00-08 structure, manifests, detached hashes and suite closure;
- JSON syntax and internal link closure;
- repository residue and high-confidence credential indicators;
- required architecture/navigation relationships;
- current Tier One, downstream-component and Tier Three terminology;
- `EHCO_DOCKER_PORTABILITY` projection classification;
- EHCO Dashboard current accepted working projection baseline;
- affirmative capability/maturity representation across active reader-facing public text;
- Language Model capability-based advanced near-final maturation representation;
- active reader-facing Language Model maturity prose aligned to capability and evidence;
- current owner-selected public component scope; and
- claim/evidence matrix structure.

Hash-preserved Packets 00-08 and exact Language Model fixture artifacts retain their accepted bytes.

## Language Model snapshot validation

`validate_public_lm_test_snapshot.py` verifies seven exact fixture artifacts / 62 cases, manifest identities, JSON structure and public evidence metadata.

## Range Reactor capability validation

`validate_public_range_reactor_snapshot.py` verifies the dedicated Range Reactor component/evidence route, eight synthetic capability vectors, manifest/source-review identity, fixture SHA-256, public navigation/claim presence, disclosure boundaries, evidence ceilings, and reader-facing Range Reactor maturity prose aligned to established system capability.

It also enforces status-language integrity in both directions. Range Reactor remains represented as a **mature deterministic proof-carrying implication, reachability, range and reasoning system** where accepted source and qualification evidence establish that capability. The mature system status remains distinct from source-only and qualification-only evidence labels. Deployment, production activation and Runtime participation remain separately owned evidence dimensions with promotion governed by the same validation boundary.

The Range Reactor snapshot itself is source-reviewed synthetic capability evidence. It provides a bounded public inspection surface while controlled implementation source and technical-effect evidence remain with their owning evidence domains.

## Release identity and provenance validation

`validate_release_identity.py` verifies the canonical registered public release identity together with the repository-level stable-baseline provenance semantics:

- version `1.0.0`, tag `v1.0.0-public`, and release title `EHCOsystem Public Architecture and Evidence Baseline v1.0.0` remain aligned across the release documents;
- `ehco.repository.yaml` binds `provenance.accepted_commit` to `eff9301e7c5ddfc0759ee0d7e3c026ad28c5670c`, the commit that accepted the current stable manifest/boundary bytes, independently from current `main`;
- repository-level `provenance.artifact_digest` is `NOT_APPLICABLE_SOURCE_ONLY_PUBLIC_PROJECTION_NO_SEPARATE_BUILD_ARTIFACT`, explicitly classifying the repository publication object as source-only;
- stable-manifest provenance and registered release identity are documented consistently in `PROVENANCE.md` and `releases/PUBLIC-RELEASE-REGISTER.md`; and
- active publication and provenance surfaces carry the resolved stable-baseline semantics.

The validator checks source semantics. GitHub tag and GitHub Release existence are provider-owned publication facts established through provider-surface readback.

## Acceptance governance

Repository validation is one acceptance input. Pull-request acceptance uses the current repository and organization rulesets, exact candidate relationship, required status checks, code-scanning conditions and review conditions.

## Validation evidence

A successful repository validation establishes the checked repository-integrity, disclosure, architecture, currentness, publication-identity and public-representation conditions for that exact revision. Claim-specific technical propositions retain their applicable evidence owner and class.
