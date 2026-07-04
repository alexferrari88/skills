# Domain-intuition generative UI workspaces

Use when the learner wants intuition for a technical/domain challenge but does not want programming instruction because agents will write the code.

## Pattern

1. Create a separate learning workspace at the user-specified path when given; otherwise prefer a user-level location such as `~/learning-workspace/<topic>`. Do not mix learning artifacts into the source repo unless explicitly requested:
   - `MISSION.md` — learner goal and constraints.
   - `RESOURCES.md` — grounded docs, local repo files, notebooks, books, and source URLs checked.
   - `GLOSSARY.md` — canonical terms the learner needs for decision-making.
   - `GENUI-CONTRACT-*.md` — why UI beats chat, answer keys/rubrics, hint ladder, transfer and no-AI checkpoint.
   - `reviews/*.md` — spaced retrieval prompts.
   - `lessons/*.html` — self-contained interactive lessons.
2. Inspect the repo/notebooks/docs enough to identify the real decision loop and common traps. Teach the decision loop, not the implementation syntax.
3. If the user has books or long PDFs, map chapters/sections to the curriculum without loading whole books into context.
4. Before building or assigning the first UI, ask 1–3 chat-side diagnostic/retrieval questions and define the success test. Then build the UI around one narrow judgment skill: diagnose → attempt → hint → feedback → retry/transfer → no-AI checkpoint → export evidence.
5. Do not record learning until the learner returns observed evidence from the UI or chat attempt.

## Good first lesson shape

- Diagnostic misconception questions with fixed answer keys.
- A toy simulator clearly labelled as toy data when it teaches a dynamic tradeoff.
- Transfer cases with decisions like `scale`, `hold`, `kill`, or `scout again`.
- A no-AI checkpoint that asks for the learner's own objection/diagnosis.
- A copy/export button that returns a learning packet for feedback.

## Pitfalls

- Do not teach Python/programming when the user's goal is domain intuition and agent direction.
- Do not make a polished static explainer and call it generative UI. The UI must adapt feedback/hints or simulate an invisible system.
- Do not claim the toy simulator shows real results unless it is actually backed by real experiment data.
- Do not create learning records for coverage alone; require evidence of learner performance.
