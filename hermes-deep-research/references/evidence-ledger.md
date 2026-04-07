# Evidence Ledger

Use this internal structure before final synthesis.

## Purpose

The ledger prevents vague synthesis and overconfident conclusions.
It can remain internal unless the user asks for it, but it must be used.

## Minimum Schema

```text
Claim:
Source URL:
Source type:
Source date / last updated:
Supports / contradicts:
Corroboration count:
Confidence: High / Medium / Low / Speculative
Classification: Fact / Synthesis / Inference / Speculation
Notes:
```

## Rules

- If a major claim has only one supporting source, label it fragile or lightly supported.
- If sources conflict, record the conflict explicitly.
- Distinguish what a source states from what you infer.
- Prefer direct upstream sources over repeated commentary about those sources.
- When comparing options, record the evidence for each criterion separately.

## Comparison / Scoring Rule

If the task requires ranking or weighted comparison:
- define criteria explicitly
- assign weights explicitly
- compute the result in Python
- explain sensitivity if small weight changes would change the ranking

## Confidence Architecture

```text
High confidence
- backed by primary sources or multiple independent reliable sources

Medium confidence
- backed by reputable secondary sources with partial triangulation

Low confidence
- sparse evidence, weak corroboration, or unclear recency

Speculative
- reasoned inference, scenario analysis, or emerging signal not yet verified
```

Never present speculative conclusions as settled facts.

## Minimal Internal Table Example

```text
Claim                                  | Evidence type | Corroboration | Confidence | Classification
X has strong enterprise adoption        | vendor + 2 independent reports | 3 | Medium | Synthesis
Y benchmark lead is vendor-only         | vendor blog only               | 1 | Low    | Fact (fragile)
Z likely wins in low-cost deployments   | benchmark + pricing + inference| 2 | Medium | Inference
```
