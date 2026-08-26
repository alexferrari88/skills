# Evaluation Guide

This directory contains two evaluation layers aligned to the official Agent Skills guidance.

## Output-quality evals

`evals.json` contains realistic task prompts, a human-readable description of successful output, and concrete assertions. There are no input files for these cases.

For each eval:

1. Start with a clean agent context.
2. Run the prompt **with** this skill.
3. Run the same prompt **without** the skill, or against the previous skill version.
4. Grade each assertion using concrete evidence from the output.
5. Compare the two outputs blind when possible.
6. Inspect whether the skill's gain is worth the additional tokens/context.

The intended “skill value” is not merely that the answer mentions spaced repetition or deliberate practice. The skill should change decisions that a generic agent often gets wrong: mistaking immediate fluency for learning, over-prescribing explanations, keeping blocked practice too long, using difficulty indiscriminately, ignoring prerequisite failures, or treating all review as explicit flashcard-style repetition.

## Trigger evals

`eval_queries.json` contains 20 realistic activation queries: 10 positives and 10 adjacent negatives.

The negative prompts are deliberately close to the domain. The skill should not activate simply because the user says “math,” “learning,” “spaced repetition,” or “active learning.” It should activate when the user wants to **design, diagnose, evaluate, sequence, adapt, or optimize a learning process** where the methodology would materially change the answer.

Because skill triggering is nondeterministic, run each query multiple times. The current official guidance suggests three runs as a reasonable starting point and a 0.5 trigger-rate threshold. If optimizing the description, keep a fixed train/validation split so the description does not overfit these exact phrasings.

## Manual checks beyond assertions

Pay special attention to these failure modes during human review:

- The answer becomes a generic learning-science list rather than a decision process.
- It prescribes every book technique even when the user's goal is casual enrichment.
- It calls any hard task a desirable difficulty despite repeated failure.
- It requires full automaticity before allowing forward progress.
- It confuses prerequisite edges with implicit-review/encompassing edges.
- It presents FIRe/HSRS as a fully specified public algorithm.
- It makes aptitude judgments from limited evidence.
- It quotes Math Academy's platform-specific metrics as universal targets.
- It treats unfinished coaching material with the same confidence as the completed cognitive-learning chapters.
