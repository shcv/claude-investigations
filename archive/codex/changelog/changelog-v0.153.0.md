# Changelog for version 0.153.0

## Summary

Codex 0.153.0 expands remote plugin management, improves the terminal workflow with Vim undo/redo, reconnect recovery, richer history, and recap controls, and adds app-server metadata and async-question support. It also introduces an opt-in context-management path for eligible ChatGPT accounts.

## Official Release Highlights

### Remote plugin management

The plugin CLI can now work with remote marketplaces: list their contents, install plugins, and remove installed plugins.

Usage:

```bash
codex plugin list
codex plugin install <plugin-id>
codex plugin uninstall <plugin-id>
```

Details:

- Remote operations use the plugin marketplace configuration and return remote-operation outcomes.
- This complements existing local plugin and marketplace workflows.

Code references:

- `RemotePluginInstallRequest` in `codex-rs/core-plugins/src/remote_mutations.rs`
- CLI command handling in `codex-rs/cli/src/plugin_cmd.rs`


### Vim composer undo and redo

What: Vim normal mode now supports undo with `u` and redo with `Ctrl+R`, including complete draft state such as pasted content and attachments.

Usage:

```text
Enable Vim mode, make an edit, then press:
u        # undo
Ctrl+R   # redo
```

Details:

- History records complete composer drafts rather than text-only edits.
- The new actions can be remapped or unbound through the `vim_normal` keymap.

Code references:

- `VimHistory` and `handle_vim_history_key` in `codex-rs/tui/src/bottom_pane/chat_composer/vim_history.rs`
- `undo` and `redo` keymap actions in `codex-rs/tui/src/keymap_setup/actions.rs`


### Optional automatic-recap suppression

What: You can disable automatic TUI recaps without disabling the manual `/recap` command.

Usage:

```toml
[tui]
auto_recap = false
```

Details:

- Automatic recap scheduling and pending automatic recap work are suppressed.
- Manual `/recap` remains available.

Code references:

- `TuiToml.auto_recap` in `codex-rs/config/src/types.rs`
- `Config.tui_auto_recap` in `codex-rs/core/src/config/mod.rs`
- `RecapTrigger::Automatic` handling in `codex-rs/tui/src/app/recap.rs`


### Richer TUI history

What: Terminal history now shows complete patches, input submitted to background terminals, and successful commands as individual completed entries.

Usage:

```text
Use the normal TUI conversation history and terminal views; no configuration is required.
```

Details:

- Completed commands are retained as distinct history items instead of being collapsed into a less detailed activity view.
- Patch and background-terminal input rendering preserve more of what happened during a turn.

Code references:

- Patch rendering in `codex-rs/tui/src/history_cell/patches.rs`
- Command lifecycle handling in `codex-rs/tui/src/chatwidget/command_lifecycle.rs`
- Execution-cell rendering in `codex-rs/tui/src/exec_cell/render.rs`


### Earlier usage-limit warning for Plus and Team

What: ChatGPT Plus and Team users now receive a warning at 50% usage for an approximately five-hour usage window, before the existing higher-threshold warnings.

Usage:

```text
No action is required. The warning appears in the TUI when the eligible rolling window reaches the threshold.
```

Details:

- The 50% threshold is limited to Plus and Team plans and approximately five-hour windows.
- Existing 75%, 90%, and 95% warning behavior remains.

Code references:

- `RATE_LIMIT_WARNING_THRESHOLDS` and `RateLimitWarningState::take_warnings` in `codex-rs/tui/src/chatwidget/rate_limits.rs`


## Improvements

### TUI reconnect recovery

The TUI automatically reconnects after an external app-server connection drops. It preserves drafts and transcripts, while submissions that may not have been accepted remain paused for review rather than being silently replayed.

Code references: reconnect handling in `codex-rs/tui/src/app/reconnect.rs` and composer recovery in `codex-rs/tui/src/bottom_pane/chat_composer/reconnect.rs`


### Guardian behavior matches approval mode

Full Access skips Guardian review for confirmation-only actions. In user-approval mode, Codex skips background Guardian scoring and prewarming while retaining sensitive-action handling and requests for user input.

Code references: Guardian review logic in `codex-rs/core/src/guardian/review.rs` and approval handling in `codex-rs/core/src/tools/handlers/request_permissions.rs`


### Guardian evidence survives more session operations

Guardian review history is retained through compaction, restarts, and user-created forks, while rollback boundaries and subagent isolation are preserved.

Code references: `GuardianHistoryCheckpoint` handling in `codex-rs/core/src/session/rollout_reconstruction.rs` and Guardian history projection in `codex-rs/app-server-protocol/src/protocol/thread_history_projection.rs`


### More reliable MCP approval and startup behavior

Remembered MCP approvals are now scoped to the selected app account rather than applying broadly, and relative MCP executable paths start more reliably on macOS.

Code references: app-account approval resolution in `codex-rs/core/src/mcp_tool_call/account.rs` and MCP launch handling in `codex-rs/mcp-server/src/`


### More resilient rollout compression and resume

Compression now includes shared histories. `codex exec resume` can select compressed rollouts by working directory, and thread forks support symlinked session roots.

Code references: `RolloutCompression` logic in `codex-rs/rollout/src/compression.rs`, rollout lookup in `codex-rs/rollout/src/search.rs`, and fork handling in `codex-rs/app-server/src/request_processors/thread_processor.rs`


