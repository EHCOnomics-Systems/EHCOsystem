---
title: EHCOsystem Public Architecture Diagrams
version: 1.1
status: current-public-architecture-navigation
published: 2026-08-28
maintainer: EHCOnomics
evidence_class: original-public-safe-architecture-diagrams
proof_ceiling: explanatory architecture only; diagrams do not create implementation, deployment, Runtime participation, market validation, or Runtime proof
supersedes: version 1.0
---

# EHCOsystem Public Architecture Diagrams

These diagrams are original public-safe explanatory views of the architecture described in [Instantiated AI](../INSTANTIATED-AI.md), [EHCOsystem — An Instantiated AI Ecosystem](../EHCO-TECHNOLOGY-ESTATE.md), and the [Ecosystem Claim → Evidence Matrix](../../assurance/ECOSYSTEM-CLAIM-EVIDENCE-MATRIX.md).

They intentionally show **relationships, estate lanes, maturity distinctions, and ownership**, not private topology, deployment configuration, protected implementation mechanics, current Runtime participation, or confidential investment material. This diagram record does not create implementation, deployment, Runtime participation, market validation, or Runtime proof.

## 1. Category, Runtime, components, portability, and projection

```mermaid
flowchart TD
    A[Instantiated AI<br/>architectural category]
    B[EHCOsystem<br/>EHCOnomics' Instantiated AI ecosystem]
    C[EHCO AI-OS<br/>realized Tier One Runtime foundation]
    D[EHCO_DOCKER_PORTABILITY<br/>PRIMARY_ACCESSIBLE_RUNTIME_PROJECTION]
    H[EHCO Dashboard<br/>current accepted working<br/>Tier Three projection baseline]
    E[Downstream governed components<br/>computational / research / application owners]
    F[Tier Three<br/>interfaces and projections]
    G[Public EHCOsystem repository<br/>architecture / evidence / diligence]

    A --> B
    B --> C
    B --> E
    B --> F
    C -. established Runtime lineage .-> D
    D --> H
    H --> F
    C -. scoped Runtime relationships<br/>only when evidenced .-> E
    E --> F
    B --> G

    D -. not an independent<br/>authority owner .-> C
    H -. projection only<br/>no dashboard authority .-> C
    G -. public representation only<br/>not Runtime authority .-> B
```

**Interpretation:** Instantiated AI is the category; EHCOsystem is the ecosystem. EHCO AI-OS is the realized Tier One Runtime foundation. `EHCO_DOCKER_PORTABILITY` is the `PRIMARY_ACCESSIBLE_RUNTIME_PROJECTION` of the established Runtime lineage. The EHCO Dashboard is the current accepted working Tier Three projection baseline within that portability estate. The portability layer, Dashboard, Tier Three surfaces, downstream components, and public repository do not become independent Runtime authority or present Runtime truth.

## 2. Computational ownership across the ecosystem

```mermaid
flowchart LR
    R[Runtime governance<br/>authority / state / release / proof] --> AIOS[EHCO AI-OS]
    RP[Primary accessible Runtime projection] --> DP[EHCO_DOCKER_PORTABILITY]
    V[Current accepted working<br/>projection baseline] --> DASH[EHCO Dashboard]
    L[Deterministic computational language] --> LM[EHCO Language Model]
    Q[Bounded range / reasoning computation] --> RR[EHCO Range Reactor]
    E[Retrieval / context / provenance / evidence] --> RAG[EHCO RAG]
    P[Persistent individual relationship] --> PRIME[EHCO Prime]
    C[Registry / discovery / candidate routing] --> AC[EHCO Agent Connect]
    M[Memory / continuity research] --> MEM[EHCO Memory]
    RF[Research substrates<br/>specification / recursion / form] --> RES[Primordia / Recursion / Fractal Systems]
    DA[Domain logic / records / workflows] --> APPS[Governed domain applications]
    T[Interfaces / reports / public-safe views] --> T3[Tier Three]

    AIOS -. established lineage .-> DP
    DP --> DASH
    DASH --> T3
```

**Interpretation:** ownership is intentionally separated. Language computation is not Runtime authority; retrieval is not application truth; coordination is not admission; application logic is not Tier One governance; and projection is not the state it displays. The principal shared component spine contains different maturity postures rather than one uniform status.

## 3. Shared foundations to domain applications

```mermaid
flowchart TD
    CAT[Instantiated AI conditions]
    RT[EHCO AI-OS<br/>Tier One Runtime foundation]

    subgraph Spine[Principal shared downstream component spine]
        LM[Language Model<br/>mature / staged and stage-verified source posture]
        RR[Range Reactor<br/>mature / qualified accepted lineage]
        RAG[RAG<br/>controlled implementation posture]
        PRIME[Prime<br/>advanced relationship-service source/control]
        AC[Agent Connect<br/>advanced coordination-service source/control]
    end

    subgraph Research[Governed research and foundation lane]
        MEM[Memory]
        PRIM[Primordia]
        REC[Recursion]
        FRA[Fractal Systems]
    end

    subgraph Apps[Continuing downstream governed domain/application expansion]
        EN[EHCO Energy]
        NL[Noble Law]
        WR[EHCO War Room]
        H[HTPI]
        PC[Project Construct]
        LU[EHCO Luminis]
        N[EHCO Nexus]
        PT[EHCO Permit Trace]
    end

    subgraph Programs[Substantial project/pilot expansion]
        G[Grasp Safety]
        P[Pegasus IT]
    end

    CAT --> RT
    CAT --> Spine
    CAT --> Research
    Spine -->|bounded contracts / reusable capability| Apps
    Spine -->|bounded contracts / reusable capability| Programs
    Research -. research / foundation contribution .-> Spine
    RT -. scoped Runtime relationships<br/>only where owning evidence establishes them .-> Spine
    RT -. scoped Runtime participation<br/>only where owning evidence establishes it .-> Apps
    RT -. scoped Runtime participation<br/>only where owning evidence establishes it .-> Programs
```

**Interpretation:** current source review supports a qualitative posture in which the foundational/shared EHCOsystem spine is substantially established and remaining work is increasingly concentrated rather than foundational. Remaining work is separated into bounded finalization/hardening, RAG implementation, research/foundation reconciliation, and continuing downstream governed domain/application expansion. Grasp Safety and Pegasus IT remain downstream governed components but are tracked as substantial project/pilot expansion outside the public core-completion denominator. Lane placement changes no persistent identity, authority, evidence class, or Runtime relationship.

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

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.1 | 2026-08-28 | Added the accepted working Dashboard projection baseline, differentiated shared-component maturity, research/application lane separation, and the Grasp/Pegasus project-pilot lane outside the public core-completion denominator. |
| 1.0 | 2026-08-26 | Added four original public-safe explanatory architecture views. |
