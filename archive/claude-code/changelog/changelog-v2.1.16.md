# Changelog for version 2.1.16


## Summary

This is a landmark release introducing **Agent Swarms** (multi-agent coordination), including the TeammateTool for spawning and managing teams of AI agents, Task tools (TaskCreate, TaskGet, TaskUpdate, TaskList) for shared task management, and native iTerm2 split pane support for macOS users. The release also adds in-process teammate execution, dynamic team joining, and plan approval workflows.


### Agent Swarms - Multi-Agent Coordination

What: Spawn and coordinate multiple AI agents working in parallel on a project. Teams have a 1:1 correspondence with task lists (Team = Project = TaskList).

Usage:
```bash
# Create a team
claude
> Use TeammateTool with operation "spawnTeam" and team_name "my-project"

# Spawn teammates via the Task tool with team_name and name parameters
> Use Task tool to spawn a teammate named "researcher" for team "my-project"
```

Details:
- Create teams with `spawnTeam` operation
- Teams automatically create corresponding task list directories at `~/.claude/tasks/{team-name}/`
- Team configuration stored at `~/.claude/teams/{team-name}/config.json`
- Teammates can communicate via `write` (single recipient) or `broadcast` (all teammates)
- Graceful shutdown workflow with `requestShutdown` → `approveShutdown`/`rejectShutdown`
- Plan approval workflow for teammates: `approvePlan`/`rejectPlan`
- Cleanup team resources when done with `cleanup` operation

Evidence: `Ds7()` at line 417104 (TeammateTool prompt, contains `"# TeammateTool"`, `"spawnTeam"`, `"requestShutdown"`)


### Dynamic Team Joining

What: Agents can discover and request to join existing teams, with leaders approving or rejecting requests.

Usage:
```bash
# Discover available teams
> Use TeammateTool with operation "discoverTeams"

# Request to join a team
> Use TeammateTool with operation "requestJoin", team_name "my-project", proposed_name "helper"

# Leader approves the request
> Use TeammateTool with operation "approveJoin", target_agent_id "helper", request_id "join-123"
```

Details:
- `discoverTeams` lists teams from `~/.claude/teams/` that you can join
- `requestJoin` sends a join request to the team leader
- Leader receives `join_request` message and uses `approveJoin` or `rejectJoin`
- Configurable timeout for join requests (default 60 seconds)

Evidence: `rY2()` (requestJoin handler), `oY2()` (approveJoin handler), `aY2()` (rejectJoin handler) with operations `"requestJoin"`, `"approveJoin"`, `"rejectJoin"`


### Task Tools for Shared Task Management

What: New set of tools for creating and managing tasks that are shared across team members.

Usage:
```bash
# Create a task
> Use TaskCreate with subject "Implement API endpoint" and description "Create the /users endpoint"

# List all tasks
> Use TaskList to see available tasks

# Update task status or ownership
> Use TaskUpdate with id "1" and status "in_progress" and owner "researcher"

# Get task details
> Use TaskGet with id "1"
```

Details:
- `TaskCreate`: Create new tasks with subject, description, and optional metadata
- `TaskGet`: Retrieve a task by ID
- `TaskUpdate`: Update task status, owner, description, or blocked_by relationships
- `TaskList`: List all tasks showing ID, status, owner, and subject
- Tasks support dependency tracking with `blocks` and `blockedBy` fields
- When a task is completed, blocked tasks become unblocked

Evidence: `Or7` at line containing `"Create a new task in the task list"`, `Xr7` (TaskCreate prompt), `DD1` (TaskGet name), `Lr7` (TaskUpdate description)


### Native iTerm2 Split Pane Support for Teammates

What: Teammates appear as split panes in iTerm2 on macOS, providing visual separation for each agent.

Usage:
```bash
# Setup is prompted automatically when spawning teammates in iTerm2
# Requires it2 CLI tool installation via pip/pipx/uv
pip install it2
```

Details:
- Automatic detection of iTerm2 environment
- Guided setup flow to install `it2` CLI tool
- Split panes created for each teammate with color-coded borders
- Falls back to tmux if iTerm2 setup is not completed
- Option to prefer tmux over iTerm2 with `--teammate-mode tmux`

Evidence: `ITermBackend` class with methods `createTeammatePaneInSwarmView`, `isAvailable`, contains `"[ITermBackend] Creating pane"`, `"iTerm2 Split Pane Setup"`, `"✓ iTerm2 split pane support is ready"`


### In-Process Teammate Execution

What: Spawn teammates within the same process instead of separate tmux panes, useful for non-interactive sessions.

Usage:
```bash
# Automatically used in non-interactive sessions
# Can be explicitly requested with --teammate-mode in-process
claude --teammate-mode in-process
```

Details:
- Teammates run as async tasks within the same process
- Enabled by default in non-interactive sessions
- Each teammate has its own abort controller for graceful shutdown
- Supports all the same operations as pane-based teammates
- Resource cleanup handled automatically

Evidence: `InProcessBackend` class at line 6920 with `type = "in-process"`, `"[InProcessBackend] spawn() called"`, `"[InProcessBackend] Started agent execution"`


### Mailbox-Based Inter-Agent Communication

What: Filesystem-based mailbox system for asynchronous communication between team members.

Details:
- Each agent has an inbox at `~/.claude/teams/{team-name}/inboxes/{agent-name}.json`
- Messages include timestamp, sender, and content
- Automatic delivery of messages when agent turn ends
- Queued messages for busy agents delivered after their turn completes
- Supports permission requests/responses, shutdown requests, plan approvals

