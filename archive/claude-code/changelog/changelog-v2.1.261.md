# Changelog for version 2.1.261

## Summary

This release adds Claude.ai-hosted plugin marketplaces and new SDK/automation launch controls for loading plugins during initialization and supplying subagent instructions from a file. It also improves organization-policy visibility and makes stalled streaming requests easier to diagnose and recover from.

## New Features


### Claude.ai-Hosted Plugin Marketplaces

What: Add a plugin marketplace hosted for your Claude.ai account, then install its plugins through the normal plugin workflow.

Usage:

```bash
claude plugin marketplace add --claudeai <marketplace-name>
claude plugin marketplace list
claude plugin install <plugin>@<marketplace>
```

Details:

- The marketplace name comes from the marketplaces available to your signed-in Claude.ai account.
- This path requires Claude.ai sign-in and plugin sync; it is unavailable for API-provider sessions that cannot access Claude.ai downloads.
- Enterprise marketplace policy can block individual hosted marketplaces or plugins.
- `--claudeai` cannot be combined with `--scope` or `--sparse`, because the marketplace is account-hosted rather than declared in local settings.

Evidence: Dedicated marketplace-add flow and validation (search for `"claude plugin marketplace add --claudeai"` and `"claude.ai marketplaces are not available here"`).


### SDK Initialization from Stream JSON

What: SDK hosts can make the first stream-JSON request an `initialize` control request, allowing launch-scoped plugins to be applied before plugin work begins.

Usage:

```bash
claude --print --input-format stream-json --await-initialize
```

Details:

- Send the `initialize` control request as the first stdin line.
- Its `plugins` field accepts local plugin paths, including entries that skip MCP discovery.
- The option requires `--input-format=stream-json` and cannot be used with `--sdk-url`.
- Later initialize requests do not load additional plugins; the initialization response reports whether the requested plugins were applied.

Evidence: Startup parser and initialize schema (search for `"--await-initialize"` and `"Loaded only by a CLI launched with --await-initialize"`).


### File-Based Subagent System Prompts

What: Load a file and append its contents to every Task-tool subagent’s system prompt.

Usage:

```bash
claude --print \
  --append-subagent-system-prompt-file ./subagent-instructions.txt \
  "Review this repository"
```

Details:

- This is intended for `--print`/non-interactive automation.
- It is mutually exclusive with `--append-subagent-system-prompt`.
- A missing or unreadable file stops the launch with a targeted error.

Evidence: CLI option handling (search for `"--append-subagent-system-prompt-file"` and `"Read a system prompt from a file and append it to every Task-tool subagent's system prompt"`).


### Reload Custom Output Styles in Running SDK Sessions

What: SDK clients can request that Claude Code re-read output-style files without restarting the session.

Details:

- The `reload_output_styles` control request refreshes built-in and custom style names.
- It also clears the shared markdown-file scan cache, so later agent, skill, and routine use sees updated files.

Evidence: SDK control schema (search for `"reload_output_styles"` and `"Re-reads the output-style directories from disk"`).

## Improvements


### Organization Policy Status and Safer Gating

Claude Code now surfaces an Organization policy status and gives clearer reasons when policy-governed features cannot run. While policy information is unavailable, features that require it—including Remote Control, cloud sessions, and `/feedback`—remain off rather than proceeding without verified policy.

Evidence: Policy status and failure messaging (search for `"Organization policy:"` and `"features that must check it first (Remote Control, cloud sessions, /feedback and others) stay off"`).


### Better Recovery from Stalled Streaming Responses

Streaming requests now distinguish “no response headers” failures from normal stream-idle failures, display a retry state, and explicitly identify buffering proxies or gateways as a likely cause. The existing `CLAUDE_STREAM_FIRST_BYTE_TIMEOUT_MS` setting can tune the initial wait.

Evidence: Retry message and terminal guidance (search for `"No response from the API after"` and `"A proxy or gateway that buffers streaming responses can cause this"`).

## Bug Fixes

- SDK launch validation now rejects malformed, oversized, missing, or non-initialize first stdin messages for `--await-initialize` instead of attempting to continue with ambiguous launch state (search for `"first stdin line exceeds the line-size ceiling"`).
- Plugin synchronization now detects duplicate managed or synced marketplace copies and avoids loading an ambiguous copy (search for `"multiple synced copies claim the managed plugin's marketplace, so none is loaded"`).


Generated with:
- tool: `harness-investigations@5a7f523-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/claude-code/changes/changes-v2.1.261.md` (filtered astdiff)
- string diff: `archive/claude-code/changes/string-diff-v2.1.261.txt`
- source modules: `archive/claude-code/original/cli-v2.1.261.modules.json`
- source normalization: `esbuild analysis snapshot; original module text retained`
