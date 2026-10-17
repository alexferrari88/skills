# Depth and Verification Reference

Read this file when pushing a task to field-leading technical or analytical rigor, upgrading a user prompt via the 4-part Depth Upgrade, testing organizational assumptions against raw data, reframing incremental targets into order-of-magnitude designs, or constructing an external validation oracle.

---

## D1 — Method Switching vs. Vocabulary Switching

A common failure mode when an agent tries to “act like an expert” is **vocabulary theater**: adopting the tone, headings, and buzzwords of a senior statistician, staff engineer, or forensic auditor while still performing the same shallow operation (eyeballing a small markdown table, writing prose bullet points, or guessing root causes from memory).

**True depth changes three things:**
1. **The input substrate** (moving down to raw, unaggregated records or source artifacts).
2. **The operating instrument** (executing code, SQL, statistical models, compilers, solvers, profilers, or simulations).
3. **The judge** (replacing model self-assessment with an external, falsifiable check).

| Domain | Surface compliance (shallow) | Field-leading depth (rigorous) |
|---|---|---|
| **Product / Churn Analysis** | Summarizing a pre-aggregated monthly churn table in markdown | Loading raw user event logs into DuckDB/SQLite, running cohort survival / hazard models, falsifying folklore, and testing predictive signals on a held-out time split |
| **Performance Engineering** | Suggesting generic caching or “optimize database queries” in prose | Capturing flamegraphs/query plans, framing a 10x–50x latency target (e.g., 10s -> 200ms) to rethink data layout, and benchmarking p50/p95/p99 before and after |
| **Software Debugging** | Guessing a fix from a stack trace snippet and saying “this should fix it” | Writing a deterministic reproduction test that fails on `HEAD`, instrumenting state, applying the fix, and proving the test and full suite pass |
| **Financial / Strategy Review** | Filling numbers into a slide template with narrative commentary | Reconciling unit economics from transaction-level ledgers, running sensitivity/Monte Carlo simulations, and stress-testing the thesis against historical drawdowns |

---

## D2 — The 4-Part Depth Upgrade Protocol

When asked to make a task or prompt **deeper (not bigger)**, execute this 4-step transformation before writing the final prompt or running the work:

1. **Unasked expert move:** Name what a top professional in the field would do here that the original request omitted (e.g., checking for survivorship bias, controlling for seasonality, testing out-of-sample, checking memory allocations).
2. **Rawest substrate:** Identify the rawest material available instead of pre-digested summaries (e.g., raw event streams, commit diffs, unaggregated ledger rows, ASTs, primary filings).
3. **Specific methods and tools:** Name the exact executable instruments required (e.g., DuckDB/SQLite, `scipy`/`statsmodels`, Kaplan-Meier survival analysis, flamegraph profiler, property-based testing with Hypothesis, Z3 solver).
4. **Outside judge:** Specify what—*other than the model or the user*—will prove the result is right (e.g., held-out test accuracy/calibration, compiler + test suite, conservation-law accounting identity, benchmark harness).

### Prompt-rewrite template

When the user asks you to upgrade their prompt for depth, deliver the 4 diagnostic answers succinctly and then provide a rewritten prompt structured like this:

```text
Goal: [Deepened objective focused on verified truth/performance, not output length]
Raw inputs to inspect: [Specific raw files, tables, logs, or sources]
Methods & instruments to run: [Exact models, queries, simulations, or tools—no prose-only substitutes]
Assumptions to challenge: [Existing beliefs to test adversarially against the raw data]
External validation gate: [Independent check, holdout split, or executable test that must pass]
Deliverable: [Concise, decision-ready output backed by the validation evidence]
```

---

## D3 — Adversarial Assumption Testing & Predictive Discovery

Organizational folklore (“churn is an onboarding problem,” “our slow builds are caused by TypeScript compilation,” “enterprise customers buy because of feature X”) is often an outdated or untested approximation.

