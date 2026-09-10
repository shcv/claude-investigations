# Changelog for version 0.150.0

## Summary

Codex 0.150.0 adds task-aware collaboration in the terminal, more precise copying and editing controls, better thread naming, and interrupt-time hooks. It also expands experimental app-server support for MCP event subscriptions and Amazon Bedrock credentials, while strengthening security and platform reliability.

## Official Release Highlights

### Task references and task management

What: Reference another Codex task from the composer with `@`, letting Codex inspect, create, wait for, rename, archive, fork, or message related tasks.

Usage:

```text
@<select a task from the picker> Please compare its findings with this task.
```

Details:

- Task mentions resolve to same-host Codex threads and add bounded task context to the request.
- The task-management tool namespace supports `list_threads`, `read_thread`, `wait_threads`, `send_message_to_thread`, `create_thread`, `fork_thread`, `set_thread_title`, and `set_thread_archived`.
- Task titles and contents are treated as untrusted data rather than instructions.

Code references:

- `TaskMention` and `apply_task_references` in `codex-rs/tui/src/task_mentions.rs`
- Task tool definitions in `codex-rs/tui/src/dynamic_tools.rs`


### Response copying and terminal links

What: `/copy` now lets you choose the entire most recent response, an individual code block, or a blockquote; supported terminals render Markdown links as clickable labels.

Usage:

```text
/copy
```

Details:

- The copy picker extracts code and quote targets from the latest assistant response.
- Hyperlink-capable terminals show concise link labels; multiplexers, unknown terminals, and unsupported terminals retain the visible destination URL.

Code references:

- `show_copy_picker` in `codex-rs/tui/src/chatwidget/interaction.rs`
- `CopyTarget` extraction in `codex-rs/tui/src/markdown.rs`
- `WebLinkDisplay` in `codex-rs/tui/src/markdown_render/web_links.rs`


### Clearer thread titles

What: New unnamed terminal tasks receive generated descriptive titles, and `/rename` can prefill an editable conversation-based suggestion.

Usage:

```text
/rename
```

Details:

- Generated titles make it easier to distinguish active tasks in task lists and mentions.
- You can edit or replace the suggestion before committing the rename.

Code references:

- Thread-title generation in `codex-rs/tui/src/app/thread_title.rs`
- `/rename` handling in `codex-rs/tui/src/chatwidget/slash_dispatch.rs`


### Custom permission shortcuts and Vim repeat

What: Keymaps can bind shortcuts for cycling available permission modes, and Vim normal mode supports `.` to repeat the most recent complete edit.

Usage:

```toml
[keymap.chat]
previous_permission_mode = "f7"
next_permission_mode = "f8"
```

Details:

- The permission-cycle actions are intentionally unbound by default, so teams can choose suitable shortcuts.
- In Vim mode, `.` repeats the last complete edit using `repeat_last_change`.

Code references:

- `previous_permission_mode` and `next_permission_mode` in `codex-rs/tui/src/keymap.rs`
- `repeat_last_change` in `codex-rs/tui/src/bottom_pane/textarea/vim_commands.rs`


### Interrupt hooks

What: Hooks can now run when an active top-level turn is interrupted.

Details:

- The new `Interrupt` hook event is dispatched only for an active turn, allowing command and MCP hook handlers to react to cancellation.
- Interrupt hooks are distinct from normal `Stop` hooks.

Code references:

- `HookEventName::Interrupt` in `codex-rs/hooks/src/lib.rs`
- `run_turn_interrupt_hooks` in `codex-rs/core/src/hook_runtime.rs`


### Bug fixes and hardening

- Untrusted projects no longer contribute project-level `AGENTS.md` instructions, and managed deny-read policy remains in force when permissions change. (`load_project_instructions` in `codex-rs/core/src/config/`)
- App-server diagnostics redact more credential-bearing provider, refresh, and attestation fields. (`RedactedString` in `codex-rs/utils/redacted-string/src/lib.rs`)
- Remote MCP bearer-token lookup and required-server startup work correctly while remaining compatible with older executors. (`resolve_http_mcp_bearer_tokens` in `codex-rs/rmcp-client/` and MCP startup handling in `codex-rs/codex-mcp/`)
- Windows elevated sandbox setup and batch launch aliases now work correctly, including under Unicode user paths. (`setup` in `codex-rs/windows-sandbox-rs/src/setup.rs`)
- Unix shutdown no longer hangs when detached processes retain terminal I/O or output buffers fill. (`unix_io` in `codex-rs/utils/pty/src/unix_io.rs`)
- Amazon Bedrock sessions use compatible multi-agent and response-compaction paths. (`AmazonBedrockModelProvider` in `codex-rs/model-provider/src/amazon_bedrock/`)

