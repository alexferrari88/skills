---
name: agy-cli
description: "Use Antigravity CLI (`agy`) to run agent sessions, non-interactive prompts, model discovery, project/workspace selection, plugin management, CLI install/update checks, changelog inspection, and conversation resume workflows. Trigger when the user asks to use Antigravity or agy, run an agy prompt, inspect agy models/plugins, install/validate/manage agy plugins, or troubleshoot the Antigravity CLI."
---

# Antigravity CLI

## Core Workflow

Use `agy` as an external agent CLI. Prefer read-only discovery first, then choose the narrowest invocation that matches the user's request.

1. Verify availability with `command -v agy` and `agy --help`.
2. Use read-only checks for orientation: `agy models`, `agy plugin list`, and `agy changelog`.
3. Prefer non-interactive print mode for automation:

```bash
agy --sandbox --mode plan --print-timeout 30s --print 'Reply with exactly: OK'
```

4. Use interactive mode only when a human needs to continue the session in a TTY:

```bash
agy --prompt-interactive 'Start by inspecting this project and ask before editing.'
```

Follow local shell-command instructions when running examples. For example, if the workspace requires a wrapper such as `rtk`, prefix the shell command with that wrapper.

## Session Modes

Use `--mode plan` when the agent should inspect, reason, or propose changes without editing. Use `--mode accept-edits` only when the user has asked Antigravity to make changes.

Add `--sandbox` by default when running prompts from automation so terminal restrictions are enabled. Do not use `--dangerously-skip-permissions` unless the user explicitly asks for it and the risk is acceptable.

Set `--print-timeout` for print mode. The default is 5 minutes; use a shorter timeout for smoke tests and a longer one for substantial tasks.

## Projects And Workspaces

Use `--project <id>` to target an existing Antigravity project, `--new-project` to create a project for the session, and repeat `--add-dir <path>` to add workspace directories.

Use `--continue` or `-c` to continue the most recent conversation. Use `--conversation <id>` when the user provides a specific conversation ID.

## Models

Run `agy models` for the current model list before pinning `--model`, because available names can change. Pass the model name exactly as printed:

```bash
agy --model 'Gemini 3.5 Flash (Low)' --sandbox --mode plan --print 'Summarize this repository.'
```

## Plugins

Use `agy plugin list` for read-only inspection and `agy plugin validate [path]` before installing a local plugin. Treat these plugin commands as state-changing: `import`, `install`, `uninstall`, `enable`, `disable`, and `link`.

Do not run `agy install` or `agy update` as routine discovery. `install` configures environment paths and shell settings, and `update` changes the CLI installation.

## Reference

Read `references/command-reference.md` when exact flag names, subcommands, or observed installed behavior matter.
