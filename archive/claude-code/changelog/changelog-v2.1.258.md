# Changelog for version 2.1.258

## Summary

This is a focused reliability release. It prevents Claude Code from starting an unnecessary model call when it receives an orphaned permission response that cannot be applied and the turn contains no user prompt.

## Bug Fixes

- Fixed an edge case in permission-response recovery: if an orphaned permission cannot be matched to an active tool use, and there is neither a prompt nor a deferred tool to process, Claude Code now completes the turn cleanly instead of continuing into a model call. Evidence: recovery path logs `"Orphaned permission could not be applied and the turn has no prompt: ending the turn without a model call"`.


Generated with:
- tool: `harness-investigations@5a7f523-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/claude-code/changes/changes-v2.1.258.md` (filtered astdiff)
- string diff: `archive/claude-code/changes/string-diff-v2.1.258.txt`
- source modules: `archive/claude-code/original/cli-v2.1.258.modules.json`
- source normalization: `esbuild analysis snapshot; original module text retained`
