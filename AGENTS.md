# EHCOsystem Assistant Development Entry

This unrestricted public repository uses the public-safe control profile `EHCO_PUBLIC_SAFE_ASSISTANT_OPERATION_CONTROL_V1`.

## Local control surface

- Stable repository identity and boundary: `ehco.repository.yaml`
- Assistant operation and status owner: `ehco.operation.yaml`
- Required source-grounded check: `EHCO Assistant Operation Gate`
- GitHub-native gate workflow: `.github/workflows/ehco-assistant-operation-gate.yml`

The accepted canonical control binding is resolved privately by GitHub Actions. Protected repository identities, revisions, paths, credentials, and internal control mechanics are not published here.

## Operating rules

Assistant-supported development in this repository must:

- preserve Google Drive as the owner of durable governed meaning and direct Git/GitHub as the owner of exact repository implementation and current repository-development state;
- preserve owning technical evidence as the only basis for build, artifact, deployment, execution, persistence, proof, authority, standing, and Runtime-effect claims;
- use the authorization modes `INSPECT`, `BUILD`, `PUBLISH`, `ACCEPT`, and `REALIZE` without treating tool access as permission;
- source-ground every existing repository object and explicitly declare every new path or object;
- keep `ehco.repository.yaml` stable except when a factual stable repository interface or boundary change is explicitly selected;
- record the selected bounded operation in `ehco.operation.yaml`;
- require owning-system readback for durable postconditions;
- keep `automatic_successor: PROHIBITED`; and
- preserve accepted numerical standing `52/53`.

Repository source, GitHub Actions, containers, dashboards, projections, assistant output, and check results do not become Tier One Runtime authority or present Runtime truth.
