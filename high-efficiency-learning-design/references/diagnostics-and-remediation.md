# Diagnostics and Remediation Reference

Read this file when placing a learner, diagnosing struggle, investigating recurring errors, deciding whether to roll back prior mastery, or repairing a learning path.


## D1 — Diagnose demonstrated performance, not self-concept

A useful diagnostic asks: **what can this learner execute correctly, independently, and with reasonable fluency right now?**

Do not ask the diagnostic to maximize the learner's score or confirm their preferred placement. A learner who can barely solve an item after extended effort, external help, or guessing has provided weaker evidence than a learner who solves it comfortably.

For placement diagnostics:

- remove external references;
- discourage guessing when a lucky answer could place the learner too far ahead;
- sample around the uncertain edge rather than randomly across the whole curriculum;
- prefer tasks that reveal multiple prerequisite relationships;
- record confidence in inferred knowledge, not only a binary known/unknown label.

## D2 — Use the knowledge frontier as the placement target

The goal is to estimate the boundary where prerequisites stop being reliably mastered.

For a hierarchical skill graph:

1. Begin with a rough estimate of the learner's level.
2. Ask an informative question near the uncertain boundary.
3. A correct answer provides evidence for the tested skill and, cautiously, its prerequisites.
4. An incorrect answer provides evidence against the tested skill and skills that depend on it.
5. Continue until the remaining uncertainty would not materially change the learner's next tasks.

Do not equate diagnostic percentage-correct with course percentage-mastered. An adaptive diagnostic intentionally asks questions where uncertainty is high, so its raw accuracy can cluster near the decision boundary.

## D3 — Choose diagnostic questions for information, not maximal difficulty

A good diagnostic item is the **simplest item that would convince a knowledgeable evaluator that the learner possesses the target skill**, while genuinely exercising the relevant prerequisites.

Avoid choosing the hardest possible item. Unnecessary difficulty raises the chance of an unrelated arithmetic slip, reading issue, or overload contaminating the signal.

Also avoid trivial items that allow success without the target skill.

## D4 — Treat borderline inferred mastery as conditional

When evidence only barely supports mastery, allow provisional progress but attach low confidence.

**Conditional-completion rule:**

- high-confidence mastery -> later isolated misses should not trigger immediate rollback;
- low-confidence inferred mastery -> contradictory downstream performance should revise the model quickly.

This avoids two bad extremes:

- making diagnostics impossibly long in pursuit of certainty;
- treating all inferred knowledge as equally trustworthy after a short diagnostic.

## D5 — Separate conservative and aggressive edges of mastery

Use a **conservative edge** when being wrong about readiness is expensive: initial placement into a demanding course, certification, safety-critical work, or a high-stakes jump.

Use a more **aggressive edge** during ordinary learning when:

- the cost of trying a frontier task is low;
- the system observes performance continuously;
- failures can trigger targeted remediation;
- the learner can make progress on independent branches.

This distinction lets a learning system move quickly without pretending all mastery estimates are equally certain.

## D6 — Diagnose struggle before attributing it to “ability”

Use the following tree. The ordering is a derived synthesis across the book.

### 1. Missing foundation?

Ask the learner to execute the key prerequisites directly, without hints. If a prerequisite is weak, fix it before adding complexity.

### 2. Instructional leap / cognitive overload?

If prerequisites are present but the combined task fails, reduce novelty per step, add a worked example, label subgoals, or externalize intermediate state.

### 3. Bad practice behavior?

Look for:

- passive watching/rereading instead of producing;
- copying a worked example;
- checking references before attempting retrieval;
- guessing/rushing;
- trying to hold too much in the head;
- repeating identical work without analyzing errors;
- excessive checking/perfectionism that throttles practice cycles.

### 4. Not enough effective practice or retention work?

If the learner can perform with support but not reliably later, increase deliberate practice, retrieval, spacing, interleaving, or automaticity work rather than changing explanation style immediately.

### 5. Adherence / state problem?

Check fatigue, distraction, long gaps, inconsistent practice, and motivation.

### 6. Low learning-rate / poor opportunity-cost fit?

Only after the above have been corrected over enough time should you consider that continued advancement may require an impractically large effort relative to the learner's goals. Describe this as an observed efficiency/ROI issue, not a fixed identity label.

## D7 — Localize failure to the point of breakdown

Do not remediate an entire course because one advanced problem failed.

For a failed multi-step task:

1. Find the first step where the learner's reasoning becomes incorrect or uncertain.
2. Identify the component skills actually required at that step.
3. Test those **key prerequisites** directly.
4. Remediate only the weak prerequisite(s).
5. Reattempt the original task after the learner can execute them.

This is higher-integrity remediation than vague advice such as “review algebra” or “practice more.”

## D8 — Do not hammer indefinitely after a failed learning task

