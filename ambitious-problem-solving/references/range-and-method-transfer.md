# Range and Cross-Disciplinary Method Transfer Reference

Read this file when a problem is trapped inside a single discipline's habits, when reframing a noun deliverable into functional verbs, when assembling constructive and adversarial (“red team”) specialist perspectives without falling into theatrical role-play, or when orchestrating parallel subagents across multiple fields.

---

## R1 — Replace Nouns with Functional Verbs

Naming a task by its conventional noun (“make a QBR deck,” “build a dashboard,” “write an onboarding doc,” “create a personal homepage”) locks both human and agent into the clichés of that medium.

Before selecting tools or disciplines, rewrite the noun as a **functional verb statement** that captures:
1. **Who** is acting or deciding;
2. **What causal understanding or action** must occur;
3. **Under what constraints, uncertainty, or adversary**;
4. **Within what time or attention budget**.

### Examples of Noun-to-Verb Reframing

| Surface Noun | Functional Verb Statement | New Fields Unlocked |
|---|---|---|
| “A quarterly business review (QBR) deck” | “Get busy executives to believe a causal story about what changed this quarter and commit to 3 resource reallocations under uncertainty in 30 minutes.” | Econometrics (causal inference), Investigative Journalism (narrative lead & evidence hierarchy), Short Selling / Forensic Accounting (adversarial falsification), Information Design (visual comparison) |
| “A personal portfolio website” | “Create an immediately memorable, tactile environment that demonstrates technical craft and invites exploration within 5 seconds of landing.” | 3D/Game Environment Design (Blender/Three.js spatial staging), Sound/Motion Design, Technical Directing |
| “An incident postmortem document” | “Reconstruct the exact causal chain of a failure without blame theater and alter system invariants so the entire failure class cannot recur.” | Aviation/Human-Factors Safety (Swiss-cheese / control-loop analysis), Chaos Engineering (fault injection), Formal Verification / Property Testing |
| “Customer churn survey analysis” | “Detect why paying users abandon the product before they self-report, separating polite excuses from behavioral drop-off.” | Biostatistics (survival/hazard modeling), Behavioral Economics (revealed vs. stated preference), UX Forensics (session-replay friction analysis) |

---

## R2 — Assemble the Crew by Method, Never by Role-Play

Once the functional verbs are clear, ask: **If the stakes were existential, what team of specialists would we assemble?**

Select **2 to 4 complementary disciplines**:
- **Constructive specialists** who build, model, or stage the work (e.g., biostatistician, investigative journalist, game technical artist, systems architect).
- **Adversarial / Red-Team specialists** whose job in the real world is to find flaws, fraud, fragile assumptions, or hidden risk (e.g., short seller, forensic accountant, opposing trial counsel, penetration tester, replication-crisis methodologist).

### The Strict Anti-Roleplay Translation Rule

**Warning:** Asking a model to *write like* a short seller or *role-play* a journalist produces cringeworthy, theatrical transcripts (“*adjusts fedora* Listen here, kid, these numbers stink...”) without improving the actual work.

Never adopt a persona's voice, costume, or fictional biography. Instead, translate each selected discipline into a **Method Specification Table** before executing:

| Discipline | 1. Core Skepticism / Question | 2. Concrete Method or Instrument | 3. Target Failure Mode Hunted |
|---|---|---|---|
| **Short Seller** | “Which growth metric is masking deteriorating unit economics or cohort decay?” | Cohort retention decomposition; CAC payback vs. LTV sensitivity; customer concentration check | Vanity top-line growth hiding accelerating churn or margin compression |
| **Forensic Accountant** | “Do the reported summary numbers reconcile 1:1 with raw transaction ledgers?” | Double-entry reconciliation; Benford/distribution anomaly checks; revenue-recognition timing audit | Unexplained adjustments, survivorship bias in filtered rows, silent denominator changes |
| **Investigative Journalist** | “What is the single most consequential verified fact, and what primary record proves it?” | Nut-graf / inverted-pyramid structuring; primary-source corroboration; stripping weasel words | Buried ledes, passive-voice evasion (“mistakes were made”), claims without primary evidence |
| **Biostatistician / Epidemiologist** | “Is this correlation an artifact of confounding, right-censoring, or Simpson's paradox?” | Kaplan-Meier survival curves; Cox proportional hazards; stratified subgroup checks | Naive average comparisons that ignore tenure censoring or cohort mix shifts |
| **Motion / 3D / Game Designer** | “How do spatial layout, pacing, and visual hierarchy guide attention without text walls?” | Scene staging (Blender/WebGL/SVG), state-transition choreography, progressive visual reveal | Static, text-dense walls that fail to convey state changes or spatial relationships |

---

## R3 — Cross-Medium and Cross-Tool Transfer

Range also means using **executable tools from adjacent domains** that users rarely think to invoke for their task:

- **3D & Spatial Tools (e.g., Blender, Three.js, shaders)** for web/interface design, architectural visualization, or physical intuition explanations.
- **Operations Research & SMT Solvers (e.g., Z3, OR-Tools, ILP)** for scheduling, configuration validation, or policy conflict detection instead of brittle handwritten heuristics.
- **Audio / Video / Programmatic Animation (e.g., Manim, FFmpeg, WebAudio, Remotion)** when temporal dynamics explain a phenomenon better than static prose.
- **Database Engines (e.g., DuckDB, SQLite)** on local CSV/JSON/log directories instead of fragile bash/regex pipelines or loading raw files into LLM context.

Before reaching for an unconventional tool, verify:
1. **Is the tool installed or cleanly installable in the current environment?**
2. **Does it solve the functional verb better than the standard medium, or is it a gimmick?** If a clean static chart answers the question in 2 seconds, a 3D WebGL scene is ornamental bloat—not ambition.

---

## R4 — Multi-Agent / Subagent Orchestration for Range

When your runtime supports subagents or parallel task delegation and the problem warrants deep multi-angle work:

1. **Decompose by method and raw data slice, not by persona.**
   - *Bad subagent brief:* “You are a skeptical Wall Street short seller. Critique this business plan.”
   - *Good subagent brief:* “Load `raw_subscriptions.parquet` and `invoices.csv`. Run a cohort survival and net-dollar-retention decomposition by acquisition channel. Test the hypothesis that Q3 growth was driven by discounting that increased 60-day churn. Return the SQL/Python script, verified table, and any falsified assumptions.”
2. **Keep subagents independent and evidence-bound.**
   - Require every subagent to return: (a) the exact command/script run, (b) the raw evidence or test output, and (c) the surviving conclusion.
3. **Synthesize via conflict resolution.**
   - In the parent agent, reconcile where the constructive analysis and the adversarial red-team analysis disagree by checking the raw substrate directly.
