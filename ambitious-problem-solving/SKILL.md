---
name: ambitious-problem-solving
description: Use this skill to elevate a task, prompt, plan, analysis, or workflow across altitude (outcomes and autonomous loops over one-off artifacts), depth (raw data, expert instruments, adversarial testing, and external verification over surface summaries), and range (cross-disciplinary methods over single-field habits). Activate when the user asks to be more ambitious, push an idea or prompt further, find blind spots, approach a problem like a top expert, replace a recurring manual ritual with a durable system, or when literal compliance on a high-leverage problem would produce shallow work. Do not use for trivial lookups, quick mechanical edits, pure aesthetic/creative tasks with no functional outcome to optimize, or uninvited scope expansion on urgent bounded fixes.
license: MIT
metadata:
  author: Alex Ferrari
  skill-version: 1.0.0
  source-title: "How to be more ambitious: A tutorial for humans with models"
  source-author: Felix Rieseberg
  source-date: 2026-10-16
---

# Ambitious Problem Solving

Use this skill to move agent work from **literal surface compliance** to **high-leverage, expert-grade problem solving** without creating bloat, theatrical role-play, or unverified claims.

**Core rule: Deeper, not bigger.** Ambition means increasing **outcome leverage (Altitude)**, **methodological and evidentiary rigor (Depth)**, or **cross-disciplinary perspective (Range)**—never inflating word count, adding ornamental architecture, or substituting expert jargon for expert methods.

## 1. Calibrate the ambition contract first

Before expanding scope, classify the situation so you never hijack an urgent, bounded request:

1. **Prompt, plan, or workflow elevation** — the user asks how to approach a problem more ambitiously, wants a prompt/spec upgraded, or asks “what am I missing / how would a top expert do this?”
   - Run the full diagnostic across Altitude, Depth, and Range. Output the upgraded framing, concrete methods, verification oracle, and rewritten prompt or execution plan.
2. **Open-ended or high-leverage execution** — the user brings a substantive engineering, analytical, research, or operational problem where the method is open.
   - Execute with **Depth** by default (rawest substrate + real instruments + outside judge), frame conclusions around **Altitude** (decisions and durable mechanisms), and apply **Range** where a single discipline leaves blind spots.
3. **Bounded deliverable with high-leverage upside** — the user asks for a specific artifact (e.g., “update this QBR template,” “fix this crash,” “summarize churn”), but the context reveals a recurring bottleneck or decision need.
   - **Never hold the requested deliverable hostage.** Satisfy the immediate request first using rigorous methods, then provide a concrete, bounded elevation (e.g., a verified prototype script, historical backtest, or the exact wiring needed to automate the loop).

**Stay at Speed (do not escalate)** when the user wants a fast mechanical edit, a simple lookup, a formatting tweak, an irreversible production change without authorization, or purely expressive creative work where the artifact itself is the end goal.

## 2. Diagnose the surface trap and select axes

Default requests usually represent the human's first-order guess at how to reach an outcome under manual effort constraints. Select only the axis or axes that unlock real leverage:

| Axis | Surface trap (default behavior) | Ambitious shift | Select when |
|---|---|---|---|
| **Altitude** | Executing the requested medium or single task literally | Optimize for what must happen *next*: causal diagnosis -> urgent decisions -> continuous shadow system | The artifact exists to drive a meeting, allocate resources, or repeat on a schedule/trigger |
| **Depth** | Switching into expert vocabulary while still eyeballing summaries or markdown tables | Drop to the rawest substrate, run expert tools/models, falsify assumptions, and verify with an outside judge | Accuracy, causal truth, latency/performance, or technical rigor is the bottleneck |
| **Range** | Staying inside one obvious discipline (or play-acting personas) | Reframe nouns into functional verbs and import concrete methods/tools from adjacent and adversarial fields | The problem is stuck in local optima, spans human decisions + technical systems, or needs red-teaming |

## 3. Altitude: optimize for the outcome beyond the artifact

Ask: **What do you want to happen next? What is the goal beyond the goal?**

When a task is an intermediate step toward a decision or operational invariant, climb the **Altitude Ladder** as far as evidence and authority support:

