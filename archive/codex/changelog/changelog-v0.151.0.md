# Changelog for version 0.151.0

## Summary

Codex 0.151.0 improves optional MCP startup, extension control over MCP results, and multi-repository plugin discovery. It also promotes scalable thread-history APIs, adds TUI conversation recaps and Vim motions, and expands app-server observability for client authors.

## Official Release Highlights

### Configurable optional MCP startup grace period

What: Configure how long Codex waits for optional MCP servers to expose their tools before starting a turn.

Usage:

```toml
mcp_optional_startup_grace_ms = 2500
```

Details:

- A pending optional server can be omitted after this grace period, allowing the turn to start without waiting indefinitely.
- Set the value to `0` to wait for the server’s own startup timeout instead of applying a separate grace window.
- This is useful when optional MCP servers are slow or intermittently available.

Code references:

- `ConfigToml::mcp_optional_startup_grace_ms` in `codex-rs/config/src/config_toml.rs`
- `Config::mcp_optional_startup_grace` in `codex-rs/core/src/config/mod.rs`


### MCP tool-result hooks for extensions

What: Extensions can now inspect or replace an MCP server’s result before Codex publishes it or provides it to the model.

Usage:

```rust
impl ToolLifecycleContributor for MyExtension {
    fn on_mcp_tool_result<'a>(
        &'a self,
        input: McpToolResultInput<'a>,
    ) -> ToolLifecycleFuture<'a> {
        // Inspect or replace input.result here.
    }
}
```

Details:

- Hooks receive MCP-call provenance, rewritten arguments, extension stores, and the mutable server result.
- They run for both successful and error results.
- The processed result is used for the completion event and subsequent model input.

Code references:

- `ToolLifecycleContributor::on_mcp_tool_result` and `McpToolResultInput` in `codex-rs/ext/extension-api/src/contributors/tool_lifecycle.rs`
- `process_mcp_tool_result` in `codex-rs/core/src/tools/lifecycle.rs`


### Per-repository plugin catalogs

What: App-server plugin catalog requests now resolve plugin configuration for each requested working directory and retain valid marketplaces when another project marketplace is invalid.

Usage:

```json
{"method":"plugin/list","id":1,"params":{"cwd":"/path/to/project"}}
```

Details:

- Local marketplaces are combined in request order.
- Duplicate sources preserve the first source while installed and enabled state is merged.
- Invalid project marketplaces are returned through `marketplaceLoadErrors` instead of hiding valid plugins or globally enabled remote catalogs.

Code references:

- `PluginRequestProcessor` in `codex-rs/app-server/src/request_processors/plugins.rs`
- `PluginListResponse::marketplace_load_errors` in `codex-rs/app-server-protocol/src/protocol/v2/plugin.rs`


### Permission, model, and sandbox correctness fixes

- Restored TUI permission profiles now persist across later turns; changing directory with `/cd` no longer weakens a restored sandbox restriction. (`RuntimePermissionProfileOverride` in `codex-rs/tui/src/app.rs`)
- Model switches and fallback models now produce a model-specific tool plan and choose a supported reasoning effort, including a safe fallback for `ultra`. (`ToolRouter` in `codex-rs/core/src/tools/router.rs`; `ModelInfo::multi_agent_reasoning_effort` in `codex-rs/models-manager/src/model_info.rs`)
- Remote filesystem sandboxing now uses the executor’s actual home directory, operating-system path conventions, and case rules when evaluating deny-read policies. (`FileSystemSandboxPolicyContext` in `codex-rs/protocol/src/permissions.rs`; `platform_os` in `codex-rs/exec-server-protocol/src/protocol.rs`)
- App-server MCP responses retain structured tool and resource errors instead of reducing them to plain text. (`mcp_error` in `codex-rs/rmcp-client/src/service_error.rs`)
- Nested subagent token use now counts against the root goal budget. (`codex-rs/ext/goal/src/accounting.rs`)
- Guardian decisions are no longer reused after permission state changes make them stale. (`codex-rs/ext/guardian-v2/src/async_scorer/authorization.rs`)

## Additional Changes Beyond Official Notes

The following user-facing CLI, TUI, and app-server changes are present in the diff but were not called out in the published highlights.

## New Features

### Conversation recaps in the TUI

What: Request a concise conversation summary with `/recap`; Codex can also generate recaps for eligible inactive conversations.

Usage:

```text
/recap
```

Details:

- Manual recaps show progress in the transcript and report actionable errors.
- Automatic recaps are bounded, ignore stale results, and retry only automatic failures.
- A recap is not generated while the current task is still running.

Code references:

- `RecapRequest` and `App::request_recap` in `codex-rs/tui/src/app/recap.rs`
- `AppEvent::GenerateRecap` handling in `codex-rs/tui/src/app/event_dispatch.rs`


### Stable paginated thread-history APIs

What: The app-server’s `thread/turns/list`, `thread/items/list`, and `thread/revert` APIs are now available without the experimental API capability.

Usage:

```json
{"method":"thread/turns/list","id":24,"params":{"threadId":"thr_123","limit":50,"sortDirection":"desc"}}
```

