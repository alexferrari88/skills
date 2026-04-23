---
name: dspy-hermes-runtime-auth
description: Reuse Hermes Agent's active runtime provider and credentials inside DSPy programs, including Predict, ChainOfThought, and RLM, without duplicating API keys. Designed to be provider-aware and shareable across Hermes installations.
version: 0.1.0
author: Alex Ferrari, Hermes Agent
license: MIT
---

# DSPy + Hermes Runtime Auth

## When to use

Use this skill when **both** are true:
- you want a DSPy program to reuse **the same provider/base URL/API credential Hermes is already using**
- you want that wiring to survive provider/model changes without rewriting the DSPy code path

Good fits:
- `dspy.Predict`, `ChainOfThought`, or other DSPy modules that should follow Hermes runtime selection
- `dspy.RLM` or other long-context workflows where the LM should inherit Hermes auth/config
- notebooks, scripts, and repo code you want to share with other Hermes users who may run different providers
- cases where you may switch between `openrouter`, `anthropic`, `openai-codex`, or a custom endpoint and still want one loader function

Prefer a simpler path when:
- you are writing a one-off script for a single fixed provider and do not care about Hermes runtime portability
- the code is intentionally tied to a vendor SDK rather than DSPy's abstraction layer

## What this skill does

It provides a **portable factory pattern**:
1. resolve Hermes runtime credentials with `hermes_cli.runtime_provider.resolve_runtime_provider()`
2. map that runtime into a DSPy-compatible LM
3. use the resulting LM in ordinary DSPy modules or `dspy.RLM(..., sub_lm=lm)`

The design goal is portability across:
- provider
- model
- base URL
- auth mode

## Verified shape

Verified locally as a small working example against one Hermes installation:
- DSPy `3.1.3`
- `dspy.RLM` available
- `deno` installed
- helper works for ordinary `dspy.Predict(...)` and a tiny `dspy.RLM(...)` run
- the live verification environment happened to resolve to `openai-codex`, which is why the template includes a narrow Codex compatibility branch

Interpret this as:
- **generic design** across Hermes providers via `resolve_runtime_provider()`
- **concrete runtime verification** on one live install

## Important limits

- Do **not** run billable benchmark/eval loops without the user's approval.
- Do **not** print tokens, `.env`, or auth-store contents.
- `dspy.RLM` needs Deno/Pyodide available on the machine.
- Some providers may need provider-specific adaptation even when runtime auth resolution succeeds.
- Today, the explicitly verified special-case branch is the Codex/Responses path; other providers follow the standard DSPy/OpenAI-compatible route.

## Recommended path

Use the helper template in `templates/hermes_dspy_runtime.py`.

## Steps

### 1. Resolve Hermes runtime

```python
from hermes_cli.runtime_provider import resolve_runtime_provider
runtime = resolve_runtime_provider()
```

This returns the active runtime choice Hermes would use, including:
- `provider`
- `api_mode`
- `base_url`
- `api_key`
- `source`

### 2. Build a DSPy LM from that runtime

Routing defaults:
- `chat_completions` → `dspy.LM(..., model_type="chat")` with OpenAI-compatible routing
- `anthropic_messages` → `dspy.LM(..., model_type="chat")` with `anthropic/...` model naming
- `codex_responses` → custom `BaseLM` wrapper backed by Hermes's Codex auxiliary shim, because that endpoint needed special handling in live testing

This means the helper is **generic by default** and only becomes provider-specific where the runtime contract forced it.

### 3. Override provider or model when needed

```python
# Use the currently active Hermes runtime
lm = load_hermes_dspy_lm()

# Force a different Hermes provider while still using Hermes auth/config
lm = load_hermes_dspy_lm(requested_provider="anthropic")

# Keep the provider but override the model
lm = load_hermes_dspy_lm(model="claude-sonnet-4-5-20250929")

# Override both
lm = load_hermes_dspy_lm(
    requested_provider="openrouter",
    model="google/gemini-3-flash-preview",
)
```

### 4. Configure DSPy

```python
import dspy
lm = load_hermes_dspy_lm()
dspy.configure(lm=lm)
```

### 5. Use with RLM

```python
import dspy

lm = load_hermes_dspy_lm()
dspy.configure(lm=lm)

rlm = dspy.RLM(
    "context, query -> answer",
    sub_lm=lm,
    max_iterations=20,
)

result = rlm(
    context=long_text,
    query="Answer the question using programmatic exploration."
)
print(result.answer)
```

## Files

- `templates/hermes_dspy_runtime.py` — provider-aware DSPy loader
- `references/provider-compatibility.md` — what is generic vs what is provider-specific today

## Anti-patterns

Do **not**:
- hardcode `OPENAI_API_KEY` when Hermes is actually using another provider
- assume a fixed provider/model combination instead of reading Hermes runtime state
- dump resolved runtime secrets to stdout/logs
- use RLM for short/simple prompts where standard DSPy or ordinary retrieval is already enough
- bypass `resolve_runtime_provider()` unless you intentionally want a different provider than Hermes

## Output expectation

This skill is for **runtime wiring**. Use it when the bottleneck is: “make DSPy follow Hermes runtime auth and provider routing cleanly, even as the runtime changes.”
