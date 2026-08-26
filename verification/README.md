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
- persistent downstream governed component identity remains separate from scoped Runtime participation;
- active public narrative uses current `Tier One`, `downstream governed component`, and `Tier Three` terminology rather than legacy spaced `Tier 1`, `Tier 2`, or `Tier 3` labels;
- the estate represents `EHCO_DOCKER_PORTABILITY` only through its bounded `PRIMARY_ACCESSIBLE_RUNTIME_PROJECTION` classification;
- the diagram record contains all four selected WP-05 explanatory views and preserves its non-implementation/non-deployment proof ceiling; and
- the release register inventories the category, ecosystem, and diagram artifacts.

Immutable historical packet identifiers such as `TIER1` remain byte-preserved. Active interpretation layers translate those historical identifiers into current terminology without rewriting packet bytes.

These checks validate repository consistency and publication semantics only. They do not self-certify that prose or diagrams constitute implementation, deployment, Runtime participation, market validation, legal compliance, or Runtime proof.

## Language Model snapshot validation

`validate_public_lm_test_snapshot.py` checks the bounded Language Model public snapshot, including the seven exact fixtures / 62 cases, manifest identities, JSON structure, disclosure boundary, and public proof-limit language. It does not execute the private Language Model engine.

## Semantic-boundary design

Shared Runtime/repository/test-estate semantics are owned by the canonical boundary record. Primary navigation pages are required to link that record rather than repeat its full prose. The validator prohibits obsolete/private source locators, legacy active tier terminology, stale publication vocabulary, and other known semantic-boundary regressions across active public interpretation surfaces.

## Acceptance governance

Repository-side validation is only one acceptance input. Before acceptance or merge, the current repository and organization rulesets must be read from GitHub and every then-applicable required status check, code-scanning condition, and review condition must be satisfied on the exact candidate relationship. The repository documentation does not freeze a historical required-check list, and technical bypass capability is not acceptance evidence.

## Proof ceiling

Passing repository validation establishes the checked repository-integrity and semantic/disclosure conditions for that commit. Individual technical propositions retain the proof ceilings of their own evidence records.
