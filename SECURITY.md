# Security and Responsible Disclosure

## Scope

This repository contains approved public architecture, evidence, provenance, research, verification and publication materials for EHCOsystem. Tier One Runtime authority and Runtime state remain owned by `INSTANTIATED_EHCO_RUNTIME`. Controlled source/test estates and downstream component source remain in their owning technical domains.

## Public evidence handling

Hash-preserved public evidence may contain approved historical paths, container names, service names, local ports, repository identifiers, revisions and other capture attributes. These attributes are interpreted through their packet time, evidence class and scope.

## Pre-publication disclosure prevention

Public GitHub is treated as an external publication boundary. Sensitive material must be stopped before it becomes a branch, commit, pull-request diff, provider narrative, tag, release note, or other provider-visible object.

The repository-owned `verification/pre_publication_gate.py` performs the fail-closed pre-provider scan for normal publisher transports. It examines newly reachable Git objects relative to accepted public `main`, including objects that are introduced and removed within the candidate history, and scans commit/ref/provider metadata without echoing matched protected values.

Install the clone-local pre-push guard with:

```text
python verification/install_publication_guard.py
```

The resulting clearance receipt is clone-local, records only public-safe identities/status data, and is bound to the exact candidate SHA/tree. Any candidate mutation invalidates the prior clearance. Pull-request/CI validation is an additional detection layer, not a substitute for this pre-provider boundary.

Opaque archive and office-container additions fail the pre-publication gate rather than being accepted as uninspected publication payloads.

## Reporting security concerns

Use an official private EHCOnomics contact channel for vulnerability reports, suspected credential exposure, implementation-sensitive findings or operational-security concerns.

A useful report includes:

- concise concern description;
- affected public document or system reference;
- reproducible steps where applicable;
- potential impact; and
- safely shareable supporting evidence.

## Protected information custody

The following classes remain in controlled EHCOnomics custody:

- proprietary Runtime and downstream-component implementation source;
- private repository/source locators and protected control anchors;
- protected Runtime transition and Instantiation Bridge mechanics;
- credentials, tokens, private keys and privileged endpoints;
- private proof packets and controlled verification artifacts; and
- production topology, access instructions and environment secrets.

## Automated checks

Repository automation validates canonical dossier hashes, packet manifests, detached hashes, JSON syntax, suite closure, internal links, high-confidence credential patterns, public architecture relationships, disclosure boundaries, pre-publication gate regression behavior and durable public representation semantics.

Human review, security review, legal review and Runtime-originated evidence complement these automated checks according to the proposition being assessed.

## Security evidence

Security conclusions are tied to their identified source, environment, method, time and evidence class. This preserves precise assurance statements across repository validation, component testing, deployment evidence and Runtime evidence.
