# Public Repository Validation

This directory contains bounded repository-side validation tooling for the canonical public dossier, Public Evidence Companion, Instantiated AI category architecture, EHCOsystem ecosystem architecture/navigation surfaces, proprietary license, semantic/disclosure boundaries, and component evidence snapshots.

## Run locally

From the repository root:

```bash
python3 verification/validate_public_evidence.py
python3 verification/validate_public_lm_test_snapshot.py
python3 verification/validate_release_identity.py
```

The public validation workflow runs the applicable validators on pull requests and on pushes covered by its workflow triggers.

## Repository and evidence integrity

`validate_public_evidence.py` checks canonical dossier identity, Packets 00-08 structure and manifests, JSON syntax, suite closure, repository residue, Markdown-link closure, high-confidence secret indicators, license presence, public semantic/disclosure boundaries, required category/architecture navigation, and the active public narrative surfaces.

Hash-preserved Packets 00-08 remain outside stylistic rewriting. Evidence-specific interpretation remains with the evidence landing pages and applicable packet records.

## Category and ecosystem validation

The validator treats `architecture/INSTANTIATED-AI.md` as an active public architecture surface. Primary navigation must route from the Instantiated AI category to the EHCOsystem ecosystem architecture, then to evidence and diligence. The validator checks that the category record identifies EHCOsystem as EHCOnomics' Instantiated AI ecosystem and that the Technology Estate preserves current downstream-governed-component terminology and the established Tier One maturity.

These checks validate repository consistency and publication semantics only. They do not self-certify that prose statements constitute implementation, deployment, Runtime participation, legal compliance, or Runtime proof.

## Language Model snapshot validation

`validate_public_lm_test_snapshot.py` checks the bounded Language Model public snapshot, including the seven exact fixtures / 62 cases, manifest identities, JSON structure, disclosure boundary, and public proof-limit language. It does not execute the private Language Model engine.

## Semantic-boundary design

Shared Runtime/repository/test-estate semantics are owned by the canonical boundary record. Primary navigation pages are required to link that record rather than repeat its full prose. The validator continues to prohibit obsolete/private source locators and other known semantic-boundary regressions across active public interpretation surfaces.

## Proof ceiling

Passing repository validation establishes the checked repository-integrity and semantic/disclosure conditions for that commit. Individual technical propositions retain the proof ceilings of their own evidence records.
