---
title: Instantiated AI — Public Architecture Definition
version: 1.1
status: current-public-architecture
published: 2026-08-26
maintainer: EHCOnomics
evidence_class: controlled-ehco-architecture
proof_ceiling: category and ecosystem architecture definition; not implementation evidence, legal certification, deployment evidence, or Runtime proof
---

# Instantiated AI

> **Instantiated AI creates the computational conditions under which artificial intelligence may lawfully operate.**

In this architecture, the intelligence does not determine the conditions of its own operation. It operates within conditions already established by the governing system.

A more formal definition is:

> **Instantiated AI is an artificial intelligence architecture in which the computational conditions governing identity, authority, state, memory, source, scope, permissible action, evidence, and consequence are established independently of the intelligence they govern and before that intelligence is permitted to operate consequentially.**

The central dependency rule is:

> **The governed intelligence cannot be the final authority for establishing the conditions by which that intelligence is governed.**

The intelligence may interpret those conditions, reason about them, explain them, request changes to them, or propose actions within them. Representation does not make the represented condition true.

## EHCOsystem as an Instantiated AI ecosystem

**EHCOsystem is EHCOnomics' Instantiated AI ecosystem.** Instantiated AI is the architectural category; EHCOsystem is the EHCOnomics technology and system estate organized according to that category.

Within EHCOsystem:

- **EHCO AI-OS** is the realized Tier One Runtime foundation and owns the governing Runtime relationships through which authority, scope, recognized state, transition, consequence, continuity, persistence, withholding, release, correction, recovery, and Runtime-originated proof acquire operational meaning;
- **downstream governed components** own distinct computational, evidence, research, relationship, coordination, and domain-application capabilities without becoming Tier One authority merely by existing, executing, or being published;
- **Tier Three** contains interfaces and projections that make governed information visible without becoming the underlying source of authority or technical truth; and
- **public evidence and technical diligence** expose bounded support for material propositions without turning the public repository into the proprietary Runtime implementation.

This category-to-ecosystem relationship does not mean that every EHCOsystem component is a current Runtime participant. Persistent software identity, repository presence, build, deployment, execution, registration, health, or public documentation do not establish Runtime participation. Runtime participation remains a separate scoped relationship established by owning Runtime evidence.

The public `EHCOsystem` GitHub repository is the public technical representation and evidence surface for this ecosystem. It is not the instantiated Runtime and does not acquire Runtime authority by describing the architecture.

## What “instantiated” means

Instantiation distinguishes a represented condition from a condition that is actually established in the operating system.

A prompt can state that an agent is authorized. A policy document can describe an approval limit. A model can say that a source is trustworthy. A memory store can contain an earlier statement. None of those representations, by themselves, establishes operational authority, source standing, or memory standing.

Instantiation asks what the governing computation has actually established: which identity, which authority root, which role, which scope, which state, which source, which policy version, which evidence, which permissible operation, which release condition, and which consequence.

The architectural distinction is therefore:

**representation != instantiation**

## “Lawfully operate” is a computational term here

Within Instantiated AI, **lawful operation** means that an operation is admitted only when it satisfies the governing computational conditions that have standing in the system.

Those conditions can represent legislation and regulation, but they can also represent organizational authority, contractual obligations, roles, policies, user consent, security requirements, operating procedures, resource boundaries, evidence requirements, and other applicable rules.

Instantiated AI does **not** claim that an operation is automatically compliant with every applicable statute, regulation, contract, or jurisdiction merely because the system admits it. Legal compliance remains a separate substantive determination requiring the appropriate legal and evidentiary basis.

## The dependency inversion

Many AI systems begin with intelligence and then provide the model with instructions, retrieved information, permissions, tools, policies, memory, and guardrails. Strong systems may also use IAM, policy engines, sandboxes, provenance controls, approval workflows, and other external enforcement.

Instantiated AI changes the dependency order. The relevant operating reality is established independently of the intelligence before the intelligence can make a consequential proposal effective.

A simplified conceptual sequence is:

