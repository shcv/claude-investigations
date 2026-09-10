# Changelog for version 2.1.242

## Summary

No user-facing Claude Code changes could be substantiated in this build. The apparent large diff is caused by the switch to split Bun modules and rebundling; the remaining string-only changes are serialization differences such as Unicode escape normalization, not changed behavior.

## Notes

- Existing settings and features shown as “added” by the bundle diff were already present in 2.1.241; for example, search both versions for `"disableFeatureDiscovery"` or `"Hide feature announcements"`.
- The string-only changes preserve the same text while changing representation, such as `"live.input carries a non-string value under the method key"`.
- No new command, CLI flag, setting, environment variable, enabled feature gate, or user-facing bug fix was verified as absent from 2.1.241.


Generated with:
- tool: `harness-investigations@1d2b109-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/claude-code/changes/changes-v2.1.242.md` (filtered astdiff)
- string diff: `archive/claude-code/changes/string-diff-v2.1.242.txt`
- source modules: `archive/claude-code/original/cli-v2.1.242.modules.json`
- source normalization: `esbuild analysis snapshot; original module text retained`