### App-server thread metadata exposes model settings

What: App-server thread objects now include nullable `model` and `reasoningEffort` fields.

Usage:

```json
{"id": 1, "method": "thread/read", "params": {"threadId": "thread_123"}}
```

Details:

- `thread/read`, `thread/list`, and thread-start notifications can expose the configured model and reasoning effort.
- Legacy or unavailable values remain `null`.
- These fields describe thread settings, not per-turn execution telemetry.

Code references:

- `Thread` model fields in `codex-rs/app-server-protocol/src/protocol/v2/thread.rs`
- Updated schemas in `codex-rs/app-server-protocol/schema/json/v2/ThreadReadResponse.json`


### Structured asynchronous questions for app-server clients

What: Eligible model catalogs can use `request_user_input_async` to ask structured questions without ending the active turn.

Usage:

```json
{
  "questions": [
    {
      "title": "Which deployment target should I use?",
      "options": ["Staging", "Production"]
    }
  ]
}
```

Details:

- Questions are delivered as asynchronous agent messages with ordered choices or free-text input.
- The tool returns immediately; the user’s response arrives later as an ordinary user message.
- Availability depends on the active model catalog.

Code references:

- `RequestUserInputAsyncHandler` in `codex-rs/core/src/tools/handlers/request_user_input_async.rs`
- `AsyncUserInputQuestion` schema in `codex-rs/app-server-protocol/schema/typescript/v2/AsyncUserInputQuestion.ts`


## Bug Fixes

- Full Access and user-approval flows avoid unnecessary Guardian work while preserving sensitive-action and user-input safeguards. (`GuardianReview` handling in `codex-rs/core/src/guardian/review.rs`)
- Feedback uploads can include bounded failed Guardian-review evidence when logs are enabled, improving diagnostics for review failures. (`guardian_review_failures` in `codex-rs/app-server/src/request_processors/feedback_processor.rs`)
- Local Markdown file links retain descriptive labels instead of replacing them with target paths. (`local_links` in `codex-rs/tui/src/markdown_render/local_links.rs`)
- The top-level `disable_paste_burst` setting remains supported as a compatibility fallback. (`ConfigToml.disable_paste_burst` in `codex-rs/config/src/config_toml.rs`)


## Additional Changes Beyond Official Notes

### App-server remote-plugin reconciliation API

What: App-server clients can now request a synchronization pass that updates installed remote plugin bundles and reports which runtime categories need refreshing.

Usage:

```json
{
  "id": 1,
  "method": "plugin/reconcile",
  "params": {"reason": "foreground refresh"}
}
```

Details:

- The response reports changed plugins and whether their MCP servers, apps, hooks, or skills may need refresh handling.
- It also reports remote IDs whose update or materialization failed.
- Clients should refresh MCP and app runtimes when indicated; skills are picked up on subsequent turns.

Code references:

- New JSON-RPC method `"plugin/reconcile"` in `codex-rs/app-server-protocol/src/protocol/common.rs`
- `PluginReconcileParams` and `PluginReconcileResponse` in `codex-rs/app-server-protocol/src/protocol/v2/plugin.rs`
- New schemas `codex-rs/app-server-protocol/schema/json/v2/PluginReconcileParams.json` and `codex-rs/app-server-protocol/schema/json/v2/PluginReconcileResponse.json`
- Reconciliation processor in `codex-rs/app-server/src/request_processors/plugins/reconcile.rs`


## In Development

### Context management [Experimental]

What: An opt-in context-management implementation provides token-budget context handling, history notes, and the `new_context` tool for eligible sessions.

Usage:

```toml
[features.context_management]
experimental_mode = true
```

Status: Runtime-gated by `features.context_management.experimental_mode`; disabled by default.

Details:

- The feature is limited to eligible ChatGPT Plus, Pro, and Pro Lite sessions using the Codex backend.
- API-key sessions, custom providers, and temporary structured threads are excluded.
- Enablement alone does not override account, backend, or model eligibility.

Code references:

- `experimental_mode` configuration schema in `codex-rs/core/config.schema.json`
- token-budget configuration resolution in `codex-rs/core/src/config/mod.rs`
- context-management history in `codex-rs/core/src/context_manager/history.rs`


### Native voice helper foundation [In Development]

What: Codex adds a private helper-process foundation for a future bundled voice feature.

Status: Not user-accessible. The TUI and existing CLI do not enable voice.

Details:

- The helper establishes a versioned inherited-pipe lifecycle and validates control frames.
- It does not open audio devices, load native plugins, negotiate WebRTC, or expose voice controls.
- Native loading, privacy controls, and audio runtime integration remain future work.

Code references:

- `codex-voice-host` README and binary in `codex-rs/voice-host/`
- `VoiceHost` client support in `codex-rs/realtime-webrtc/src/client.rs`


## Notes

- Move paste-burst configuration to the TUI section when updating configuration:

```toml
[tui]
disable_paste_burst = true
```

The legacy top-level `disable_paste_burst = true` remains supported as a fallback, but `[tui]` now takes precedence.


Generated with:
- tool: `harness-investigations@c7c8b06-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/codex/diff/v0.153.0.diff` (raw diff)
- official release notes: `archive/codex/changes/release-notes-v0.153.0.md`
