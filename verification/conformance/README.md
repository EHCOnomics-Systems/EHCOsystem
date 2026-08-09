# EHCO AI-OS Public Conformance

## Purpose

This directory defines public black-box conformance properties derived from accepted public EHCO AI-OS architecture and invariants.

It does not disclose proprietary implementation mechanics and does not claim that the Runtime, any private implementation, or any deployment has passed these properties unless an identified public evidence record expressly establishes that result.

The accepted standing remains **52/53**. Conformance specifications and repository checks do not calculate or alter standing.

## Current specification

- [Public Contracts](PUBLIC-CONTRACTS.md)

## Conformance boundary

A public conformance case should state:

- the public property being evaluated;
- the bounded input or scenario class;
- the expected observable outcome;
- the evidence source for the expectation;
- the environment/version/time of any execution record;
- the proof ceiling of the result.

A conformance result must not be promoted into Runtime admission, universal behavioral proof, production security, deployment authorization, or independent certification unless a separately applicable governing record establishes that relationship.
