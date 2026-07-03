# Lesson Contract

Use this before a chat lesson, HTML artifact, or generative UI lesson. Keep it short. The contract exists to prevent vague explanations and ensure the lesson has practice, feedback, transfer, and review.

## Template

```md
# Lesson Contract: {title}

## Mission link
{Why this matters to the user's real goal. Link to MISSION.md if available.}

## Target skill
By the end, the learner can: {observable action}.

## Prerequisite check
Ask or infer:
- {question/check 1}
- {question/check 2}

## Likely misconception
{The wrong mental model or common trap to test for.}

## Success test
The learner succeeds if they can: {specific task, not "understand X"}.

## Teaching move
Choose one:
- direct micro-explanation
- worked example
- guided discovery
- misconception contrast
- simulation/manipulation
- drill with feedback

## Practice sequence
1. Worked example: {what will be modelled}
2. Completion problem: {what learner fills in}
3. Independent attempt: {what learner does without reveal}
4. Transfer case: {new surface form}

## Feedback plan
When the learner answers, respond with:
- correctness
- why
- misconception if present
- next action
- retry variant

## Review prompts
Create 2-5 prompts for future retrieval:
- {prompt 1}
- {prompt 2}
- {prompt 3}
```

## Rules

- One lesson, one target skill.
- Make the success test observable.
- Do not plan more explanation than the first attempt needs.
- Use multiple choice only when discrimination is the learning goal; otherwise prefer recall/short answer.
- Transfer must change surface features while preserving the underlying structure.
- If the user only wants a direct answer, skip this contract and label direct-answer mode.
