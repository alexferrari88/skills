# skills

A collection repo for reusable skills and skill-like workflows.

This repository currently contains:

- **`hermes-deep-research`** — Hermes-native deep research skill for multi-source synthesis, verification, parallel subresearch, and decision-grade reporting.

## Repository layout

```text
skills/
├── README.md
├── LICENSE
└── hermes-deep-research/
    ├── SKILL.md
    ├── references/
    └── templates/
```

## Install

### Hermes / skills-compatible agents

Install the deep research skill from this collection repo with:

```bash
npx skills add https://github.com/alexferrari88/skills --skill hermes-deep-research
```

## Included skill: hermes-deep-research

### What it does
- Multi-angle discovery
- Full-source reading for important claims
- Browser fallback for JS-heavy pages
- Parallel subresearch with subagents
- Python-backed ranking/scoring
- Decision memo / deep report / OSS due diligence / scout brief templates

### Good use cases
- Deep research
- Tool / vendor / model comparisons
- Current-state / landscape reviews
- GitHub / OSS due diligence
- Decision memos tied to evidence

### Not for
- Simple lookups
- One-source questions
- Fast rough-answer requests

## Canonical source-of-truth

On this machine, the installed Hermes skill path:

```text
~/.hermes/skills/research/hermes-deep-research
```

is symlinked to the repository copy at:

```text
~/src/skills/hermes-deep-research
```

That means edits made through the Hermes skill path automatically affect the repo working tree, and vice versa.

## License

MIT
