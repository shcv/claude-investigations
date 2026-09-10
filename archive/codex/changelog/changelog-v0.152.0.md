# Changelog for version 0.152.0

## Summary

Codex 0.152.0 improves the interactive Vim composer, rate-limit recovery, MCP reliability, and app-server integration. It also adds configuration for the built-in sleep tool, a newer OpenAI MCP elicitation capability, and recency sorting for app-server projects.

## Official Release Highlights

### Vim Draft Search

What: Vim-mode composers can search within the current draft using `/` and `?`, with match highlighting and `n`/`N` repeat navigation.

Usage:

```text
/needle<Enter>
n
N
```

Details:

- `/` searches forward and `?` searches backward.
- `n` repeats in the current direction; `N` repeats in the opposite direction.
- Fresh drafts now reliably begin in Insert mode after sending a message or running a slash command.

Code references:

- `VimSearch` in `codex-rs/tui/src/bottom_pane/textarea/vim_search.rs`
- `VimSearchKeymap` in `codex-rs/tui/src/keymap/vim_search.rs`
- composer integration in `codex-rs/tui/src/bottom_pane/chat_composer.rs`


### Actionable Rate-Limit Banners

What: The terminal UI now presents actionable banners when an account is rate-limited.

Usage:

```text
When a rate-limit banner appears, select its displayed action to check usage,
manage credits, reset limits, or manage a plan.
```

Details:

- Available actions vary with the returned account and workspace limit data.
- The TUI refreshes rate-limit information and renders account-aware recovery actions.

Code references:

- `BackendBannerAction` in `codex-rs/tui/src/backend_banners/actions.rs`
- rate-limit rendering in `codex-rs/tui/src/backend_banners/render.rs`
- `GetAccountRateLimitsResponse` in `codex-rs/app-server-protocol/src/protocol/v2/account.rs`


### Credential-Recovery Progress

What: Codex now reports provider reauthentication progress in both the terminal UI and `codex exec`, including Amazon Bedrock recovery.

Usage:

```bash
codex exec "continue the task"
```

Details:

- Recovery start and completion are surfaced as progress messages instead of appearing as a silent pause.
- App-server clients receive provider, thread, turn, and message details in the associated notifications.

Code references:

- `AuthRecoveryNotification` in `codex-rs/app-server-protocol/src/protocol/v2/notification.rs`
- `"modelProvider/authRecoveryStarted"` and `"modelProvider/authRecoveryCompleted"` in `codex-rs/app-server-protocol/src/protocol/common.rs`
- Bedrock recovery handling in `codex-rs/model-provider/src/amazon_bedrock/mod.rs`


### Package-Style MCP Server Names

What: MCP server names may now contain `:`, `@`, `/`, and `.`, enabling names such as package identifiers across MCP configuration, CLI commands, and authentication.

Usage:

```toml
[mcp_servers."@scope/example.server"]
command = "example-mcp"
```

Details:

- The relaxed validation is used consistently by MCP add/remove and authentication flows.
- Quote names containing punctuation in TOML table keys.

Code references:

- server-name validation in `codex-rs/config/src/mcp_types.rs`
- MCP command handling in `codex-rs/cli/src/mcp_cmd.rs`


### Per-Tool MCP Output Limits

What: Individual MCP tools can define an output-token limit, and the limit remains consistent after a session is resumed.

Usage:

```toml
[mcp_servers.example]
command = "example-mcp"

[mcp_servers.example.tools.expensive_report]
output_token_limit = 2000
```

Details:

- Limits apply to the tool output retained in model context.
- Codex preserves the applicable limit through resumed history rather than reverting to a different truncation behavior.

Code references:

- `output_token_limit` in `codex-rs/config/src/mcp_types.rs`
- `McpToolConfig` in `codex-rs/config/src/mcp_types.rs`
- truncation handling in `codex-rs/codex-mcp/src/binding.rs`


### Configurable App-Server Shell-Command Timeouts

What: App-server clients can specify a timeout for `thread/shellCommand`, including values longer than the prior one-hour default.

Usage:

```json
{
  "method": "thread/shellCommand",
  "id": 27,
  "params": {
    "threadId": "thr_b",
    "command": "./workflow.sh",
    "timeoutMs": 28800000
  }
}
```

Details:

- Omitting `timeoutMs` retains the one-hour default.
- `timeoutMs: 0` requests an immediate timeout; it does not mean unlimited execution.
- The RPC acknowledgement remains immediate, and this command continues to run unsandboxed on the app-server host.

Code references:

- `ThreadShellCommandParams` in `codex-rs/app-server-protocol/src/protocol/v2/thread.rs`
- schema `codex-rs/app-server-protocol/schema/json/v2/ThreadShellCommandParams.json`


### Planning Tool Is Now Opt-In

What: The `update_plan` tool is disabled unless explicitly enabled in configuration.

Usage:

```toml
[tools.update_plan]
enabled = true
```

Details:

- This changes the prior default: an omitted `tools.update_plan` section no longer enables the tool.
- Codex also removes its built-in plan-tool guidance when the tool is unavailable.

Code references:

- `UpdatePlanToolConfig` in `codex-rs/config/src/config_toml.rs`
- `resolve_update_plan_enabled` in `codex-rs/core/src/config/mod.rs`
- `without_update_plan_instructions` in `codex-rs/core/src/context/update_plan_instructions.rs`

## Additional Changes Beyond Official Notes

### OpenAI MCP Elicitation Forms