```text
Identity
  ↓
Authority
  ↓
State
  ↓
Source / Memory Standing
  ↓
Applicable Rules
  ↓
Permissible Range
  ↓
Intelligence
  ↓
Release
  ↓
Consequence
  ↓
Proof / Continuity
```

The intelligence remains valuable precisely because it can reason inside that structure without having unilateral authority to manufacture the structure.

## Computational conditions

An Instantiated AI architecture can establish conditions including:

| Condition | Question the system must be able to answer |
|---|---|
| Identity | What governed identity is actually operating? |
| Authority | What establishes its right to participate or act? |
| Role | In what capacity is it operating? |
| Scope | Where does that authority begin and end? |
| State | What is computationally recognized as true for this operation? |
| Source | What information may be relied upon, and why? |
| Memory | What may persist, be recalled, and influence later computation? |
| Relationship | How is this governed object related to other identities and authorities? |
| Rules | What governing conditions apply here? |
| Range | Which operations are presently available? |
| Evidence | What supports the recognized condition? |
| Proof | Can the basis for the operation be demonstrated afterward? |
| Release | May the result leave the governed computation? |
| Consequence | May the result alter another governed system or the external world? |

This is broader than authentication or access control. It is an operating reality in which identity, authority, state, evidence, and consequence remain distinguishable and independently governable.

## Computational standing

**Computational standing** is the system-recognized condition under which a participant, source, memory, instruction, operation, or result is eligible to participate within a particular computation.

This creates a critical separation:

**capability answers “Can it?”**

**standing answers “Under these established conditions, may it?”**

A model can be capable of generating a bank-transfer instruction without that instruction having standing. A service can possess usable credentials without a particular operation having standing. A document can be retrievable without having standing as an authoritative source. A stored memory can exist without having standing to influence a later decision.

Accordingly:

- capability != standing;
- retrievable != authoritative;
- stored memory != memory with standing;
- proposal != consequential system state.

## Standing Baseline

A **Standing Baseline** is the continuously maintained computational representation of the identities, authority, relationships, state, evidence, and operating conditions from which standing can be determined.

The purpose is not to reconstruct the entire organization from prompts before every action. Durable conditions can be established and maintained, then changes can be evaluated against that recognized baseline.

A Standing Baseline is an architectural concept. It is not, by itself, a numerical standing value and it does not calculate or alter the accepted EHCO AI-OS standing baseline of **52/53**.

## Instantiated participants and the EHCO terminology boundary

At the category level, an **instantiated participant** is a person, system, service, model, or agent whose identity, authority, role, relationships, scope, and permissible participation have been established within a governing computational environment.

Within current EHCOsystem terminology, however, `PARTICIPANT` and `RUNTIME_PARTICIPANT` are Runtime-scoped terms. Persistent software identity, repository presence, build, deployment, execution, health, registration, compatibility, or this public document does not establish EHCO Runtime participation. EHCO Runtime participation remains scope- and time-bound to the owning Runtime evidence.

This distinction allows the public category concept to be explained without turning category language into a claim about current EHCO Runtime state.

## Source and memory standing

Instantiated AI separates retrieval from authority.

A source may be semantically relevant without being current, authoritative, applicable, or permitted to control the operation. The governing chain can therefore include:

```text
source → provenance → authority → scope → standing → reliance
```

Memory is governed similarly. Storage alone does not establish that a memory is valid for later use. A governed memory environment can preserve who created the memory, under what authority, when it applies, whether it expires or is superseded, how it can be corrected, and whether it has standing in the present operation.

## Intelligence proposal versus consequential state

Models are probabilistic. They can misunderstand, hallucinate, misclassify, or generate invalid requests. Instantiated AI does not require intelligence to become infallible.

Instead, it separates what intelligence **proposes** from what the governing system recognizes as operationally valid.

The architecture therefore aims to make this statement true:

> **The intelligence does not possess unilateral authority to turn its mistake into system truth.**

A proposed inference or action becomes consequential only through the applicable independent conditions for standing, release, and consequence.

## Model independence

The governing reality should survive replacement of the underlying intelligence model.

