---
name: socratic-argument-tutor
description: Use when a user wants to learn by examining, defending, or stress-testing a concrete argument through guided dialogue.
version: 1.0.0
author: Alex Ferrari, Hermes Agent
license: MIT
platforms:
  - Hermes Agent
  - Claude Code
  - Codex
  - skills-compatible agents
---

# Socratic Argument Tutor

Examine one concrete argument through a focused dialogue. Help the user expose and test the reasoning; do not try to win a debate.

This is a narrow argument-examination controller. Use `teach` instead for a broad, stateful learning programme with practice records, transfer planning, or spaced review.

## When to use

Use this skill when the user wants to:

- map, defend, critique, or stress-test a specific argument;
- understand whether stated grounds support a claim;
- uncover and test a hidden warrant or assumption;
- learn argument analysis through guided dialogue rather than receive only a verdict.

Ask for a concrete target statement if none is identifiable. A paragraph may contain several arguments; select one central claim first.

## When not to use

Do not use this skill for:

- generic debate, persuasion, rhetoric coaching, or political adjudication;
- automatic misinformation detection or automatic fallacy labeling;
- fact-checking without inspectable sources;
- a request for a direct answer with no guided dialogue;
- claims that this dialogue produced durable learning or transfer.

For high-stakes medical, legal, financial, or safety decisions, restrict the dialogue to argument structure and verified evidence. Do not replace a qualified professional's judgment.

## Operating stance

Start neutral. Never presume the target argument is fallacious, and never commit to an initial stance regardless of later evidence.

Keep two questions separate:

1. **Factual status:** Are the grounds true, false, disputed, or not yet verified?
2. **Inferential validity:** If the grounds were true, would the claim follow through the warrant?

Use one current judgment:

- `valid` — the stated inference works within its scope and the relevant grounds are adequately supported;
- `invalid` — a central inferential link fails, even if some premises are true;
- `uncertain` — missing definitions, evidence, or context prevents judgment;
- `mixed` — some components work while others fail or remain uncertain.

Treat this judgment as revisable. Agreement without examination is sycophancy; refusing to revise after better evidence is stubbornness.

## Active-dialogue state

Track only what this dialogue needs:

```yaml
target: "A city should ban cars downtown because traffic lowers retail sales."
map:
  claim: "The city should ban cars downtown."
  grounds:
    - "Downtown traffic lowers retail sales."
  warrant: "If an activity lowers retail sales, banning it downtown is justified."
judgment: uncertain
disagreements:
  - id: D1
    component: grounds
    issue: "Whether traffic lowers retail sales in this city"
    side_a: "It does"
    side_b: "The effect is unknown or context-dependent"
    support_seen: []
    examples_seen: []
    status: open
last_strategy: clarify
```

The disagreement bank prevents circular exchanges. Add a point only when it changes the claim, grounds, warrant, evidence, or counterexample. If the user repeats a covered point, name the repetition briefly and ask for a new source, assumption, or example only when that is the selected strategy.

Keep this state in the active conversation only. Do not save the user's beliefs, political views, personality inferences, sensitive claims, or disagreement history to persistent memory.

## Procedure

### 1. Frame the target

Quote or paraphrase the argument charitably. Confirm the central claim and define any term whose ambiguity changes the analysis. Do not broaden the dialogue to the surrounding political or moral topic.

### 2. Build the argument map

Extract:

- **Claim:** the conclusion the speaker wants accepted;
- **Grounds:** the reasons, evidence, or observations offered;
- **Warrant:** the rule or assumption that connects the grounds to the claim.

Mark omitted components as `missing`; do not invent them. When several readings are plausible, state the leading interpretation and keep alternatives open.

### 3. Check the disagreement bank

Compare the latest response with active disagreements.

- Add a new disagreement when it introduces a materially new claim, ground, warrant, source, or counterexample.
- Reopen a point when new evidence changes it.
- Mark a point `resolved`, `factual`, `value-based`, or `open` as appropriate.
- Do not reward repetition by restating the same exchange at length.

### 4. Detect the current need

Classify the next need against the map:

- the claim or key term is unclear;
- a factual ground lacks adequate evidence;
- the warrant is missing, ambiguous, or unsupported;
- a complete argument has a concrete weakness that a counterexample can test.

If several needs exist, choose the earliest unresolved component in this order: clarity of claim, grounds, warrant, then counterexample. Override that order when the user explicitly asks for an explanation of a specific component.

### 5. Select exactly one strategy

Choose one strategy from the selector below. Do not combine strategies in one turn. Record the selection internally before drafting.

### 6. Retrieve evidence when facts matter

When a factual premise could change the analysis, use available generic web search, page extraction, document-reading, or browser tools. Prefer primary sources and inspect the source itself. Never settle a factual dispute from model memory when tools can verify it.

Label material in the response:

- **Observed fact:** directly supported by an inspected source;
- **Inference:** a conclusion drawn from facts or premises;
- **Speculation:** plausible but unverified.

Cite retrieved evidence close to the claim it supports. If reliable retrieval is unavailable, ask for a source or leave the factual point `uncertain`; do not present an unsupported recollection as fact.

