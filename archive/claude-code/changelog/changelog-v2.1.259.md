# Changelog for version 2.1.259

## Summary

This release adds consent and policy controls for cloud sessions that run tools on your computer, plus live reloading for plugin hook modules during development. It also hardens organization-managed MCP configuration and protects settings writes from concurrent-update failures.

## New Features

### Cloud-session tool serving controls

What: Cloud sessions can use tools on a connected computer, with an explicit consent choice for whether auto-mode commands may run without asking each time.

Usage:

```bash
claude --cloud <session-id>
```

Details:

- The first relevant cloud-session flow can ask whether to allow unattended commands.
- `/config` exposes this as “Unattended commands from cloud sessions on this computer.”
- Administrators or users can disable unattended execution with `remoteTools.allowUnattendedServing: false`; then cloud-session commands require per-command approval.
- An Anthropic emergency switch can disable serving and cancel in-flight commands.

Evidence: Cloud consent and policy controls (search for `"Let cloud sessions run commands on this computer without asking?"`, `"Unattended commands from cloud sessions on this computer"`, and `"remoteTools.allowUnattendedServing"`).


### Live reload for plugin hook modules

What: Claude Code now watches installed plugin directories and reloads hook modules after their files change.

Usage:

```bash
# Edit a hook module in an enabled local plugin while Claude Code is running.
# The changed hook module is reloaded automatically.
```

Details:

- Watches only plugins with hook modules and reloads them after a debounced file change.
- Reload failures keep the previous module active instead of leaving the plugin without hooks.
- Set `CLAUDE_CODE_PLUGIN_DIR_WATCH=false` to disable watching.

Evidence: Plugin hook watcher (search for `"CLAUDE_CODE_PLUGIN_DIR_WATCH"`, `"plugin-dir watch: watching"`, and `"reload failed, the previous version stays loaded"`).

## Improvements

### Safer managed MCP server configuration

Organization-managed MCP servers now receive stricter validation and source isolation.

- `managedMcpServers` is accepted only from administrator-controlled managed settings, not host-provided, user-writable, or ordinary settings sources.
- Managed entries must be keyed by server name and use HTTP/SSE URLs; environment-variable expansion is not allowed.
- Invalid managed-server configuration is ignored with a diagnostic instead of being treated as runnable local program configuration.

Evidence: Managed MCP validation (search for `"managedMcpServers is only honored from the organization's managed settings sources"`, `"managed settings can only deliver \"http\" or \"sse\" servers"`, and `"${VAR} references are not expanded in managed settings"`).


### More reliable settings updates under contention

Concurrent Claude Code processes now preserve pending authentication and settings changes more defensively when the config lock or disk re-read fails.

Evidence: Config-write recovery (search for `"saveConfigWithLock: merge base is missing auth"` and `"Config lock still held by a live process after retries"`).

## Bug Fixes

- Cloud-session command recovery now reports whether an interrupted command ran, did not run, or has an unknown outcome, reducing the risk of blindly repeating a potentially partial command. Search for `"It may have run there (partially or fully): check its effect before repeating it."`

- Managed settings with an invalid `remoteTools` object now fail closed: unattended cloud command serving is disabled until the configuration is fixed. Search for `"remoteTools was present but invalid; treating allowUnattendedServing as false"`.

## In Development

Features with infrastructure added but not yet enabled. These are shipped “dark” and may become available in future versions.


### JavaScript function hooks [In Development]

What: Plugin hook modules gain a JavaScript function-hook runtime with host operations such as turn control and UI integration.

Status: Feature-flagged

Details:

- The rollout is controlled by `tengu_plugin_hooks_modules`, whose built-in default is false.
- `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS` can override the rollout decision for testing or controlled environments.
- Type declarations for hook modules can be generated through the plugin API tooling.

Evidence: Function-hook rollout gate (search for `"tengu_plugin_hooks_modules"` and `"overridden by the CLAUDE_CODE_ENABLE_FUNCTION_HOOKS environment variable"`).


Generated with:
- tool: `harness-investigations@5a7f523-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/claude-code/changes/changes-v2.1.259.md` (filtered astdiff)
- string diff: `archive/claude-code/changes/string-diff-v2.1.259.txt`
- source modules: `archive/claude-code/original/cli-v2.1.259.modules.json`
- source normalization: `esbuild analysis snapshot; original module text retained`
