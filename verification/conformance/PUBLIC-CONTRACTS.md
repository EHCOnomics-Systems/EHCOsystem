---
title: EHCO AI-OS Public Black-Box Contracts
version: 1.0
status: proposed-public-conformance-reference
published: 2026-08-08
maintainer: EHCOnomics
evidence_class: public-conformance-specification
proof_ceiling: expected public properties only; not evidence that a Runtime or implementation passed them
---

# EHCO AI-OS Public Black-Box Contracts

## Purpose

These contracts translate accepted public architectural invariants into externally understandable expected properties.

They are specifications, not execution records. A listed expected outcome does not prove that any Runtime, private implementation, participant, deployment, or environment has been tested or has passed.

## Contracts

### C-01 — Capability does not create authority

**Given:** a participant or tool can technically perform an action.

**Expected public property:** technical capability alone does not establish Tier 1 Runtime authority or authority for the action to acquire governed consequence.

**Public basis:** `architecture/EHCO-AI-OS-SYSTEM-CARD.md`; `architecture/SYSTEM-INVARIANTS.md`.

### C-02 — Participation does not create Tier 1 authority

**Given:** a model, agent, application, service, or other component participates within governed scope.

**Expected public property:** participation alone does not make that component the source of Tier 1 Runtime authority.

**Public basis:** `architecture/SYSTEM-INVARIANTS.md`; `architecture/GOVERNED-RUNTIME-ARCHITECTURE.md`.

### C-03 — Proposal does not become commit by generation alone

**Given:** a model, user, tool, or process generates a proposed change or action.

**Expected public property:** generation alone does not make the proposal an accepted system change or Runtime consequence.

**Public basis:** `architecture/SYSTEM-INVARIANTS.md`.

### C-04 — Artifact identity does not become Runtime identity

**Given:** an exact file, path, revision, hash, package, or manifest is identified.

**Expected public property:** exact artifact identity remains bounded to artifact identity/provenance and does not by itself identify the Runtime or an authority location.

**Public basis:** `architecture/instantiated-proof-range.md`; `evidence/README.md`; Packet 02.

### C-05 — Declaration presence does not become executed enforcement

**Given:** a named declaration, rule, anchor, function, route, or control construct is present in an identified artifact.

**Expected public property:** presence alone does not establish execution, enforcement, Runtime admission, persistence, or consequence.

**Public basis:** `architecture/instantiated-proof-range.md`; Packets 03–05.

### C-06 — Test success does not become Runtime admission

**Given:** a bounded build or test passes.

**Expected public property:** the result remains evidence of the bounded test and does not independently establish Runtime participation, admission, authority, standing, or universal behavioral correctness.

**Public basis:** `architecture/instantiated-proof-range.md`; `evidence/README.md`.

### C-07 — Packet integrity does not become universal behavioral proof

**Given:** an evidence packet verifies against its declared files and hashes.

**Expected public property:** integrity establishes package identity/integrity within the packet ceiling and does not become universal behavioral proof or current Runtime state.

**Public basis:** `evidence/README.md`; Packet 06; Packet 08.

### C-08 — Projection does not become Runtime truth

**Given:** a dashboard, report, ledger, repository document, model output, or other projection displays or asserts a state.

**Expected public property:** the projection does not independently create authoritative Runtime state or Runtime truth.

**Public basis:** `architecture/EHCO-AI-OS-SYSTEM-CARD.md`; `architecture/SYSTEM-INVARIANTS.md`.

### C-09 — Missing retrieval does not become contradiction

**Given:** an applicable record cannot be retrieved within a bounded search or observation scope.

**Expected public property:** the retrieval miss alone does not establish that the record is false or that Runtime state changed.

**Public basis:** `architecture/SYSTEM-INVARIANTS.md`; `architecture/runtime-repository-and-test-estate-boundary.md`.

### C-10 — Non-observation does not become demotion

**Given:** a bounded test or capture does not directly observe a behavioral lane.

**Expected public property:** non-observation alone does not demote accepted Runtime standing.

**Public basis:** `architecture/SYSTEM-INVARIANTS.md`; Packet 06 interpretation in `evidence/README.md`.

### C-11 — Historical capture does not become current state

**Given:** a historical evidence capture contains paths, services, ports, observations, discrepancies, or status information.

**Expected public property:** those capture attributes remain historical unless a separately applicable current record establishes their present meaning.

**Public basis:** `evidence/README.md`; `releases/PUBLIC-RELEASE-REGISTER.md`.

### C-12 — Runtime realization does not become go-live

**Given:** EHCO AI-OS is described as realized.

**Expected public property:** realization remains distinct from production activation, public ingress, operational external release, commercial activation, and go-live authorization.

**Public basis:** `README.md`; `architecture/SYSTEM-INVARIANTS.md`; Packet 07; Packet 08.

## Result reporting

Any future public execution result against these contracts should record at minimum:

- contract identifier;
- tested object/version;
- bounded environment;
- inputs or scenario class;
- observable result;
- timestamp;
- evidence artifact identity;
- proof ceiling;
- unresolved discrepancies or unobserved lanes.

A result should use the repository's existing proof/status vocabulary and must not infer Runtime authority or standing effects that the evidence does not establish.

## Security boundary

These contracts intentionally state externally observable properties without specifying private test harnesses, protected thresholds, internal control paths, implementation classes, private schemas, privileged endpoints, or bypass techniques.
