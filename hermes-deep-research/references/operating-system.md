# Operating System

Use this file for the detailed execution flow behind `hermes-deep-research`.

## Phase 0 — Frame the Task

Before searching, define all of the following:
- exact question
- decision or use-case behind the question
- mode
- deliverable type
- time horizon
- topic type: general, technical, market, vendor, or GitHub/OSS

If ambiguity materially changes the answer, ask a bounded-choice clarification.
Otherwise, infer defaults and proceed.

## Phase 1 — Build the Research Map

Break the task into:
- core question
- 3-5 subquestions
- evidence types needed
- likely best source classes
- likely counterarguments or failure modes

Typical evidence classes:
- primary documentation
- official company / vendor material
- academic or institutional research
- regulator / standards material
- reputable news
- expert technical commentary
- practitioner case studies
- community signal
- benchmark, usage, price, or adoption data

## Phase 2 — Broad Exploration

Start with `web_search` to map the territory.

Search from at least 3 angles where relevant:
- official / primary sources
- independent analysis / news
- skeptical / critical / opposing views
- recent developments
- comparisons / alternatives
- implementation evidence / case studies

Do not stop after the first decent result set.

## Phase 3 — Source Selection

Promote only high-value URLs into the read queue.

Default source priority:
1. official docs / repo / company / filings / standards
2. peer-reviewed or institutional research
3. reputable trade press / major journalism
4. expert technical blogs / practitioner writeups
5. community discussions and social signal

For every major subquestion, identify at least one primary or near-primary source if possible.

## Phase 4 — Deep Extraction

Read high-value sources in full.

Rules:
- do not synthesize important claims from snippets alone
- follow upstream references when a stronger source is cited
- use browser tools if extraction is partial, JS-heavy, blocked, or visually dependent
- if one source makes an important claim, seek corroboration before elevating it

## Phase 5 — Parallel Specialist Passes

Use `delegate_task` when:
- the topic has 3+ separable dimensions
- the mode is Deep or Forensic
- a skeptic/counterargument pass would materially improve quality

Recommended split:
- Specialist A: strongest case / primary thesis
- Specialist B: counter-thesis / weaknesses / risks
- Specialist C: data, chronology, benchmarks, or technical validation

For technical or market-heavy work, split by domain instead:
- architecture / mechanism
- adoption / market / business
- risk / criticism / fragility

The main session owns final synthesis.

## Phase 6 — Evidence Ledger

Before drafting, record an internal ledger of major claims.
Use `references/evidence-ledger.md`.

Minimum fields:
- claim
- source URL
- source type
- publication/update date if relevant
- corroboration count
- confidence level
- classification: fact / synthesis / inference / speculation

## Phase 7 — Synthesis

Only synthesize once the evidence ledger is sufficient.

The synthesis must answer:
- What is well-supported?
- What is plausible but not proven?
- What do sources disagree about?
- What matters most for the user's decision?
- What remains unknown?

## Phase 8 — Critique and Refine

Run a deliberate skeptic pass.

Ask:
- Which conclusions rest on thin evidence?
- Which claims depend on vendor framing?
- Where could recency distort the conclusion?
- What would a strong critic say?
- What evidence would change the answer?

Revise after the skeptic pass.

## Phase 9 — Package for the User

Choose the best-fit template.

Do not dump raw notes.
Deliver a decision-grade artifact with:
- direct answer first
- evidence-backed reasoning
- clear uncertainty handling
- actionable bottom line

## Packaging Rule

Lead with the answer, not the work log.
