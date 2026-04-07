---
name: hermes-deep-research
description: Hermes-native deep research protocol for multi-source synthesis, verification, parallel subresearch, and decision-grade reporting using web_search, web_extract, browser fallback, delegate_task, and Python-backed scoring.
version: 0.2.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [research, deep-research, due-diligence, synthesis, verification, citations, scouting]
    related_skills: [writing-plans, systematic-debugging, subagent-driven-development]
    strengths: [tool-routing, evidence-ledger, uncertainty-handling, parallelization, report-packaging]
---

# Hermes Deep Research

## Overview

This skill is Hermes Agent's native protocol for producing **decision-grade research**, not just long answers.

It combines:
- multi-angle discovery
- full-source reading for important claims
- explicit contradiction handling
- Python-backed ranking and scoring
- parallel subresearch when the topic is broad
- report packaging matched to the user's real decision context

**Core principle:** deep research is complete only when the question is answered, the evidence is triangulated, uncertainty is explicit, and the output is usable.

## The Five Non-Negotiables

```text
1. Never answer a deep-research request from memory alone.
2. Search from multiple angles before synthesizing.
3. Read key sources in full; do not rely on snippets for important claims.
4. Use Python for arithmetic, ranking, scoring, and weighted comparisons.
5. Separate fact, synthesis, inference, and speculation.
```

If any of these are violated, the research is incomplete.

## When to Use

Use this skill when the user asks for:
- deep research
- comprehensive analysis
- state of the art / landscape review
- compare X vs Y
- due diligence on a company, tool, model, framework, or repository
- current state of a topic requiring multi-source synthesis
- research that should end in a recommendation, memo, or evidence-backed report

### Do NOT use for
- simple factual lookups
- one-source questions
- lightweight Q&A answerable with one or two searches
- routine debugging unless the primary work is external research
- requests where the user explicitly wants a fast rough answer instead of depth

If the task is simple, use normal lookup flow instead.

## Defaults

If the user does not specify otherwise:

```text
Mode: Standard
Deliverable: Deep Research Report
Time horizon: recent 12-24 months unless the topic is historical
Audience: technically literate decision-maker
```

If the user says "just research it," infer reasonable defaults and proceed.

When clarification materially helps, ask bounded-choice questions rather than open-ended ones.

## Modes and Deliverables

```text
Modes
- Scout    : 3-5 high-signal sources; fast orientation
- Standard : 8-15 sources; default decision support
- Deep     : 15-30 sources; broader triangulation + critique
- Forensic : 20-40+ sources or concentrated primary-source review; adversarial validation

Deliverables
- Deep Research Report      : broad topic / landscape / state-of-the-art
- Decision Memo             : choose / avoid / defer / prioritize
- GitHub / OSS Due Diligence: repo, framework, tool, maintainer-risk review
- Scout Brief               : compressed chat-native output
```

Choose the lightest mode that still answers the question.

## Execution Protocol

Progress through these phases in order. Do not jump to synthesis before evidence is sufficient.

```text
0. Frame the task
1. Build the research map
2. Broad exploration
3. Source selection
4. Deep extraction
5. Parallel specialist passes
6. Evidence ledger
7. Synthesis
8. Critique and refine
9. Package for the user
```

### Phase 0: Frame the task
Define:
- the exact question
- the decision or use-case behind it
- the mode
- the deliverable
- the relevant time horizon
- whether the task is general, technical, market, or GitHub/OSS-focused

### Phase 1: Build the research map
Break the problem into:
- core question
- 3-5 subquestions
- evidence types needed
- likely source classes
- likely counterarguments / failure modes

### Phase 2-9
Load the relevant reference files below and follow them.

## Reference File Map

Load these references as needed during execution:

```text
references/operating-system.md
- Detailed phase instructions for framing, mapping, synthesis, critique, and packaging

references/tool-routing.md
- Exact rules for when to use web_search, web_extract, browser tools, delegate_task, execute_code, file tools, and session_search

references/evidence-ledger.md
- Internal claim-tracking structure, confidence handling, and comparison/scoring rules

references/research-patterns.md
- Topic-specific checklists for comparisons, vendor diligence, GitHub/OSS work, and market/landscape analysis

references/confidence-and-citations.md
- Confidence architecture, attribution rules, inline-link behavior, and scout-output rules
```

## Templates

Choose the best-fit template and adapt it to the task:

```text
templates/deep-research-report.md
templates/decision-memo.md
templates/oss-due-diligence.md
templates/scout-brief.md
templates/subagent-brief.md
```

## Quality Gates

Do not finalize until all applicable checks pass.

```text
[ ] The user's actual question is answered directly
[ ] At least 3 meaningful angles were explored when the task warranted depth
[ ] Key sources were read in full, not inferred from snippets alone
[ ] Major claims have citations or explicit attribution
[ ] Contradictions and uncertainty are visible
[ ] Fact vs synthesis vs inference are not blurred
[ ] Arithmetic, ranking, or scoring was done in Python
[ ] Recommendation is tied to evidence, not vibe
[ ] Output format matches the user's real decision context
[ ] The final answer leads with the conclusion, not the work log
```

If a gate fails, continue researching or revise the output.

## Failure and Fallback Rules

If the first search pass is weak:
- broaden keyword phrasing
- search official sources separately
- search skeptical / critical framing explicitly
- add date qualifiers when recency matters

If extraction fails:
- escalate to browser tools
- inspect page state / console if content should be present but is not

If evidence remains thin:
- say so directly
- downgrade confidence
- narrow the claim
- recommend what additional evidence is needed

Do not pad thin research into fake confidence.

## Anti-Patterns

Do NOT:
- answer from prior knowledge without fresh research
- stop after one search query
- cite only vendor marketing when independent evidence is available
- use snippets as if they were full evidence
- present a recommendation without showing tradeoffs
- hide conflicting evidence
- perform arithmetic in prose
- dump an unstructured pile of notes instead of a usable conclusion

**Deep research is not long output. Deep research is disciplined evidence synthesis.**
