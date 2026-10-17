# Evaluation Guide

This directory contains two evaluation layers aligned with the official Agent Skills evaluation methodology (`agentskills.io/skill-creation/evaluating-skills` and `optimizing-descriptions`).

## 1. Output-quality evals (`evals.json`)

`evals.json` contains 8 realistic task prompts, human-readable expected outputs, and concrete assertions testing whether the skill changes agent decisions in the intended ways:

1. **Prompt elevation (Depth without bloat):** Applying the 4-part Depth Upgrade (unasked expert move, rawest substrate, real instruments, outside judge) without simply making the deliverable longer.
2. **Process elevation (Altitude + backtest + shadow mode):** Moving from a manual QBR slide template to causal diagnosis, urgent decisions, and a historically backtested shadow mechanism.
3. **Autonomy prerequisite auditing (Crash-free invariant):** Identifying the 4 operational prerequisites required to move from fixing individual bugs to maintaining a continuous invariant.
4. **Adversarial assumption testing & predictive discovery:** Treating organizational folklore (“churn is an onboarding problem”) as a falsifiable hypothesis on raw data and requiring a held-out split for any newly proposed leading indicator.
5. **Order-of-magnitude target reframing without reward hacking:** Using the “200ms test” to escape incrementalism while enforcing honest benchmark verification.
6. **Cross-disciplinary Range without persona role-play:** Using noun-to-verb functional reframing and constructive + red-team methods (short seller, forensic accountant, investigative journalist) while strictly avoiding theatrical dialogue.
7. **Mode C calibration (Not holding an urgent deliverable hostage):** Fulfilling an immediate, time-sensitive request first before offering a bounded higher-leverage upgrade.
8. **Boundary recognition (Expressive creative work):** Recognizing when high-altitude corporate/systemic abstraction does not fit a purely expressive creative goal.

## 2. Trigger evals (`eval_queries.json`)

`eval_queries.json` contains 20 realistic activation queries: 10 `should_trigger: true` and 10 `should_trigger: false` near-misses.

Run each query multiple times (e.g., 3 runs per query) and use a 0.5 trigger-rate threshold. Keep a fixed train/validation split if tuning the frontmatter `description`.
