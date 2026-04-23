# When to Use RLM

This note explains **when `dspy.RLM` is the right abstraction**.

It is synthesized from:
- the RLM paper (`arXiv:2512.24601`)
- Alex Zhang's blog/docs
- ecosystem writeups
- X/Twitter discussion surfaced via Grok search, prioritizing `@lateinteraction`, `@raw_works`, and `@a1zhang`

## Core mental model

RLM is best when the context should be treated as an **object to work over**, not just text to stuff into a prompt.

The model should be able to:
- inspect the context programmatically
- transform it
- recurse over subsets
- aggregate intermediate results

That is a different use case from:
- ordinary prompting
- simple retrieval
- shallow summarization/compaction

## The strongest use cases

### 1. Deep research over large corpora
Use RLM when the system needs to reason across many documents, not just retrieve one quote.

Why it fits:
- the model can inspect many candidate documents
- recurse on subsets
- compare evidence across sources
- aggregate findings programmatically

This is close to the paper/blog's BrowseComp-Plus / deep-research framing.

### 2. Information aggregation
Use RLM when the answer is assembled from many local facts spread across the context.

Why it fits:
- retrieval may find one relevant passage but miss the global structure
- summarization may erase exactly the detail you need
- RLM can compute across many slices before answering

### 3. Code repository understanding
Use RLM when understanding requires moving across many files/modules/functions.

Why it fits:
- the model can inspect code selectively
- recurse into files or subsystems
- compare implementation fragments
- synthesize global behavior from local reads

### 4. Dense-access long-context tasks
Use RLM when the answer depends on much of the context, not a tiny subset.

Why it fits:
- context compaction is risky
- the model needs broad coverage
- pairwise or cross-document comparisons matter

This is the spirit of OOLONG-style tasks and other "almost every line matters" settings.

### 5. Programmatic context operations before answering
Use RLM when the task naturally involves:
- filtering
- chunking
- counting
- grouping
- comparing
- map/reduce style passes

If the model should write code to manage the context before producing an answer, that is an RLM signal.

## When not to use RLM

Do **not** use RLM when:
- a normal DSPy call solves it cleanly
- retrieval is enough because only a few passages matter
- the task is mostly summarization/generation
- the challenge is external tool use rather than recursive understanding of one large context object

## Practical decision rule

Ask:

1. Does the answer depend on **many dispersed details**?
2. Would compaction or simple retrieval likely lose important structure?
3. Would it help if the model could write code to inspect and recurse over the context?

If the answer is **yes** to all three, `dspy.RLM` is a strong candidate.

## Important nuance from ecosystem discussion

RLM is not just “sub-agents” or “tool use.”

The important distinction is that the model is using symbolic/programmatic recursion to understand a context object, rather than merely delegating a few verbalized subtasks.

That is why RLM often makes sense for:
- huge corpora
- codebases
- long research bundles
- comparison-heavy long-context reasoning

and often does **not** make sense for:
- short prompts
- ordinary QA
- simple RAG
- routine generation
