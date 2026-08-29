---
title: EHCOsystem Public Architecture Diagrams
version: 1.3
status: current-public-architecture-navigation
published: 2026-08-28
maintainer: EHCOnomics
evidence_class: original-public-safe-architecture-diagrams
evidence_scope: explanatory architecture relationships
supersedes: version 1.2
---

# EHCOsystem Public Architecture Diagrams

These diagrams provide public-safe views of the category, Runtime, component estate, computational ownership, maturity lanes, and evidence progression described in [Instantiated AI](../INSTANTIATED-AI.md), [EHCOsystem — An Instantiated AI Ecosystem](../EHCO-TECHNOLOGY-ESTATE.md), and the [Ecosystem Claim → Evidence Matrix](../../assurance/ECOSYSTEM-CLAIM-EVIDENCE-MATRIX.md).

## 1. Category, Runtime, portability, components, and projection

```mermaid
flowchart TD
    A[Instantiated AI<br/>architectural category]
    B[EHCOsystem<br/>EHCOnomics' Instantiated AI ecosystem]
    C[EHCO AI-OS<br/>realized Tier One Runtime<br/>standing 52/53]
    D[EHCO_DOCKER_PORTABILITY<br/>PRIMARY_ACCESSIBLE_RUNTIME_PROJECTION]
    H[EHCO Dashboard<br/>current accepted working<br/>Tier Three projection baseline]
    E[Downstream governed components<br/>computational / research / application owners]
    F[Tier Three<br/>interfaces and projections]
    G[Public EHCOsystem repository<br/>architecture / evidence / diligence]

    A --> B
    B --> C
    B --> E
    B --> F
    B --> G
    C -->|established Runtime lineage| D
    D --> H
    H --> F
    C -->|scoped governed relationships| E
    E --> F
```

**Interpretation:** the category is Instantiated AI; the ecosystem is EHCOsystem; EHCO AI-OS owns Tier One Runtime authority; Docker Portability carries the primary accessible Runtime projection; Dashboard provides the current accepted Tier Three projection baseline; downstream components own their computational and domain capabilities; the public repository publishes architecture and evidence.

## 2. Computational ownership across the ecosystem

```mermaid
flowchart LR
    R[Runtime governance<br/>authority / state / release / proof] --> AIOS[EHCO AI-OS]
    RP[Primary accessible Runtime projection] --> DP[EHCO_DOCKER_PORTABILITY]
    V[Working projection baseline] --> DASH[EHCO Dashboard]
    L[Deterministic computational language] --> LM[EHCO Language Model]
    Q[Bounded range / reasoning computation] --> RR[EHCO Range Reactor]
    E[Retrieval / context / provenance / evidence] --> RAG[EHCO RAG]
    P[Persistent individual relationship] --> PRIME[EHCO Prime]
    C[Registry / discovery / candidate routing] --> AC[EHCO Agent Connect]
    M[Memory / continuity research] --> MEM[EHCO Memory]
    RF[Research substrates<br/>specification / recursion / form] --> RES[Primordia / Recursion / Fractal Systems]
    DA[Domain logic / records / workflows] --> APPS[Governed domain applications]
    T[Interfaces / reports / public-safe views] --> T3[Tier Three]

    AIOS --> DP
    DP --> DASH
    DASH --> T3
```

## 3. Shared foundations to domain applications

```mermaid
flowchart TD
    CAT[Instantiated AI conditions]
    RT[EHCO AI-OS<br/>Tier One Runtime foundation]

    subgraph Spine[Principal shared downstream component spine]
        LM[Language Model<br/>mature deterministic computational language<br/>advanced near-final maturation]
        RR[Range Reactor<br/>mature deterministic range / reasoning]
        RAG[RAG<br/>accepted controlled baseline<br/>Stage 1 implementation active]
        PRIME[Prime<br/>mature relationship-service source/control]
        AC[Agent Connect<br/>mature coordination-service source/control]
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

    CAT --> RT
    CAT --> Spine
    CAT --> Research
    Spine -->|bounded contracts / reusable capability| Apps
    Research -->|research / foundation contribution| Spine
    RT -->|governed Runtime relationships| Spine
    RT -->|governed Runtime relationships| Apps
```

**Interpretation:** the foundational/shared spine is substantially established. The Language Model's mature deterministic foundation is in advanced near-final strengthening and qualification. Current ecosystem development also includes RAG implementation, research/foundation reconciliation, and continuing domain/application expansion.

## 4. Technical evidence progression

```mermaid
flowchart LR
    A[Architecture proposition]
    B[Source / artifact identity]
    C[Qualification / deterministic tests]
    D[Observed execution / Runtime evidence]
    E[Controlled technical diligence]
    F[Market / customer / commercial evidence]
    G[Investment / commercial analysis]

    A --> B --> C --> D --> E --> F --> G
```

**Interpretation:** each evidence class establishes a specific proposition. Reviewers can move from architecture through source identity, qualification, observed effects, controlled diligence, and commercial evidence while preserving the owner and scope of each claim.

## Reading route

Use these diagrams for orientation, then follow the [Ecosystem Claim → Evidence Matrix](../../assurance/ECOSYSTEM-CLAIM-EVIDENCE-MATRIX.md) for claim-specific evidence and the [Runtime, Repository, and Test-Estate Boundary](../runtime-repository-and-test-estate-boundary.md) for evidence-domain ownership.

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.3 | 2026-08-28 | Recast Language Model maturity as advanced near-final strengthening of an established deterministic system rather than an internal development-stage projection. |
| 1.2 | 2026-08-28 | Recast all diagrams around affirmative ownership, capability and maturity relationships and aligned the component set to the current public scope. |
| 1.1 | 2026-08-28 | Added differentiated component maturity and the Dashboard projection baseline. |
