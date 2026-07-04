# Numerai research-lead tutoring pattern

Use when continuing Alex's Numerai Classic learning workspace or teaching model-evaluation intuition as a research lead rather than an implementer.

## Durable learner fit

- Teach intuition and decision gates, not Python implementation.
- Use concrete research-lead choices: scale / hold / kill / revise / ask the agent for a specific check.
- Prefer ADHD-friendly multiple-choice prompts with explicit confidence 0-100.
- Keep each turn to one narrow attempt-first question; give feedback only after the learner answers.
- Record learning evidence only when the learner chooses, explains, calibrates, transfers, or exposes a misconception.

## Effective loop from the session

1. Diagnose from workspace state and previous records.
2. Ask one attempt-first multiple-choice question.
3. On answer, give verdict first and one compact rule.
4. If the answer is evidence of learning, write a dated learning record immediately.
5. Progress by transfer cases, not explanation dumps.
6. At a boundary, update `SESSION-HANDOFF.md` with last completed concept, verified learning, and next concept.

## Concept sequence that worked

- Stable positive baseline is not automatically scale-ready when highly benchmark-like.
- Next experiment should attack the actual objection: try a variation designed to be less benchmark-like, then test whether validation survives.
- Uniqueness alone is not enough: a lower-similarity model with negative or weak recent validation is not useful.
- A promising but noisy variation should be held/investigated, not scaled.
- Good agent briefs follow: objection -> targeted change -> checks to rerun -> decision gate.
- BMC can be introduced after this intuition as: after removing benchmark-like behavior, is useful contribution left?
- Prevent the next misconception: positive BMC is one gate, not a magic override for poor recent-era stability or ugly drawdowns.

## Good prompt shape

```text
<short diagnosis / where we are>

Attempt:
<concrete Numerai result card>

What is the best decision / agent instruction?

A. plausible trap
B. correct gate-aware choice
C. opposite trap
D. tempting shortcut

Reply with A/B/C/D + confidence 0-100.
```

## Feedback shape

- `Correct — B.` or `Not quite — the trap is...`
- One compact rule.
- One transfer question.
- Avoid broad theory until the learner has made the next decision.
