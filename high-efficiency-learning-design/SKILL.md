---
name: high-efficiency-learning-design
description: Use this skill to design, audit, or troubleshoot high-efficiency learning for hierarchical skills, especially mathematics, technical subjects, tutoring flows, study plans, curricula, assessments, and adaptive learning systems. Activate when deciding what a learner should practice next, why they are stuck or forgetting, how much guidance, practice, or review to give, whether they are ready to advance, or how to structure worked examples, retrieval, spacing, interleaving, diagnostics, remediation, or learning incentives, even if the user never mentions learning science or Math Academy. Do not use merely to solve or explain subject-matter problems, discuss education casually, or optimize entertainment or superficial exposure.
metadata:
  source-title: The Math Academy Way
  source-version: Working draft, 17 August 2026
  skill-version: 1.0.0
---

# High-Efficiency Learning Design

Use this skill to turn a learning goal into a sequence of tasks that maximizes **durable, independent performance per unit of focused effort**. It is strongest for hierarchical, practice-intensive domains where advanced performance depends on reliable prerequisite skills.

Do not optimize for how fluent, easy, entertaining, or impressive practice feels in the moment. Those signals can diverge from later retention and transfer. At the same time, do not manufacture difficulty: effort is useful only when it produces successful retrieval, discrimination, refinement, or skill growth.

## 1. Check applicability before prescribing

Use the full method when the user wants serious skill acquisition, durable retention, reliable execution, acceleration, or an efficient learning system.

Use only a lightweight subset when the user's goal is casual enrichment, orientation, entertainment, or very low-volume exposure. In that case, say that the optimization target differs from mastery-oriented talent development and avoid imposing an unnecessarily intense regimen.

Reduce guidance for genuine experts working near the frontier of a field. Open-ended discovery and creative production become appropriate after a large domain-specific knowledge base exists; they are usually inefficient as the primary acquisition method for novices.

Do not infer that a learner has reached a fixed ability limit merely because they struggle. First test fixable causes: missing foundations, task size, practice behavior, practice dose, retention, fatigue, and motivation.

## 2. Define the target in observable performance terms

Before designing practice, identify:

1. **Target capability** — what the learner should be able to do.
2. **Context of use** — exam, professional task, next course, competition, general retention, etc.
3. **Mastery evidence** — what successful independent performance looks like.
4. **Time horizon** — immediate competence, months-long retention, or long-term expertise.
5. **Constraints** — available time, tools, instructor support, deadlines, motivation, and prior knowledge.

Prefer evidence such as correct problem solving, successful production, discrimination between similar cases, cumulative performance, and delayed retrieval. Treat self-reported familiarity, rereading fluency, recent blocked-practice accuracy, and grades as weaker evidence unless independently validated.

## 3. Map dependencies and find the learner's frontier

Represent the target as a prerequisite graph when the domain is meaningfully hierarchical. It can be informal for a study plan or explicit in software.

For each target skill:

1. List the direct prerequisite skills actually used to perform it.
2. Mark which prerequisites the learner has demonstrated, not merely encountered.
3. Identify the **knowledge frontier**: unmastered skills whose prerequisites are already mastered.
4. Select new learning tasks from that frontier.
5. Prefer core prerequisites that unlock many downstream skills when several frontier tasks are equally useful.

Do not front-load every historical knowledge gap. Repair gaps that are prerequisites for the current goal; let unrelated gaps wait until they become relevant unless the user explicitly wants comprehensive remediation.

## 4. Diagnose bottlenecks before changing the plan

When a learner is stuck, slow, inaccurate, or forgetting, check these causes in this order. This ordering is a derived synthesis of the book's diagnostic logic, not an explicit numbered sequence from the author.

1. **Missing or weak prerequisites.** Can the learner execute the component skills independently and reliably?
2. **Excess cognitive load.** Is the instructional step too large, are too many novel elements being juggled, or should intermediate work be externalized?
3. **Ineffective practice behavior.** Is the learner mostly watching, rereading, copying, guessing, using references as a crutch, or repeating without adjustment?
4. **Insufficient or poorly scheduled practice.** Is there enough successful practice, spacing, interleaving, and retrieval to reach and retain mastery?
5. **Adherence and context.** Are fatigue, distraction, inconsistent sessions, weak incentives, or lack of motivation preventing productive practice?
6. **Learning-rate / opportunity-cost ceiling.** Consider this only after the earlier causes have been addressed over enough time to observe the learner's real learning rate.

Read `references/diagnostics-and-remediation.md` when the task is primarily placement, troubleshooting, error analysis, or remediation.

