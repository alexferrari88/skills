# Learning Record Format

Learning records live in `./learning-records/` and use sequential numbering: `0001-slug.md`, `0002-slug.md`, etc. Create the directory lazily.

A learning record is **evidence of learning**, not a session log. Write one only when the learner demonstrates understanding, corrects a misconception, passes/fails transfer, or exposes a blocker that should steer future teaching.

## Template

```md
---
status: active
---

# Learning Record {NNNN}: {short title}

## Target skill
{Observable skill or concept the learner was working toward.}

## Prior state
{Known prior knowledge, confidence, misconception, or uncertainty before the lesson.}

## Evidence observed
{What the learner actually did: answer, explanation, solved step, transfer attempt, error pattern, or explicit blocker. Quote or summarize the evidence.}

## Feedback given
{Specific correction, principle, or next action given to the learner.}

## Transfer status
{passed | partial | failed | not tested}

{If tested: describe the transfer case and result. If not tested: state why it was deferred.}

## Review prompts
- {future retrieval prompt 1}
- {future retrieval prompt 2}
- {future retrieval prompt 3}

## Next teaching move
{What to teach or review next, and why.}
```

## Numbering

Scan `./learning-records/` for the highest existing number and increment by one.

## When to write one

Write a record when any of these is true:

1. The learner demonstrated a non-trivial skill or concept.
2. The learner corrected a misconception.
3. The learner failed or partially passed a transfer task.
4. The learner disclosed prior knowledge that changes what should be taught next.
5. The mission shifted because of learning.
6. A blocker emerged that predicts future difficulty.

## What does not qualify

Do not record:

- material merely covered;
- passive reading;
- generic session summaries;
- praise;
- untested claims of mastery;
- definitions that belong in `GLOSSARY.md`;
- temporary task progress.

## Evidence standard

Prefer concrete evidence:

```text
Weak: "We covered spaced repetition."
Better: "Learner correctly explained why massed rereading feels fluent but retains poorly, then designed a 3-prompt review schedule."
```

## Supersession

When a later record contradicts or deepens an earlier one, mark the old record:

```yaml
status: superseded by LR-NNNN
```

Do not delete learning history unless the user asks.
