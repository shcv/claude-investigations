# Changelog for version 2.0.51

## 🎯 Highlights

This release introduces **Opus 4.5 model support** for first-party API users, adds the new **EnterPlanMode tool** enabling Claude to proactively request plan mode, and significantly improves **rate limit warnings** with utilization percentages and smart thresholds. Multiple UX enhancements including grouped agent display and trailing thinking block filtering improve the overall experience.

## 🚀 New Features

### Opus 4.5 Model Support
**What:** Opus 4.5 is now available as the most capable model for complex work, replacing Opus 4.1 as the default for first-party API users.

**How to use:**
```bash
# Select Opus 4.5 via the model command
/model opus

# Or specify directly
claude --model opus
```

**Details:**
- Opus 4.5 becomes the default for Max and Team subscribers using first-party API
- Bedrock/Vertex/Foundry users continue to use Opus 4.1
- Model descriptions updated: "Most capable for complex work"
- One-time migration automatically resets model selection for eligible users
- A notification informs users about Opus 4.5 availability on first use
- **Evidence**: Model registry at `rcA()` line 163104, default logic at `QUA()` line 224121, selector at `rJ6` line 224397

### EnterPlanMode Tool
**What:** A new tool that allows Claude to proactively request permission to enter plan mode for complex tasks requiring careful exploration before implementation.

**How to use:**
```bash
# Claude will automatically suggest entering plan mode for complex tasks
# You'll see a prompt: "Enter plan mode?"
# Press 'y' to approve or 'n' to decline
```

**Details:**
- Requires user approval before entering plan mode
- Designed for tasks with multiple valid approaches, architectural decisions, or unclear requirements
- Includes extensive documentation on when to use vs. not use plan mode
- Cannot be used from agent contexts (main conversation only)
- **Evidence**: Tool definition at `GRA` variable in `_50` at line 425698, prompt at `vb2` line 425575

### Rate Limit Utilization Warnings
**What:** Rate limit warnings now show exact utilization percentages and use intelligent thresholds based on both token usage and time remaining.

**How it appears:**
```
75% of 5-hour limit used · resets in 2h
50% of weekly limit used · resets in 3d
```

**Details:**
- Shows percentage of limit used instead of generic "Approaching limit" messages
- Smart thresholds: warns at 75%/60%, 50%/35%, 25%/15% (tokens/time) for weekly limits
- 5-hour limits now show warnings (previously silent)
- Considers usage rate vs. time remaining in window
- **Evidence**: Function `N49()` at line 467497, threshold config at `j$3`/`S$3` line 467531

### Grouped Agent Display
**What:** When multiple Task agents run simultaneously, the UI now shows a collapsed summary view that can be expanded with ctrl+o.

**How it appears:**
```
Running 3 agents… (ctrl+o to expand)
├─ investigator (Check auth flow) · 5 tool uses · 2.3k tokens
├─ investigator (Find routes) · 3 tool uses · 1.8k tokens
└─ investigator (Review tests) · 7 tool uses · 3.1k tokens
```

**Details:**
- Reduces visual clutter when multiple agents run in parallel
- Shows agent type, description, tool use count, and token usage
- Displays "X agents finished" when complete
- Same-type agents show grouped label (e.g., "Running 3 investigator agents…")
- **Evidence**: Main renderer `i49()` at line 469450, item renderer `g49()` at line 469102

## 🔧 Improvements

### Extra Usage Integration Enhanced
The extra usage feature now has deeper integration with account state and re-authentication flows.
- Added `hasExtraUsageEnabled` account property tracked via OAuth
- `/extra-usage` command now triggers re-authentication to sync state
- Pro users with extra usage enabled get access to Opus features
- **Evidence**: Account property at `DC1()` line 67554, API mapping at line 67521

### Improved Rate Limit Error Messages
Rate limit error messages now provide actionable guidance specific to your subscription tier.
- Messages suggest specific actions: `/upgrade to Max`, `turn on /extra-usage`, `/model opus`
- Different guidance for Pro, Max, Team, and Enterprise users
- Sonnet weekly limit now has distinct messaging from general weekly limit
- **Evidence**: Function `YLA()` at line 336478

### Model Description Updates
- Sonnet 4.5: "Best for everyday tasks" (was "Smartest model for daily use")
- Opus: "Most capable for complex work"
- Haiku 4.5: "Fastest for quick answers" (was "Fastest model for simple tasks")
- Dynamic pricing display using `jc()` helper function
- **Evidence**: Model options at `qh1`, `kzB`, `xzB` around line 224380

### November 2025 Limits Update Notice
Max and Team users see an informational notice about limit changes:
- Opus cap removed - can use Opus 4.5 up to overall limit
- Sonnet now has its own separate limit
- **Evidence**: Function `TN3()` at line 477797

### Trailing Thinking Block Filtering
Assistant messages ending with thinking blocks now have those blocks automatically filtered out before display.
- Prevents display of incomplete or dangling thinking blocks
- Logs telemetry about filtered blocks for debugging
- Replaces content with "[No message content]" if all blocks were thinking
- **Evidence**: Function `GT3()` at line 504394, helper `oX9()` at line 504391

### Default Model Logic for Max/Team Users
Max and Team subscribers now default to Opus 4.5 instead of requiring manual model selection.
- First-party API users get Opus 4.5 by default
- Cloud provider (Bedrock/Vertex) users continue with Opus 4.1
- Respects `ANTHROPIC_DEFAULT_OPUS_MODEL` environment variable override
- **Evidence**: Function `PnA()` at line 224154, `QUA()` at line 224121

## 🐛 Bug Fixes

### Model Detection Extended
The model detection functions now correctly recognize Opus 4.5 model IDs.
- `claude-opus-4-5` pattern now properly identified
- Fixes potential issues with model-specific features not activating for Opus 4.5
- **Evidence**: Detection at `KAB()` line 163004, `Pw()` line 224165
