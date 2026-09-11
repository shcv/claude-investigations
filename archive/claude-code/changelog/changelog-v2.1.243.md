# Changelog for version 2.1.243

## Summary

No user-facing Claude Code changes could be substantiated in this build. The large structural diff is rebundling noise from split Bun modules; the only changed string literals are build metadata.

## Notes

- No new commands, flags, settings, environment variables, feature gates, user-visible messages, or verified bug fixes were found.
- The AST-extracted string diff contains only the build timestamp and revision change: `"2026-08-24T21:05:22Z"` and `"8565f923a3ec61dc4c61bf7bfd995521c702c9fc"`.
- Both original module archives contain 1,378 modules. The apparent additions, removals, and low-similarity structural records reflect changed module wrappers, import bindings, and order rather than product behavior.


Generated with:
- tool: `harness-investigations@d83141a-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/claude-code/changes/changes-v2.1.243.md` (filtered astdiff)
- string diff: `archive/claude-code/changes/string-diff-v2.1.243.txt`
- source modules: `archive/claude-code/original/cli-v2.1.243.modules.json`
- source normalization: `esbuild analysis snapshot; original module text retained`