### Step 1: Reproduce or falsify the folklore first
- Before building recommendations on top of a stated belief, try to **reproduce the belief directly from raw data**.
- Operational prompt: *“We believe X causes Y. Query the raw records to test whether X actually explains Y once we control for confounders, and show the exact effect size.”*
- If the raw data contradicts or weakly supports the assumption, lead with that falsification. Saving a team from optimizing the wrong variable is one of the highest-leverage outcomes an agent can deliver.

### Step 2: Produce new predictive knowledge
- Once grounded in raw data, move beyond descriptive reporting (“what happened”) to **generative/predictive modeling** (“what mechanism explains this, and what earliest signal predicts it?”):
  1. Build a quantitative model or simulation of the system that reproduces historical behavior from raw logs.
  2. Search for blind spots or early leading indicators not currently tracked.
  3. **Mandatory holdout gate:** Evaluate any newly discovered signal on **unseen / held-out data** (e.g., train on months 1–9, test on months 10–12). Never claim discovery of a predictive signal from in-sample fit alone.

---

## D4 — Order-of-Magnitude Target Reframing (The “200ms Test”)

In human-model collaboration, asking for a 2x improvement (e.g., reducing page load from 10s to 5s) invites incremental tinkering (compressing an asset, tweaking a timeout). Asking for a **10x–50x improvement** (e.g., 10s -> 200ms) invalidates incrementalism and forces a search over a different design space (edge precomputation, local-first sync, zero-copy indexing, eliminating network round-trips).

### How an agent must apply this safely

When Felix Rieseberg advises humans to *“pick unreasonable goals and tell the model that they're very reasonable,”* he is describing a **search-space expansion hack** to overcome premature model surrender. When an agent applies this principle to itself, it must separate **ambitious search** from **honest reporting**:

1. **Reframe the search target:** When given an incremental goal, explicitly ask: *“What architectural or algorithmic assumptions would have to change if our target were 10x–50x stricter?”*
2. **Persist past initial friction:** Do not abandon a high-leverage path after the first error or missing library; inspect the bottleneck and test whether it is genuinely unsolvable or merely requires a deeper tool.
3. **Never fake the metric or cheat invariants (Anti-Reward-Hacking Rule):**
   - Never hardcode test outputs, drop required data, weaken security/correctness checks, or hallucinate benchmark numbers to claim an extreme target was reached.
   - If the 200ms architecture achieves 380ms on the real benchmark (down from 10,000ms), report the **verified 380ms result**, explain the physical/system floor, and show the benchmark log.

---

## D5 — Designing the Outside Judge (External Oracle Catalog)

**Rule:** Never let the model grade its own ambitious work when an external oracle can be constructed.

Use the strongest oracle available for the domain:

| Task type | Weak judge (avoid) | Strong outside judge (use) |
|---|---|---|
| **Data science / Churn / Forecasting** | “The chart looks reasonable” or in-sample $R^2$ | Temporal holdout split, cross-validation, calibration curve, baseline comparison against a naive predictor |
| **Code / Bug Fix / Refactoring** | “The code looks clean and should work” | Deterministic failing-then-passing reproduction test, property-based tests, typechecker/linter, cross-platform CI run |
| **Performance / Systems Optimization** | “I replaced $O(n^2)$ with a hash map so it's faster” | Repeatable benchmark script (`hyperfine`, profiler trace, query `EXPLAIN ANALYZE`) on realistic data volume |
| **Financial / Accounting / Data ETL** | “I summarized the totals in the table” | Automated double-entry / conservation-of-mass reconciliation script asserting row counts and sum identities (`assert abs(diff) < 1e-6`) |
| **Process / Alerting Redesign** | “This new alert rule is much smarter” | Historical replay / backtest showing exact lead-time gain and false-positive rate on past incidents |
| **Visual / Frontend / 3D Artifact** | “Here is the HTML/Three.js code” | Headless browser render + console-error check + screenshot inspection (or live executable preview) |
