# Changelog for version 2.1.0


## Summary

This release focuses on improving the SDK mode experience, enhancing git commit attribution mechanics, and cleaning up memory resources. Key improvements include context-aware error messages for SDK mode users, pre-emptive trailer injection into git commits (replacing post-commit amendment), a new paste content caching system for large content, and better OAuth URL redaction for security.


### Paste Content Caching

What: Large pasted content is now cached to disk rather than stored inline in session transcripts.

Details:
- Content larger than 1KB is stored in a separate `paste-cache` directory
- Content is hashed (SHA-256, truncated to 16 chars) and stored as individual text files
- Old paste cache files are automatically cleaned up on startup based on age
- This reduces memory pressure and transcript file sizes for sessions with large pastes

Evidence: `OMB()` at line 225421, `MMB()` at line 225432, `RMB()` at line 225443 (paste storage/retrieval/cleanup, uses `"paste-cache"` directory)


### Pre-emptive Git Commit Trailer Injection

What: Git commit attribution trailers are now injected into the commit command before execution, rather than amending commits after the fact.

Details:
- Uses `PreToolUse` hook to intercept git commit commands
- Injects `Claude-Generated-By`, `Claude-Steers`, `Claude-Permission-Prompts`, `Claude-Escapes`, and `Claude-Plan` trailers directly into the commit message
- Supports both HEREDOC-style commit messages and quoted `-m` style messages
- Eliminates race conditions and edge cases from the previous post-commit amendment approach
- Tracks injection state via `trailersInjectedForCurrentCommit` flag

Evidence: `x$7()` at line 530968 (contains `"Attribution hook: PreToolUse - Injecting trailers into git commit command"`)


### Double-Dash Argument Separator for MCP Commands

What: The `claude mcp add` command now supports `--` to separate the command from its arguments.

Usage:
```bash
claude mcp add myserver -- node server.js --port 3000
```

Details:
- Allows cleaner separation when MCP server commands have their own arguments
- Arguments after `--` are passed directly to the server command

Evidence: `ZC9()` at line 535512 (contains `"--" && Q.length > 0`)


### SDK Mode-Aware Error Messages

Error messages for PDF and image handling now provide context-appropriate guidance based on whether Claude Code is running in SDK mode:

- **PDF too large**:
  - Interactive: "PDF too large. Please double press esc to edit your message and try again."
  - SDK mode: "PDF too large. Try reading the file a different way (e.g., extract text with a CLI tool)."

- **Password-protected PDF**:
  - Interactive: "PDF is password protected. Please double press esc to edit your message and try again."
  - SDK mode: "PDF is password protected. Try using a CLI tool to extract or convert the PDF."

- **Image too large**:
  - Interactive: "Image was too large. Double press esc to go back and try again with a smaller image."
  - SDK mode: "Image was too large. Try resizing the image or using a different approach."

Evidence: `Hi8()` at line 278470, `Di8()` at line 278475, `Fi8()` at line 278480 (contain `d2()` SDK mode check)


### OAuth URL Parameter Redaction

Sensitive OAuth parameters are now redacted from URLs in logs and error messages for improved security.

Details:
- Redacts: `state`, `nonce`, `code_challenge`, `code_verifier`, `code`
- Parameters are replaced with `[REDACTED]` in logged URLs

Evidence: `gB2()` at line 296262 (contains `Q.searchParams.set(B, "[REDACTED]")`)


### Tool Search Mode Telemetry

Enhanced telemetry for tool search mode decisions, providing better observability into when and why tool search is enabled or disabled.

Details:
- Logs `tengu_tool_search_mode_decision` events with reason codes:
  - `model_unsupported`, `mcp_search_unavailable`, `tst_enabled`
  - `auto_above_threshold`, `auto_below_threshold`, `mcp_cli_mode`, `standard_mode`
- Includes MCP tool count and threshold information

Evidence: `G70()` at line 280942 (contains `l("tengu_tool_search_mode_decision"`)


### Session Data Type Classification

Added classification of internal file paths for session memory and transcripts, enabling better handling of internal data access.

Evidence: `un8()` at line 282585 (returns `"session_memory"` or `"session_transcript"`)


### Tree-Sitter Parser Memory Cleanup

The shell command parser now properly cleans up tree-sitter AST trees after parsing to prevent memory leaks.

Details:
- Calls `tree.delete()` after extracting pipe positions and redirection nodes
- Pre-extracts needed data before cleanup to avoid use-after-free

Evidence: Line 1050 in diff: `return (Q.tree.delete(), !0);` and line 1067: `return (G.tree.delete(), new Ww2(A, Z, Y));`


### Focus Tracking State Cleanup

Improved terminal focus tracking cleanup on exit, with proper state reset to prevent orphaned event listeners.

Evidence: `Ew0()` at line 457322 (contains `process.stdout.write("\x1B[?1004l")`, `Fw0 = !1`)


### Cache Clearing on Reset

Added explicit cache clearing when resetting application state, improving memory management.

Evidence: `mD1()` at line 467837 (contains `hV.cache.clear?.()` and multiple other cache clears)

## Bug Fixes

- Fixed potential memory leak in tree-sitter shell parser by properly deleting AST trees after use (`Ww2` class at line 370359)
- Fixed terminal focus mode not being properly disabled on exit in some cases (`Tt2()` at line 457328)


### Year-End 2025 Rate Limit Promotion

The holiday promotion banner displaying "A gift for you - Your rate limits are 2x higher through 12/31" has been removed as the promotion period has ended.

Evidence: Removed function `re2()` at line 460646, `vw0()` at line 460649 (contained `"tengu_year_end_2025_campaign_promo"`)
