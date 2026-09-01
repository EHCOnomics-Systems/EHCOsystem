---
title: EHCOsystem Public Architecture Diagrams
version: 1.6
status: current-public-architecture-navigation
published: 2026-08-31
maintainer: EHCOnomics
evidence_class: original-public-safe-architecture-diagrams
evidence_scope: explanatory architecture relationships
supersedes: version 1.5
---

# EHCOsystem Public Architecture Diagrams

These diagrams provide public-safe views of the category, Runtime, component estate, computational ownership, maturity lanes, and evidence progression described in [Instantiated AI](../INSTANTIATED-AI.md), [EHCOsystem — An Instantiated AI Ecosystem](../EHCO-TECHNOLOGY-ESTATE.md), and the [Ecosystem Claim → Evidence Matrix](../../assurance/ECOSYSTEM-CLAIM-EVIDENCE-MATRIX.md).

## 1. Category, Runtime, portability, local operation, components, and projection

```mermaid
flowchart TD
    A[Instantiated AI<br/>architectural category]
    B[EHCOsystem<br/>EHCOnomics' Instantiated AI ecosystem]
    C[EHCO AI-OS<br/>realized Tier One Runtime<br/>REALIZED / COMPLETE_IN_ACCEPTED_SCOPE<br/>standing 52/53]
    D[EHCO_DOCKER_PORTABILITY<br/>PRIMARY_ACCESSIBLE_RUNTIME_PROJECTION<br/>deployment-ready portable delivery form]
    L[Self-hosted local Docker Runtime<br/>Dashboard + bridge + worker<br/>networking + persistent surfaces]
    H[EHCO Dashboard<br/>local host port 8080<br/>Tier Three projection baseline]
    E[Downstream governed components<br/>computational / research / application owners]
    F[Tier Three<br/>interfaces and projections]
    G[Public EHCOsystem repository<br/>architecture / evidence / diligence]

    A --> B
    B --> C
    B --> E
    B --> F
    B --> G
    C -->|established hardened Runtime lineage| D
    D -->|portable local operation| L
    L --> H
    H --> F
    C -->|scoped governed relationships| E
    E --> F
```

**Interpretation:** the category is Instantiated AI; the ecosystem is EHCOsystem; EHCO AI-OS is the realized Tier One Runtime at accepted standing 52/53; Docker Portability carries the primary accessible Runtime projection and deployment-ready portable delivery form; owning Docker/host evidence establishes self-hosted local operation; Dashboard provides the current accepted Tier Three projection baseline from that local operating environment; downstream components own their computational and domain capabilities; the public repository publishes architecture and evidence.

## 2. Computational ownership across the ecosystem

```mermaid
flowchart LR
    R[Runtime governance<br/>authority / state / release / proof] --> AIOS[EHCO AI-OS]
    RP[Primary accessible Runtime projection<br/>deployment-ready portable delivery] --> DP[EHCO_DOCKER_PORTABILITY]
    LO[Self-hosted local Docker operation] --> LOCAL[Dashboard / bridge / worker]
    V[Working projection baseline<br/>local port 8080 capture] --> DASH[EHCO Dashboard]
    L[Deterministic computational language] --> LM[EHCO Language Model]
    Q[Proof-carrying implication / reachability<br/>range / reasoning computation] --> RR[EHCO Range Reactor]
    E[Retrieval / context / provenance / evidence] --> RAG[EHCO RAG]
    P[Persistent individual relationship] --> PRIME[EHCO Prime]
    C[Registry / discovery / candidate routing] --> AC[EHCO Agent Connect]
    M[Memory / continuity research] --> MEM[EHCO Memory]
    RF[Research substrates<br/>specification / recursion / form] --> RES[Primordia / Recursion / Fractal Systems]
    DA[Domain logic / records / workflows] --> APPS[Governed domain applications]
    T[Interfaces / reports / public-safe views] --> T3[Tier Three]

    AIOS --> DP
    DP --> LOCAL
    LOCAL --> DASH
    DASH --> T3
```

## 3. Shared foundations to domain applications

```mermaid
flowchart TD
    CAT[Instantiated AI conditions]
    RT[EHCO AI-OS<br/>Tier One Runtime foundation]

    subgraph Spine[Principal shared downstream component spine]
        LM[Language Model<br/>mature deterministic computational language<br/>final source/artifact closure established<br/>staging verification frontier]
        RR[Range Reactor<br/>mature deterministic proof-carrying<br/>implication / reachability / range / reasoning]
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

**Interpretation:** the foundational/shared spine is substantially established. The Language Model has established deep final capability/source closure and governed final component artifact build, qualification and release; its current selected lifecycle frontier is staging execution and verification of that exact released artifact. Production verification/deployment and Tier One Runtime participation remain separate evidence dimensions. Range Reactor is a mature deterministic proof-carrying implication/reachability and range/reasoning system with accepted source, qualification and physical-host evidence supporting that maturity. Current ecosystem development also includes RAG implementation, research/foundation reconciliation, and continuing domain/application expansion.

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

Use these diagrams for orientation, then follow the [Canonical Public Claim Registry](../../assurance/PUBLIC-CLAIM-REGISTRY.json) and [Ecosystem Claim → Evidence Matrix](../../assurance/ECOSYSTEM-CLAIM-EVIDENCE-MATRIX.md) for claim-specific evidence, the [Range Reactor component record](../../range-reactor/README.md) for Range Reactor capability detail, and the [Runtime, Repository, and Test-Estate Boundary](../runtime-repository-and-test-estate-boundary.md) for evidence-domain ownership.

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.6 | 2026-08-31 | Synchronized Language Model maturity to established deep final capability/source closure and governed final component artifact build, qualification and release, with staging execution/verification as the current lifecycle frontier. |
| 1.5 | 2026-08-29 | Added realized accepted-scope maturity, deployment-ready portability, self-hosted local Docker operation, Dashboard local port-8080 relationship and physical Range Reactor qualification framing. |
| 1.4 | 2026-08-28 | Expanded Range Reactor computational ownership and public evidence routing. |
| 1.3 | 2026-08-28 | Recast Language Model maturity as advanced near-final strengthening of an established deterministic system rather than an internal development-stage projection. |
| 1.2 | 2026-08-28 | Recast all diagrams around affirmative ownership, capability and maturity relationships and aligned the component set to the current public scope. |
