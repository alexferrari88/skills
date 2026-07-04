# Research-lead domain tutoring pattern

Use when the learner wants to direct agents/code in a technical domain without becoming the implementer.

## Pattern

1. Teach the decision loop, not the implementation API.
2. Start from a concrete report/result the learner must judge.
3. Ask for a scale / hold / kill / investigate decision before explaining.
4. Turn every objection into the next experiment instruction:
   - If performance is unstable: ask where/when it breaks and compared with what.
   - If the signal may be redundant: ask for a variation that changes a plausible signal source, then test whether performance survives.
   - If novelty destroys validation: mark it as differently wrong, not additive.
5. Record learning only after an observed choice, corrected misconception, or transfer result.
6. At boundaries, persist a handoff with: last completed concept, last verified learning, next concept, and one restart prompt.

## Tutor phrasing

Prefer short research-lead rules:

- "Attack the actual objection."
- "Uniqueness is useful only if validation survives."
- "Average score says whether there may be signal; era pattern says where it breaks; similarity says whether it is redundant."

## Pitfalls

- Do not drift into coding instruction when the mission is judgement/directing work.
- Do not reward novelty by itself; require survival under validation.
- Do not treat a positive average as scale-ready if the failure anatomy is still unknown.
- Do not continue with a full explanation when the user requested one attempt-first question; keep the loop small.
