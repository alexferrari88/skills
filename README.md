# skills

A public collection repo for reusable Hermes and skills-compatible agent skills.

## Included skills

- **`hermes-deep-research`** — Hermes-native deep research skill for multi-source synthesis, verification, parallel subresearch, and decision-grade reporting.
- **`dspy-hermes-runtime-auth`** — reuse Hermes Agent's active runtime provider, base URL, and credentials inside DSPy without copying API keys.
- **`dspy-rlm-hermes-runtime-auth`** — companion skill for deciding when `dspy.RLM` is the right abstraction and wiring it to Hermes runtime auth cleanly.
- **`tasker`** — automating Android tasks, profiles, scenes, and actions using Tasker configurations, JavaScriptlets, intents, and shell commands.

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

## License

MIT