What: Codex now supports the newer `openai/elicitation/create` MCP extension for form-style user input.

Usage:

```json
{
  "capabilities": {
    "extensions": {
      "openai/elicitation": {
        "form": {}
      }
    }
  }
}
```

Details:

- An MCP server can send `openai/elicitation/create` with `mode: "form"`, a message, and a requested schema.
- This is additive to the legacy `openai/form` request; Codex retains compatibility with that older form.
- App-server clients receive the new `McpServerElicitationRequest::OpenAiElicitationForm` variant.

Code references:

- `OPENAI_ELICITATION_EXTENSION_ID` in `codex-rs/protocol/src/mcp.rs`
- `OpenAiElicitationRequestParams` in `codex-rs/rmcp-client/src/elicitation_client_service.rs`
- `McpServerElicitationRequest::OpenAiElicitationForm` in `codex-rs/app-server-protocol/src/protocol/v2/mcp.rs`


### Recency-Sorted App-Server Projects

What: App-server clients can list projects by their most recent non-archived thread, instead of only their manually assigned position.

Usage:

```json
{
  "method": "project/list",
  "id": 28,
  "params": {
    "sortKey": "recencyAt",
    "sortDirection": "desc"
  }
}
```

Details:

- `recencyAt` is returned on each project as Unix seconds, or `null` when the project has no qualifying thread.
- The default remains position sorting in ascending order.
- Recency sorting defaults to descending order and places empty projects last.
- This is an experimental app-server API capability.

Code references:

- `ProjectSortKey` and `ProjectListParams` in `codex-rs/app-server-protocol/src/protocol/v2/project.rs`
- `ProjectRequestProcessor::project_list` in `codex-rs/app-server/src/request_processors/projects.rs`
- migration `codex-rs/state/migrations/0052_projects_recency.sql`


### Configurable Sleep-Tool Exposure

What: The built-in interruptible `clock.sleep` tool now has its own stable feature configuration and can be exposed regardless of model metadata.

Usage:

```toml
[features.sleep_tool]
enabled = true
mode = "always_on"
```

Details:

- The default `model_driven` mode preserves prior behavior: exposure follows the current-time feature’s legacy sleep setting or a model advertising clock support.
- `always_on` registers the sleep tool whenever the feature is enabled.
- The sleep feature is enabled by default, while the default selection mode remains model-driven.

Code references:

- `SleepToolMode` and `SleepToolConfigToml` in `codex-rs/features/src/feature_configs.rs`
- `Feature::SleepTool` in `codex-rs/features/src/lib.rs`
- sleep registration in `add_core_utility_tools` in `codex-rs/core/src/tools/spec_plan.rs`

## Improvements

### Model-Advertised Clock Tools

Models that advertise `"clock"` in their supported-tool metadata can now receive the built-in current-time tool even when the legacy current-time-reminder feature is not enabled. This lets the model catalog control clock availability without requiring users to configure the reminder feature.

Code references: `add_core_utility_tools` in `codex-rs/core/src/tools/spec_plan.rs`


### Faster Plugin Recommendations

Plugin recommendations begin loading during session startup, reducing the delay before Codex can suggest an available plugin.

Code references: `plugin_recommendations_enabled` in `codex-rs/features/src/lib.rs` and startup handling in `codex-rs/tui/src/app/startup.rs`

## Bug Fixes

- Automatic-approval reviews retain larger messages and more transcript context, while preserving user instructions, answers, and valid authorizations through history compaction. (`ConversationTranscriptConfig` in `codex-rs/guardian-context/src/transcript.rs`)
- Resumed threads restore their persisted working directory when no new directory is supplied, and session-metadata updates preserve filesystem permissions. (`PersistedResumeSettings` handling in `codex-rs/app-server/src/request_processors/thread_processor.rs`)
- MCP tools remain usable while caches refresh or remote plugin state changes; HTTP authentication retries refresh helper-provided headers. (`ToolCatalogCache` in `codex-rs/codex-mcp/src/tool_catalog_cache.rs`; header refresh in `codex-rs/rmcp-client/src/http_headers.rs`)
- Opening the model picker refreshes available models without discarding the selected row. (`refresh_models` in `codex-rs/tui/src/app_server_session/models.rs`)
- Windows sandbox elevation uses a compatible PowerShell selection path for Microsoft Store PowerShell; terminal-query handling no longer leaves subprocesses hanging, and older JediTerm cursor rendering is repaired. (`fallback_powershell_shell_for_elevated_windows_sandbox` in `codex-rs/windows-sandbox-rs/src/wrapper.rs`; terminal queries in `codex-rs/sandboxing/src/terminal_queries.rs`)
- Cloud-task custom backend URLs reject untrusted origins and redirects so saved ChatGPT credentials are not forwarded to arbitrary hosts. (`HttpClient::new_without_redirects` in `codex-rs/cloud-tasks-client/src/http.rs`)

## Notes

App-server and integration clients should update strict protocol schemas to accept the additive `timeoutMs` field on `thread/shellCommand`, the `recencyAt` project field and project-list sorting fields, plus the auth-recovery notifications. MCP clients that implement elicitation should advertise `openai/elicitation` with `form` support before expecting `openai/elicitation/create` requests.


Generated with:
- tool: `harness-investigations@c7c8b06-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/codex/diff/v0.152.0.diff` (raw diff)
- official release notes: `archive/codex/changes/release-notes-v0.152.0.md`
