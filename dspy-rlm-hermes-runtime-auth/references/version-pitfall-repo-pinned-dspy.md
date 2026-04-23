# Bootstrap RLM in a Repo That Pins Older DSPy

Use this when the target repo or project environment does not expose `dspy.RLM`.

## Symptom

You install the repo normally, then check:

```python
import dspy
hasattr(dspy, "RLM")
```

and get `False`.

A repo can pin an older DSPy even when its normal install flow succeeds. In one live verification case, the standard sync path installed DSPy `3.0.4`, and `dspy.RLM` was missing.

## Recommended fix

Do not fight the repo env.

Run a separate temporary environment with a known-good DSPy version:

```bash
PYTHONPATH=/path/to/hermes-agent \
uv run --with dspy-ai==3.1.3 --with openai python your_script.py
```

## Minimal pattern

1. Write `hermes_dspy_runtime.py` locally from the skill template.
2. Put the Hermes agent package on `PYTHONPATH` so imports like `hermes_cli...` and `agent.auxiliary_client...` resolve.
3. Verify the runtime before doing any real work.

### Sanity checks

```python
import dspy
print(dspy.__version__)
print(hasattr(dspy, "RLM"))
```

Expected:
- DSPy `3.1.3` or newer in the temp env
- `True` for `hasattr(dspy, "RLM")`

### Tiny end-to-end smoke test

```python
import dspy
from hermes_dspy_runtime import load_hermes_dspy_lm

lm = load_hermes_dspy_lm(max_tokens=300)
dspy.configure(lm=lm)

rlm = dspy.RLM("context, query -> answer", sub_lm=lm, max_iterations=6)
result = rlm(context="alpha is first. beta is second.", query="What is alpha?")
print(result.answer)
```

## When to use this workaround

Use it when:
- you only need RLM for analysis, not to modify the repo itself
- the repo pins an older DSPy
- you want to preserve Hermes runtime auth without rewriting provider logic

## When not to use it

Do not use this workaround if the real goal is to upgrade the repo itself. In that case, update the project dependencies intentionally instead of sneaking around them.
