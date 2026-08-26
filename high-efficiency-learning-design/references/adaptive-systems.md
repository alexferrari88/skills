# Adaptive Learning Systems Reference

Read this file only when designing software, an intelligent tutor, a knowledge graph, task-selection logic, adaptive diagnostics, hierarchical spaced repetition, learning-efficiency metrics, or gamified accountability.

This reference contains the most Math-Academy-specific material in the skill. Treat **HSRS, FIRe, Spaced Repetition Compression, XP logic, and some diagnostic mechanisms as source-specific architecture**, not as independently validated universal algorithms. The book discloses enough to preserve design ideas but not enough to reproduce the production system exactly.


## A1 — Represent curriculum structure explicitly

For a hierarchical domain, model at least these relations where they matter:

- **prerequisite:** B must be mastered before A can be learned efficiently;
- **key prerequisite:** B is the specific prerequisite being exercised at a local step inside A and is therefore a high-value remediation target;
- **encompassing:** successful execution of A actually practices B as a component;
- **partial encompassing:** A practices only part or an easier case of B;
- **equivalence / alternate representation:** optional relation for duplicated or course-specific variants.

Do not collapse prerequisite and encompassing into one edge type. A topic can depend conceptually on a prerequisite without providing enough execution of that prerequisite to count as review.

## A2 — Maintain a knowledge profile with evidence and confidence

For each learner-topic pair, store more than a binary completed flag when the system needs robust adaptation.

Useful state dimensions include:

- estimated mastery/performance;
- confidence in that estimate;
- recency and history of independent successful retrieval;
- review state / expected retention;
- observed learning speed or difficulty for this learner-topic pair;
- whether credit was directly demonstrated or inferred.

The book's “conditional completion” is a practical pattern: permit forward progress when evidence barely supports mastery, but mark the state low-confidence so contradictory evidence can rapidly remove that credit.

## A3 — Next-task selection should reconcile several objectives

A useful adaptive selector operates as a control loop:

1. **Update evidence** from the learner's latest task.
2. **Construct frontier candidates** whose prerequisites are sufficiently mastered.
3. **Construct review obligations** from retention state.
4. **Identify legitimate encompassings** that let one task satisfy multiple obligations.
5. **Filter or penalize bad acquisition sequences** such as highly confusable novel topics back-to-back.
6. **Score candidates** by goal progress, downstream unlock value, due-review coverage, future review reduction, and useful diversity.
7. **Serve a small high-quality choice set** rather than an unrestricted curriculum if learner choice would systematically reduce efficiency.
8. **Observe the outcome and update again.**

The user may choose among near-equivalent high-value tasks. Agency is easier to preserve by constraining choices to good options than by allowing any topic at any time.

## A4 — Use high-granularity mastery, not course-level completion alone

A course-level grade hides heterogeneous knowledge. Track mastery at the smallest unit for which different learner outcomes would meaningfully change the next teaching decision.

Too coarse:

- “Algebra: 80%”

More actionable:

- individual topic mastery;
- within-topic knowledge points or stages of increasing difficulty;
- key-prerequisite links from each stage to the foundations it exercises.

Granularity has a cost. Add finer nodes when they enable different scaffolding, diagnostics, remediation, or sequencing decisions; do not split content merely to make the graph larger.

## A5 — Adaptive diagnostic loop

For an explicit prerequisite graph, choose questions to reduce uncertainty around the learner's frontier.

High-level algorithm:

1. Initialize priors from known history or a broad starting estimate.
2. Identify topics whose mastery state most affects the frontier but remains uncertain.
3. Select a question that provides strong evidence about one of those topics and meaningfully exercises its prerequisites.
4. Propagate the result cautiously through prerequisite/postrequisite relations.
5. Track confidence separately from the state estimate.
6. Stop when remaining uncertainty is unlikely to change the next learning path enough to justify more diagnostic cost.
7. Keep low-confidence inferences conditional and revise them rapidly from later task evidence.

The source describes additional implementation-specific inference shortcuts and supplemental diagnostics. Reuse the principles, not the product's exact heuristics, unless independently reconstructed and tested.

## A6 — Conservative vs aggressive frontier in software

Maintain different thresholds for different actions rather than one universal mastery cutoff.

- **Initial placement / major skip:** conservative threshold; false-positive mastery is costly.
- **Offering a low-cost next lesson with continuous feedback:** more aggressive threshold can increase progress because a mistaken estimate is recoverable.
- **Removing a skill from future review:** conservative again; false confidence can create long-term gaps.

This avoids forcing one probability or score to serve every decision.

## A7 — Hierarchical spaced repetition: conceptual architecture

The book's HSRS generalizes spaced repetition from independent items to a hierarchy where advanced tasks implicitly rehearse components.

### Fractional Implicit Repetition (FIRe)

When advanced task A is completed successfully:

1. identify simpler skills B that A truly exercises;
2. assign implicit repetition credit to B;
3. use less than full credit when A only partially exercises B or the repetition occurs earlier than ideal;
4. propagate credit through relevant hierarchy paths only where the relationship is justified;
5. update B's future review obligation accordingly.

### Spaced Repetition Compression

Given several due or upcoming reviews:

