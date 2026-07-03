# Generative UI Lesson Format

Generative UI is not the default. Use it only when it beats chat or static HTML for learning.

## Gate

Build or recommend generative UI only if it does at least one of these better than chat:

- adapts hints to the learner's actual response;
- gives misconception-specific feedback;
- generates verified practice variants;
- makes an invisible or dynamic system manipulable;
- supports stateful debugging, classification, graph, math, or simulation tasks;
- gives a human tutor better real-time coaching suggestions.

Do not use generative UI for novelty, decoration, or linear exposition.

## Required contract

```md
# Generative UI Contract: {title}

## Learning job
{retrieval | feedback | simulation | scaffold fading | transfer | misconception repair | calibration}

## Why chat is insufficient
{Specific reason. If this is weak, do not build UI.}

## Learner action
{What observable action the learner takes.}

## Feedback mechanism
{How correctness/quality is judged. Include answer key, rubric, or checked solution trace.}

## Hint ladder
1. orienting question
2. attention cue
3. principle hint
4. partial step
5. worked step
6. full solution after attempt

## Transfer mechanism
{How the UI tests a new case rather than the exact practiced case.}

## Grounding
{Sources, answer keys, tests, or validation checks used to prevent fabricated feedback.}

## No-AI checkpoint
{A short independent task the learner completes without generative help.}
```

## Design rules

- The UI path remains structured; learner control is local: next, retry, reveal hint, reveal answer.
- Do not give arbitrary open-ended exploration to novices.
- Put feedback next to the learner's action.
- Make the model stop short of full answer until the learner attempts.
- Store enough state to know attempts, hints used, confidence, and errors.
- Prefer generated practice from templates with answer keys over unconstrained generation.

## Rejection rules

Reject or downgrade to chat/static HTML when:

- no answer key or rubric exists;
- the interaction does not change based on learner input;
- the UI mainly makes the lesson prettier;
- the learner can bypass thinking more easily than practise thinking;
- the domain is high stakes and no qualified human will review;
- the task is a stable reference sheet or one worked example.

## Minimal viable implementation

Before building a full app, test the learning loop in chat:

```text
diagnose → attempt → hint ladder → feedback → retry → transfer
```

Build UI only after that loop proves useful.
