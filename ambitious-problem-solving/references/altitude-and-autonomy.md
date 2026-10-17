# Altitude and Autonomy Reference

Read this file when elevating a one-off artifact into a decision-driving output, redesigning a recurring human workflow into a continuous system, or auditing whether an agent has the environment prerequisites required to operate autonomously at a higher abstraction.

---

## A1 — The Altitude Ladder: From Artifact to System

When a user assigns a task, they usually specify **their best guess at an intermediate artifact** (a slide deck, a status report, a single bug fix, a spreadsheet update) rather than the outcome that artifact exists to produce.

To find the right altitude, ask: **What happens in the meeting, workflow, or system right after this task is finished?**

| Level | Focus | Core question | Typical deliverable |
|---|---|---|---|
| **L0 — Literal Task** | The requested medium/artifact | “How do I fill in or complete what was asked?” | Updated template, isolated patch, surface summary |
| **L1 — Causal Sensemaking** | The underlying reality | “What actually changed in the raw data, why did it change, and what should we do about it?” | Evidence-backed root-cause diagnosis from primary data |
| **L2 — Decision Forcing** | Action under uncertainty | “Given everything observed, which 3 decisions are most urgent right now, and what are the trade-offs?” | Ranked decision memo with concrete options and for/against arguments |
| **L3 — Systemic Replacement** | Durable loop / invariant | “Why does this manual review or task exist at all? How do we catch the problem earlier and continuously?” | Automated monitor/workflow backtested on history and deployed in shadow mode |

### Worked progression (Quarterly Business Review example)

- **L0:** Update the numbers in the existing QBR slide template.
- **L1:** Ingest raw revenue, usage, support, and cohort logs; determine what materially changed this quarter, why, and what interventions follow.
- **L2:** Identify the three most urgent resource-allocation or product decisions leadership faces this week, and draft the strongest case for and against each option.
- **L3:** Recognize that QBRs exist so leadership catches drift early and reallocates capital and people. Design a continuous anomaly-and-reallocation trigger, **prove on the last 4–8 quarters of historical data that it would have flagged real problems weeks earlier than the quarterly deck**, and run it alongside the existing QBR for one quarter.

---

## A2 — Tell-Tale Signs That Altitude Elevation Is Warranted

Elevate altitude when one or more of these signals are present:

1. **A meeting follows the artifact:** If humans will sit in a room to interpret the artifact and decide what to do, do the causal interpretation and decision-framing up front (L1 -> L2).
2. **The task is a recurring calendar ritual:** Weekly triage, monthly reporting, quarterly reviews, or release checklists usually compensate for slow manual sensemaking. Ask what continuous mechanism could detect the signal at the moment it occurs (L3).
3. **The user is fixing the Nth instance of the same failure class:** Fixing one crash, one broken migration, or one data-pipeline drift invites the question: *what invariant should hold continuously, and how can the system enforce it?*

### When NOT to elevate altitude

- **Purely expressive or aesthetic work:** Writing a poem, scoring a short film, or crafting a personal note does not have a hidden “resource-allocation meeting” behind it. Keep the focus on Depth and Range if requested, not bureaucratic abstraction.
- **Ungrounded abstractions (“Go make money”):** Never escalate to a goal level where the agent lacks causal levers, observability, and a fast verification signal. An abstraction level is valid only if the agent can **observe state, take bounded actions, and verify outcomes** at that level.
- **Urgent tactical blockers:** If a production server is down or a user needs a 2-line hotfix in 60 seconds, execute L0/L1 immediately; propose L3 only after the fire is out.

---

## A3 — The Backtest-and-Shadow Rule for Process Replacement

Never propose deleting or replacing an existing human workflow based on a theoretical redesign. High-altitude process replacements must pass two gates before cutover:

1. **Historical backtest (retrospective proof):**
   - Run the proposed detector, scoring rule, or automated workflow against historical incidents, past quarters, or git history.
   - Measure: *Would this mechanism have caught the actual problems earlier? How many false alarms would it have generated?*
2. **Parallel shadow run (prospective proof):**
   - Run the new system **beside** the current human workflow for a defined period (e.g., one sprint, one release cycle, or one quarter).
   - Compare its recommendations or automated patches against human decisions before removing human-in-the-loop checkpoints.

---

## A4 — The 4-Prerequisite Audit for Autonomous Loops

Asking an agent to “keep our app crash-free” or “continuously keep documentation in sync with code” fails if you treat it as a prompt change instead of a **workflow and environment change**.

Before designing or activating an autonomous higher-altitude loop, audit these four prerequisites:

### 1. Automated Signal Ingestion
- **Requirement:** Can the agent fetch raw crash reports, error telemetry, failing CI logs, or business metrics directly via CLI, API, or MCP without a human copy-pasting snippets?
- **If missing:** Build or configure the read-only connector/fetcher script first.

### 2. Deterministic State-to-Source Mapping
- **Requirement:** Can the agent map a production symptom (e.g., `app_version: 4.12.3`, stack trace address, customer cohort ID) to the exact git commit, symbol table, feature flag state, or database schema?
- **If missing:** Add build-metadata injection, release-tag mapping, or symbolication lookup before attempting autonomous triage.

### 3. Independent Reproduction Environment
- **Requirement:** Does the agent have access to the target runtime, OS/platform matrix (Linux, macOS, Windows, browser, container), and test fixtures needed to reproduce the failure independently?
- **If missing:** Provision a reproducible local harness, container, or cross-platform runner so the agent is not guessing in the dark.

### 4. Closed-Loop External Verification
- **Requirement:** Can the agent prove—via an automated test, regression suite, canary metric, or invariant check—that its proposed fix resolves the reproduced issue and introduces no regressions?
- **If missing:** Write the reproduction test and verification gate before allowing autonomous code or config mutations.

### How to report an Autonomy Audit

When a user asks for a high-altitude autonomous workflow, output a concrete readiness table:

```text
Target invariant: [e.g., Keep desktop client crash-free across releases]
1. Signal ingestion:       [READY / MISSING] -> [exact tool/script or gap to close]
2. State-to-source map:    [READY / MISSING] -> [exact version->commit mapping or gap]
3. Reproduction runtime:   [READY / MISSING] -> [exact test environment or gap]
4. Verification oracle:    [READY / MISSING] -> [exact test/benchmark command or gap]
Immediate next action:     [Wire up the first missing prerequisite OR run shadow loop]
```