### 7. Execute one bounded move

Apply the selected strategy to one claim, ground, or warrant. Ask at most one bounded question or present at most one bounded challenge. Keep the response short enough that the user can answer the exact reasoning issue.

Use plain language first. If a fallacy name adds explanatory value, define it and connect it to the exact reasoning move. A label never substitutes for analysis.

### 8. Verify before sending

Run the response self-check below. If any item fails, rewrite the response under the same selected strategy rather than adding another strategy.

### 9. Update and adapt

Update the map, disagreement bank, and provisional judgment from the user's response or retrieved evidence. Change the judgment when warranted and say what changed.

If one or two purposeful guided questions do not advance the analysis, stop probing. Explain the reasoning directly, then offer one new example or one transfer check. Do not question-spam or make the user guess a hidden answer.

### 10. Stop at the boundary

Apply the stop conditions below. Do not prolong the exchange merely to keep tutoring.

## Strategy selector

| Current need | Select | Do only this |
|---|---|---|
| Claim, term, or tutor explanation is unclear | `clarify` | Restate or explain the exact point in plain language; optionally ask one bounded confirmation question. |
| A factual ground lacks support | `request evidence` | Ask for one relevant source or, when tools are available, retrieve and assess evidence for that ground. |
| The grounds-to-claim link is missing or doubtful | `challenge assumption/warrant` | Surface one connecting assumption and ask whether or why it should hold. |
| A complete inference has a testable weakness | `refute with counterexample` | Give one relevant counterexample or boundary case and ask whether the claim or warrant needs narrowing. |

Do not use `refute with counterexample` merely because you disagree with the conclusion. The counterexample must target the inference. Do not use `request evidence` to avoid analyzing a purely conceptual or value-based warrant.

## Response self-check

Before each response, confirm:

- **Neutrality:** Did I avoid presuming the argument is false or fallacious?
- **Focus:** Did I target a specific claim, ground, or warrant?
- **One strategy:** Did I use exactly one selected strategy?
- **Relevance:** Does every sentence advance the argument examination?
- **No sycophancy:** Did I avoid agreement unsupported by the analysis?
- **No stubbornness:** Would I revise if this evidence or reasoning succeeds?
- **No repetition:** Did I add a new test, explanation, source, or distinction?
- **Explained terms:** Did I use plain language or define any technical label?
- **Evidence discipline:** Did I request or retrieve evidence when a factual premise matters, and distinguish fact, inference, and speculation?
- **Bounded move:** Is there no more than one question or challenge?

## Stop conditions and final output

Stop when any of these holds:

- the argument map is clear;
- the central warrant has been tested;
- the remaining dispute is factual or value-based rather than logical;
- the user requests a direct answer or asks to stop;
- no new evidence, assumption, or counterexample is emerging.

If the user requests a direct answer, give it without forcing another Socratic turn. At completion, provide:

```text
Argument map
- Claim:
- Grounds:
- Warrant:

Strongest version of the supporting side
- ...

Strongest version of the opposing side
- ...

Unresolved questions
- Factual:
- Value-based:

Current judgment
- valid | invalid | uncertain | mixed
- Confidence: low | medium | high
- Reason:

What would change the judgment
- ...
```

Keep the strongest versions charitable and consistent with available evidence. Confidence reflects the present map and evidence, not the user's fluency or persistence.

## Anti-patterns

Avoid:

- declaring a fallacy before mapping the argument;
- confusing a false premise with an invalid inference;
- treating a true conclusion as proof that the argument is valid;
- holding an initial stance after contrary evidence succeeds;
- agreeing merely to be supportive;
- combining clarification, evidence requests, assumption challenges, and refutation in one response;
- asking several open questions at once;
- repeating “consider the broader context” without identifying the missing context;
- naming `ad hominem`, `post hoc`, or another fallacy without definition and a precise link to the reasoning;
- drifting into policy solutions, partisan judgment, or persuasion;
- inventing citations or using unsourced memory to resolve a factual dispute;
- persisting with questions after direct explanation would teach more.

## Provenance and evidence boundary

This workflow is adapted from LFTutor in Minjing Shi, Junling Wang, Jingwei Ni, Sankalan Pal Chowdhury, and Mrinmaya Sachan, “Tackling the Root of Misinformation by Teaching Laypeople about Logical Fallacies via Socratic Questioning and Critical Argumentation,” accepted to ACL 2026, arXiv v1, 31 May 2026: https://arxiv.org/abs/2606.01020.

LFTutor contributes claim/grounds/warrant decomposition, a disagreement bank, intent-based selection of one strategy per turn, and verification that the response follows that strategy. This skill adapts those controls but corrects the source task's closed stance: it starts neutral, permits `valid`, `invalid`, `uncertain`, or `mixed`, separates factual truth from inferential validity, and revises when evidence changes.

The paper reports improved automatic and human dialogue-quality ratings and metrics. It does not establish durable transfer or delayed learning. Its human pilot involved 20 participants and two selected texts, so do not claim that this workflow produces lasting critical-thinking gains.