## 5. Match practice mode to the learner's stage

### Acquisition: guide, then make the learner perform

For novel material, default to **active + direct** instruction:

1. Give the minimum explanation needed to orient the learner.
2. Show a worked example or demonstration that makes the procedure and subgoals explicit.
3. Immediately require the learner to perform a closely related task.
4. Give corrective feedback.
5. Repeat with small variations and gradually harder cases.
6. Continue until the learner reaches **baseline mastery**: reliable enough performance to build further skills on top.

Do not confuse active learning with unguided discovery or group work. A learner can be highly active while receiving explicit instruction and feedback.

### Deliberate practice: maximize useful action-feedback-adjustment cycles

A good practice task targets a specific weakness, sits near the edge of reliable performance, can be completed in a reasonably short cycle, produces diagnostic feedback, and allows an immediate adjustment on the next attempt.

Avoid both failure modes:

- **mindless repetition** of already comfortable performance;
- **heroic challenge problems** so difficult that one attempt consumes the time that could have produced many useful refinement cycles.

### Consolidation: introduce desirable difficulty

After baseline mastery:

- stop excessive blocked overlearning;
- space later encounters so some forgetting occurs;
- interleave different problem types so the learner must identify the method;
- require retrieval before allowing reference material;
- broaden cumulative assessment beyond recently practiced material.

### Automaticity and expertise: fade support

Do not require full automaticity before advancing. Move forward at baseline mastery, then develop automaticity through later retrieval, review, and **layering** more advanced skills that reuse the prerequisite.

As expertise increases, remove worked-example support and use more transfer, synthesis, open-ended, and creative tasks. This is the expertise-reversal principle: support that helps novices can become redundant or constraining for experts.

Read `references/practice-design.md` for lesson design, worked examples, cognitive load, automaticity, group work, reference use, paper/external memory, and timed practice.

## 6. Control difficulty and scaffolding

Aim for the hardest task the learner can overcome **successfully and in a useful amount of time**. Difficulty is desirable only when the learner can ultimately retrieve or perform the skill; persistent failure is not a learning strategy.

When cognitive load is the bottleneck:

- split the task into smaller knowledge units;
- label subgoals;
- use a worked example before independent performance;
- externalize intermediate state on paper or another workspace;
- reduce simultaneous novelty;
- then fade these supports as execution becomes fluent.

Err slightly toward extra scaffolding when uncertain. The trade-off is asymmetric: modest overscaffolding mainly costs time, while underscaffolding can cause overload, errors, and complete failure to learn.

## 7. Sequence acquisition, spacing, interleaving, and non-interference correctly

These strategies solve different problems; do not collapse them into “mix things up.”

- **Initial blocking:** a small block of similar problems helps a learner execute a newly introduced method.
- **Non-interference:** do not introduce highly confusable new concepts back-to-back when that increases associative interference. Separate their initial acquisition with dissimilar material.
- **Interleaving:** after baseline mastery, mix previously learned problem types so the learner must discriminate which method applies.
- **Spacing:** revisit the same skill after time has passed rather than massing all review into one session.
- **Layering:** prefer advanced tasks that genuinely exercise mastered prerequisites because they advance knowledge while reinforcing foundations.

A useful synthesis is: **separate confusable concepts during fragile initial acquisition; later interleave them deliberately to train discrimination.** This is a derived interpretation combining the book's non-interference and interleaving rules.

Read `references/sequencing-and-retention.md` for study schedules, review timing, implicit repetitions, exam-prep exceptions, and the tensions among these strategies.

## 8. Use retrieval and review to build retention, not freshness

Default review behavior:

1. Attempt from memory first.
2. If genuinely stuck, peek only at the missing cue or next step.
3. Close the reference.
4. Reconstruct and complete the task independently.
5. Revisit later after a longer interval if successful; shorten the interval or remediate if unsuccessful.

Do not keep all knowledge 100% fresh all the time. Efficient spaced review intentionally allows memory to become somewhat effortful to retrieve. Exception: before a fixed high-stakes exam or performance, temporarily shift into a **freshness/test-prep mode** with earlier reviews and representative full-task practice.

Count an advanced task as implicit review of a prerequisite only when the advanced task actually makes the learner execute that prerequisite. Conceptual dependence alone is not enough.

## 9. Remediate without lowering the bar

When a learner fails despite prior evidence of mastery, do not immediately erase that evidence. A single miss may be noise, fatigue, or a bad attempt.

Use this corrective loop:

