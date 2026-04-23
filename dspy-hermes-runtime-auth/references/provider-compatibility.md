# Provider Compatibility

This skill is designed to be **portable across Hermes installations**, but not every provider surface is identical.

## Generic by design

These parts are intended to work for most Hermes users without modification:
- resolve active runtime via `resolve_runtime_provider()`
- let Hermes decide provider, base URL, and credential source
- override `requested_provider` and/or `model` without rewriting the DSPy call site
- use the same loader for ordinary DSPy modules and `dspy.RLM`

## Expected standard paths

### OpenAI-compatible chat-completions runtimes
Expected shape:
- `api_mode = chat_completions`
- loader returns `dspy.LM(..., model_type="chat")`

Examples:
- OpenRouter
- many custom `/v1` endpoints
- other OpenAI-compatible providers supported by Hermes

### Anthropic Messages runtimes
Expected shape:
- `api_mode = anthropic_messages`
- loader normalizes model naming to `anthropic/<model>`
- still returns `dspy.LM(..., model_type="chat")`

## Explicit special case today

### Codex / Responses-style runtimes
Live testing showed that the ChatGPT Codex endpoint needed extra handling beyond bare `dspy.LM(..., model_type="responses")`.

So the template currently uses:
- a custom `BaseLM` wrapper
- Hermes's Codex auxiliary shim
- Codex-specific headers when available

This is a **compatibility branch**, not the core identity of the skill.

## Caveats

- Some provider/model combinations may still need small adapter branches.
- Custom endpoints can differ in subtle ways even when they claim OpenAI compatibility.
- Responses-style backends are the most likely to require special handling.
- A runtime can resolve successfully yet still have provider-specific request quirks.

## Publishing guidance

If you share this skill with other Hermes users:
- present `dspy-hermes-runtime-auth` as the canonical entrypoint
- state clearly which paths were live-tested vs expected-by-design
- avoid claiming universal provider coverage unless you have actually tested it

## Minimum verification checklist for another Hermes install

- `import dspy` works
- `resolve_runtime_provider()` returns a provider, base URL, and non-empty API key/token
- `dspy.Predict(...)` works with the loader
- if using RLM, `deno --version` works and a tiny `dspy.RLM(...)` call succeeds
