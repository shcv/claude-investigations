# GitHub Issue: Session labels show raw XML tags in --resume picker

## Description

When using `--resume` or `/resume`, session labels sometimes display raw XML content instead of clean, human-readable text:

```
<command-name>/clear</command-name> <command-message>clear</command-message> <command-args></command-args…
```

Or system messages:

```
[Request interrupted by user for tool use]
```

## Steps to Reproduce

1. Start a Claude Code session
2. Run `/clear` (or interrupt a tool use with Escape)
3. Start a new session in the same project
4. Run `claude --resume` or `/resume`
5. Observe the session list - previous sessions show raw XML as labels

## Expected Behavior

Session labels should show clean, human-readable text, not internal XML markup or system messages.

## Analysis

The `_i1` sanitization function (used by `dc` to generate labels) only strips `<ide_opened_file>` and `<ide_selection>` tags. It doesn't handle:
- `<command-name>`, `<command-message>`, `<command-args>`
- `<local-command-caveat>`, `<local-command-stdout>`
- `[Request interrupted...]` markers

The `Cf6` function (extracts first prompt) added filtering for built-in commands in v2.1.31, but interrupt markers and custom commands still leak through.

## Environment

- Claude Code version: 2.1.31
- OS: Linux

---

# GitHub Issue: `classifyHandoffIfNeeded is not defined` crashes backgrounded agents

## Description

When a subagent (Task tool) is moved to the background during execution and then completes, it crashes with:
```
classifyHandoffIfNeeded is not defined
```

This is a function that is called but never defined in the codebase.

## Steps to Reproduce

1. Start a Claude Code session
2. Have Claude use the Task tool to launch a subagent (without `run_in_background: true`)
3. While the agent is running, press `ctrl+b` to background it
4. Wait for the agent to complete in the background
5. Agent fails with "classifyHandoffIfNeeded is not defined"

## Expected Behavior

Agents backgrounded with ctrl+b should complete successfully and return their results.

## Analysis

The function `classifyHandoffIfNeeded` is called at one location (line 421994) but has no definition anywhere in the codebase:

```javascript
E1 = await classifyHandoffIfNeeded({
  agentMessages: q1,
  toolPermissionContext: S1.toolPermissionContext,
  abortSignal: D1.abortController.signal,
  isNonInteractiveSession: J.options.isNonInteractiveSession,
  subagentType: q,
  totalToolUseCount: h1.totalToolUseCount,
});
```

### Why this bug is rare

The bug **only affects agents moved to background mid-execution**. It does NOT affect:
- Agents that run synchronously to completion
- Agents started with `run_in_background: true` from the beginning

The code has two separate async completion paths:
1. **Explicit async path** (lines 421849-421909): Used for `run_in_background: true`. Does NOT call the undefined function.
2. **Moved-to-background path** (lines 421966-422035): Used when user presses ctrl+b. DOES call the undefined function.

The function appears to have been intended to classify/tag agent output when completion happens in background (perhaps to determine if a "handoff" notification is needed), but the implementation was never added.

## Impact

- Agents backgrounded with ctrl+b will crash on completion
- Agent work may be lost
- Error message is confusing (suggests code issue rather than trigger condition)

## Environment

- Claude Code version: 2.1.31 (bug present since v2.1.26)
- OS: Linux
