# Changelog for version 0.154.0

## Summary

Codex 0.154.0 adds GPT-6-Astra, experimental isolated worktrees, inline answers to asynchronous questions, and Windows app-server daemon support. It also improves copy/paste fidelity, session safety, plugin/MCP refresh behavior, and adds several app-server and executor capabilities not covered in the published highlights.

## Official Release Highlights


### GPT-6-Astra model availability

What: GPT-6-Astra is available in the model picker and Amazon Bedrock model catalogs.

Usage:

```text
Open the model picker and select GPT-6-Astra.
```

Details:

- The bundled catalog describes GPT-6-Astra as the model for complex, demanding work.
- It supports text and image input, configurable reasoning effort through `ultra`, and a listed context window of 272,000 tokens.

Code references:

- `gpt-6-astra` entry in `codex-rs/models-manager/models.json`
- Bedrock catalog additions in `codex-rs/model-provider/`


### Isolated worktrees [Experimental]

What: Codex can create a managed Git worktree for a new session or an explicit fork, isolating its changes from the current checkout.

Usage:

```toml
[features]
worktrees = true
```

```bash
codex --worktree
codex exec --worktree "implement the change"
codex fork --worktree <session-id>
```

Details:

- Enable it from `/experimental` or with `features.worktrees = true`, then restart Codex.
- The TUI adds `/worktree` and a worktree browser for navigating associated sessions.
- Worktrees require local execution and are unavailable for code review, normal session resume, `--ephemeral`, and `--ignore-user-config`. To branch an existing exec session, use `codex exec fork --worktree`.

Code references:

- `Feature::Worktrees` in `codex-rs/features/src/lib.rs`
- `reject_unsupported_worktree_for_subcommand` in `codex-rs/cli/src/main.rs`
- `WorktreeManager` integration in `codex-rs/exec/src/lib.rs`
- `SlashCommand::Worktree` in `codex-rs/tui/src/slash_command.rs`


### Inline answers while Codex continues working

What: Codex can present asynchronous questions inline, allowing you to answer without discarding the draft in the main composer.

Usage:

```text
Choose a suggested answer, select Other to type a custom answer, or return to the composer with Escape.
```

Details:

- Pending questions preserve individual answer drafts.
- Suggested options include an `Other` choice for free-form responses.
- You can move among pending questions, skip a focused question, and return to the normal composer while retaining the answer draft.

Code references:

- `SendMessageToUserAsyncHandler` in `codex-rs/core/src/tools/handlers/send_message_to_user_async.rs`
- `AsyncQuestions` in `codex-rs/tui/src/bottom_pane/async_questions/mod.rs`
- `question_esc_back`, `prompt_stack_back`, and `skip_question` schema entries in `codex-rs/core/config.schema.json`


### Windows app-server daemon support

What: Windows can run the managed background app-server daemon, including lifecycle control and managed binary updates.

Usage:

```bash
codex app-server daemon start
codex app-server daemon restart
codex app-server daemon stop
codex app-server daemon version
```

Details:

- `bootstrap` installs durable management for SSH-driven use.
- Windows support validates local control-socket peers, uses managed install paths, and supports managed updater replacement.
- The daemon requires the standalone Codex installation managed by the Codex installer.

Code references:

- `AppServerDaemonSubcommand` in `codex-rs/cli/src/main.rs`
- Windows backend support in `codex-rs/app-server-daemon/src/backend/windows.rs`
- `ensure_supported_platform` in `codex-rs/app-server-daemon/src/lib.rs`


### Vim replace mode and terminal Escape recovery

What: Vim-mode users can enter `R` replace mode in the TUI composer; replace edits support undo and dot-repeat.

Usage:

```text
In Vim Normal mode, press R, type replacements, then use u or . as usual.
```

Details:

- Replace mode overwrites characters under the cursor while preserving recovery data for undo.
- Escape handling is hardened for terminals that emit legacy escape sequences.

Code references:

- `VimAction::EnterReplaceMode` in `codex-rs/tui/src/bottom_pane/textarea/vim_commands.rs`
- `enter_replace_mode` keymap schema in `codex-rs/core/config.schema.json`


### Rich response copying and expanded `/copy`

What: Copying Markdown responses now places rendered HTML on native clipboards, and `/copy` can target status output or individual fields.

Usage:

```text
/copy
```

Details:

- Rich-text applications receive formatted Markdown where the native clipboard supports HTML; plain-text, SSH, tmux, WSL, and terminal-mediated fallbacks keep text output.
- Images become alt text in copied HTML, preventing remote image requests during paste.

Code references:

- `CopyFormat::Markdown` and `copy_to_clipboard` in `codex-rs/tui/src/clipboard_copy.rs`
- `render_markdown` in `codex-rs/tui/src/clipboard_html.rs`
- `StatusHistoryHandle::copy_text` in `codex-rs/tui/src/status/card.rs`


### Session, plugin, MCP, and approval fixes

Details:

