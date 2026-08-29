# Public Repository Validation

This directory contains repository-side validation tooling for the canonical public dossier, Public Evidence Companion, Instantiated AI architecture, EHCOsystem technology-estate architecture, diagrams, navigation, maturity representation, evidence matrices, public Language Model snapshot, disclosure controls and publication identity.

## Run locally

```bash
python3 verification/validate_public_evidence.py
python3 verification/validate_public_lm_test_snapshot.py
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
- absence of internal Language Model stage/unit/program mechanics from active reader-facing maturity prose;
- current owner-selected public component scope; and
- claim/evidence matrix structure.

Hash-preserved Packets 00-08 and exact Language Model fixture artifacts retain their accepted bytes.

## Language Model snapshot validation

`validate_public_lm_test_snapshot.py` verifies seven exact fixture artifacts / 62 cases, manifest identities, JSON structure and public evidence metadata.

## Acceptance governance

Repository validation is one acceptance input. Pull-request acceptance uses the current repository and organization rulesets, exact candidate relationship, required status checks, code-scanning conditions and review conditions.

## Validation evidence

A successful repository validation establishes the checked repository-integrity, disclosure, architecture, currentness and public-representation conditions for that exact revision. Claim-specific technical propositions retain their applicable evidence owner and class.
