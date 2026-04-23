# Experimental web_search bridge

This note documents an additive experiment for `dspy-rlm-hermes-runtime-auth`.

## Goal
Expose Hermes `web_search` inside `dspy.RLM` without modifying Hermes core code or the stable templates.

## Reversibility
This experiment is reversible because it only adds:
- `templates/hermes_dspy_rlm_web_search_experiment.py`
- this note
- backup snapshots under `references/backups/`

The existing stable files remain intact:
- `SKILL.md`
- `templates/hermes_dspy_runtime.py`

To restore the pre-experiment state in practice, ignore or delete the experimental template and note. The backed-up copies remain available for full restoration if needed.

## What we learned
- A Hermes-backed `web_search` bridge can work inside `dspy.RLM` from the skill/template layer alone; no Hermes core or DSPy core patch was required for the experiment.
- A forced micro-test succeeded: the RLM called `web_search("recursive language models alex zhang")` and returned the top result title.
- On this machine, the default DSPy `PythonInterpreter` failed early because Deno could not resolve `npm:pyodide` from the local setup. In the experimental template, adding `--node-modules-dir=auto` to the interpreter command fixed that local startup problem without touching stable templates.
- Wrapping the bridge tool in `try/except` and returning a compact error dict is better than letting host exceptions propagate; otherwise the model just sees a vague tool/environment failure and cannot reason over it.
- Compact tool returns are important. The current bridge intentionally returns only `title`, `url`, and `description` for the top N search results to keep REPL output manageable.

## Practical implication
For future additive experiments, start with:
- read-only tools
- compact return schemas
- explicit call logging
- local interpreter tweaks in the experimental layer only
