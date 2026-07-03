# Artifact Lesson Format

Use this for reusable HTML lessons or reference artifacts. Artifact mode is justified only when the artifact improves practice, feedback, transfer, simulation, or later reference.

## Gate

Create an artifact only if at least one is true:

- the learner will revisit it;
- diagrams or layout reduce cognitive load;
- in-browser interaction gives immediate feedback;
- the concept benefits from simulation/manipulation;
- the artifact is part of a multi-session programme;
- the artifact compresses a lesson into a durable reference.

Do not create a static essay and call it a lesson.

## Required structure

```md
# {Lesson title}

## Objective
One observable skill.

## Prerequisite check
1-3 questions or a tiny task.

## Micro-explanation
Short, concrete, source-backed when factual.

## Worked example
Annotated example with principle labels.

## Your turn: completion problem
Learner fills in a missing step.

## Feedback / answer reveal
Revealable, adjacent to the task. Include why, not just answer.

## Independent attempt
Same structure, less support.

## Transfer challenge
Different surface form; same underlying principle.

## Review prompts
2-5 no-notes retrieval prompts.

## Quick reference
Compressed checklist, formula, glossary, or decision rule.

## Sources
Citations for factual claims.
```

## Interaction rules

Every interactive element must have a learning job:

```text
retrieval
feedback
self-explanation
scaffold fading
simulation/manipulation
transfer
misconception repair
calibration
```

Remove interactions that only decorate.

## HTML design rules

- One objective per page.
- Segment content into short sections.
- Keep related labels, controls, visuals, and feedback close together.
- Use revealable hints before answer reveal.
- Keep styling quiet and readable.
- Avoid seductive details: decorative animation, avatars, gamified chrome, irrelevant examples, or generated side content.
- Include print-friendly reference sections when useful.

## Feedback contract

Each question/task should return:

- correctness;
- why;
- likely misconception;
- next action;
- retry or variant.

## File naming

Save lessons under `./lessons/` as:

```text
0001-dash-case-title.html
0002-dash-case-title.html
```

Scan the directory for the highest existing number and increment.

## Verification

Before calling an artifact done:

- open or inspect the generated file;
- confirm all local links work;
- confirm each task has an answer or rubric;
- confirm factual claims have sources;
- confirm the lesson includes retrieval, feedback, and transfer.
