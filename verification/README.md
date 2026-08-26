# Public Repository Validation

This directory contains bounded repository-side validation tooling for the canonical public dossier, Public Evidence Companion, Instantiated AI category architecture, EHCOsystem ecosystem architecture/diagrams/navigation surfaces, proprietary license, semantic/disclosure boundaries, and component evidence snapshots.

## Run locally

From the repository root:

```bash
python3 verification/validate_public_evidence.py
python3 verification/validate_public_lm_test_snapshot.py
python3 verification/validate_release_identity.py
```

The public validation workflow runs the applicable validators on pull requests and on pushes covered by its workflow triggers.

## Repository and evidence integrity

`validate_public_evidence.py` checks canonical dossier identity, Packets 00-08 structure and manifests, JSON syntax, suite closure, repository residue, Markdown-link closure, high-confidence secret indicators, license presence, public semantic/disclosure boundaries, required category/architecture/diagram navigation, and the active public narrative surfaces.

Hash-preserved Packets 00-08 remain outside stylistic rewriting. Evidence-specific interpretation remains with the evidence landing pages and applicable packet records.

## Category, ecosystem, and diagram validation

The validator treats `architecture/INSTANTIATED-AI.md`, `architecture/EHCO-TECHNOLOGY-ESTATE.md`, and `architecture/diagrams/README.md` as active public architecture surfaces. Primary navigation must route from the Instantiated AI category to the EHCOsystem ecosystem architecture and its public-safe diagrams, then to evidence and diligence.

The validator checks that:

- the category record identifies EHCOsystem as EHCOnomics' Instantiated AI ecosystem;
- the Technology Estate preserves current downstream-governed-component terminology and established Tier One maturity;
- the estate represents `EHCO_DOCKER_PORTABILITY` only through its bounded `PRIMARY_ACCESSIBLE_RUNTIME_PROJECTION` classification;
- the diagram record contains all four selected WP-05 explanatory views and preserves its non-implementation/non-deployment proof ceiling; and
- the release register inventories the category, ecosystem, and diagram artifacts.

These checks validate repository consistency and publication semantics only. They do not self-certify that prose or diagrams constitute implementation, deployment, Runtime participation, market validation, legal compliance, or Runtime proof.

## Language Model snapshot validation

`validate_public_lm_test_snapshot.py` checks the bounded Language Model public snapshot, including the seven exact fixtures / 62 cases, manifest identities, JSON structure, disclosure boundary, and public proof-limit language. It does not execute the private Language Model engine.

## Semantic-boundary design

Shared Runtime/repository/test-estate semantics are owned by the canonical boundary record. Primary navigation pages are required to link that record rather than repeat its full prose. The validator continues to prohibit obsolete/private source locators and other known semantic-boundary regressions across active public interpretation surfaces.

## Proof ceiling

Passing repository validation establishes the checked repository-integrity and semantic/disclosure conditions for that commit. Individual technical propositions retain the proof ceilings of their own evidence records.