1. Inspect where the attempt broke down.
2. If the learner had strong prior evidence, pause the failed path rather than hammering indefinitely; practice another valid path and retry later.
3. If failure repeats at the same local step, identify the **key prerequisites** used at that step and review them explicitly.
4. If those prerequisite reviews fail, descend another level and reteach/repractice the implicated foundation.
5. Reattempt the original task without lowering its independent-performance criterion.
6. If many adequately prepared learners fail at the same step, treat it as a content/scaffolding defect and revise the instruction instead of blaming every learner.

Hints may be useful for diagnosis or reorientation, but do not count a hinted solution as evidence of independent mastery.

## 10. Adapt amount, not mythical “learning style”

Do not personalize instruction around visual/auditory/kinesthetic learning-style labels. Adapt to **observed performance** instead:

- faster learner -> larger instructional steps, fewer repetitions, longer review intervals;
- slower learner -> smaller steps, more repetitions, more explicit review;
- high error rate under load -> more externalization/scaffolding;
- strong untimed but weak cumulative/timed performance -> more retrieval, interleaving, and automaticity work.

Hold the mastery criterion stable while varying the amount and granularity of practice needed to reach it.

## 11. Design assessments as learning and measurement

Use frequent, low-stakes retrieval as part of learning. For diagnostics and mastery decisions, prefer questions that reveal what the learner can do independently rather than questions optimized to make them feel successful.

Use timed testing only after the learner can perform accurately in untimed conditions. Timing is useful when the target requires automaticity or speed; premature timing can create an undesirable difficulty.

Do not telegraph the exact method before a cumulative assessment when the purpose is to test method selection or independent recall.

## 12. Align incentives with learning

If using points, streaks, leaderboards, rewards, or penalties, make sure the easiest way to earn the reward is also the desired learning behavior.

Reward both useful volume and quality. Audit for exploits such as guessing quickly, avoiding hard tasks, copying, overusing hints, farming easy repetitions, or dividing group work so one person learns and others coast.

Do not import Math Academy's XP values, pass-rate targets, or anti-gaming thresholds as universal constants. They are product-specific implementations, not portable laws.

Read `references/adaptive-systems.md` when designing software, a knowledge graph, an adaptive tutor, task-selection logic, diagnostics at scale, hierarchical spaced repetition, or gamification.

## 13. Handle adherence as a separate bottleneck

A pedagogically optimal plan is useless if the learner will not execute it. Prefer repeatable, focused sessions over occasional blowouts. End or reduce a session when fatigue is visibly degrading accuracy, attention, or next-day consistency.

For children or learners who need external structure, begin with close supervision of learning behavior and fade it only after productive habits are demonstrated. Keep later check-ins sufficient to detect drift.

Several coaching and habit chapters in the source are explicitly unfinished. Read `references/coaching-and-adherence.md` only when adherence, parent supervision, habit formation, or motivation is central, and treat its provisional rules with less confidence than the finished learning-design chapters.

## 14. Output a decision, not a literature summary

When applying this skill, normally produce:

1. **Goal and mastery evidence** — what counts as success.
2. **Diagnosis** — the most likely bottleneck(s), with evidence and uncertainty.
3. **Learning design** — what to learn/practice next, how tasks are scaffolded, and when to advance.
4. **Retention plan** — spacing, interleaving, retrieval, and cumulative assessment.
5. **Adaptation loop** — what measurements cause the plan to speed up, slow down, remediate, or change.
6. **Boundary conditions** — where the method may not fit the user's actual goal.

Be explicit when a recommendation is a derived synthesis rather than a direct rule from the source.

## Reference loading map

- Read `references/practice-design.md` for **lesson/practice construction**, worked examples, cognitive load, automaticity, feedback, group work, paper, or reference use.
- Read `references/sequencing-and-retention.md` for **curriculum order, study schedules, mastery progression, spacing, interleaving, non-interference, retrieval, or acceleration**.
- Read `references/diagnostics-and-remediation.md` for **placement, a stuck learner, recurring mistakes, knowledge gaps, rollback, remediation, or evaluating whether the instruction itself is defective**.
- Read `references/adaptive-systems.md` only for **software/adaptive-learning design**, knowledge graphs, HSRS/FIRe, diagnostic algorithms, task selection, learning-efficiency metrics, or anti-gaming design.
- Read `references/coaching-and-adherence.md` only for **habit, motivation, parent/coach supervision, or study-behavior problems**; parts of its source are unfinished.
- Read `references/source-map.md` only for **provenance, auditing, source-page lookup, or distinguishing direct claims from derived interpretations**. It is not part of the normal execution path.

Load only the references needed for the current task. Do not load references merely because they exist, and do not follow reference-to-reference chains.
