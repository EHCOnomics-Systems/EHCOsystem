---
title: Public Documentation and Evidence Provenance
version: 2.1
status: current-public-reference
published: 2026-09-01
maintainer: EHCOnomics
evidence_class: provenance-and-interpretation-reference
evidence_scope: public provenance classification and integrity routing
---

# Public Documentation and Evidence Provenance

EHCOsystem public material is organized by **origin, evidence class, scope, time, and owner**.

## Accepted Runtime / Full Flex provenance

The accepted **EHCO Full Flex Public Packet v1** is bound to SHA-256 `7F80C27D085AE871A00AED412C6F20EA9A76CB0677C93AEBA381CD1FD70EC8E5`.

The public repository carries:

- the [Full Flex public-safe record](evidence/runtime/full-flex/v1/PUBLIC_SAFE_RECORD.json);
- the accepted packet receipt; and
- the detached accepted packet hash.

The raw accepted packet remains in owning evidence custody because those bytes contain internal source-routing metadata. This public-custody choice preserves the accepted evidence identity and technical result while keeping internal routing outside the public tree.

`INSTANTIATED_EHCO_RUNTIME` remains the owner of Tier One Runtime authority and Runtime state. Technical execution effects retain their owning evidence class.

## Explanatory and navigation material

Reader-facing Markdown explains the architecture, technology relationships, evidence routes, and verification path. Its evidence class is explanatory/navigation material. It does not replace the technical evidence that established an underlying effect.

## Architecture and component records

Architecture records express accepted public system identity, computational ownership, terminology, lifecycle relationships, and component roles.

Component records preserve the strongest established public-safe maturity in each applicable dimension. Language Model capability/source closure, artifact qualification/release, and governed staging verification remain distinct established dimensions. Range Reactor component capability and its selected measured result remain distinct evidence classes.

## Historical hash-bound evidence

The Public Evidence Companion Packets 00–08 preserve packet-scoped records, manifests, checksums, observations, discrepancies, source identities, and verification results at their recorded event time.

Their cryptographic identity and event-time scope remain unchanged. They provide historical lineage behind the accepted public architecture and evidence routes.

## Public-safe component evidence

Language Model public fixtures, the Language Model deterministic capability demonstration, Range Reactor capability vectors, Range Reactor operational-closure records, and Full Flex public-safe records expose reviewer-usable evidence without publishing private source topology.

Public hashes, manifests, fixture identities, workload identities, selected results, and repository validators provide the integrity route appropriate to each public artifact.

## Stable repository provenance baseline

`ehco.repository.yaml` is the stable repository identity and boundary record. Its `provenance.accepted_commit` identifies the commit that accepted the stable manifest/boundary baseline represented by that file, independently from later `main` revisions.

For the accepted stable EHCOsystem manifest baseline, the accepted commit is `eff9301e7c5ddfc0759ee0d7e3c026ad28c5670c`.

The public repository is a source-only `PUBLIC_EVIDENCE` projection. Its repository-level `provenance.artifact_digest` records `NOT_APPLICABLE_SOURCE_ONLY_PUBLIC_PROJECTION_NO_SEPARATE_BUILD_ARTIFACT`. Evidence objects such as Full Flex, the dossier, historical packets, Dashboard derivatives, Language Model fixtures, and Range Reactor public evidence retain their own identities.

## Registered repository release identity

The registered repository release identity is version `1.0.0`, with registered tag name `v1.0.0-public` and release title `EHCOsystem Public Architecture and Evidence Baseline v1.0.0`.

**Registered release identity and provider materialization are separate publication states.** The registered tag name is a repository identity field; it does not by itself establish that GitHub currently materializes that tag or a GitHub Release object. Provider-owned tag/release objects establish provider materialization when those objects exist.

## Repository verification

`python3 verification/verify_all_public.py` validates the exact checked-out public revision across repository integrity, claims, Runtime/Full Flex public-safe custody, Language Model fixture/demonstration integrity, Range Reactor public evidence, publication identity, and durable public semantics.

A green repository check establishes the public source/repository conditions for that revision. It does not regenerate technical evidence.

## Protected implementation custody

Complete proprietary implementation, credentials, private source topology, detailed deployment configuration, internal integration mechanics, active infrastructure, and private evidence routing remain in controlled EHCOnomics custody.

## Review method

1. understand the architecture and component first;
2. identify the proposition;
3. identify its evidence class;
4. inspect the selected public artifact or record;
5. verify integrity and scope through the public validation route; and
6. preserve the evidence class in the conclusion.

For a whole-estate route, see [Ecosystem Technical Diligence](ECOSYSTEM-DILIGENCE.md). For Tier One depth, see [EHCO AI-OS Technical Diligence](TECHNICAL-DILIGENCE.md).