If a learner has made a serious attempt but the material is not clicking, immediate repetition of the entire failed task can waste time and build frustration.

When prior evidence suggests the prerequisites are probably present:

1. stop the blocked path;
2. work on another valid frontier skill or take a break;
3. allow initial learning to consolidate;
4. retry later;
5. if failure repeats at the same point, trigger prerequisite remediation.

This is not avoidance. The blocked path remains unresolved and must be revisited.

The book reports strong Math Academy retry statistics, but those numbers are product-specific and are not part of this portable rule.

## D9 — Roll back in proportion to the evidence

A failure should update the knowledge model, but the update magnitude should depend on prior evidence.

- Strong, repeated prior evidence + one miss -> small update; inspect noise/state/context first.
- Weak or inferred prior evidence + one diagnostic failure -> larger update.
- Repeated failures at the same component -> strong evidence for a real gap.
- Failure on an advanced task does not automatically prove every prerequisite is weak; localize first.

This prevents oscillating between “mastered” and “not mastered” on noisy evidence while still correcting overconfident placement quickly.

## D10 — Use four remediation modes

### Corrective remediation

Trigger after an observed failure. Target the prerequisite or micro-skill implicated by the point of breakdown.

### Preventative remediation

If a learner repeatedly needs more practice or forgets quickly on a foundational skill, strengthen it before downstream failures multiply. This is especially important for high-reuse prerequisites.

### Foundational remediation

Repair lower-level knowledge that gates the current goal. Do **not** automatically repair every unrelated historical gap first. If a foundational topic is necessary but demotivating, it can be interleaved with progress on independent branches so the learner still experiences forward motion.

### Content remediation

If many learners who demonstrably possess the prerequisites fail the same item, worked example, or transition, suspect the instructional content. Split the step, improve the explanation, add a missing example, or fix the item. Preserve the mastery standard; improve the path to it.

## D11 — More explanations are not the default remediation

When one explanation fails, another framing can help. But repeated demand for “a different explanation” may conceal a prerequisite gap, excess cognitive load, or insufficient practice.

Before generating the fifth explanation of the same concept, ask:

- Can the learner execute the prerequisite skills?
- Is the example one difficulty step above their current performance, or five?
- Have they actually tried problems after the explanation?
- Are they retrieving or just re-consuming the explanation?
- Do other prepared learners also fail at this point?

If the content is already clear to prepared learners, targeted prerequisite work is often more useful than endlessly paraphrasing the same idea.

## D12 — Treat recurring “silly mistakes” as performance data

Do not dismiss repeated errors because the learner labels them careless.

A one-off slip may be noise. A pattern can indicate:

- weak automaticity;
- too much mental bookkeeping;
- rushing;
- an unstable procedure;
- a conceptual misconception that only appears intermittent.

In a hierarchical skill, small component error rates compound in long tasks. Require sufficient reliability before using the component as a foundation for more complex performance.

## D13 — Distinguish familiarity, mastery, and automaticity in error analysis

Use three tests:

- **Familiarity:** “Does this look known when shown?”
- **Mastery:** “Can the learner solve/produce it independently and consistently?”
- **Automaticity:** “Can they do it quickly and with little conscious load while handling a larger task?”

A learner who says “I know this” but needs the formula visible may be familiar without being mastered. A learner who solves accurately but very slowly may be mastered without being automatic.

Prescribe the missing stage, not a generic review.

## D14 — Interpret open-book vs closed-book discrepancies diagnostically

If open-book lesson performance is high but closed-book cumulative performance is low:

1. do not conclude the explanation was ineffective;
2. test whether the learner was solving alongside references;
3. increase independent retrieval attempts;
4. space and interleave reviews;
5. check whether the learner can select methods without being primed;
6. inspect automaticity on recurring low-level operations.

If closed-book retrieval still fails after proper practice, then revisit prerequisites or content.

## D15 — Evaluate the learning system with delayed evidence

Do not judge an instructional change only by its immediate lesson pass rate. Extra scaffolding can raise pass rates through priming without durable learning.

Verify changes with less-primed evidence:

- later reviews;
- cumulative quizzes;
- transfer problems;
- downstream tasks that reuse the skill;
- delayed retests.

A content change is successful when it improves later independent performance, not merely when it makes the lesson easier.

## Diagnostic output template

When asked to diagnose a learner, report:

1. **Observed symptom** — what is actually going wrong.
2. **Most likely layer** — foundation, load, behavior, dose/retention, adherence, or longer-run learning rate.
3. **Evidence to collect next** — the smallest test that distinguishes competing causes.
4. **Immediate intervention** — what to change now.
5. **Escalation rule** — what failure/success would make you descend, advance, or change strategy.
6. **Confidence** — which parts are demonstrated versus inferred.
