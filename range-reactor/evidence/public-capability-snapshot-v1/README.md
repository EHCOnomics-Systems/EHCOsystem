# EHCO Range Reactor Public Capability Snapshot v1

## Purpose

This snapshot publishes a selected set of **public-safe synthetic Range Reactor capability vectors** derived from review of the accepted owning-source lineage.

The vectors are intentionally synthetic rather than byte copies of controlled implementation or private test artifacts. They expose the proposition being tested, the expected deterministic property, and the evidence boundary while preserving the controlled-source disclosure boundary.

## Evidence class

The snapshot is **source-reviewed synthetic capability evidence**. It establishes the published vector bytes, manifest identity, source-review binding, capability categories and evidence ceiling.

The broader Range Reactor maturity record remains grounded in accepted owning source and qualification evidence. This snapshot provides a public inspection window into selected established capability relationships.

## Covered capability dimensions

The eight vectors cover:

- deterministic replay;
- contradiction preservation;
- finite-bound frontier preservation;
- possible-versus-inevitable reachability distinction;
- semantic collapse with retained witness fibers;
- independent rejection of forged collapse/certificate data;
- source-mutation identity sensitivity; and
- grounded proof custody for obligation discharge.

## Source-review identity

The manifest records the exact accepted owning-source revision reviewed for this publication. The revision is an identity binding only; controlled repository location and implementation bytes remain outside the public snapshot.

## Evidence ceiling

These vectors provide bounded public evidence for the selected capability propositions. They do not establish theoretical completeness, generalized Full-Range exhaustion, production deployment, Runtime admission/binding/invocation/participation, Runtime authority/state/proof, artifact release, or standing change.

## Files

- `MANIFEST.json` — snapshot identity, accepted-source review binding, fixture hash, case count, scope and proof ceiling.
- `capability-vectors.json` — eight public-safe synthetic capability vectors.

## Verification

Run:

```bash
python3 verification/validate_public_range_reactor_snapshot.py
```

The validator checks exact snapshot structure and fixture SHA-256, required public component/navigation relationships, controlled-source disclosure boundaries, and Range Reactor public-maturity wording.

Use of these materials is governed by the repository root `LICENSE`.
