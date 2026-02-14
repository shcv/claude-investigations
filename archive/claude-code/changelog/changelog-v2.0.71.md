# Changelog for version 2.0.71


## Summary

This release introduces a new keyboard shortcut (`alt+t` / `option+t`) for toggling thinking mode directly from the prompt input, along with improved prompt suggestion handling that allows accepting suggestions by pressing Enter on an empty prompt. The internal MCP SDK has also been upgraded with protocol version 2025-11-25 support.


### Thinking Mode Toggle Hotkey

What: New keyboard shortcut to toggle extended thinking mode on/off directly from the prompt input.

Usage:
Press `alt+t` (or `option+t` on macOS) while focused on the prompt input to open the thinking toggle picker.

Details:
- Opens a dedicated picker UI showing "Enabled" and "Disabled" options
- Displays a warning when changing mid-conversation: "Changing mid-conversation may reduce quality. For best results, set this at the start of a session."
- Logs telemetry event `tengu_thinking_toggled_hotkey` for tracking usage
- Press `Enter` to confirm selection, `Esc` to cancel

Evidence: `$r2()` at line 464580 (ThinkingPicker component, contains `"Toggle thinking mode"` and `"Enable or disable thinking for this session"`) and `HsA` at line 179809 (hotkey definition, `displayText: "alt+t"`)


### Accept Prompt Suggestion with Enter

What: Pressing Enter on an empty prompt input now automatically accepts and submits a visible prompt suggestion.

Usage:
1. When Claude displays a prompt suggestion (gray placeholder text)
2. Press `Enter` without typing anything
3. The suggestion is automatically accepted and submitted

Details:
- Only triggers when a prompt suggestion is visible (`promptSuggestion.shownAt > 0`)
- Calls `markAccepted()` before submission for telemetry tracking
- Previously, pressing Enter on an empty prompt would do nothing

Evidence: Submit handler at line 32049-32056 (input handler, checks `t.trim() === "" && JA.promptSuggestion.text && JA.promptSuggestion.shownAt > 0`)


### Improved Token Counting for Custom System Prompts

The `/context` command now accurately accounts for custom system prompts and appended system prompts when calculating token usage. Previously, the system prompt token count didn't consider SDK users' custom prompts.

Evidence: `NK0()` at line 384355 (context calculation, now uses `ySA()` with `customSystemPrompt` and `appendSystemPrompt` parameters)


### Enhanced Teleportation Telemetry

Session teleportation (resume from web) now tracks whether the first message after resuming succeeds or fails, helping diagnose issues with session transfers.

Evidence: `obA()` at line 2424 (sets `teleportedSessionInfo.isTeleported` and `hasLoggedFirstMessage`), with events `tengu_teleport_first_message_success` and `tengu_teleport_first_message_error`


### MCP SDK Protocol Update

The MCP SDK has been updated to support protocol version `2025-11-25`, with the supported versions list now including: `2025-11-25`, `2025-06-18`, `2025-03-26`, `2024-11-05`, `2024-10-07`.

Evidence: `jn` at line 255378 (protocol version constant `"2025-11-25"`) and `UB1` at line 255540 (supported versions array)
