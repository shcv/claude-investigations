# Changelog for version 2.1.265

## Summary

This release expands configuration migration to Cursor, lets interactive sessions use `--fallback-model`, and adds project-memory access for Claude sessions attached to a claude.ai Project. Plugin directories can now act as containers for multiple plugins.

## New Features

### Import Cursor configuration

What: `claude import` can now scan and import supported Cursor configuration, rules, commands, skills, hooks, and MCP settings.

Usage:

```bash
claude import cursor --dry-run
```

Details:

- Review the preview before applying it; use `--yes=<digest>` only after reviewing the generated digest.
- Cursor-only UI state, such as custom modes and dashboard-managed settings, is not automatically imported.
- Imported skills are checked for shell-execution markers and invalid frontmatter.

Evidence: The command usage now includes `"claude import [codex|gemini|cursor]"`; Cursor-specific import sources include `"Cursor Custom Modes"` and `"Imported Cursor rule"`.


### Project memory access

What: Claude can read the memory files associated with a claude.ai Project attached to the current session, allowing relevant cross-chat project context to be consulted on demand.

Details:

- This is available only when the session is already bound to a Project; there is no CLI flag to select or discover a Project.
- Claude can list memory-file metadata with `project_memory_list` and read a selected file with `project_memory_read`.
- Project memory is read-only through this interface, is read on demand rather than automatically each turn, and changes made by other chats are not seen until a new session.
- Project memory may be authored by other people or sessions, so Claude treats it as data rather than instructions.

Evidence: The new Project tool methods are `"project_memory_list"` and `"project_memory_read"`; its guidance says `"Memory is what Claude has remembered for this project across chats."`

## Improvements

### Use fallback models in interactive sessions

`--fallback-model` is no longer documented as print-mode-only, so an interactive Claude session can fail over to a specified model when the primary model is overloaded or unavailable.

Usage:

```bash
claude --fallback-model sonnet
```

Details:

- Supply a comma-separated list to try fallbacks in order.
- Claude retries the primary model at the start of each user turn.

Evidence: The `--fallback-model <model>` help text removed `"(only works with --print)"` while retaining `"Enable automatic fallback to specified model(s)"`.


### Load a directory of plugins

A `--plugin-dir` path may now point to a folder containing multiple plugins; Claude loads each child plugin.

Usage:

```bash
claude --plugin-dir ./plugins
```

Details:

- Individual plugin directories and `.zip` plugins remain supported.
- The same nested-folder behavior applies when configuring plugins for dispatched agent sessions.

Evidence: The option now states `"a folder of plugins loads each child"`.

## In Development

Features with infrastructure added but not intended for normal interactive use.


### Serve-only cloud-session helper [In Development]

What: A hidden `--attach-serve <session_id>` mode can attach a serve-only helper to an existing cloud session.

Status: Dark-launched / desktop-only

Details:

- It is described as `"spawned by the desktop app; not for interactive use"`.
- It requires a `cse_...` session ID, stream-JSON input and output, non-interactive execution, and an enabled headless cloud client.
- It cannot be combined with `--cloud` or `--remote`.

Evidence: Search for `"--attach-serve <session_id>"` and `"requires the serve-only headless launch"`.


Generated with:
- tool: `harness-investigations@5a7f523-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/claude-code/changes/changes-v2.1.265.md` (filtered astdiff)
- string diff: `archive/claude-code/changes/string-diff-v2.1.265.txt`
- source modules: `archive/claude-code/original/cli-v2.1.265.modules.json`
- source normalization: `esbuild analysis snapshot; original module text retained`
