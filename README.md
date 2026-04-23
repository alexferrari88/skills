# skills

A public collection repo for reusable Hermes and skills-compatible agent skills.

## Included skills

- **`hermes-deep-research`** — Hermes-native deep research skill for multi-source synthesis, verification, parallel subresearch, and decision-grade reporting.
- **`dspy-hermes-runtime-auth`** — reuse Hermes Agent's active runtime provider, base URL, and credentials inside DSPy without copying API keys.
- **`dspy-rlm-hermes-runtime-auth`** — companion skill for deciding when `dspy.RLM` is the right abstraction and wiring it to Hermes runtime auth cleanly.

## Repository layout

```text
skills/
├── README.md
├── LICENSE
├── hermes-deep-research/
│   ├── SKILL.md
│   ├── references/
│   └── templates/
├── dspy-hermes-runtime-auth/
│   ├── SKILL.md
│   ├── references/
│   └── templates/
└── dspy-rlm-hermes-runtime-auth/
    ├── SKILL.md
    ├── references/
    └── templates/
```

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
```

## Skill summaries

### `hermes-deep-research`
Best for evidence-led deep research where important claims need full-source reading, cross-checking, and structured output.

### `dspy-hermes-runtime-auth`
Best for portable DSPy code that should follow Hermes runtime changes across providers, models, and custom endpoints without duplicating secrets.

### `dspy-rlm-hermes-runtime-auth`
Best for long-context tasks where the model should recursively inspect and compute over a large context object instead of forcing one giant prompt through a single context window.

## Local maintenance note

The recommended local sync pattern is:
- treat the repo copy as the publishable source tree
- hardlink files into `~/.hermes/skills/...` for Hermes runtime compatibility
- avoid directory symlinks and linked-file symlinks, which can break skill discovery or linked-file loading

Hardlinks keep content edits in sync for existing files, but newly added, renamed, or deleted files still need matching structural updates.

## License

MIT
