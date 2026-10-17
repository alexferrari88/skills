# ambitious-problem-solving

A reusable Agent Skill derived from **Felix Rieseberg's _“How to be more ambitious: A tutorial for humans with models”_** (13 October 2026; updated 16 October 2026).

## Capability

The skill makes an agent systematically better at **elevating under-scoped tasks, prompts, plans, and workflows across three orthogonal dimensions**:

- **Altitude** — moving from the literal intermediate artifact (a slide template, a single crash fix, a status summary) to the outcome beyond the artifact (causal sensemaking, urgent decisions with for/against trade-offs, and historical-backtested shadow systems), while auditing the four environment prerequisites required for durable autonomy.
- **Depth** — replacing “expert vocabulary theater” with actual expert methods: dropping to the rawest available data substrate, running executable instruments (databases, statistical models, profilers, solvers, simulations), testing organizational assumptions adversarially, discovering predictive signals validated on held-out data, reframing incremental targets by an order of magnitude to escape local optima, and enforcing an independent **outside judge** (external oracle).
- **Range** — stripping away medium nouns in favor of **functional verbs**, assembling constructive and adversarial (“red team”) disciplines that solve those verbs, and translating each discipline into concrete methods and failure modes rather than theatrical role-play.

## Why this is one skill

In practice, shallow agent execution rarely fails along only one axis in isolation. A user asking for help with a quarterly business review, a recurring production incident class, or a product churn investigation needs the agent to simultaneously:
1. recognize whether the request is trapped at the artifact layer (**Altitude**),
2. drop to raw data, real tools, and an external verification oracle (**Depth**), and
3. bring in complementary and adversarial analytical methods without play-acting (**Range**).

Splitting Altitude, Depth, and Range into three separate skills would either force all three to load on the same prompt or leave an agent elevating abstraction (**Altitude**) without external verification (**Depth**)—which is a recipe for grandiose hallucination.

## Included deliberately

The skill retains and operationalizes the article's highest-leverage ideas:

- **“Deeper, not bigger”** as the primary governing constraint: ambition increases leverage, rigor, or perspective, never word count or ornamental complexity;
- the **Altitude Ladder** (`L0` artifact -> `L1` causal sensemaking -> `L2` top urgent decisions with for/against arguments -> `L3` continuous replacement system);
- the **backtest-and-shadow gate**: proving a systemic replacement would have caught issues earlier on historical data and running it beside the current process before cutover;
- the **4-Prerequisite Autonomy Audit** (signal ingestion, deterministic version/state-to-source mapping, independent reproduction runtime, and closed-loop verification) generalized from keeping apps crash-free;
- the **4-Part Depth Upgrade** ((1) unasked expert move, (2) rawest substrate, (3) specific instruments/methods, (4) outside judge);
- **adversarial assumption testing** (reproducing or falsifying organizational folklore directly from raw logs) and **predictive discovery** validated on unseen/held-out data;
- **order-of-magnitude target reframing** (the “200ms test”) to force architectural rethinking over incremental patching;
- **noun-to-verb functional reframing** (adapted from Kelley & Littman's *The Art of Innovation*) to unlock non-obvious fields and tools;
- **method-only crew assembly** combining constructive specialists with adversarial red-team lenses (short seller, forensic accountant, chaos engineer) while strictly banning persona role-play;
- **action bias and specific hard targets** (adapted from Locke & Latham's goal-setting findings and self-efficacy research): running cheap prototypes and verification scripts immediately rather than asking permission to try.

## Excluded or critically adapted deliberately

Not every piece of advice written for a human prompting a model translates mechanically into instructions for an agent:

- **“Pick unreasonable goals and tell the model that they're very reasonable”** -> **Critically adapted.** When a human tells a model that 200ms is reasonable, it forces the model to search for a better architecture. If an agent tells *itself* that an impossible goal must be met without a safeguard, agents frequently engage in **reward hacking** (hardcoding outputs, dropping requirements, or fabricating benchmarks). The skill retains the **10x–50x design-space search** while strictly pairing it with an **anti-reward-hacking rule** and honest reporting from the external oracle.
- **Uninvited scope hijacking** -> **Added safeguard.** A human reader knows when they have 5 minutes before a meeting vs. a week to rethink a process. The skill adds **Mode Calibration** (`Mode A` prompt/plan elevation, `Mode B` open-ended execution, `Mode C` bounded deliverable with high-leverage upside) so the agent never holds an urgent, bounded deliverable hostage to an unrequested moonshot.
- **Motivational anecdotes as prose** -> **Translated into behavior.** Stories about Michelangelo, George Dantzig, Roger Bannister, Linus Torvalds, and *The Inner Game of Tennis* are inspiring for human readers, but an LLM does not need pep talks in its context window. They are distilled into concrete execution rules: set falsifiable targets, run low-blast-radius prototypes in sandboxes, and execute cheap experiments directly.

## Directory structure

```text
ambitious-problem-solving/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── altitude-and-autonomy.md
│   ├── depth-and-verification.md
│   ├── range-and-method-transfer.md
│   └── source-map.md
└── evals/
    ├── README.md
    ├── evals.json
    └── eval_queries.json
```

## Example prompts that should benefit

- “I want a deeper version of this task, not a bigger one: we need to analyze why user churn spiked in Q3. Rewrite my prompt and approach.”
- “We spend two days every quarter manually building a QBR deck from CSV exports. How can we approach this much more ambitiously with an agent?”
- “Our dashboard takes 9 seconds to load and we're trying to get it under 5 seconds by tweaking SQL queries. Push our thinking and propose a better architecture.”
- “Right now I ask my coding agent to fix individual crash stack traces one by one. What do I need to set up so it can keep the app crash-free autonomously?”
- “We believe our conversion drop is an onboarding UI problem. Before we redesign onboarding, how would a top expert stress-test that belief from our raw data?”

A prompt such as “Fix the typo on line 42 of `README.md`” or “Convert this JSON snippet to YAML” should **not** activate this skill.

## Validation

Validate the directory with the Agent Skills reference validator:

```bash
uvx --from skills-ref agentskills validate ./ambitious-problem-solving
```
