# Changelog for version 2.0.56

## 🎯 Highlights

Version 2.0.56 introduces proactive rate limit warnings that notify users before hitting limits, a new `/plan` command for viewing and editing plan files, and significant reliability improvements to the telemetry system. SDK users gain new capabilities to customize system prompts and define agents programmatically.

## 🚀 New Features

### Proactive Rate Limit Warnings
**What:** Claude Code now warns you before you hit rate limits by monitoring your usage percentage in real-time, rather than only alerting when limits are reached.

**How it works:**
- 5-hour limits: Warning at 90% usage when 72% through the window
- Weekly limits: Graduated warnings at 25%, 50%, and 75% based on time progression
- Warnings now show exact usage: "75% of weekly limit used · resets in 2 days"

**Details:**
- New function `BX5()` at line 341284 reads `anthropic-ratelimit-unified-*-utilization` headers
- New threshold configuration `eW5` at line 341262 defines warning triggers
- Five-hour limit warnings were completely disabled in v2.0.55 (returned `null`), now active
- **Evidence**: `BX5()` at line 341284, `AX5()` at line 341260, `tW5()` at line 341242

### New `/plan` Command
**What:** View or edit your current session's plan file directly from the command line.

**How to use:**
```bash
# View the current plan
/plan

# Open plan file in your editor
/plan open
```

**Details:**
- Shows plan content, file path, and editor name
- Displays "No plan found for current session" if no plan exists
- **Evidence**: Command definition `Xj3` at line 495530-495591

### Plan Mode Attachment Throttling
**What:** Plan mode instructions are now sent to Claude every 5 turns instead of every turn, reducing token usage while maintaining plan awareness.

**Details:**
- New constant `gX5.TURNS_BETWEEN_ATTACHMENTS = 5` at line 343717
- New function `cX5()` at line 343068 counts turns since last plan attachment
- Reduces repetitive context by ~80% in long planning sessions
- **Evidence**: `pX5()` at line 343087, `cX5()` at line 343068

### Plan File Reference Attachment
**What:** The transcript now shows "Plan file referenced (/path/to/plan)" when plan mode is active, providing visibility into which plan file is being used.

**Details:**
- New function `o10()` at line 342568 creates the attachment
- Helpful when resuming sessions to see which plan is active
- **Evidence**: `o10()` at line 342568, rendering at line 468780

### Command-Based MCP Server Matching
**What:** Enterprise admins can now allow or deny MCP servers by their exact command invocation, not just by name.

**How to use:**
```json
{
  "allowedMcpServers": [
    { "serverName": "weather" },
    { "serverCommand": ["npx", "-y", "@company/approved-server"] }
  ]
}
```

**Details:**
- Each entry must have EITHER `serverName` OR `serverCommand`, not both
- Command matching requires exact array equality (all arguments must match)
- Backward compatible - name-based matching still works
- New functions `TzA()` at line 509000 and `KiA()` at line 509003 for type checking
- **Evidence**: `O8B()` at line 185472, `Tv1()` at line 185485, schema at line 509164-509190

### SDK Init Parameters for System Prompts and Agents
**What:** SDK users can now customize system prompts and define agents programmatically during initialization.

**How to use:**
```javascript
await sdk.init({
  systemPrompt: "You are a specialized assistant...",
  appendSystemPrompt: "Additional instructions...",
  agents: {
    "coder": {
      "description": "Coding specialist",
      "prompt": "You are an expert programmer...",
      "tools": ["bash", "write"],
      "model": "claude-opus-4"
    }
  }
})
```

**Details:**
- `systemPrompt` - Override the default system prompt
- `appendSystemPrompt` - Add to the default system prompt
- `agents` - Define agents as JSON without file-based configuration
- **Evidence**: `$v3()` at line 521902, new parameter handling at lines 521915-521920

### KillShell Tool
**What:** New tool that allows terminating background shell processes by ID.

**Details:**
- Variable `KI1 = "KillShell"` at line 480255
- Complements the existing background shell functionality
- **Evidence**: `KI1` at line 480255

## 🔧 Improvements

### Telemetry Reliability Overhaul
**What:** Failed telemetry events are now queued, batched, and retried with exponential backoff instead of being lost.

**Details:**
- Events saved to `~/.claude/telemetry/1p_failed_events.{session}.{batch}.json`
- Maximum 8192 queued events, batch size of 200
- Exponential backoff: 500ms → 2s → 4.5s → 8s → 30s (capped)
- Events persist across CLI restarts and are retried on next session
- Default timeout increased from 5s to 10s
- **Evidence**: Class `zm1` at line 234387, `queueFailedEvents()` at line 234542, `retryPreviousBatches()` at line 234448

### LSP Diagnostics Volume Limiting
**What:** LSP diagnostics are now limited to 10 per file and 30 total, sorted by severity to preserve the most important issues.

**Details:**
- Constants `D21 = 10` (per file) and `RG2 = 30` (total) at line 341029
- Severity sorting via `TG2()` at line 340898: Errors → Warnings → Info → Hints
- Cross-turn deduplication prevents same diagnostic from appearing repeatedly
- Diagnostics cleared when file is modified via `H21()` at line 341024
- **Evidence**: `SG2()` at line 340948, `rIA` tracking map at line 341032

### Enhanced Plan Mode Workflow
**What:** The plan mode system prompt has been restructured for clearer phases and better guidance.

**Details:**
- Simplified from 5 phases with detailed multi-agent instructions
- Default behavior now launches Plan agents for most tasks
- Clearer guidance on when to skip agents (trivial tasks only)
- **Evidence**: `Pk3()` at line 510641

### Settings Change Auth Cache Clearing
**What:** Authentication caches are now automatically cleared when settings change, preventing stale credential issues.

**Details:**
- New code in `mg()` state handler at line 519860
- Calls `npA()` and `apA()` to clear auth caches on settings changes
- **Evidence**: `mg()` at line 519860, lines 519882-519887

### Heredoc Parsing Improvements
**What:** Better handling of heredocs in bash commands, including comment detection and nested heredoc filtering.

**Details:**
- New function `cS3()` at line 507823 detects if position is inside a comment
- Unique session-based heredoc markers via `uS3()` at line 507807
- Filters out nested heredocs that appear inside other heredocs
- **Evidence**: `pF0()` at line 507843, `cS3()` at line 507823

### Plan Mode File Path Handling
**What:** The file path checking for protected files now includes the plan file path.

**Details:**
- Function `NX5()` (was `TF5`) at line 342574 now checks against `yU(Q)` (plan file path)
- Prevents accidental modifications to the active plan file outside plan mode
- **Evidence**: `NX5()` at line 342574

## 🐛 Bug Fixes

### Rate Limit UI State Management
**What:** Rate limit warning notifications now properly track state to avoid duplicate notifications.

**Details:**
- New state tracking in `VZ9()` at line 477794
- Uses `useState` for `isUsingOverage` tracking
- Prevents "Now using extra usage" notification from appearing multiple times
- **Evidence**: `VZ9()` at line 477794

### Escape Key Handling in Transcript Mode
**What:** Fixed escape key behavior in transcript mode when operating in subagent context.

**Details:**
- Function `B89()` (was `O49`) at line 474049 now checks `ic` context
- Prevents unnecessary `jJ()` calls when in subagent mode
- **Evidence**: `B89()` at line 474049
