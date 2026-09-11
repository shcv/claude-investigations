# Changelog for version 2.1.246

## Summary

This release adds infrastructure for scheduled cloud agents, optional project-file synchronization into cloud sessions, and durable personal/project memory stores. It also expands the Auto mode controls available through `/permissions` and adds a cloud-session setting-forwarding switch.

## New Features

### Scheduled Cloud Agents [Gradual Rollout]

What: Create and manage isolated Claude Code cloud agents that run on a recurring schedule or once at a specified time.

Usage:

```bash
/schedule
```

Details:

- Routines can use a five-field UTC cron expression or a one-time RFC3339 `run_once_at` timestamp.
- Scheduled agents run in Anthropic cloud sessions, not on your local machine; they use their own checkout, sandbox, tools, and optional MCP connections.
- The scheduler requires a Claude.ai login and eligible remote-session access.
- The command is gated by `tengu_surreal_dali` with a default of `false`, so it may not yet appear for every account.

Evidence: Cloud-agent scheduler (search for `"Schedule Cloud Agents"` and `"/schedule"`); registration is gated by `tengu_surreal_dali` and `"allow_remote_sessions"`.


### Cloud Project File Sync [Gradual Rollout]

What: Cloud sessions can offer to synchronize a project directory from your machine, allowing Claude to continue working with your current files after the local machine disconnects.

Usage:

```bash
claude --cloud
```

Details:

- When offered, choose “Yes, sync this project directory” to synchronize the project into the cloud session.
- The implementation states that secrets, credentials, and gitignored files are excluded; synced files are encrypted at rest.
- The sync system has explicit handling for unsupported layouts, oversized changes, unavailable device binding, and cloud-container restarts.
- The rollout is controlled by directory-sync feature gates including `tengu_dir_sync_folder_repo` and `tengu_dir_sync_folder_seed`, so availability may vary.

Evidence: Sync consent dialog (search for `"Sync this project directory to the cloud?"` and `"Yes, sync this project directory"`); rollout gates `tengu_dir_sync_folder_repo` and `tengu_dir_sync_folder_seed`.


### Memory Stores

What: Claude can use durable personal and project memory documents, including shared project stores where available.

Details:

- Memory tools can list stores and documents, read documents, and create or replace documents with version-conflict protection.
- Personal memories are Markdown documents; project stores can be shared with collaborators.
- Sensitive content is rejected: the implementation explicitly forbids saving secrets or credentials.
- Store availability is runtime-dependent; a session may have no provisioned memory store.

Evidence: Memory-store tools (search for `"Memory stores available in this session"` and `"Never write secrets or credentials into a memory"`).


### Cloud-Session Settings Forwarding

What: Cloud launches can explicitly control whether local Claude Code settings are sent to the cloud session.

Usage:

```bash
claude --cloud --forward-home-settings false
```

Details:

- `--forward-home-settings` accepts `true` or `false`.
- It applies only when creating or attaching to a cloud session, or when using `--environment`.
- Forwarded settings include local instructions, rules, preferences, and portable permission rules.

Evidence: Cloud-launch option (search for `"--forward-home-settings <true|false>"` and `"whether this machine's settings go into a cloud session"`).

## Improvements

### Expanded Auto Mode Controls in `/permissions`

`/permissions` now includes richer Auto mode editing: users can add, edit, and delete classifier rules; distinguish soft and hard deny rules; enable or disable built-in rule sets; and edit the classifier environment as a document.

Evidence: Auto mode interface (search for `"Extra rules for the auto mode classifier"` and `"Edit environment"`).

## Notes

Cloud scheduling and project synchronization are server-controlled rollouts. Updating to 2.1.246 installs the client-side capability, but does not guarantee that `/schedule` or project-sync consent will be available for a given account.


Generated with:
- tool: `harness-investigations@d83141a-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/claude-code/changes/changes-v2.1.246.md` (filtered astdiff)
- string diff: `archive/claude-code/changes/string-diff-v2.1.246.txt`
- source modules: `archive/claude-code/original/cli-v2.1.246.modules.json`
- source normalization: `esbuild analysis snapshot; original module text retained`
