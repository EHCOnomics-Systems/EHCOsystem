# EHCO AI-OS Public Evidence Companion

This directory is the public landing surface for the EHCO AI-OS Public Evidence Companion associated with the **EHCO AI-OS Governed Operational Architecture — Public Edition v1.8**.

The companion is a bounded public evidence and verification surface for the realized EHCO AI-OS Runtime. It preserves provenance, standing projections, source bindings, enforcement anchors, continuity records, observed captures, delivery boundaries, and suite verification. It does not replace Runtime authority, independently create or alter standing, or authorize production deployment, public ingress, operational external release, or go-live.

## Current source and packet-time identity

The current canonical source owner for EHCO AI-OS is the controlled `ehconomics/EHCO_AI-OS` repository.

Source-root, worktree, file-path, and hash identifiers inside Packets 00–08 identify the exact records or snapshots bound when each packet was created. They remain part of the packet provenance. A packet-time label such as a canonical source root must not be interpreted as the current source owner, a separate Runtime, or an authority location.

The packets are not rewritten merely because the controlled source estate advances. Current source ownership and current Runtime status are stated by current control records; packet identifiers preserve the evidence they originally bound.

## Published release

The canonical Version 1 package is published at [`evidence/public-evidence-companion/v1/`](public-evidence-companion/v1/) and contains Packets 00–08. The dossier PDF is included in Packet 00 as a hash-bound source document and is also projected from the repository-level [`dossiers/`](../dossiers/) directory.

Repository publication means that the identified public artifacts are visible for inspection. It does **not** change any packet-level authority, standing, deployment, production-activation, ingress, go-live, or operational release status.

## Packet structure

### Packet 00 — Dossier Identity and Boundary

Binds the evidence companion to the exact public dossier identity and records that the packet has no authority, standing, Runtime-truth, deployment, or release effect.

### Packet 01 — Instantiated Standing

Projects the accepted **52/53** operational standing baseline in a bounded, public-safe, machine-verifiable form. It records the accepted baseline and its status boundaries; the packet does not independently create or alter the standing it projects.

### Packet 02 — Canonical Runtime Source Binding

Binds a provenance source snapshot to exact SHA-256 values. Source code and local absolute paths are excluded except where a separately classified hash-preserved evidence record expressly retains one. The packet does not claim gate-chain implementation coverage or live Runtime observation.

### Packet 03 — Tier 1 Authority Enforcement

Records exact source identity and the presence of named Tier 1 enforcement anchors. It does not execute the Runtime, create standing, alter authority, or authorize release.

### Packet 04 — Runtime Packet and Continuity Anchors

Records source bindings and named implementation declarations concerning Runtime packet, continuity, and recursive-support anchors. It does not claim live execution, end-to-end behavioral proof, persistence or restart validation, recovery validation, or complete source disclosure.

### Packet 05 — Proof, Collapse, Recovery, Release, and Projection Anchors

Records source bindings and named declarations for proof, receipt, collapse, quarantine, freeze, recovery, release, and public projection. It does not claim live Runtime execution, end-to-end behavioral proof, proof-admission validation, test results for the named mechanisms, production authorization, or complete source disclosure.

### Packet 06 — Observed Live Capture and Release Status

Contains hash-bound observed local-live capture artifacts and release-authority records. Its evidence disposition is mixed: direct observations, direct discrepancies, cross-snapshot differences, and behavioral gaps remain explicitly separated. External operational release and production activation are not granted.

### Packet 07 — Public Boundaries and Delivery Status

Records separation among architecture, standing, validation, projection, and delivery. It preserves open Packet 06 discrepancies and gaps, treats Kubernetes as a target translation rather than proven production realization, and does not authorize public ingress, operational external release, production activation, or go-live.

### Packet 08 — Suite Verification and Closure

Verifies the dossier identity, packet manifests, declared files, packet verification statuses, receipts, and non-authorization boundaries. It does not resolve Packet 06 discrepancies or gaps, authorize operational release or activation, or convert packaging into Runtime authority.

## Disclosure boundary

The public suite may include:

- public dossier identity and cryptographic hashes;
- claim and standing records;
- manifests and packet receipts;
- bounded verification results;
- public-safe status records;
- approved hash-preserved evidence;
- bounded packet-verification tooling.

The suite does not include the proprietary Runtime implementation source. Verification tooling is not classified as Runtime implementation source.

## Evidence discipline

A packet may establish source identity, manifest integrity, the presence of a named declaration, a recorded observation, or a bounded verification result. Those findings do not silently become deployment, admission, standing, production operation, operational external release, or go-live authorization.

The companion preserves mixed, blocked, pending, divergent, and not-directly-observed states rather than converting them into passes or failures.

## Validation

The repository validation workflow checks the canonical dossier hash, packet directory closure, JSON syntax, packet manifests, detached manifest hashes, suite closure, prohibited staging residue, and high-confidence secret indicators. See [Public Evidence Validation](../verification/README.md).
