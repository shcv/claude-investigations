# Changelog for version 2.1.245

## Summary

This is a maintenance release with no verified user-facing CLI changes relative to 2.1.243. No new commands, flags, settings, permission rules, feature gates, or user-facing strings were added; the extracted string diff contains only the build timestamp and Git revision update.

Evidence: package metadata changes from `VERSION: "2.1.243"` to `VERSION: "2.1.245"`; search for `"2026-08-25T04:00:18Z"`.

## Notes

The large structural diff is attributable to split Bun-module rebundling: chunk names, imports, wrapper types, symbol names, and module order changed, but the original module sources and string-literal comparison provide no evidence of a user-noticeable product change.


Generated with:
- tool: `harness-investigations@d83141a-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/claude-code/changes/changes-v2.1.245.md` (filtered astdiff)
- string diff: `archive/claude-code/changes/string-diff-v2.1.245.txt`
- source modules: `archive/claude-code/original/cli-v2.1.245.modules.json`
- source normalization: `esbuild analysis snapshot; original module text retained`
