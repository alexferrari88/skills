# high-efficiency-learning-design

A production-oriented Agent Skill derived from **Justin Skycak's _The Math Academy Way: Using the Power of Science to Supercharge Student Learning_**, first-edition working draft updated 17 August 2026.

## Capability

The skill makes an agent better at **designing, auditing, and diagnosing high-efficiency mastery-based learning in hierarchical skill domains**. It turns the book's ideas into decisions about prerequisite sequencing, worked examples, deliberate practice, cognitive load, baseline mastery, automaticity, spacing, interleaving, retrieval, diagnostics, remediation, task selection, and learning incentives.

This is intentionally not a “Math Academy knowledge” or book-summary skill. The activation scope is the class of problems for which the book offers a distinctive method: deciding what a learner should practice next, why learning is failing, how to build durable mastery, or how to design an adaptive learning system.

## Why this is one skill

The book's strongest ideas are tightly coupled. Mastery learning determines what may be learned next; cognitive load determines the size of the step; deliberate practice determines the task form; spacing/interleaving/retrieval determine retention; diagnostics and remediation repair failures; and adaptive-system logic coordinates all of them. Splitting these into separate skills would often force multiple skills to activate for one learning-design decision and would hide important interactions.

The product-specific technical material is therefore isolated through progressive disclosure in `references/adaptive-systems.md` rather than made into a separate skill.

## Included deliberately

The skill retains the book's operationally distinctive ideas, especially:

- optimize durable independent performance per unit focused effort rather than immediate fluency;
- distinguish desirable difficulty from cognitive overload and needless struggle;
- use active, guided practice for novices rather than equating active learning with discovery or group work;
- treat deliberate practice as high-volume action-feedback-adjustment cycles at the edge of reliable performance;
- use a prerequisite graph / knowledge frontier to choose the next learnable skill;
- advance at baseline mastery while developing automaticity longitudinally through layering and review;
- separate confusable concepts during fragile acquisition, then interleave them later to train discrimination;
- space retrieval so memory is effortful but recoverable rather than keeping everything continuously fresh;
- diagnose struggle before attributing it to ability;
- use targeted remediation at the exact point of failure without lowering the final mastery bar;
- distinguish learner failure from content failure when many prepared learners break at the same step;
- adapt practice amount, granularity, and review to observed performance rather than “learning styles”;
- count advanced practice as implicit review only when it genuinely exercises the prerequisite;
- align gamification and accountability with actual learning and close obvious gaming loopholes.

## Excluded deliberately

The skill omits or strongly de-emphasizes material that does not improve agent decisions:

- long historical narratives, quotations, and literature “receipts”;
- company marketing, pricing, competitor comparisons, and the book's 4x-learning claim;
- polemical sections about institutions or educational ideologies except where they yield a portable design rule;
- platform-specific XP numbers, pass-rate benchmarks, and exact anti-gaming thresholds;
- anecdotes that illustrate a point already captured by a general rule;
- claims about innate talent as a basis for labeling individuals. The operational rule retained is narrower: do not infer inability before fixing foundations, practice design, dose, and adherence, and judge continued investment by observed learning rate and opportunity cost;
- unfinished “Notes for Future Additions” as if they were established recommendations.

## Interpretive decisions

Some rules are syntheses rather than verbatim methods from the book. `references/source-map.md` marks these as **Derived interpretation**. The most important are:

1. The ordered bottleneck diagnostic in `SKILL.md` combines separate chapters on missing foundations, cognitive load, practice behavior, insufficient practice, motivation, and learning-rate limits.
2. “Separate confusable concepts during initial acquisition, then interleave them after baseline mastery” reconciles the non-interference chapter with the interleaving chapter and FAQ guidance that initial blocked practice is appropriate.
3. For real-world acceleration decisions, the skill treats prerequisite mastery as the content-readiness criterion but does not pretend it resolves external logistics, institutional policy, or the learner's broader goals.
4. The technical HSRS/FIRe material is represented as a source-specific architecture, not an executable clone. The book does not provide enough complete, implementation-level mathematics to reconstruct Math Academy's production algorithms reliably.

## Source maturity

The source itself is a working draft. Chapters 11 and 24–28 contain explicit “in progress” markers, and the final notes say substantial material remains to be written. The core skill therefore relies most heavily on the completed chapters about active learning, deliberate practice, mastery, cognitive load, automaticity, layering, non-interference, spaced repetition, interleaving, retrieval, remediation, gamification, diagnostics, and learning efficiency. Coaching/habit material is quarantined in a reference with a provisional warning.

## Directory structure

```text
high-efficiency-learning-design/
├── SKILL.md
├── README.md
├── references/
│   ├── practice-design.md
│   ├── sequencing-and-retention.md
│   ├── diagnostics-and-remediation.md
│   ├── adaptive-systems.md
│   ├── coaching-and-adherence.md
│   └── source-map.md
└── evals/
    ├── README.md
    ├── evals.json
    └── eval_queries.json
```

No `scripts/` directory is included. The deterministic-looking parts of the book are either simple enough to express as decision rules or too product-specific/incompletely specified to implement honestly. A scoring script would create false precision rather than reliability.

No `assets/` directory is included because the skill has no recurring static artifact or template that improves execution.

## Example prompts that should benefit

- “My student can do each algebra worksheet right after the lesson but fails cumulative tests. Redesign the practice.”
- “I’m building an adaptive calculus tutor. How should it decide what topic a learner sees next?”
- “I keep getting stuck in calculus even though I understand the lectures. Diagnose what I should change.”
- “Design a six-month study plan that gets me from rusty algebra to calculus and keeps old material from decaying.”
- “Review this course: each unit has a lecture, 30 same-type problems, and a test, then the topic never appears again.”
- “My child is fast at new lessons but makes lots of basic arithmetic mistakes. Should we keep accelerating?”

A prompt such as “Explain the quadratic formula” should **not** activate this skill unless the user also asks how to teach, practice, sequence, retain, or diagnose learning of it.

## Evaluation

`evals/evals.json` follows the official Agent Skills evaluation format: realistic prompts, a human-readable success definition, optional files (none are needed here), and objective assertions where useful.

Run each case twice in clean contexts: once with the skill and once without it (or against a previous skill version). Grade the assertions and inspect the outputs manually. The most valuable deltas are cases where a generic model would recommend more explanations, more blocked practice, generic “learning styles,” or indiscriminate challenge problems while the skill instead diagnoses prerequisites, retrieval, task granularity, or practice-stage mismatches.

`evals/eval_queries.json` contains 20 activation tests: 10 should-trigger and 10 adjacent should-not-trigger prompts. Run each several times because triggering is nondeterministic; the official guidance suggests three runs as a reasonable starting point and a 0.5 trigger-rate threshold.

## Validation

Validate the directory with the current reference validator:

```bash
skills-ref validate ./high-efficiency-learning-design
```

Also check that `SKILL.md` remains comfortably under the specification's recommended 500-line / ~5,000-token execution budget and that references are loaded directly from `SKILL.md`, not through chains.

## Maintenance guidance

The source is explicitly evolving. If a later edition materially changes the unfinished coaching chapters, diagnostic algorithms, HSRS details, or the relationship among non-interference/interleaving/spacing, update the corresponding focused reference first and revise `SKILL.md` only if the change belongs in every activation.

When revising the skill, resist the temptation to add every new fact from the book. Add a rule to the always-loaded core only if an agent is likely to make the wrong decision without it.
