# Changelog for version 2.0.32

## 🎯 Highlights

Version 2.0.32 delivers significant performance improvements with optimized terminal rendering that eliminates flicker, introduces an automated tool execution API for building agentic workflows, and enhances the user feedback system for better accuracy. The release also removes seasonal Halloween content and adds helpful UI hints for users with 1M context access.

## 🚀 New Features

### Automated Tool Execution API (BetaToolRunner)

**What:** A new `toolRunner()` method in the Messages API that automatically executes tools in an agentic loop, eliminating the need to manually handle tool_use/tool_result message cycles.

**How to use:**
```javascript
const runner = client.beta.messages.toolRunner({
  model: "claude-sonnet-4-20250514",
  max_tokens: 1024,
  max_iterations: 10, // Limit agentic loops
  tools: [
    {
      name: "get_weather",
      run: async (input) => {
        // Your tool implementation
        return "Sunny, 72°F";
      }
    }
  ],
  messages: [{ role: "user", content: "What's the weather?" }]
});

// Stream each iteration
for await (const messageStream of runner) {
  // Handle streaming response
}

// Or wait for completion
const finalMessage = await runner.done();
```

**Details:**
- Automatically detects `tool_use` blocks in assistant responses and executes matching tools
- Supports both streaming and non-streaming modes
- Configurable iteration limits via `max_iterations` parameter
- Tools must implement a `run()` method that returns results
- Optional `parse()` method for input validation/transformation
- Returns properly formatted `tool_result` messages with error handling
- Can be controlled manually via `generateToolResponse()` and `pushMessages()` methods
- **Evidence**: Class `TYA` at line 82603, function `bh9()` at line 82564, variable `uZ1` at line 82604, new `toolRunner()` method at line 82828

### /stickers Command

**What:** New slash command to order official Claude Code stickers

**How to use:**
```bash
/stickers
```

**Details:**
- Opens browser to https://www.stickermule.com/claudecode
- Falls back to displaying URL if browser open fails
- Available in all contexts (always enabled, not hidden)
- Does not support non-interactive mode
- **Evidence**: Variable `$d2` at line 463792

### Enhanced Context Window Hints

**What:** Automatic notifications when users with Sonnet 1M access approach context limits

**How to use:**
These hints appear automatically when relevant:
```bash
# Warning when context is full:
Run /compact or /model sonnet[1m] to continue

# Tip after compaction:
Tip: You have access to Sonnet 1M with 5x more context
```

**Details:**
- Only shown to users with 1M context access (controlled via access check)
- Highlights the 5x context multiplier benefit
- Integrated into warning and tip notification system
- Improves discoverability of the 1M context feature
- **Evidence**: Functions `Wh6()` at line 317408 and `p8A()` at line 317415

### Optimized Terminal Rendering

**What:** New screen diffing algorithm that only updates changed characters instead of clearing and re-rendering the entire terminal, eliminating flicker and improving performance.

**How it works:**
The renderer now:
1. Compares previous and current screen buffers character-by-character
2. Only updates positions where content changed
3. Manages cursor movement efficiently during incremental updates
4. Falls back to full re-render only when screen dimensions change

**Details:**
- Significantly reduces terminal flicker during updates
- Improves performance for large terminal windows
- Better user experience during streaming responses
- Implements transaction-based cursor management for atomic updates
- **Evidence**: Functions `qRA()` at line 70135, `uR0()` at line 70140, `mR0()` at line 70379, class `dR0` at line 70395

## 💪 Improvements

### Feedback Survey System Refinements

**What changed:** The in-app feedback survey mechanism was refactored for improved accuracy and maintainability

**Key improvements:**
- Switched from tracking user message counts to tracking actual submission counts, preventing inconsistencies from message editing or restoration
- Moved survey-specific state from mixed local/global storage to centralized app-level state management
- Simplified conditional logic with early returns for better maintainability
- Adjusted triggering configuration:
  - Enabled for all models (was disabled by default)
  - Reduced probability from 100% to 0.5% when conditions are met
  - Reduced turn requirement between surveys from 15 to 10
  - Effectively disabled global cooldown (increased from 1 hour to ~1157 days)
  - Removed per-conversation cooldown (30 minutes)

**Net effect:** Surveys appear less frequently but with more accurate tracking across sessions

