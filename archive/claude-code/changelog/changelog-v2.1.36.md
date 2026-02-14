# Changelog for version 2.1.36


## Summary

This release introduces **Fast Mode**, a new high-speed output mode for Opus 4.6 that uses the same model with faster token generation. Fast mode is billed as extra usage at a premium rate with separate rate limits, and can be toggled with the new `/fast` command.


### Fast Mode

What: High-speed output mode for Claude Opus 4.6 that provides faster token generation without switching to a different model. Currently available as a research preview.

Usage:
```bash
# Toggle fast mode from the prompt
/fast

# Or configure in settings.json
{
  "fastMode": true
}
```

Details:
- Uses the same Opus 4.6 model with accelerated output generation
- Billed as extra usage at a premium rate with separate rate limits
- Interactive toggle shows current status: "Fast mode ON" or "Fast mode OFF"
- When enabled, displays with the penguin icon (↯) and orange color theming
- Has its own rate limits; when reached, enters a cooldown period and automatically re-enables when reset
- Model automatically switches to Opus 4.6 if not already selected

**Availability**:
- Requires a paid subscription
- Requires extra usage billing to be enabled (`/extra-usage`)
- Requires the native binary (not available via npm install)
- Not available on Bedrock, Vertex, Foundry, or in the Agent SDK
- Organizations can disable fast mode for their accounts

**Rate Limiting**:
- Displays "Fast limit reached and temporarily disabled · resets in X" when hitting limits
- Shows "Fast limit reset · now using fast mode" when cooldown expires
- Tracks remaining time to reset in the UI

**Promotions**:
- May show discount percentages for extra usage (e.g., "50% off through [date]")

Evidence: Fast mode system (search for `"Fast mode"`, `"tengu_penguins_enabled"`, `"/fast"`)


### New User Setting: `fastMode`

What: New boolean setting to persist fast mode state across sessions.

Usage:
```json
{
  "fastMode": true
}
```

Details:
- When `true`, fast mode is enabled
- When absent or `false`, fast mode is off
- Can be set via the `/fast` command or directly in settings.json

Evidence: Setting schema (search for `"When true, fast mode is enabled"`)


### Enhanced Opus 4.6 Promotional Messaging

Promotional messages now include fast mode mentions for users who have extra usage enabled:
- "Opus 4.6 is here · $50 free extra usage · Try fast mode or use it when you hit a limit /extra-usage to enable"
- "Opus 4.6 is here · Try fast mode"

Evidence: Promotional strings (search for `"Try fast mode"`)


### Fast Mode System Prompt Context

The system prompt now includes `<fast_mode_info>` context explaining fast mode to Claude:
> "Fast mode for Claude Code uses the same Claude Opus 4.6 model with faster output. It does NOT switch to a different model. It can be toggled with /fast."

Evidence: System prompt template (search for `"<fast_mode_info>"`)


### Interactive Fast Mode Toggle UI

The `/fast` command provides an interactive toggle interface with:
- Current ON/OFF status with visual highlighting
- Tab to toggle, Enter to confirm, Esc to cancel
- Rate limit status and reset countdown when in cooldown
- Link to documentation: https://code.claude.com/docs/en/fast-mode
- Displays pricing information and any active discounts

Evidence: Toggle UI component (search for `"Tab to toggle · Enter to confirm"`)
