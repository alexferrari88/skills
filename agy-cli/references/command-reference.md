# agy Command Reference

This reference was built from the installed `/home/alex/.local/bin/agy` CLI. Re-check `agy --help` when exact behavior matters.

## Top-Level Flags

```text
--add-dir                       Add a directory to the workspace (repeatable)
-c, --continue                  Continue the most recent conversation
--conversation                  Resume a previous conversation by ID
--dangerously-skip-permissions  Auto-approve all tool permission requests without prompting
-i, --prompt-interactive        Run an initial prompt interactively and continue the session
--log-file                      Override CLI log file path
--mode                          Set the agent execution mode for this session (accept-edits, plan)
--model                         Model for the current CLI session
--new-project                   Create a new project for this session
-p, --print, --prompt           Run a single prompt non-interactively and print the response
--print-timeout                 Timeout for print mode wait (default 5m0s)
--project                       Project ID for the current CLI session
--sandbox                       Run in a sandbox with terminal restrictions enabled
```

## Subcommands

```text
changelog       Show changelog and release notes
help            Show help for subcommands
install         Configure environment paths and shell settings
models          List available models
plugin          Manage plugins (install, uninstall, list, enable, disable)
plugins         Alias for plugin
update          Update CLI
```

## Plugin Commands

`agy plugin --help` style flags are not supported by this installed CLI. Use `agy plugin help` for the summary.

```text
agy plugin list
agy plugin import [source]        # source can be gemini, claude, or a path
agy plugin install <target>       # supports plugin@marketplace
agy plugin uninstall <name>
agy plugin enable <name>
agy plugin disable <name>
agy plugin validate [path]
agy plugin link <mp> <target>
```

Observed read-only behavior:

- `agy plugin list` prints `No imported plugins.` when no plugins are imported.
- `agy plugin validate --help` treats `--help` as a path and fails if that path lacks `plugin.json`.
- `agy plugin install --help` treats `--help` as a target and fails because it is not a directory.

## Install And Update

`agy install` configures shell/path integration:

```text
agy install [--dir <path>] [--skip-aliases] [--skip-path]
```

`agy update` updates the CLI. On this install, `agy update --help` only prints `Usage of update:` and exits with code 2.

## Read-Only Discovery

```bash
command -v agy
agy --help
agy models
agy plugin list
agy changelog
```

Observed `agy changelog` output for this install:

```text
1.0.0:
* Initial release of the Antigravity CLI.
```

Observed `agy models` output for this install:

```text
Gemini 3.5 Flash (Medium)
Gemini 3.5 Flash (High)
Gemini 3.5 Flash (Low)
Gemini 3.1 Pro (Low)
Gemini 3.1 Pro (High)
Claude Sonnet 4.6 (Thinking)
Claude Opus 4.6 (Thinking)
GPT-OSS 120B (Medium)
```

## Tested Non-Interactive Invocation

This invocation returned `OK`:

```bash
agy --sandbox --mode plan --print-timeout 30s --print 'Reply with exactly: OK'
```
