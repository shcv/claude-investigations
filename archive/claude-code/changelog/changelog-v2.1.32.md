# Changelog for version 2.1.32


## Summary

This release introduces **Claude Opus 4.6** as the new flagship model with 1M context window, adds a **"Summarize from here"** feature for targeted conversation compaction, expands session IDs to accept tagged identifiers beyond UUIDs, and simplifies Agent Teams by removing the join request workflow. The Discovery onboarding tutorial system has been removed entirely.


### Claude Opus 4.6 Support

What: Claude Opus 4.6 is now available as the most capable model for complex coding work, featuring a 1M token context window.

Usage:
```bash
claude --model opus
# Or within a session:
/model
```

Details:
- Opus 4.6 with 1M context window supports longer sessions with large codebases
- Uses rate limits faster than Sonnet
- Available via `/model` command or `--model opus` flag
- Model selection updated in plan mode: "Opus 4.6 in plan mode, Sonnet 4.5 otherwise"
- First-party model ID: `claude-opus-4-6`

Evidence: Model definitions (search for `"claude-opus-4-6"` and `"Opus 4.6"`)


### Summarize from Here

What: Summarize your conversation from a specific point, rather than compacting the entire history.

Usage:
- Navigate to any message in the transcript (Ctrl+O)
- Select "Summarize from here" option
- Optionally add context for the summary
- Messages from that point onward are summarized

Details:
- Provides targeted compaction control
- Shows "Summarizing…" indicator during operation
- Displays "Conversation summarized (Ctrl+O for history)" notification on completion
- Prevents summarizing when there's nothing after the selected message

Evidence: Summarize feature UI (search for `"Summarize from here"`)


### Tagged Session IDs

What: Session IDs now accept tagged identifiers in addition to UUIDs, enabling more flexible session management.

Usage:
```bash
claude --session-id my-project-session
claude --resume my-project-session
```

Details:
- Session ID format expanded from UUID-only to "UUID or tagged ID"
- Error message updated: "Must be a valid UUID or tagged ID"
- Makes resuming sessions easier with memorable identifiers

Evidence: Session ID validation (search for `"tagged ID"`)


### Custom OAuth URL Support

What: Enterprise deployments can now configure custom OAuth endpoints via environment variable.

Usage:
```bash
export CLAUDE_CODE_CUSTOM_OAUTH_URL="https://your-oauth-endpoint.com"
claude
```

Details:
- Only approved endpoints are permitted
- Error thrown if endpoint is not on the allow list: "CLAUDE_CODE_CUSTOM_OAUTH_URL is not an approved endpoint"
- Supports FedRAMP endpoints (`claude.fedstart.com`, `claude-staging.fedstart.com`)

Evidence: OAuth configuration (search for `"CLAUDE_CODE_CUSTOM_OAUTH_URL"`)


### $50 Free Extra Usage Promotion

What: New promotional offer tied to Opus 4.6 launch—$50 of free extra usage.

Usage:
- Promotion displayed alongside Opus 4.6 availability notices
- Access via `/extra-usage` command

Details:
- Announcement: "Opus 4.6 is here · $50 free extra usage"
- Integrated into the referral program: "Share Claude Code and earn $50 of extra usage"

Evidence: Extra usage promotion (search for `"$50 free extra usage"`)


### Agent Teams Simplified

What: The Agent Teams join request workflow has been removed, simplifying team operations to just spawn and cleanup.

Details:
- Removed operations: `discoverTeams`, `requestJoin`, `approveJoin`, `rejectJoin`
- New simplified description: "Operation: spawnTeam to create a team, cleanup to remove team and task directories"
- Task assignment now uses `TaskUpdate` with `owner` parameter instead of `TeammateTool`'s `assignTask`
- Terminology change: "swarm" → "team" in documentation

Evidence: TeammateTool operations (search for `"spawnTeam to create a team, cleanup"`)


### MCP Error Handling Improvements

What: Better error messages for MCP (Model Context Protocol) server connection issues.

Details:
- New error categories: "MCP connection timeout", "MCP server not connected", "MCP tool timeout", "MCP tool unexpected response format"
- System prompt now notes: "MCP servers connect/disconnect between turns"

Evidence: MCP error messages (search for `"MCP connection timeout"`)


### MEMORY.md Guidance Updated

What: Improved guidance for managing the MEMORY.md file with recommendations for separate topic files.

Details:
- New recommendation: "Create separate topic files (e.g., `debugging.md`, `patterns.md`) for detailed notes and link to them from MEMORY.md"
- Warning when MEMORY.md is too long: "Move detailed content into separate topic files and keep MEMORY.md as a concise index"
- Documentation clarifies: "MEMORY.md is read from disk each turn and can be edited by the model"

Evidence: MEMORY.md guidance (search for `"separate topic files"`)


### Image Attachment Display

What: Clearer indication when images are attached to messages.

Details:
- New display text: "(Image attached)" and "(See attached image)"
- Provides visual confirmation of image context

Evidence: Image attachment labels (search for `"Image attached"`)


### Symlink Target Visibility

What: When editing files through symlinks, the UI now shows the actual target path.

Details:
- Shows "Symlink target: [path]" for symlinked files
- For targets outside working directory: "This will modify [path] (outside working directory) via a symlink"

Evidence: Symlink display (search for `"Symlink target:"`)


### Improved Session Resume Messages

What: Better error handling when resuming sessions with unavailable agent configurations.

Details:
- New message: 'Resumed session had agent "[name]" but it is no longer available. Using default behavior.'
- Graceful fallback instead of failure

Evidence: Session resume handling (search for `"but it is no longer available"`)


### Model Issue Error Messages

What: New error message when a selected model is unavailable or inaccessible.

Details:
- Message: "There's an issue with the selected model ([model]). It may not exist or you may not have access to it."
- Suggests using `--model` flag or `/model` command to select a different model

Evidence: Model error handling (search for `"There's an issue with the selected model"`)


### Background Agent Summarization

What: New internal system for background summarization of agent contexts.

Details:
- AgentSummary system manages automatic context summarization for long-running agents
- Timer-based summarization with proper cleanup on stop

Evidence: Agent summarization (search for `"[AgentSummary]"`)

## Bug Fixes

- Fixed YAML frontmatter parsing error messages to include more context (search for `"Failed to parse YAML frontmatter"`)
- Changed "was killed" to "was stopped" in task termination messages for clearer UX (search for `"was stopped"`)
- Fixed "User aborted" message for permission denial flow (search for `"User aborted"`)
- Updated ellipsis in "Teleporting to session" from "..." to "…" for typographic consistency


### Discovery Onboarding System

The "Discover Claude Code" feature tutorial system has been removed entirely:

- Removed categories: "Quick Wins", "10x Your Speed", "Level Up Your Code", "Make It Yours", "Power User", and others
- Removed all associated tips and progress tracking
- Removes approximately 60+ onboarding tutorial strings

This was an interactive feature discovery system that guided users through Claude Code capabilities. Its removal suggests this functionality may be moving elsewhere (e.g., documentation or web).

Evidence: Onboarding categories (search for `"Quick Wins"` in old version)
