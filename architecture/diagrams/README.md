---
title: EHCOsystem Public Architecture Diagrams
version: 1.0
status: current-public-architecture-navigation
published: 2026-08-26
maintainer: EHCOnomics
evidence_class: original-public-safe-architecture-diagrams
proof_ceiling: explanatory architecture only; diagrams do not create implementation, deployment, Runtime participation, market validation, or Runtime proof
---

# EHCOsystem Public Architecture Diagrams

These diagrams are original public-safe explanatory views of the architecture described in [Instantiated AI](../INSTANTIATED-AI.md), [EHCOsystem — An Instantiated AI Ecosystem](../EHCO-TECHNOLOGY-ESTATE.md), and the [Ecosystem Claim → Evidence Matrix](../../assurance/ECOSYSTEM-CLAIM-EVIDENCE-MATRIX.md).

They intentionally show **relationships and ownership**, not private topology, deployment configuration, protected implementation mechanics, current Runtime participation, or confidential investment material. This diagram record does not create implementation, deployment, Runtime participation, market validation, or Runtime proof.

## 1. Category, Runtime, components, portability, and projection

```mermaid
flowchart TD
    A[Instantiated AI<br/>architectural category]
    B[EHCOsystem<br/>EHCOnomics' Instantiated AI ecosystem]
    C[EHCO AI-OS<br/>realized Tier One Runtime]
    D[EHCO_DOCKER_PORTABILITY<br/>PRIMARY_ACCESSIBLE_RUNTIME_PROJECTION]
    E[Downstream governed components<br/>computational / research / application owners]
    F[Tier Three<br/>interfaces and projections]
    G[Public EHCOsystem repository<br/>architecture / evidence / diligence]

    A --> B
    B --> C
    B --> E
    B --> F
    C -. established Runtime lineage projection .-> D
    C -. scoped Runtime relationships only when evidenced .-> E
    C --> F
    E --> F
    B --> G

    D -. not the source repository<br/>not an independent authority owner .-> C
    G -. public representation only<br/>not Runtime authority .-> B
```

**Interpretation:** Instantiated AI is the category; EHCOsystem is the ecosystem. EHCO AI-OS is the realized Tier One Runtime foundation. `EHCO_DOCKER_PORTABILITY` is the `PRIMARY_ACCESSIBLE_RUNTIME_PROJECTION` within the established hardened Runtime/root-image lineage; it is distinct from the EHCO AI-OS source repository and from repository-local Docker/Compose test realizations. Downstream component identity does not itself establish Runtime participation. Tier Three and the public repository project governed information without becoming Runtime truth or authority.

## 2. Computational ownership across the ecosystem

```mermaid
flowchart LR
    R[Runtime governance<br/>authority / state / release / proof] --> AIOS[EHCO AI-OS]
    L[Deterministic computational language] --> LM[EHCO Language Model]
    Q[Bounded range / reasoning computation] --> RR[EHCO Range Reactor]
    E[Retrieval / context / provenance / evidence] --> RAG[EHCO RAG]
    M[Memory / continuity research] --> MEM[EHCO Memory]
    P[Persistent individual relationship] --> PRIME[EHCO Prime]
    C[Registry / discovery / candidate routing] --> AC[EHCO Agent Connect]
    RF[Research substrates<br/>specification / recursion / form] --> RES[Primordia / Recursion / Fractal Systems]
    DA[Domain logic / records / workflows] --> APPS[Governed domain applications]
    V[Interfaces / dashboards / reports] --> T3[Tier Three]
```

**Interpretation:** ownership is intentionally separated. Language computation is not Runtime authority; retrieval is not application truth; coordination is not admission; application logic is not Tier One governance; projection is not the state it displays.

## 3. Shared foundations to domain applications

```mermaid
flowchart TD
    CAT[Instantiated AI conditions]
    RT[EHCO AI-OS<br/>Tier One Runtime foundation]

    subgraph Shared[Shared downstream foundations and services]
        LM[Language Model]
        RR[Range Reactor]
        RAG[RAG]
        MEM[Memory]
        PRIME[Prime]
        AC[Agent Connect]
        RES[Research foundations]
    end

    subgraph Apps[Domain application estate]
        G[Grasp Safety]
        EN[EHCO Energy]
        NL[Noble Law]
        WR[EHCO War Room]
        H[HTPI]
        PC[Project Construct]
        LU[EHCO Luminis]
        N[EHCO Nexus]
        PT[EHCO Permit Trace]
        P[Pegasus IT]
    end

    CAT --> RT
    CAT --> Shared
    Shared -->|bounded contracts / reusable capability| Apps
    RT -. scoped Runtime participation<br/>only where owning evidence establishes it .-> Apps
    RT -. scoped Runtime relationships .-> Shared
```

**Interpretation:** the applications are not unrelated products bolted onto an AI-OS. They are governed domain components that can consume reusable EHCO capabilities under bounded contracts while retaining their own domain logic, records, evidence, application lifecycle, and realization state. Runtime participation remains orthogonal and evidence-scoped.

## 4. Technical evidence to market evidence ladder

```mermaid
flowchart LR
    A[Architecture proposition]
    B[Source / artifact identity]
    C[Qualification / deterministic tests]
    D[Observed execution or Runtime evidence<br/>when actually established]
    E[Controlled technical diligence]
    F[Market / customer / commercial evidence<br/>only when separately established]
    G[Investment or commercial conclusion<br/>outside this repository unless separately approved]

    A --> B --> C --> D --> E --> F --> G
```

**Interpretation:** evidence classes accumulate only when the relevant owning evidence exists. A public architecture statement does not become implementation evidence; a passing component test does not become deployment or Runtime proof; technical evidence does not manufacture market validation; and this public technical repository does not publish confidential investment conclusions merely because they may be informed by the same underlying technology estate.

## Reading rule

Use these diagrams for orientation, then verify material propositions through the [Ecosystem Claim → Evidence Matrix](../../assurance/ECOSYSTEM-CLAIM-EVIDENCE-MATRIX.md). The [Runtime, Repository, and Test-Estate Boundary](../runtime-repository-and-test-estate-boundary.md) controls detailed Runtime/source/evidence interpretation.
