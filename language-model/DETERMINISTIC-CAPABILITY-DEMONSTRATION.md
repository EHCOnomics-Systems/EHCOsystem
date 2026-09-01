# EHCO Language Model — Deterministic Capability Demonstration

The **EHCO Language Model** is a deterministic computational-language system built as:

> **DETERMINISTIC_COMPUTATIONAL_LANGUAGE / SINGLE_PATH / EXPLICIT_EHCO_COMPUTATION / ZERO_WEIGHT_ONLY / ZERO WEIGHTS TRAINED**

This page turns the accepted public Language Model fixture and qualification evidence into one readable capability demonstration. It does not create a new maturity claim or replace the accepted qualification estate. The examples below are selected from the exact public fixture artifacts already published in this repository; their source fixture Git identities are stable public repository objects, while private implementation topology is intentionally absent.

## Demonstration at a glance

| Capability | Example input | Accepted disposition | Deterministic result / meaning | Public witness |
|---|---|---|---|---|
| grammatical composition | `the cat walks` | `PASS` | singular subject/verb composition is accepted | `LM_ZW_CAP_SLICE_002_SYNTAX_COMPOSITION.json` |
| ambiguity preservation | `the sheep went` | `RETAIN_AMBIGUITY` | number ambiguity is preserved rather than guessed away | `LM_ZW_CAP_SLICE_002_SYNTAX_COMPOSITION.json` |
| compositional withholding | `the cat walk` | `WITHHOLD` | missing composition support produces typed withholding | `LM_ZW_CAP_SLICE_002_SYNTAX_COMPOSITION.json` |
| context-sensitive interpretation | `walk` in instruction context | `PASS` | instruction context yields one accepted candidate | `LM_ZW_CAP_SLICE_003_REFERENCE_CONTEXT.json` |
| context/reference boundary | `walk` in report context | `WITHHOLD` | unresolved reference is withheld with `MISSING_REFERENCE_RESOLUTION` | `LM_ZW_CAP_SLICE_003_REFERENCE_CONTEXT.json` |
| reference ambiguity | `the cat walks` + `the sheep went` | `RETAIN_AMBIGUITY` | two candidates remain explicit when disambiguation is unavailable | `LM_ZW_CAP_SLICE_003_REFERENCE_CONTEXT.json` |
| ambiguity/withholding precedence | ambiguous syntax + unresolved report reference | `WITHHOLD` | an unresolved required reference outranks an otherwise retained ambiguity | `LM_ZW_CAP_SLICE_004_AMBIGUITY_WITHHOLDING.json` |
| fail-closed unknown capability | unknown adapter / unsupported probe | `CAPABILITY_FAILURE` | missing representation is typed rather than improvised | `LM_ZW_CAP_SLICE_004_AMBIGUITY_WITHHOLDING.json` |
| bounded Language Math | `prove x plus 0 equals x` | `PASS` | accepted bounded mathematical-language form is handled deterministically | `LM_ZW_CAP_SLICE_012_MATHEMATICAL_LANGUAGE.json` |
| Language Math withholding | `prove 2 + 2 equals 4` through unsupported symbolic surface | `WITHHOLD` | unsupported representation is withheld with `MISSING_REPRESENTATION` | `LM_ZW_CAP_SLICE_012_MATHEMATICAL_LANGUAGE.json` |
| whole-path composition | lexical → sense → syntax → semantic composition → context → Language Math | `PASS` | accepted stages compose through the deterministic whole path | `LM_ZW_WHOLE_PATH_COMPOSITIONAL_EVAL_001.json` |
| whole-path failure frontier | valid early stages + invalid syntax | `WITHHOLD` | processing stops at the typed syntax frontier rather than fabricating later results | `LM_ZW_WHOLE_PATH_COMPOSITIONAL_EVAL_001.json` |

## What the examples demonstrate

### Composition is explicit

The accepted syntax/composition fixture distinguishes grammatical composition, retained ambiguity, typed withholding, unsupported locale behavior, and unsupported probe behavior. The system does not collapse all inputs into a generic “answer”; it carries a typed disposition through deterministic computation.

### Context and reference are computational inputs

The accepted reference/context fixture demonstrates that the same surface form can have different dispositions when the governed context changes. It also preserves multiple reference candidates when resolution is ambiguous and withholds when required reference support is absent.

### Ambiguity is retained when the system cannot lawfully collapse it

The accepted ambiguity/withholding fixture composes multiple language capabilities and explicitly demonstrates precedence among `PASS`, `RETAIN_AMBIGUITY`, `WITHHOLD`, and `CAPABILITY_FAILURE`. A passing child does not erase a required withholding condition, and ambiguity remains visible when that is the correct deterministic result.

### Language Math proves only within its represented language

The accepted mathematical-language fixture includes successful bounded proof forms such as `prove x plus 0 equals x`, reflexive order, and symmetry from an explicit assumption. It also demonstrates withheld results for unsupported free-language, symbolic, question-form, missing-relation, evidence-ineligible, and multi-goal inputs. This is deterministic proof/withholding behavior, not probabilistic completion.

### The whole path preserves a failure frontier

The accepted whole-path fixture composes lexical identity, sense, syntax, semantic composition, context/reference, and deterministic mathematical language. It records where evaluation stops when ambiguity, missing composition, missing reference resolution, missing mathematical representation, or a typed capability failure is encountered.

## Deterministic replay, round-trip, and service equivalence

The accepted public qualification index records explicit qualification coverage for:

- exact canonical identity replay;
- deterministic aggregate replay and case-order invariance;
- pairwise semantic equivalence;
- verified round-trip preservation and corruption rejection;
- canonical state ordering and provenance preservation;
- cross-caller semantic conformance;
- failure-frontier custody;
- deterministic direct-engine/component-service equivalence;
- HTTP-boundary equivalence to the component response; and
- typed fail-closed HTTP behavior for missing identity or untyped qualification dispositions.

These qualification dimensions complement the exact fixture examples above: the fixtures provide inspectable inputs and expected dispositions, while the qualification index exposes the accepted replay, preservation, transport-equivalence, and failure-handling dimensions used to qualify the deterministic component.

## Public evidence route

- [Language Model component record](README.md)
- [Public Test Snapshot v1](evidence/public-test-snapshot-v1/README.md)
- [Qualification Test Index](evidence/public-test-snapshot-v1/QUALIFICATION_TEST_INDEX_2026-08-24.md)
- [Exact public fixtures](evidence/public-test-snapshot-v1/actual-tests/)

The public snapshot contains **seven exact fixture artifacts covering 62 cases**. This demonstration is a reader-oriented projection of those accepted capabilities; it does not publish private repository names, private commits, private paths, internal control identifiers, or development choreography.