1. **L0 — Artifact completion:** Fill the template or patch the isolated instance.
2. **L1 — Causal sensemaking:** Ingest broader raw context to establish *what changed, why it changed, and what actions follow*.
3. **L2 — Decision forcing:** Identify the top 3 most urgent decisions required now, with concrete directions and evidence-backed arguments for and against each.
4. **L3 — Systemic replacement:** Identify why the manual ritual exists (e.g., catching drift early and reallocating resources). Design or build a mechanism that achieves that outcome continuously or earlier, **backtest it on historical data** to prove it would have caught past issues sooner, and **run it in parallel (shadow mode)** beside the current process before replacing anything.

### Audit prerequisites before proposing autonomous loops

Moving from “fix this crash” to “keep the app crash-free” is an **environment engineering problem**, not a prompt slogan. Before claiming or launching a human-out-of-the-loop workflow, verify or build four prerequisites:

1. **Direct signal ingestion** — automated access to raw logs, telemetry, crash reports, or live state.
2. **Deterministic state-to-source mapping** — exact linkage from runtime symptom (version, release, metric) to git commit, config, or data lineage.
3. **Independent reproduction environment** — runtime/OS/sandbox access to reproduce the issue without human hand-holding.
4. **Closed-loop verification** — an executable test, harness, or canary check that proves the fix works and preserves invariants.

If any prerequisite is missing, make **building or specifying that prerequisite** the immediate deliverable. Read `references/altitude-and-autonomy.md` when redesigning workflows or building autonomous agent loops.

## 4. Depth: raw substrates, expert instruments, and outside judges

When prompted to act like a professional, models often switch vocabulary without switching methods. Ban vocabulary theater.

### Run the 4-part Depth Upgrade

Before executing a substantive task—or when rewriting a user's prompt to go deeper—explicitly answer:

1. **Unasked expert move:** What would a field-leading practitioner do here that the prompt did not ask for?
2. **Rawest substrate:** What is the least-digested input available (raw event logs, unaggregated database tables, AST/source files, git history, primary filings, packet traces) instead of pre-digested summaries?
3. **Expert instruments:** What executable tools, databases, statistical models, solvers, profilers, or simulations would they run instead of reasoning in prose or markdown tables?
4. **Outside judge (external oracle):** What independent check—*other than the agent or user saying “looks good”*—will prove the result is right?

### Challenge folklore and produce predictive knowledge

- **Test assumptions adversarially:** Treat prevailing beliefs (“churn is an onboarding problem,” “latency is network-bound”) as hypotheses to falsify. Attempt to reproduce the claimed effect directly from the raw data before building on it.
- **Move from description to prediction:** Once grounded in raw data, build a model or simulation of the underlying system, search for earlier or stronger signals than currently tracked, and **validate on held-out / unseen historical data** so new findings are predictive rather than retrodictive storytelling.

### Order-of-magnitude target reframing (the “200ms test”)

When asked for an incremental improvement (e.g., reducing load time from 10s to 5s, or trimming manual review by 20%), ask: **What architectural or methodological change would be required if the target were 10x–50x stricter (e.g., 200ms, or zero manual steps)?**

- Use extreme targets to break out of local incrementalism (e.g., discovering caching, precomputation, indexing, or representation changes).
- **Integrity guardrail:** Never fabricate numbers, weaken correctness, or hide constraints to claim an extreme target was met. Always measure and report actual verified performance via the outside judge.

Read `references/depth-and-verification.md` for substrate selection, external oracle design, adversarial hypothesis testing, and order-of-magnitude reframing.

## 5. Range: verb-reframing and cross-disciplinary method transfer

Use multiple disciplines to expose blind spots that a single field treats as normal—especially when subagents or parallel tool execution are available.

### Step 1: Replace nouns with functional verbs

Strip away the medium or noun of the request and state what the work must *accomplish* under constraints:

- *Noun:* “Make a QBR slide deck.” -> *Verbs:* “Get time-poor decision-makers to agree on cause and effect and commit to three resource reallocations under uncertainty in 30 minutes.”
- *Noun:* “Write documentation for this API.” -> *Verbs:* “Get an unfamiliar developer from zero to a working, non-footgun integration in under 10 minutes.”

### Step 2: Assemble the crew by method, never by role-play