## Additional Changes Beyond Official Notes

The following substantive changes are present in the release diff but were not called out in the published highlights.

## New Features

### MCP event subscriptions [Experimental]

What: App-server clients can subscribe to events emitted by a configured MCP server and receive forwarded notifications.

Usage:

```json
{
  "method": "mcpServer/event/stream/start",
  "params": {
    "threadId": "thread-id",
    "server": "my-mcp-server",
    "subscriptionId": "build-events",
    "name": "build/progress",
    "arguments": {}
  }
}
```

Details:

- Stop a subscription with `mcpServer/event/stream/stop` and its `subscriptionId`.
- Forwarded events use the `mcpServer/event/stream` notification surface and retain the MCP event method and parameters.
- This is explicitly experimental.

Code references:

- `McpServerEventStreamStartParams`, `McpServerEventStreamStopParams`, and `McpServerEventStreamNotification` in `codex-rs/app-server-protocol/src/protocol/v2/mcp.rs`
- `mcpServer/event/stream/start` documentation in `codex-rs/app-server/README.md`
- New schema `codex-rs/app-server-protocol/schema/json/v2/McpServerEventStreamNotification.json`

## Improvements

### MCP runtime connection status for app-server clients

App-server MCP inventory responses now expose a thread’s observed `runtimeStatus`, distinguishing states such as `connected`, `authenticationRequired`, `failed`, and `disabled` without starting or reconnecting a server.

Code references: `McpServerConnectionStatus` and `McpServerStatus::runtime_status` in `codex-rs/app-server-protocol/src/protocol/v2/mcp.rs`


### Amazon Bedrock setup and managed AWS access keys [Experimental]

What: App-server clients can configure Amazon Bedrock through discovered AWS credentials, named profiles, Bedrock API keys, or managed AWS access keys.

Usage:

```json
{
  "method": "account/login/start",
  "params": {
    "type": "amazonBedrockAccessKeys",
    "accessKeyId": "...",
    "secretAccessKey": "...",
    "region": "us-west-2"
  }
}
```

Details:

- `account/bedrock/discover` can report available profile and environment credential metadata without returning secrets.
- `account/bedrock/setup` validates a selected AWS source and writes the Amazon Bedrock provider configuration.
- Clients must initialize the app server with `experimentalApi: true`; restart it after changing provider configuration.

Code references:

- `BedrockAccessKeys` login support in `codex-rs/app-server-protocol/src/protocol/v2/account.rs`
- Bedrock setup processing in `codex-rs/app-server/src/request_processors/account_processor/bedrock_setup.rs`
- `AmazonBedrockModelProvider` in `codex-rs/model-provider/src/amazon_bedrock/mod.rs`


### Hostname in the configurable status line

What: The interactive status-line picker can display the hostname of the machine running Codex.

Details:

- Codex uses a normalized hostname and prefers a locally resolved canonical FQDN when available.
- The hostname is omitted when unavailable.

Code references:

- `StatusLineItem::Hostname` in `codex-rs/tui/src/bottom_pane/status_line_setup.rs`
- `host_name` in `codex-rs/config/src/host_name.rs`

## In Development

### Durable realtime timeline items [Experimental]

What: App-server realtime activity can be retained as thread-scoped timeline entries, including transcript segments and realtime-session lifecycle events.

Status: Experimental protocol surface.

Details:

- Completed realtime timeline items are durably interleaved with ordinary turn items returned by `thread/timeline/list`.
- Clients should handle the additive `thread/realtime/item/*` notifications and ignore unknown notification methods for compatibility.
- This improves recovery and history projection for realtime conversations; it does not alter `ThreadItem`, `thread/read`, `thread/resume`, or `thread/fork`.

Code references:

- `ThreadRealtimeItem` and `ThreadRealtimeItemContent` in `codex-rs/app-server-protocol/src/protocol/v2/realtime.rs`
- New schemas `codex-rs/app-server-protocol/schema/json/v2/ThreadRealtimeItemStartedNotification.json` and `codex-rs/app-server-protocol/schema/json/v2/ThreadRealtimeItemCompletedNotification.json`

## Notes

App-server clients should treat the new MCP event-stream methods and Amazon Bedrock setup/login variants as experimental, and should tolerate newly added notifications and nullable MCP runtime-status fields for compatibility with older servers.


Generated with:
- tool: `harness-investigations@c7c8b06-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/codex/diff/v0.150.0.diff` (raw diff)
- official release notes: `archive/codex/changes/release-notes-v0.150.0.md`
