# Changelog for version 2.1.241

## Summary

This is a focused bug-fix release. Non-interactive Claude Code sessions can now honor the configured default for thinking summaries instead of unconditionally suppressing them.

## Bug Fixes

### Respect thinking-summary settings in non-interactive sessions

What: Claude Code no longer forces thinking display to `none` merely because a session is non-interactive.

Usage:

```json
// ~/.claude/settings.json
{
  "showThinkingSummaries": true
}
```

```bash
claude -p "Explain this repository's architecture."
```

Details:

- This fixes non-interactive runs ignoring the existing `showThinkingSummaries` setting.
- Explicit `thinking_display: "omitted"` behavior is unchanged.
- No migration is required.

Evidence: The non-interactive early return was removed from the display-mode selection path; search for `"showThinkingSummaries"` and `"thinking_and_connector_text"`.


Generated with:
- tool: `harness-investigations@94f81fe-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/claude-code/changes/changes-v2.1.241.md` (filtered astdiff)
- string diff: `archive/claude-code/changes/string-diff-v2.1.241.txt`
