# Review Prompt Format

Review prompts live in `./reviews/` and support spaced retrieval. They are deliberately lightweight markdown; do not build a scheduler until repeated use proves it is needed.

## File naming

Use one file per topic or lesson:

```text
reviews/0001-dash-case-topic.md
```

## Template

```md
# Review: {topic}

## Source
- Lesson: {lesson file or chat date}
- Learning record: {LR-NNNN if available}

## Target skill
{What the learner should retrieve or do without notes.}

## Prompts

### Prompt 1
Question: {no-notes retrieval question}
Expected answer / rubric: {short answer or criteria}
Due: {next session | +1 day | +3 days | +7 days | custom}
Last result: {untested | passed | partial | failed}
Confidence: {optional}

### Prompt 2
Question: {near-transfer or contrast question}
Expected answer / rubric: {short answer or criteria}
Due: {next session | +1 day | +3 days | +7 days | custom}
Last result: {untested | passed | partial | failed}
Confidence: {optional}

### Prompt 3
Question: {farther transfer or misconception check}
Expected answer / rubric: {short answer or criteria}
Due: {next session | +1 day | +3 days | +7 days | custom}
Last result: {untested | passed | partial | failed}
Confidence: {optional}

## Next review decision
{What to do after the next attempt: increase spacing, reteach, interleave, or retire.}
```

## Rules

- Prompts should require recall, explanation, discrimination, or transfer.
- Avoid recognition-only multiple choice unless discrimination is the target.
- Keep each prompt short enough to use at the start of a session.
- If the learner fails, give feedback and schedule a closer retry.
- If the learner passes twice with good confidence calibration, increase spacing or retire.

## Session start behaviour

When using this skill in a workspace with `reviews/`, begin with 1-3 due review prompts before new teaching. Do not overload the session with every review file.
