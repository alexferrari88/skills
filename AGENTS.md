# AGENTS.md

## Git hygiene

- Use Conventional Commits for commit messages after completing work.
- If this repository has a configured remote, push committed changes to the remote branch.

## Local maintenance note

The recommended local sync pattern is:
- treat the repo copy as the publishable source tree
- hardlink files into `~/.hermes/skills/...` for Hermes runtime compatibility
- avoid directory symlinks and linked-file symlinks, which can break skill discovery or linked-file loading

Hardlinks keep content edits in sync for existing files, but newly added, renamed, or deleted files still need matching structural updates.