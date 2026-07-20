# skills

A public collection repo for reusable Hermes and skills-compatible agent skills.

## Included skills

- **`hermes-deep-research`** — Hermes-native deep research skill for multi-source synthesis, verification, parallel subresearch, and decision-grade reporting.
- **`dspy-hermes-runtime-auth`** — reuse Hermes Agent's active runtime provider, base URL, and credentials inside DSPy without copying API keys.
- **`dspy-rlm-hermes-runtime-auth`** — companion skill for deciding when `dspy.RLM` is the right abstraction and wiring it to Hermes runtime auth cleanly.
- **`tasker`** — automating Android tasks, profiles, scenes, and actions using Tasker configurations, JavaScriptlets, intents, and shell commands.
- **`teach`** — evidence-backed tutoring runtime for stateful lessons, practice, feedback, transfer, and spaced review.
- **`agy-cli`** — use Antigravity CLI (`agy`) for agent sessions, non-interactive prompts, model discovery, and plugin management.
- **`local-web-extract`** — extract complete URL content through self-hosted Firecrawl with deterministic Crawl4AI fallback.

## Install

Use this collection repo with any skills-compatible agent:

```bash
npx skills add https://github.com/alexferrari88/skills --skill <skill-name>
```

Examples:

```bash
npx skills add https://github.com/alexferrari88/skills --skill hermes-deep-research
npx skills add https://github.com/alexferrari88/skills --skill dspy-hermes-runtime-auth
npx skills add https://github.com/alexferrari88/skills --skill dspy-rlm-hermes-runtime-auth
npx skills add https://github.com/alexferrari88/skills --skill tasker
npx skills add https://github.com/alexferrari88/skills --skill teach
npx skills add https://github.com/alexferrari88/skills --skill agy-cli
npx skills add https://github.com/alexferrari88/skills --skill local-web-extract
```

## Skill summaries

### `hermes-deep-research`
Best for evidence-led deep research where important claims need full-source reading, cross-checking, and structured output.

### `dspy-hermes-runtime-auth`
Best for portable DSPy code that should follow Hermes runtime changes across providers, models, and custom endpoints without duplicating secrets.

### `dspy-rlm-hermes-runtime-auth`
Best for long-context tasks where the model should recursively inspect and compute over a large context object instead of forcing one giant prompt through a single context window.

### `tasker`
Best for creating, modifying, or debugging Android automation profiles, tasks, scenes, custom JavaScriptlets, shell commands, and intents in Tasker.

### `teach`
Best for adaptive tutoring sessions where the learner should attempt, receive feedback, retry, transfer, and leave durable learning records instead of just reading an explanation.

### `agy-cli`
Best for running and managing Antigravity CLI (`agy`) sessions, models, plugins, and non-interactive prompts from an agent workflow.

### `local-web-extract`
Best for complete URL extraction when ordinary agent fetching fails or is incomplete, using self-hosted Firecrawl first and Crawl4AI as a visible fallback.

## License

MIT
