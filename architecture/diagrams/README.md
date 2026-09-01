---
title: EHCOsystem Public Architecture Diagrams
version: 2.0
status: current-public-architecture-navigation
published: 2026-09-01
maintainer: EHCOnomics
evidence_class: original-public-safe-architecture-diagrams
evidence_scope: explanatory architecture relationships
---

# EHCOsystem Public Architecture Diagrams

These diagrams provide a compact visual route through the [Instantiated AI](../INSTANTIATED-AI.md) category, [EHCOsystem Technology Estate](../EHCO-TECHNOLOGY-ESTATE.md), Runtime projection, shared technologies, applications, and evidence.

## 1. Category to ecosystem

```mermaid
flowchart TD
    A[Instantiated AI<br/>architectural category]
    B[EHCOsystem<br/>EHCOnomics' Instantiated AI ecosystem]
    C[EHCO AI-OS<br/>realized Tier One Runtime<br/>52/53]
    D[EHCO_DOCKER_PORTABILITY<br/>PRIMARY_ACCESSIBLE_RUNTIME_PROJECTION<br/>deployment-ready portable delivery]
    E[Shared downstream technologies<br/>Language Model / Range Reactor / RAG / Prime / Agent Connect]
    F[Research foundations]
    G[Governed applications]
    H[Tier Three interfaces / projections]

    A --> B
    B --> C
    B --> E
    B --> F
    B --> G
    C --> D
    C -->|governed Runtime relationships| E
    E --> G
    D --> H
    E --> H
    G --> H
```

## 2. Computational ownership

```mermaid
flowchart LR
    AIOS[EHCO AI-OS] --> RG[Runtime governance<br/>authority / state / transition / release / proof]
    DP[EHCO_DOCKER_PORTABILITY] --> PORT[portable Runtime projection]
    LM[Language Model] --> LANG[deterministic computational language]
    RR[Range Reactor] --> RANGE[deterministic range / reasoning]
    RAG[EHCO RAG] --> RET[retrieval / provenance / evidence]
    PRIME[EHCO Prime] --> REL[relationship continuity]
    AC[Agent Connect] --> COORD[registry / discovery / routing]
    APPS[Governed applications] --> DOM[domain intelligence / workflows]
```

## 3. Language Model and Range Reactor

```mermaid
flowchart TD
    LM[EHCO Language Model<br/>mature deterministic computational language]
    LMA[deep final capability/source closure]
    LMB[immutable artifact<br/>built / qualified / released]
    LMC[governed staging<br/>execution / verification established]
    RR[EHCO Range Reactor<br/>mature deterministic range/reasoning]
    RRM[selected matched A/B<br/>14.304307x wall<br/>14.208722x CPU<br/>94.755854% allocation reduction]
    RRS[semantic closure<br/>82 passed / 0 failed]

    LM --> LMA --> LMB --> LMC
    RR --> RRM
    RR --> RRS
```

## 4. Public review path

```mermaid
flowchart LR
    R[README / front door]
    I[Instantiated AI]
    A[Architecture / Technology Estate]
    C[Components]
    E[Selected evidence]
    V[Verification]
    D[Deep diligence]

    R --> I --> A --> C --> E --> V --> D
```

## Continue reading

- [EHCOsystem Technology Estate](../EHCO-TECHNOLOGY-ESTATE.md)
- [Components and Runtime Relationships](../ecosystem-components-and-participation.md)
- [Language Model](../../language-model/README.md)
- [Range Reactor](../../range-reactor/README.md)
- [Current Runtime / Full Flex evidence](../../runtime/README.md)
- [Public verification](../../verification/README.md)
