# LEARNER-PROFILE.md Format

`LEARNER-PROFILE.md` lives at the workspace root. It is the evidence-backed learner model for this topic, not a transcript summary or biography.

Create it lazily when a multi-session workspace needs continuity.

## Template

```md
# Learner Profile: {topic}

## Background
- {Explicitly stated prior experience, adjacent knowledge, or constraints.}

## Observed strengths
- {Strength} — Evidence: {learning record, observed answer, transfer result, or explicit user statement}

## Recurring gaps
- {Gap} — Evidence: {learning record or repeated observed difficulty}

## Misconceptions to watch
- {Misconception} — Status: active | repaired | uncertain — Evidence: {record or observed exchange}

## Calibration
- {Pattern in confidence vs correctness, if observed. Leave blank or say "not enough evidence" if untested.}

## Effective scaffolds
- {MCQ + confidence, worked example, analogy, code-first, visual diagram, etc.} — Evidence: {what happened}

## Do not assume
- {Things not yet tested, even if they were explained.}
```

## Rules

- Keep topic-local learning state here; use Hermes memory only for stable cross-topic preferences.
- Separate explicit user statements from observed performance.
- Do not write claims like "understands X" unless the learner passed a retrieval, retry, transfer, or self-explanation check.
- A single mistake is not a recurring gap until it persists after feedback or appears in a transfer case.
- Prefer `uncertain` / `not enough evidence` over overconfident learner modeling.
- When a later record repairs a gap, update the status instead of deleting history.