Evidence: `TeammateMailbox` functions `writeToMailbox`, `readMailbox`, `markMessagesAsRead` with logging `"[TeammateMailbox] Wrote message to"`, `"[TeammateMailbox] readMailbox"`


### New CLI Flags for Teammate Mode

What: New command-line flags for configuring teammate spawning behavior.

Usage:
```bash
claude --teammate-mode tmux          # Force tmux backend
claude --teammate-mode in-process    # Force in-process backend
claude --teammate-mode auto          # Auto-select based on environment

# Used internally when spawning teammates:
claude --agent-id <id> --agent-name <name> --team-name <name>
claude --agent-color <color>
claude --plan-mode-required
claude --parent-session-id <id>
```

Details:
- `--teammate-mode`: Choose how teammates are spawned (tmux, in-process, auto)
- `--agent-id`, `--agent-name`, `--team-name`: Identity flags for teammate sessions
- `--agent-color`: Assign a color for the teammate's UI
- `--plan-mode-required`: Require plan approval before implementation
- `--parent-session-id`: Link to parent session for analytics

Evidence: CLI flag construction at lines 5617-5622, 7145-7193 with flags `"--agent-id"`, `"--agent-name"`, `"--team-name"`, `"--agent-color"`, `"--plan-mode-required"`


### Git Worktree Support for Teammates

What: Each teammate can work in their own git worktree for isolated file modifications.

Details:
- Worktrees created automatically for teammates when needed
- Cleaned up via `git worktree remove` or manual removal on cleanup
- Supports parallel work on the same repository without conflicts

Evidence: `removeWorktree()` function with `git worktree remove --force`, `"[TeammateTool] Removed worktree via git"`, `worktreePath` field in teammate objects


### Enhanced Backend Registry for Pane Management

The backend registry now intelligently selects the appropriate pane backend:
- Detects iTerm2 and checks for it2 CLI availability
- Prefers iTerm2 native split panes when available
- Falls back to tmux with informative messaging
- Supports user preference for tmux over iTerm2

Evidence: `[BackendRegistry] Selected: iterm2 (native iTerm2 with it2 CLI)`, `[BackendRegistry] Selected: tmux (fallback in iTerm2, it2 setup recommended)`


### Teammate Preview UI

New UI for viewing teammate status and activity:
- Shows teammate name, status (running/idle/awaiting approval), and progress
- Color-coded teammate indicators
- Idle time tracking
- Interactive controls: kill, shutdown, cycle mode, prune idle

Evidence: `hs7()` function (teammate preview component), `"shift+↑/↓ to select teammate"`, `"select · Enter view · k kill · s shutdown · p prune idle"`


### Slack MCP Tool Recognition

Added recognition for Slack MCP tools to enable better integration with authenticated Slack access.

Evidence: `"mcp__claude_ai_Slack__slack_send_message"`, `"mcp__claude_ai_Slack__slack_read_thread"`, `"mcp__slack__send_message"`, `"mcp__slack__read_thread"`


### Remote IDE Server Path Handling

Improved path handling for remote IDE server directories (.vscode-server, .cursor-server, .windsurf-server).

Evidence: Path checking includes `".vscode-server"`, `".cursor-server"`, `".windsurf-server"` at line 1669-1674


### First Render Timing Logging

Added startup performance logging to track first ink render time.

Evidence: `"[render] first ink render: ${Math.round(process.uptime() * 1000)}ms since process start"`

## Bug Fixes

- Fixed potential issues with teammate context initialization during session reconnection (`[Reconnection] Initialized agent context from session`)
- Fixed message marking logic in mailbox system (`markMessagesAsRead`, `markMessageAsReadByIndex` with proper lock handling)
- Fixed cleanup of in-process teammate tasks when aborted (`[TeammateTool] Aborted controller for in-process teammate`)
- Fixed worktree removal when git command fails (falls back to manual rm)


### Perfetto Tracing Removed

The Perfetto performance tracing feature has been removed from this release.

Evidence: Removed `PERFETTO_TRACING` flag check, removed trace writing functions `writePerfettoTrace`, `writePerfettoTraceSync`, removed all `[Perfetto]` logging statements


### HybridTransport POST Debugging Removed

Removed verbose HTTP POST debugging from the hybrid transport layer.

Evidence: Removed `"HybridTransport: POST URL ="`, `"HybridTransport: POST success"`, `"HybridTransport: POST failed"` logging


### Teammate Mode Requirements

- **tmux mode**: Requires tmux installed on your system. Start a tmux session before spawning teammates.
- **iTerm2 mode**: Requires macOS with iTerm2 and the it2 CLI tool installed.
- **in-process mode**: No external dependencies, but teammates run in the same process.


### Task List Coordination

When working in teams:
1. Use `TaskList` periodically to find available work
2. Claim tasks by setting yourself as owner with `TaskUpdate`
3. Mark tasks completed when done
4. Check `TaskList` again to find newly unblocked work


### Environment Variables for Teammates

Spawned teammates have these environment variables:
- `CLAUDE_CODE_AGENT_ID`: Unique identifier for the agent
- `CLAUDE_CODE_AGENT_TYPE`: Role/type of the agent
- `CLAUDE_CODE_TEAM_NAME`: Name of the team
- `CLAUDE_CODE_PLAN_MODE_REQUIRED`: Whether plan approval is required
