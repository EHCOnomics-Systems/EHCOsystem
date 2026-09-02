# EHCOsystem Assistant Development Entry

This public repository uses the public-safe control profile `EHCO_PUBLIC_SAFE_ASSISTANT_OPERATION_CONTROL_V1`.

## Local control surface

- Stable repository identity and boundary: `ehco.repository.yaml`
- Assistant operation and status owner: `ehco.operation.yaml`
- Required source-grounded check: `EHCO Assistant Operation Gate`
- GitHub-native gate workflow: `.github/workflows/ehco-assistant-operation-gate.yml`

The accepted canonical control binding is resolved through private GitHub Actions custody.

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