1. search for a small set of explicit reviews or new frontier tasks whose encompassed skills cover multiple obligations;
2. prefer choices that make forward progress while satisfying due review;
3. once current due reviews are covered, consider tasks that reduce near-future review load;
4. preserve enough breadth in the frontier so future optimization still has choices.

This resembles a dynamic covering/selection problem, but **do not invent a numeric optimization formula that the book does not supply**.

## A8 — Suppress implicit credit when the learner-topic pair is weak

The book reports a source-specific rule: when a topic is difficult relative to a particular learner and its spaced-repetition process is slowed, Math Academy can shut off incoming implicit repetition credit and force explicit reviews.

Portable rationale:

- a strong learner may recognize and practice a prerequisite implicitly inside an advanced task;
- a weak learner may execute the advanced task without robustly retrieving/generalizing that prerequisite;
- explicit review gives cleaner evidence and stronger practice.

Use this as a design hypothesis to test, not a universal constant.

## A9 — Treat review scheduling as learner-topic specific

Do not keep one global forgetting rate per learner or one fixed difficulty per topic if the system has enough data to learn finer differences.

At minimum, adapt intervals from:

- the learner's performance history;
- the intrinsic difficulty of the topic;
- the quality and timing of prior repetitions;
- whether repetition was explicit or implicit.

A learner who consistently retains a topic should receive longer intervals. A learner who repeatedly forgets it should receive more explicit and earlier review.

## A10 — Optimize learning efficiency, not task throughput

The book defines learning efficiency as progress through the course relative to time spent working. Preserve the distinction between:

- **performance/accuracy:** how successfully the learner completes tasks;
- **pace:** how quickly productive tasks are completed;
- **progress:** how much meaningful curriculum capability is added;
- **learning efficiency:** meaningful progress per unit focused effort/time.

A system can raise apparent pace by serving easy tasks while reducing learning efficiency. Likewise, excessive perfectionism can raise local accuracy while reducing total progress.

Design telemetry to detect both failure modes.

## A11 — Prioritize goal-relevant core topics

A “core” topic is important because many later relevant topics depend on it. In graph terms, downstream dependency structure is a useful priority signal.

For goal-directed curricula:

1. trace the target's prerequisite closure;
2. prioritize high-reuse nodes early;
3. exclude unrelated supplemental nodes only if the product explicitly promises a streamlined route rather than comprehensive coverage;
4. make the scope contract visible to the user.

Do not call omitted material “unimportant” in general; it may simply be irrelevant to the current goal path.

## A12 — Gamification must close the learning loop

A reward system should make **productive learning behavior** the easiest route to reward.

Reward signals can include:

- useful volume of completed work;
- accuracy or successful mastery;
- consistency over time;
- completion of tasks selected for genuine learning value.

Audit exploits:

- rapid guessing to maximize throughput;
- avoiding difficult tasks;
- repeated farming of already-mastered easy tasks;
- using external answers or hints while receiving full credit;
- intentionally failing to force easier remediation;
- dividing group labor so only one participant learns.

Do not reuse the book's XP conversion rates, penalties, leaderboard bands, or pass-rate statistics without product-specific validation.

## A13 — Separate progress metrics from effort/reward metrics

A learner can do a high amount of productive work yet add little new curriculum progress because they are repairing foundations or paying review obligations. Conversely, a learner can advance rapidly through easy material with little effort.

Keep at least conceptual separation among:

- **knowledge state / progress** — what the learner can now do;
- **effort / work credit** — how much productive practice they completed;
- **retention obligations** — what must be revisited;
- **engagement/reward** — what the product chooses to incentivize.

Conflating these makes both analytics and incentives easier to game or misinterpret.

## A14 — Treat the dashboard as a dynamic menu, not a static queue

When every completed task changes mastery, review obligations, and unlocks, recompute future priorities dynamically.

It can still be reasonable to leave already-present high-value options visible for stability, user expectation, and anti-avoidance reasons. Do not churn the interface merely because the optimizer can calculate a microscopically better ordering after every click.

The core invariant is that visible choices should remain defensible learning options under the updated state.

## A15 — Know when technology is required for fidelity

Humans can apply approximate mastery, spacing, interleaving, and remediation manually. But high-granularity individualized scheduling across many learners and thousands of topics becomes an inhuman tracking problem.

If the design calls for:

- per-learner-per-topic review schedules;
- graph propagation of implicit repetition;
- confidence-aware adaptive diagnostics;
- frequent dynamic task reselection;
- item-level content analytics;

then treat software as a structural requirement, not a convenience.

For manual teaching, simplify the method explicitly rather than pretending to deliver full algorithmic personalization.

## Technical limitations of this source

Do **not** implement a claimed production clone of Math Academy's HSRS or diagnostic engine from this book alone. The manuscript describes the conceptual mechanisms and some technical detail, but omits enough production-specific mathematics, parameter estimation, edge weighting, data calibration, and operational safeguards that a faithful reconstruction would require additional source material and empirical tuning.

If a user requests an implementation:

1. clearly label which components are directly specified by the book;
2. label proposed formulas/weights as new design choices;
3. create offline simulations and ablation tests before learner deployment;
4. compare against simpler baselines such as explicit per-topic spacing and prerequisite-only mastery;
5. never present inferred parameters as Math Academy's actual production values.
