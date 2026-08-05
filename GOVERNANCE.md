# Repository Governance

## Purpose

This repository publishes the public architecture, research lineage, evidence classes, and publication-safe materials of the EHCOsystem.

It is not the production source estate and does not govern the private Runtime, participant implementations, deployment systems, internal proof records, or confidential verification environment.

## Publication control

Material may be added only when it is:

- already approved for public release;
- derived from an accepted public architecture or evidence source;
- stripped of unapproved proprietary implementation detail;
- classified accurately by evidence type and proof ceiling;
- reviewed for security, confidentiality, and intellectual-property exposure;
- placed at its canonical repository path with its identity and integrity controls preserved.

## Evidence classes

Public claims must be identified through one of the following classes:

1. **Controlled EHCO architecture** — an accepted EHCO architectural position.
2. **Public EHCO lineage** — a previously published EHCO article, repository identifier, revision identifier, or public document expressly approved for lineage use.
3. **External fact or incident** — a documented event or requirement from an external primary source.
4. **EHCO analysis or proposition** — an engineering conclusion advanced by EHCO.
5. **Controlled-review evidence** — confidential evidence whose existence and proof ceiling may be described publicly but whose implementation details are withheld.
6. **Hash-preserved historical evidence** — an approved historical capture retained byte-for-byte where alteration or redaction would break its declared cryptographic identity.

No evidence class may be presented as another. EHCO publications do not constitute independent validation. Repository existence does not prove deployment. Testing does not prove admission or production operation.

## Approved historical and lineage exceptions

A public artifact may retain a bounded historical path, container name, local port, repository name, commit SHA, pull-request number, or similar lineage attribute only when all of the following are true:

- the attribute is expressly approved for public disclosure or classified by an applicable public disclosure policy;
- retention is necessary for historical fidelity, source lineage, or hash-preserved integrity;
- the artifact contains no credential, secret, private key, access token, or active privileged endpoint;
- the record states or inherits a proof ceiling that prevents the attribute from being treated as current Runtime truth, active infrastructure authority, or deployment authorization.

This exception does not authorize publication of protected implementation mechanics or uncontrolled internal locators.

## Contribution policy

Public issues and corrections may be submitted. External code contributions are not currently accepted because this repository is documentation-focused and is not an open-source implementation distribution.

Proposed documentation changes must not introduce:

- unapproved private repository or file names;
- unapproved internal paths, commits, schemas, or verifier mechanics;
- credentials, secrets, privileged endpoints, protected topology, or current deployment details;
- private proof-packet contents;
- unsupported claims of universal proof, exclusivity, or production completion.

## Change control

Changes to the immutable public Runtime baseline require explicit approval from EHCOnomics. Editorial improvements may clarify language but may not alter accepted architectural relationships.

Later research and ecosystem findings must remain distinguishable from the immutable Runtime baseline. Scoped publication gaps, absent repository sections, dashboards, ledgers, and assistant interpretations do not independently change accepted standing or Runtime truth.

## Validation

Changes affecting the canonical dossier or Public Evidence Companion must pass the repository validation workflow. Validation confirms bounded repository integrity only; it does not create authority, standing, deployment, production activation, or operational release authorization.

## Contact

Questions concerning publication, review, or use of this repository should be directed through the official EHCOnomics website.