**Evidence**: Function `Ky2()` at line 445844 (renamed from `mS2`), configuration `ku5` at line 445950, state structure at line 298044

### Import Optimizations

**What changed:** Consolidated and reorganized import statements for better tree-shaking and bundle size optimization

**Changes:**
- Replaced `import We from "stream"` with `import { PassThrough as sr5 } from "stream"` at line 482663
- Replaced `import XI1 from "node:child_process"` with `import { execSync as l6Q, spawn as yd8 } from "node:child_process"` at line 249497
- Replaced `import _P9 from "node:os"` with `import { homedir as Wo5 } from "node:os"` at line 484356
- Added `import { cwd as XT0 } from "node:process"` at line 70828
- Added `import { join as Dn2, basename as Pr5 } from "path"` at line 481476

**Evidence**: Diff lines 10-21 (removed) and 534-537, 955-958, 1093-1096, 1105-1112 (added)

### Initialization Flow Enhancement

**What changed:** The SDK initialization function now sends authentication status after successful initialization when in headless mode

**Details:**
- After initialization completes, checks for ongoing authentication
- Sends `auth_status` event with authentication state, output, and error information
- Only triggers in headless/non-interactive contexts (parameter `J` must be true)
- Helps SDKs and automation tools track authentication progress
- **Evidence**: Function `Go5()` (renamed from `kr5`) at line 483837, lines 1288-1301 show the new auth status emission

### Helper Utility Functions

Several new utility functions were added to improve code organization:

- `yn1()` at line 416368: Enhanced slice function with offset support (replaces `Fn1()`)
- `kn1()` at line 416372: Relative path calculator that returns absolute path if result would escape working directory
- `_n1()` at line 416377: Formats limit/offset parameters for display
- `Sb5()` at line 430186: Reads `CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY` environment variable with default value of 10
- `YuA()` at line 207879: Strips `<sandbox_violations>` tags from content using regex
- `dS2()` at line 470949: Comparison function for checking if one value exceeds another in a specific context

### State Management Updates

**What changed:** Added `feedbackSurvey` object to app-level state structure

**New state fields:**
```javascript
feedbackSurvey: {
  timeLastShown: null,
  submitCountAtLastAppearance: null
}
```

**Details:**
- Persists survey appearance timing and submission count
- Enables accurate rate limiting across sessions
- Synced to global settings via state change handler
- **Evidence**: State structure at line 298044, sync handler in `Wb()` (renamed from `Bb`) at line 482021

## 🐛 Bug Fixes

### Message Selection After Restoration

**What:** Fixed message selection index calculation after restoring previous conversations

**Details:**
- Removed logic that attempted to find the previously selected message by ID after restoration
- Now resets to first message (index 0) when message list changes
- Prevents out-of-bounds errors when message IDs don't match after restoration
- **Evidence**: Function `w11()` at line 439713 (simplified from `I11()` at line 439313)

## 🧹 Cleanup

### Seasonal Content Removal

**What:** Removed Halloween-themed ASCII art mascot variants

**Details:**
- Removed functions: `do1()`, `cg5()`, `pg5()`, `ig5()`, `ag5()`
- Removed feature flag check: `tengu_halloween`
- Removed environment variable check: `CLAUDE_CODE_FORCE_HALLOWEEN`
- Simplified mascot rendering to single implementation (function `Ft1()` at line 444608)
- The Halloween mascots featured witch hats with green decoration that were displayed during October/November 2024
- **Evidence**: Diff lines 222-416 (removed functions), new simplified function at line 444608

### Prompt Template Consolidation

**What:** Consolidated prompt template definitions into reusable variable references

**Details:**
- TodoWrite tool description moved to variable `HoB`/`DoB` at line 205368
- ExitPlanMode tool description moved to variable `DR2`/`KR2` at line 434031
- Reduces duplication and makes prompt updates easier to maintain
- **Evidence**: Variables removed from v2.0.31 lines 205049-220 and 433633-253, re-added as variables in v2.0.32

## 📊 Version Information

- **SDK Version:** Updated from 0.60.0 to 0.66.0
- **Variable `Dh` at line 81689**

## 🔧 Technical Changes

### Constants Added

- `Mk0` at line 83970: `"\n\nHuman:"` prompt separator
- `Ok0` at line 83971: `"\n\nAssistant:"` prompt separator

### Module Initialization

- `b10` at line 481665: New initialization block for path-related utilities
