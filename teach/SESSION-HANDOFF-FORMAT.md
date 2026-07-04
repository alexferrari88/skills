# SESSION-HANDOFF.md Format

`SESSION-HANDOFF.md` lives at the workspace root. It is overwritten at concept boundaries to make the next session restart cleanly.

It is not a learning record. It is a compact operational handoff.

## Template

````md
# Session Handoff: {topic}

## Where we are
{One short paragraph summarizing the current lesson state and workspace context.}

## Last completed concept
{Concept or skill just completed, or "none" if still in diagnosis.}

## Last verified learning
{Evidence-backed claim only. Include learning record ID if available. If not tested, say so.}

## Open uncertainty
- {Untested claim, unresolved misconception, or missing prerequisite}

## Next concept
{The next narrow concept or practice target.}

## Next session start
Ask one attempt-first question about:
{Specific retrieval, transfer, or diagnostic prompt.}

## Copy-paste restart prompt
```text
Continue my learning session from {workspace-path}.
Use the teach skill.
Read MISSION.md, LEARNER-PROFILE.md if present, OBJECTIVES.md if present, GLOSSARY.md, the latest learning-records, reviews, and SESSION-HANDOFF.md.
Last completed concept: {concept}.
Last verified learning: {evidence}.
Next concept: {next concept}.
Continue in learning-by-doing mode: diagnose briefly, then ask one attempt-first question.
```
````

## Rules

- Overwrite this file at natural boundaries rather than appending long history.
- Keep it short enough to scan in under one minute.
- Do not claim learning that lacks evidence.
- If the next move is a review, specify the exact review prompt or review file.
