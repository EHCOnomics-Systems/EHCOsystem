# Security and Responsible Disclosure

## Scope

This repository contains public documentation, approved public evidence, and bounded validation tooling. It does not contain the proprietary EHCO Runtime, production systems, credentials, protected endpoints, current deployment topology, private schemas, verifier internals, or confidential proof records.

Approved public evidence may retain a bounded historical path, container name, local port, repository identifier, commit SHA, or similar lineage attribute when its applicable disclosure policy expressly permits retention for historical fidelity or cryptographic integrity. Such attributes are not credentials, active instructions, current Runtime truth, or deployment authorization.

## Reporting concerns

Do not publish suspected vulnerabilities, exposed secrets, private implementation details, or evidence that may affect production systems in a public issue.

Report security concerns through the official EHCOnomics contact channel and include:

- a concise description of the concern;
- the affected public document or system reference;
- steps to reproduce, where appropriate;
- the potential impact;
- any supporting evidence that can be shared safely.

## Public disclosure boundary

Public documentation may describe governed properties, architectural distinctions, evidence classes, proof ceilings, approved public source lineage, and hash-preserved historical evidence. It must not disclose:

- proprietary Runtime or participant implementation source;
- unapproved internal file paths, commits, schemas, or control anchors;
- Runtime transition logic or Instantiation Bridge mechanics;
- credentials, tokens, private keys, privileged endpoints, or protected infrastructure details;
- private proof packets or controlled verification artifacts.

## Automated checks

The repository validation workflow checks high-confidence credential patterns, canonical dossier hashes, packet manifests, detached hashes, JSON syntax, suite closure, and prohibited staging residue. Automated checks reduce accidental disclosure risk but do not replace human review.

## No security warranty

The presence of public architecture documentation, evidence packets, or passing repository checks does not constitute a warranty that every implementation, integration, deployment, or production environment is secure. Security claims are limited to the evidence and proof ceiling expressly stated.