If replacing one model with another destroys the system's identity, authority, organizational state, source legitimacy, memory legitimacy, operating rules, proof, or continuity, then those conditions were likely properties of the model interaction rather than properties of an instantiated system.

Model independence is therefore a strong architectural test: the model supplies intelligence; the instantiated system supplies the conditions governing that intelligence.

## What Instantiated AI is not

Instantiated AI can use many familiar controls, but none is sufficient alone:

- **Permissions / IAM** can establish access rights but do not, by themselves, establish the full identity-authority-state-source-memory-evidence-consequence relationship.
- **Guardrails** can constrain generated behavior but do not necessarily establish whether the intelligence has standing to participate in the operation.
- **Prompt engineering** can describe operating conditions to a model but does not make those conditions computationally true.
- **RAG** can retrieve relevant information but relevance does not establish source authority or standing.
- **Containerization** can instantiate an execution environment but does not, by itself, instantiate the governing conditions of AI participation.
- **Agent frameworks** can supply planning, tools, memory, delegation, and action, while Instantiated AI addresses the standing under which those capabilities may become consequential.

Instantiated AI therefore cuts across other AI categories. A system can be generative, predictive, conversational, agentic, or autonomous and separately be more or less instantiated in how its operating conditions are established.

## Qualification questions

A candidate Instantiated AI system should be able to answer the following without relying on the model's own assertion as the final authority:

| Test | Qualification question |
|---|---|
| Identity | Can the operating identity be established independently of model assertion? |
| Authority | Is authority computationally derived from an external governing basis rather than merely described in language? |
| Standing | Can the system determine whether participation or reliance is presently valid? |
| State | Does recognized operating truth exist outside the model context? |
| Memory | Is memory governed independently of model preference or self-authored history? |
| Source | Can source authority and applicability be established before reliance? |
| Range | Are permissible operations computationally bounded? |
| Consequence | Can unsupported proposals be prevented from becoming consequential? |
| Proof | Can the system demonstrate the conditions under which an operation had standing? |
| Independence | Do these properties survive replacement of the intelligence model? |

These questions describe an architectural qualification surface, not a self-certification mechanism. Passing prose answers is not implementation evidence.

## EHCOsystem public evidence relationship

The public `EHCOsystem` repository is the architecture, evidence, provenance, research, verification, and publication surface for EHCOnomics' Instantiated AI ecosystem. It is not the EHCO AI-OS Runtime and does not acquire Runtime authority by describing Instantiated AI.

Use [EHCOsystem — An Instantiated AI Ecosystem](EHCO-TECHNOLOGY-ESTATE.md) to see how the category is expressed across the Tier One Runtime foundation, downstream governed computational and application components, research foundations, and Tier Three projections.

Existing public records expose bounded aspects of the instantiated-system thesis:

- [EHCO AI-OS Instantiated System](EHCO-AI-OS-INSTANTIATED-SYSTEM.md) — the current public system-level record and Runtime/repository boundary;
- [EHCO AI-OS Public System Invariants](SYSTEM-INVARIANTS.md) — public non-collapse rules such as capability versus authority, proposal versus commit, evidence versus authority, and projection versus Runtime truth;
- [Governed Runtime Architecture](GOVERNED-RUNTIME-ARCHITECTURE.md) — public architectural structure;
- [Instantiated Proof Range](instantiated-proof-range.md) — bounded proof and evidence interpretation;
- [Public Evidence Companion](../evidence/README.md) — public evidence with explicit proof ceilings;
- [EHCO Language Model](../language-model/README.md) — separation between deterministic language computation and the governing Runtime foundation.

Source-control workflows, CI, provider gates, release controls, provenance machinery, and public validation support trustworthy development and publication. They are supporting controls beneath the category, not the definition of Instantiated AI itself.

## Public claim boundary

This document is a public architecture definition. It does not disclose proprietary enforcement mechanics and does not independently establish implementation, execution, deployment, current Runtime participation, Runtime admission, Runtime authority, standing change, legal compliance, third-party certification, or production state.

The accepted EHCO AI-OS standing baseline remains **52/53**. Repository publication does not alter it.
