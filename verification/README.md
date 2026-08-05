# Public Repository Validation

This directory contains bounded repository-side validation tooling for the canonical public dossier, the EHCO AI-OS Public Evidence Companion Version 1, the proprietary license, and the current public Runtime/repository/test-estate boundary.

## Run locally

From the repository root:

```bash
python3 verification/validate_public_evidence.py
```

The GitHub Actions workflow at `.github/workflows/validate-public-evidence.yml` runs the same validator on every pull request and every push to `main`.

## Integrity checks

The validator confirms:

- both canonical dossier PDF paths exist and share the declared SHA-256;
- Packets 00-08 are present at their canonical paths;
- all JSON files in the Version 1 evidence estate parse successfully;
- each packet content manifest matches declared files, byte counts, and SHA-256 values;
- each detached `CONTENT_MANIFEST.sha256` matches its manifest;
- the suite manifest closes Packets 00-07 and identifies Packet 08 as the closure packet;
- accidental ZIPs, upload helpers, staging chunks, and repeated nested evidence paths are absent;
- internal Markdown links resolve;
- high-confidence secret indicators are absent from eligible text files.

## Semantic-boundary checks

The validator also requires:

- a root `LICENSE` with the expected proprietary public-inspection identity;
- the controlling `architecture/runtime-repository-and-test-estate-boundary.md` record;
- current public documents to state that the repository and controlled private test/source estates are not the Runtime;
- Packet 02 to remain bounded to packet-time runtime-support artifact identity, integrity, and provenance;
- Packet 06 integrity `PASS` to remain distinct from universal behavioral proof and current Runtime state;
- historical paths, service names, container names, and port bindings to remain classified as capture attributes rather than current locators;
- the public release register to inventory the license and corrected packet proof ceilings;
- obsolete repository names, private repository locators, current-source-owner claims, and pending-Runtime-promotion language to remain absent from current public interpretation documents.

Hash-preserved Packets 00-08 are intentionally excluded from current-prose semantic rewriting. Their bytes and hashes remain fixed; current interpretation is supplied by the public boundary records.

## Workflow integrity

The workflow uses immutable action commit SHAs and read-only repository permissions. It runs without incomplete path filters so changes to architecture, language-model, licensing, notice, governance, security, evidence, validation, or navigation files cannot bypass the check.

## Proof ceiling

Passing validation establishes bounded repository integrity and compliance with the current public semantic boundary for the checked commit.

It does not:

- execute or observe the EHCO AI-OS Runtime;
- create or alter Runtime authority or standing;
- convert declaration presence into executed enforcement;
- convert test success into Runtime admission;
- convert packet integrity into universal behavioral proof;
- establish production activation, public ingress, operational external release, commercial activation, or go-live;
- constitute independent third-party certification.