- Existing sessions now refresh installed plugin tools, skills, hooks, and live tool catalogs after external plugin changes.
- MCP OAuth refreshes coordinate across connections, retain login challenges on failure, and do not automatically replay rejected tool calls.
- Startup defers workspace-controlled helper execution until trust is established; the macOS sandbox also blocks terminal-input injection.
- Remote resume and fork preserve saved permissions, while fresh sessions and forks honor server-provided model defaults unless explicitly overridden.
- A conversation opened elsewhere is presented as a read-only transcript with retry support, preserving the local draft.
- Automatic approval review retains authorization evidence across compaction and rejects approvals invalidated by newer instructions or answers.

Code references:

- `mcp_refresh` in `codex-rs/app-server/src/mcp_refresh.rs`
- OAuth credential coordination in `codex-rs/rmcp-client/src/oauth/`
- workspace trust checks in `codex-rs/utils/path-utils/src/system_commands.rs`
- external-writer handling in `codex-rs/tui/src/chatwidget.rs`
- retained authorization context in `codex-rs/history/src/retained_context.rs`


### Bundled OpenAI Docs skill update

What: The bundled OpenAI Docs skill now includes GPT-6-Astra migration, compatibility, and prompting guidance.

Code references:

- GPT-6-Astra guidance under `codex-rs/skills/src/assets/samples/openai-docs/`


## Additional Changes Beyond Official Notes


### Direct remote exec-server transport with AWS SigV4

What: The experimental `exec-server` can connect to a remote environment using a direct WebSocket transport authenticated with AWS SigV4.

Usage:

```bash
codex exec-server \
  --remote wss://example.execute-api.us-east-1.amazonaws.com \
  --environment-id my-environment \
  --remote-transport direct \
  --aws-sigv4 \
  --aws-profile production \
  --aws-region us-east-1
```

Details:

- Direct transport requires `--aws-sigv4`; SigV4 requires direct transport.
- You can set the AWS profile, region, and signing service; the service defaults to `execute-api`.
- Direct transport does not support the exec-server forwarding subcommand.

Code references:

- `ExecServerRemoteTransport` and `ExecServerCommand::validate_remote_transport` in `codex-rs/cli/src/main.rs`
- `RemoteEnvironmentTransport::Direct` in `codex-rs/exec-server/src/remote/`


### Local file citations render as terminal links

What: Codex-rendered file citations are converted into local terminal links, including paths with line or column suffixes.

Details:

- Citation directives are ignored inside code blocks, existing links, images, HTML, and reference definitions.
- Relative citations are resolved against the session working directory and special URL characters are encoded before rendering.

Code references:

- `FileCitations` in `codex-rs/tui/src/markdown_render/file_citations.rs`


### Clearer session identity in the TUI

What: The default status line now includes the thread name, and the default terminal title includes activity, thread name, and project name.

Details:

- Existing custom `tui.status_line` and terminal-title settings continue to take precedence.

Code references:

- `DEFAULT_STATUS_LINE_ITEMS` in `codex-rs/tui/src/chatwidget.rs`
- `status_line` and terminal-title defaults in `codex-rs/core/config.schema.json`


## Improvements


### Account usage and reserve-fallback protocol support

App-server clients can declare whether they support Luna Reserve fallback and can request lighter background usage refreshes. Rate-limit responses now expose whether ordinary included usage is allowed and the normal model associated with a quota alias.

Code references: `GetAccountRateLimitsParams` and `GetAccountRateLimitsResponse` in `codex-rs/app-server-protocol/src/protocol/v2/account.rs`


### Configurable app-server idle unload delay

App-server deployments can set how long inactive, unsubscribed threads remain loaded before unload; the default is 60 seconds and changes take effect after restarting the server.

Usage:

```toml
thread_unload_delay_secs = 0
```

Code references: `thread_unload_delay_secs` in `codex-rs/core/config.schema.json`


## In Development


### Trusted-client user verification APIs [Experimental]

What: App-server v2 adds an experimental protocol for a trusted native client to check enrollment, enroll or delete a local credential, and produce a proof over a displayed challenge.

Usage:

```json
{
  "method": "userVerification/verify",
  "params": {
    "challenge": "base64url-challenge",
    "title": "Approve action",
    "description": "Confirm this request on this device."
  }
}
```

Status: Experimental app-server protocol surface.

Details:

- The verification response carries a credential ID and a P-256/SHA-256 signature.
- Status is local only: it does not prompt the user or query server registration.
- The protocol explicitly categorizes unavailable, cancelled, failed, and invalid-request outcomes.

Code references:

- `"userVerification/status"`, `"userVerification/enroll"`, `"userVerification/delete"`, and `"userVerification/verify"` in `codex-rs/app-server-protocol/src/protocol/common.rs`
- `UserVerificationVerifyParams` and `UserVerificationVerifyResponse` in `codex-rs/app-server-protocol/src/protocol/v2/user_verification.rs`


## Notes

`codex mcp-server` has been removed. Scripts or integrations still invoking that deprecated entry point must be updated; this release does not retain a compatibility command.

Code reference: removal of `Subcommand::McpServer` and `McpServerCommand` in `codex-rs/cli/src/main.rs`


Generated with:
- tool: `harness-investigations@c7c8b06-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/codex/diff/v0.154.0.diff` (raw diff)
- official release notes: `archive/codex/changes/release-notes-v0.154.0.md`
