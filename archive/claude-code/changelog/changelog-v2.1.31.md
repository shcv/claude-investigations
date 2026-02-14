# Changelog for version 2.1.31

## Summary

This release introduces a major expansion of the Persistent Agent Memory system with a configuration UI, three memory scopes (user, project, local), and MEMORY.md-based storage. It also adds streamlined SDK output message types, improved error messages with actual file size limits, enhanced tool usage instructions in the system prompt, and a session resume hint on exit.

### Persistent Agent Memory System [Gradual Rollout]
What: A comprehensive persistent memory system that lets Claude remember insights, patterns, and learnings across conversations, stored in MEMORY.md files within configurable directory scopes.

Usage:
Agent memory is configured through a new interactive dialog accessible during onboarding or settings. Users choose one of:
- **User scope** (`~/.claude/agent-memory/`) -- general learnings across all projects
- **Project scope** (`.claude/agent-memory/`) -- project-specific, shared via version control
- **Local scope** (`.claude/agent-memory-local/`) -- project-specific, not checked into version control
- **None** -- no persistent memory

Details:
- Memory is stored in `MEMORY.md` files that are automatically loaded into the system prompt
- Claude is instructed to organize memory semantically by topic, not chronologically
- Records insights about problem constraints, strategies that worked or failed, and lessons learned
- Claude proactively updates memory as it discovers useful patterns during work
- MEMORY.md is truncated at 200 lines with a warning when exceeded, encouraging users to compact or reorganize
- When MEMORY.md is empty, Claude is prompted to start recording learnings for future sessions
- Can be disabled with `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` environment variable

Evidence: Persistent Agent Memory feature with configuration UI (search for `"Persistent Agent Memory"`, `"Configure agent memory"`, `"Organize memory semantically by topic"`, and `"no persistent memory"`). Gated by `tengu_oboe` feature flag (default `!1` = false).


### Streamlined SDK Output Types
What: Two new message types for SDK consumers that provide a simplified view of Claude's output, stripping away thinking blocks and tool call details.

Details:
- `streamlined_text` -- preserves the text content from assistant messages but removes thinking and tool_use blocks
- `streamlined_tool_use_summary` -- replaces verbose tool_use blocks with a human-readable summary string (e.g., "Read 2 files, wrote 1 file")
- These message types are filtered out in the normal CLI transport layer and are intended for SDK streaming consumers
- Marked as `@internal` in the schema descriptions

Evidence: New Zod schema types (search for `"streamlined_text"` and `"streamlined_tool_use_summary"`)


### Session Resume Hint on Exit
What: When a session ends in a TTY terminal, Claude Code now displays a dimmed hint showing the exact command to resume that session.

Details:
- Displays `Resume this session with: claude --resume <session-id>` when exiting
- Only shown in TTY mode (not in piped/scripted contexts)
- Uses the session name if available, or the session ID

Evidence: Resume hint on exit (search for `"Resume this session with:"`)

### Expanded Tool Usage Instructions in System Prompt
The system prompt now provides individual, per-tool instructions for when to use dedicated tools instead of Bash, replacing the previous single-paragraph format. The new format:

- Lists each tool explicitly: Read instead of cat/head/tail/sed, Edit instead of sed/awk, Write instead of cat with heredoc, Glob instead of find/ls, Grep instead of grep/rg
- Uses stronger wording: "Do NOT use the [Bash] to run commands when a relevant dedicated tool is provided"
- Emphasizes this as "CRITICAL to assisting the user"
- Wraps the tool-specific lines inside a top-level instruction, creating a clearer hierarchy

Previously, Glob and Grep were not explicitly mentioned as alternatives to bash commands.

Evidence: Expanded tool usage policy (search for `"exclusively for system commands and terminal operations that require shell execution"` and `"Do NOT use the"`)


### Improved Error Messages for Large Files
Error messages for oversized PDFs and requests now include the actual size limits and suggest `pdftotext` as a specific alternative tool.

- Old: `"PDF too large. Try reading the file a different way (e.g., extract text with a CLI tool)."`
- New: `"PDF too large (max N pages, Xmb). Try reading the file a different way (e.g., extract text with pdftotext)."`
- Old: `"Request too large. Try with a smaller file."`
- New: `"Request too large (max Xmb). Try with a smaller file."`

Evidence: Improved error messages with limits (search for `"PDF too large ("` and `"Request too large ("`)


### Conditional Pricing in Model Selector
Model descriptions in the model picker now conditionally show pricing information based on the user's account type. First-party (subscription) users see cost indicators, while API users do not.

Evidence: Conditional pricing display (search for `H4() !== "firstParty"` in model selector functions near line ~147370)


### Permission Mode: Delegate Description
The `delegate` permission mode now has an explicit description in the schema: "Delegate mode, restricts team leader to only Teammate and Task tools." Previously the mode existed in the enum but lacked a description string.

Evidence: Delegate mode documentation (search for `"delegate"` in the permission mode `.describe()` string)


### Agent Teams Plan Gating
Agent Teams (TeammateTool, SendMessage, spawnTeam) now checks plan eligibility before allowing team operations. Users on ineligible plans receive a clear error message instead of a silent failure.

Evidence: Plan check for Agent Teams (search for `"Agent Teams is not yet available on your plan."`)


### Keybindings Schema URL Migration
The JSON schema URL for keybindings configuration has migrated from Anthropic's platform domain to SchemaStore, a public schema registry.

- Old: `https://platform.claude.com/docs/schemas/claude-code/keybindings.json`
- New: `https://www.schemastore.org/claude-code-keybindings.json`

Evidence: Schema URL change (search for `"schemastore.org/claude-code-keybindings.json"`)


### Tool Permission Context in System Prompt
The system prompt now includes context about how tool permissions work, explaining that tools are executed in a user-selected permission mode and that denied tool calls should not be re-attempted without adjusting the approach.

Evidence: Permission context in system prompt (search for `"Tools are executed in a user-selected permission mode"`)


### WebSocket Interval-Based Keepalive
A new periodic interval-based keepalive mechanism has been added to the WebSocket transport, supplementing the existing activity-triggered keepalive. This should improve connection stability during idle periods in remote sessions.

Evidence: New keepalive interval (search for `"WebSocketTransport: Sent keep_alive (interval)"` and `keepaliveInterval`)

### Tool Names in Messages [In Development]
What: A feature that changes how deferred tool search prompts are constructed when tool names are injected into messages.

Status: Feature-flagged via `tengu_tst_names_in_messages` (default false)

Details:
- Controlled by `CLAUDE_CODE_TST_NAMES_IN_MESSAGES` environment variable or the `tengu_tst_names_in_messages` feature flag
- When enabled, returns a different tool search prompt variant (`CS9`) instead of the default
- Appears to change how the ToolSearchTool presents its available tools list

Evidence: Tool names in messages feature (search for `"CLAUDE_CODE_TST_NAMES_IN_MESSAGES"`, gated by `tengu_tst_names_in_messages`)