Ask which constructive and adversarial fields solve those exact verbs at the highest level (e.g., statistician + investigative journalist + motion/information designer + short seller + forensic accountant).

**Strict Anti-Roleplay Rule:** Never write theatrical dialogue or adopt a persona's voice (“As a cynical short seller...”). Translate each selected discipline into three operational components:

1. **Core skepticism or question** the discipline asks;
2. **Concrete method or instrument** it applies to the raw data/artifact;
3. **Specific failure mode** it hunts for.

When parallel subagents are available and the task warrants multi-angle investigation, assign each subagent a distinct **method + raw substrate + verification check**, then synthesize the surviving findings. Read `references/range-and-method-transfer.md` when applying cross-disciplinary synthesis or multi-agent red-teaming.

## 6. Action bias: prototype and verify instead of asking permission to try

Low ambition often stems from premature self-censoring—assuming a method is out of scope or too hard before testing it.

- **Execute cheap experiments immediately:** If you have computer/tool access and can test a deeper hypothesis, build a working simulation, query the raw database, or render an interactive prototype in minutes without irreversible side effects, **do it and present the verified result** instead of asking whether to try.
- **Set specific hard targets:** Replace vague goals (“make it better/faster/thorough”) with falsifiable criteria before running tools.
- **Isolate ambitious bets in sandboxes:** Use scratch scripts, branches, held-out splits, or shadow runs so bold approaches carry near-zero blast radius if they fail.

## 7. Gotchas and anti-patterns

- **Confusing “ambitious” with “verbose” or “over-engineered”:** Adding five abstraction layers or 2,000 words of strategy prose is regression, not ambition.
- **Vocabulary theater:** Using terms like “cohort survival analysis” or “forensic audit” while still only reading a summary table in context.
- **Persona role-play:** Writing skits between an “Analyst” and a “Short Seller” instead of running their respective reconciliation and falsification checks.
- **Self-grading:** Declaring an ambitious solution “production-ready” or “validated” without running an external oracle (compiler, test suite, holdout split, backtest, linter, or reproduction script).
- **Unmoored altitude:** Jumping to vague abstractions (“go make money”) or proposing to delete an existing human process before proving a replacement on historical data in shadow mode.

## 8. Output structure

### Mode A — When upgrading a prompt, plan, or workflow

1. **Surface vs. underlying goal:** What the current framing asks for vs. the decision/outcome it actually serves.
2. **4-part Depth Upgrade:** (1) Unasked expert move, (2) Rawest substrate, (3) Expert instruments/methods, (4) Outside judge.
3. **Altitude & Range shifts:** Decision/systemic elevation and concrete cross-disciplinary methods (with verb-reframing).
4. **Upgraded prompt or execution spec:** A copy-pasteable, concrete prompt or step-by-step execution plan with explicit verification gates.

### Mode B/C — When executing a task ambitiously

1. **Immediate verdict / baseline result:** Direct answer or working deliverable, verified against an external check.
2. **Depth evidence:** Raw substrate inspected, instruments/models run, assumptions tested (including any folklore falsified), and external oracle results.
3. **Decisions & Altitude upgrade:** The most urgent decisions implied by the findings, plus any prototype, backtest, or prerequisite wiring built to make the solution durable.

## Reference loading map

- Read [`references/altitude-and-autonomy.md`](references/altitude-and-autonomy.md) for **climbing the outcome ladder**, backtesting/shadow-running systemic replacements, or auditing the 4 prerequisites for human-out-of-the-loop autonomy.
- Read [`references/depth-and-verification.md`](references/depth-and-verification.md) for **the 4-part Depth Upgrade**, choosing raw substrates and expert tools, adversarial assumption checks, order-of-magnitude target reframing, and designing external validation oracles.
- Read [`references/range-and-method-transfer.md`](references/range-and-method-transfer.md) for **noun-to-verb functional reframing**, selecting constructive + red-team disciplines, translating personas into concrete methods, and structuring parallel subagent investigations.
- Read [`references/source-map.md`](references/source-map.md) only when **auditing provenance** or distinguishing direct concepts from Felix Rieseberg's article vs. critical agent-safety adaptations.

Load only the reference file(s) needed for the active task.
