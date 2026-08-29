---
title: Public Documentation and Evidence Provenance
version: 1.2
status: current-public-reference
published: 2026-08-29
maintainer: EHCOnomics
evidence_class: provenance-and-interpretation-reference
evidence_scope: provenance classification and source routing
supersedes: version 1.1
---

# Public Documentation and Evidence Provenance

EHCOsystem public material is organized by **origin, evidence class, scope, time and owner**.

## Explanatory and navigation material

Human-directed, AI-assisted explanatory Markdown organizes the public technical story and routes reviewers to architecture and evidence. Its evidence class is explanatory/navigation material.

## Architecture and controlled public references

Architecture documents express the accepted public system model, computational ownership, terminology, lifecycle relationships and system boundaries.

## Hash-bound evidence packets

The Public Evidence Companion preserves packet-scoped records, manifests, checksums, source identities, observations, discrepancies and verification results. Each packet retains its original time, scope, evidence class and cryptographic identity.

## Runtime and machine observations

Runtime, test, capture and machine observations are tied to their identified environment, capture time, source set and evidence class. Current Runtime propositions use current Runtime evidence; historical observations retain their historical time.

## Repository verification tooling

Executable verification tooling validates public repository structure, identity, manifests, links, disclosure safety, architecture relationships, maturity representation and semantic controls for the checked revision.

## Stable repository provenance baseline

`ehco.repository.yaml` is the stable repository identity and boundary record. Its `provenance.accepted_commit` identifies the commit that accepted the stable manifest/boundary baseline represented by that file; it is not an alias for current `main`.

For the current stable EHCOsystem manifest baseline, the accepted commit is `eff9301e7c5ddfc0759ee0d7e3c026ad28c5670c`, the PR #24 merge that last changed and accepted the current manifest bytes.

The public repository is a source-only `PUBLIC_EVIDENCE` projection and does not define a separately built repository artifact. Its repository-level `provenance.artifact_digest` therefore records `NOT_APPLICABLE_SOURCE_ONLY_PUBLIC_PROJECTION_NO_SEPARATE_BUILD_ARTIFACT`. This avoids a circular self-hash and does not borrow the digest of any unrelated dossier, evidence packet, Dashboard derivative, Language Model fixture or Range Reactor record.

Those public artifacts retain their own established identities and evidence classes.

## Registered release identity and live publication

The registered public release identity is version `1.0.0`, tag `v1.0.0-public`, with release title `EHCOsystem Public Architecture and Evidence Baseline v1.0.0`.

Registered release identity and live provider publication are distinct publication states. The GitHub tag and GitHub Releases surfaces establish live release materialization when those provider objects exist; repository documentation alone does not create them.

## Protected implementation custody

Complete proprietary Runtime implementation, controlled logic, protected schemas, credentials, detailed deployment configuration, integration mechanics, active infrastructure and confidential private-core evidence remain in controlled EHCOnomics custody.

Qualified diligence uses proposition-matched evidence such as exact source/revision identity, hashes or digests, event records, discrepancy dispositions, reviewer-selected safe tests, witnessed build/execution and written verification findings.

## Review method

1. identify the technical proposition;
2. identify the governed object and owner;
3. inspect the applicable source/evidence class;
4. verify exact identity, scope and time;
5. inspect qualification or observed execution evidence when the proposition concerns behavior; and
6. preserve the evidence class and source relationship in the conclusion.

For the shortest public route, see [EHCO AI-OS Technical Diligence](TECHNICAL-DILIGENCE.md). For the whole estate, see [Ecosystem Technical Diligence](ECOSYSTEM-DILIGENCE.md).

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.2 | 2026-08-29 | Define the non-circular stable-manifest provenance baseline, source-only repository artifact-digest treatment and separation of registered release identity from live provider publication. |
| 1.1 | 2026-08-28 | Recast provenance around affirmative evidence ownership, classification and review routing. |
| 1.0 | 2026-08-10 | Initial provenance reference. |
