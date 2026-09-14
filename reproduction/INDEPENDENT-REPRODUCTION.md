# Independent Reproduction Instructions

Status: **public-candidate instructions; independent reproduction receipt not yet established.**

These instructions are intended for a technically competent reviewer who is independent of the EHCOnomics implementation/development environment and uses only public material.

## Reviewer eligibility

The reviewer must:
- not have implemented the selected EHCOsystem public proof harness;
- operate outside the EHCOnomics implementation/development environment;
- have no private EHCOnomics repository, Drive, implementation, or Runtime credentials for this reproduction; and
- use only publicly available instructions and artifacts.

Prior exposure to other EHCOnomics material does not satisfy or defeat this receipt by itself. The reproduction record must state whether any prior private material was actually used for this reproduction and whether any unpublished EHCOnomics intervention was required.

## Fixed identities

- Public C1B preregistration identity: `8a1a05b4865eaefa716e77cbe669e819e7d6e5b3`
- Frozen C1B manifest SHA-256: `440ae3a567f0d7db29a2c3348d0a7eb296ca5eece0b31a78fb9b58932efba357`
- Accepted C1 Public Proof Kernel identity: `c208cb7cd002d016359f39aba1e3aef3f820befc`
- Public Proof Kernel executable SHA-256 (`proof/public-kernel/v1/kernel.py`): `ef497581702c4929e0e32beef66e39250c95c450d2c90a64efef85c390cb3d31`
- OPA v1.20.2 official Linux x86-64 static asset SHA-256: `69da5179ee403d10fa11bab6cfb4ffb0d23dba5f9b682fa977db772a1da5670f`
- Original official result SHA-256 for comparison after reproduction: `0010b0f2f0369d9328d34e23d44e7117c038038ce4260a14cb51d0b1ad71e38b`

The preregistration identity is the protocol authority. A later result-publication or launch-candidate commit does not rewrite the pre-result protocol.

## Clean-environment procedure

1. Resolve the public preregistration identity above and inspect `comparison/c1b/v1/`.
2. Obtain the public repository result-bearing candidate at the exact provider-resolvable revision supplied by the result-publication PR/checkpoint and record that exact Git commit in the receipt.
3. Run `python3 verification/verify_all_public.py`.
4. Run the bounded Public Proof Kernel using a reviewer-chosen or locally generated fresh nonce and verify its receipt.
5. Obtain Open Policy Agent v1.20.2 from the official upstream release.
6. Verify the OPA Linux x86-64 static binary SHA-256 equals `69da5179ee403d10fa11bab6cfb4ffb0d23dba5f9b682fa977db772a1da5670f`.
7. Run the published C1B comparison exactly as instructed by the preregistered protocol using a fresh reviewer nonce and retain every outcome.
8. Do not suppress, replace, or rerun an unfavorable/failed case to obtain a preferred result.
9. Compare the independently reproduced result to the published original result without treating equality as a prerequisite for recording the reproduction.
10. Record the environment, commands, public artifact identities, run/result identities, output hashes, every material failure or deviation, and whether unpublished EHCOnomics intervention was required.
11. Produce the machine-readable reproduction receipt using `reproduction/INDEPENDENT_REPRODUCTION_RECEIPT.schema.json`.

## Receipt binding requirements

The receipt schema is intentionally stricter than a narrative checklist. It requires the returned record to bind:

- the exact `EHCOnomics-Systems/EHCOsystem` Git revision used as the reproduction target;
- the frozen public preregistration identity;
- the reviewer-independence facts, including whether prior private material was used and whether unpublished intervention was required;
- the observed clean-environment class, operating system, CPU architecture, Python/OPA versions and executed commands;
- the canonical public verifier command, exit status and output hash;
- the accepted Public Proof Kernel identity, executable digest, freshness nonce, run identity, run-receipt digest and output hashes;
- the frozen C1B protocol/manifest, exact OPA reference-baseline identity, fresh comparison nonce, independent result identity and output hashes;
- whether any preferred-result rerun occurred;
- all deviations, observations and limitations; and
- the receipt's own integrity digest.

Record what actually happened. Do not change a false, failed, contaminated, divergent or incomplete observation merely to make the receipt appear successful. Schema validity establishes structural completeness only; it does not by itself establish C1D acceptance.

## Receipt SHA-256

Set:

- `receipt_hash_algorithm` to `SHA256`; and
- `receipt_hash_scope` to `CANONICAL_JSON_EXCLUDING_RECEIPT_SHA256`.

To calculate `receipt_sha256`, remove the `receipt_sha256` member, serialize the remaining JSON as UTF-8 with keys sorted lexicographically, no insignificant whitespace, JSON separators `,` and `:`, and non-ASCII characters encoded directly rather than ASCII-escaped. Hash those bytes with SHA-256 and record the lowercase hexadecimal digest as `receipt_sha256`.

The hash rule deliberately excludes the digest field itself so the receipt does not depend on a circular self-hash.

## Required receipt interpretation

A reproduction receipt establishes what the independent reviewer actually reproduced from the public instructions and artifacts. It must retain failures and deviations and must not overstate them.

A returned receipt remains subject to C1D intake validation against the exact public identities and independence conditions. In particular, schema-valid evidence is not launch acceptance when the record shows private-material use, unpublished intervention, a preferred-result rerun, an ineligible environment, identity mismatch, integrity failure, or another material unresolved deviation.

A successful receipt does not create Runtime authority, change standing 52/53, certify proprietary same-code identity, prove production deployment, or establish universal superiority.
