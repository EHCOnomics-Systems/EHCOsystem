# EHCOsystem Assistant Development Entry

This public repository uses the public-safe control profile `EHCO_PUBLIC_SAFE_ASSISTANT_OPERATION_CONTROL_V1`.

## Local control surface

- Stable repository identity and boundary: `ehco.repository.yaml`
- Assistant operation and status owner: `ehco.operation.yaml`
- Required source-grounded check: `EHCO Assistant Operation Gate`
- GitHub-native gate workflow: `.github/workflows/ehco-assistant-operation-gate.yml`
- Pre-publication disclosure gate: `verification/pre_publication_gate.py`
- Clone-local push guard installer: `verification/install_publication_guard.py`

The accepted canonical control binding is resolved through private GitHub Actions custody.

## Pre-publication confidentiality invariant

The public GitHub repository is a publication destination, not a staging area for unqualified material.

Before a normal development transport creates or updates a provider-visible branch, tag, pull-request narrative, release narrative, or other public GitHub object, the exact candidate content and the provider-facing metadata under that transport must pass the repository-owned pre-publication disclosure gate.

For a local clone, install the tracked guard once:

```text
python verification/install_publication_guard.py
```

The installed pre-push hook scans every Git object newly reachable from the candidate relative to accepted public `main`, including transient blobs later removed from the final tree, commit messages, path names, and the provider-visible ref name. A successful scan writes a clone-local clearance receipt under `.git/` bound to the exact candidate SHA and tree SHA.

Provider-facing title/body/release text that is not part of the Git candidate must be placed in a local text file and supplied to `verification/pre_publication_gate.py` with `--metadata-file` before that metadata is published.

A clearance receipt becomes invalid when the candidate SHA changes. GitHub Actions, CodeQL, repository rulesets, and the EHCO Assistant Operation Gate remain mandatory defense-in-depth controls, but they do not replace the pre-provider confidentiality boundary.

A direct API/provider write is permitted only when an equivalent fail-closed pre-provider scan has already qualified the exact bytes, commit message/ref metadata, and provider narrative that will be made public. Do not use a provider API as a route around the pre-publication gate.

## Operating rules

Assistant-supported development:

- preserves Google Drive as the owner of durable governed meaning and direct Git/GitHub as the owner of exact repository implementation/current repository-development state;
- uses owning technical evidence for build, artifact, deployment, execution, persistence, proof, authority, standing and Runtime-effect claims;
- uses authorization modes `INSPECT`, `BUILD`, `PUBLISH`, `ACCEPT` and `REALIZE` with authorization and tool capability tracked separately;
- source-grounds existing repository objects and explicitly declares new paths/objects;
- keeps `ehco.repository.yaml` stable for stable repository identity/boundary facts;
- records the selected bounded operation in `ehco.operation.yaml`;
- requires owning-system readback for durable postconditions;
- keeps `automatic_successor: PROHIBITED`; and
- preserves accepted numerical standing `52/53`.

`INSTANTIATED_EHCO_RUNTIME` owns Tier One Runtime authority and current Runtime state. Repository source, GitHub Actions, containers, dashboards, projections and checks retain their own evidence classes.