Details:

- `thread/items/list` can page all persisted items or restrict results to one `turnId`.
- `thread/revert` replaces a loaded paginated thread’s durable history with the prefix before `beforeTurnId`; it does not revert local filesystem changes.
- Pagination cursors support incremental history loading without resuming a thread.

Code references:

- `ThreadTurnsListParams` and `ThreadItemsListParams` in `codex-rs/app-server-protocol/src/protocol/v2/thread.rs`
- `ThreadRevertParams` and `ThreadRevertResponse` in `codex-rs/app-server-protocol/src/protocol/v2/thread.rs`
- Stable methods `"thread/turns/list"`, `"thread/items/list"`, and `"thread/revert"` in `codex-rs/app-server-protocol/src/protocol/common.rs`

## Improvements

### Completion usage metadata for app-server clients

`rawResponse/completed` notifications can now include provider-supplied `usageMetadata.amount` without converting the amount from its original string representation. This applies to regular turns and remote compaction responses.

Code references: `ResponseUsageMetadata` and `RawResponseCompletedNotification` in `codex-rs/app-server-protocol/schema/json/v2/RawResponseCompletedNotification.json`


### Persistent reasoning effort

Models can advertise the `persistent` reasoning-effort setting. Codex preserves that setting in configuration and presents it as “Persistent” in the TUI, while translating it to the provider’s required wire value.

Code references: `ReasoningEffort::Persistent` in `codex-rs/protocol/src/openai_models.rs`


### Expanded Vim editing motions

Vim-mode editing now supports `f`, `F`, `t`, and `T` character motions plus `gg` and `G` buffer jumps. The motions work with change, delete, and yank operators, dot-repeat, and configurable key bindings.

Code references: `VimMotion` in `codex-rs/tui/src/bottom_pane/textarea/vim.rs`; Vim key handling in `codex-rs/tui/src/bottom_pane/textarea.rs`


### Managed one-shot command fallback

When managed requirements disable resumable unified execution, Codex can retain completion-only command execution without exposing `write_stdin` or a resumable process.

Code references: `ExecCommandLifetime::OneShot` and `one_shot_exec_command_spec` in `codex-rs/core/src/tools/handlers/unified_exec/exec_command.rs`

## Bug Fixes

- Git remote URLs are sanitized before being included in rollout, thread, analytics, and cloud-task metadata, preventing embedded credentials from being exposed. (`SanitizedGitUrl` in `codex-rs/protocol/src/sanitized_git_url.rs`)
- Amazon Bedrock API keys are redacted from debug output. (`codex-rs/login/src/auth/bedrock_api_key.rs`)
- TUI composer hyperlinks now remain intact when text wraps. (`codex-rs/tui/src/bottom_pane/textarea/hyperlinks.rs`)
- macOS process sandboxes no longer receive unnecessary scratch-directory access. (`codex-rs/sandboxing/src/seatbelt.rs`)

## In Development

### Turn-scoped model-settings updates [Experimental]

What: App-server clients can change model, reasoning effort, summary, or service tier for one live turn without altering the thread’s future settings.

Usage:

```json
{"method":"turn/settings/update","id":42,"params":{"threadId":"thr_123","turnId":"turn_456","model":"gpt-5","effort":"high"}}
```

Status: Runtime-gated by `capabilities.experimentalApi` and the disabled-by-default `step_model_switching` feature.

Details:

- The method returns `applied` or `targetUnavailable`.
- Already captured model steps are unchanged.
- Parent-owned Multi-Agent V2 subagents reject direct updates.

Code references: `TurnSettingsUpdateParams` and `TurnSettingsUpdateStatus` in `codex-rs/app-server-protocol/src/protocol/v2/turn.rs`; `"turn/settings/update"` in `codex-rs/app-server-protocol/src/protocol/common.rs`


### Amazon Bedrock setup wizard [In Development]

What: Eligible TUI sign-in flows can offer Amazon Bedrock setup using discovered AWS profiles, environment credentials, access keys, or a Bedrock API key.

Usage:

```toml
[features]
bedrock_setup_wizard = true
```

Status: Runtime-gated by the disabled-by-default `bedrock_setup_wizard` feature.

Details:

- The wizard collects an AWS Region and masks secrets during entry.
- It persists the selected provider configuration through app-server setup.
- Existing managed Bedrock login remains experimental; this adds an opt-in onboarding flow.

Code references: `Feature::BedrockSetupWizard` in `codex-rs/features/src/lib.rs`; `BedrockState` in `codex-rs/tui/src/onboarding/bedrock.rs`

## Notes

App-server clients should migrate paginated thread handling away from full-history hydration. For `thread/resume` and `thread/fork`, pass `excludeTurns: true`, then page with `thread/turns/list` and `thread/items/list`; `thread/read` should omit `includeTurns` unless full legacy-style hydration is required.


Generated with:
- tool: `harness-investigations@c7c8b06-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/codex/diff/v0.151.0.diff` (raw diff)
- official release notes: `archive/codex/changes/release-notes-v0.151.0.md`
