# Publish Blurb

## Short blurb

Reuse Hermes Agent's active runtime provider and credentials inside DSPy without copying API keys. This skill gives you a provider-aware loader for `dspy.Predict`, `ChainOfThought`, and `dspy.RLM`, so DSPy code can follow Hermes runtime changes across providers, models, and custom endpoints.

## README / skill hub blurb

`dspy-hermes-runtime-auth` lets DSPy programs reuse the same provider, base URL, and credentials that Hermes Agent is already using.

Instead of hardcoding `OPENAI_API_KEY`, vendor SDK setup, or a single fixed provider, the skill resolves Hermes runtime state through `resolve_runtime_provider()` and maps it into a DSPy-compatible LM.

That gives you one portable entrypoint for:
- `dspy.Predict`
- `dspy.ChainOfThought`
- `dspy.RLM`
- scripts, notebooks, and shared repo code that should keep working when a Hermes user changes provider or model

The design is generic by default and provider-aware where needed. Most OpenAI-compatible chat-completions paths follow the standard DSPy route. A narrower compatibility branch handles Codex-style Responses runtimes because that endpoint needed special handling in live testing.

Use this skill when you want DSPy to inherit Hermes auth and provider routing cleanly, without duplicating secrets or rewriting your code every time the runtime changes.

## One-line tagline

Make DSPy follow Hermes runtime auth and provider routing cleanly, even as the runtime changes.
