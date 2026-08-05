# Public Evidence Validation

This directory contains bounded repository-side validation tooling for the canonical public dossier and the EHCO AI-OS Public Evidence Companion Version 1.

## Validator

Run locally from the repository root:

```bash
python3 verification/validate_public_evidence.py
```

The GitHub Actions workflow at `.github/workflows/validate-public-evidence.yml` runs the same validator when relevant repository paths change.

## Checks

The validator confirms:

- both canonical dossier PDF paths exist and share the declared SHA-256;
- Packets 00–08 are present at their canonical paths;
- all JSON files in the Version 1 evidence estate parse successfully;
- each packet content manifest matches declared files, byte counts, and SHA-256 values;
- each detached `CONTENT_MANIFEST.sha256` value matches its manifest;
- the suite manifest closes Packets 00–07 and identifies Packet 08 as the closure packet;
- accidental ZIPs, upload helpers, staging chunks, and repeated nested evidence paths are absent;
- internal Markdown links resolve;
- high-confidence secret indicators are absent from text files.

## Proof ceiling

Passing validation establishes bounded repository integrity for the checked paths. It does not execute the Runtime, create or change standing, prove deployment, authorize production activation, authorize public ingress, authorize operational external release, or create go-live status.
