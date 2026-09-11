# Changelog for version 2.1.252

## Summary

This maintenance release improves how eligible synced sessions refresh their instructions and context after account, policy, directory, or settings changes. It also makes temporary task-output storage safer when its directory has moved, been replaced, or resolves through an unsafe link.

## Improvements

### Automatic Refresh of Session Instructions and Context

What: Claude Code can now re-read and replace session instructions and contextual values when the session state changes.

Usage: No action required. This occurs automatically after events such as a conversation compaction, managed-policy refresh, added working directory, synced settings, or account change.

Details:

- Replacement instructions explicitly supersede their earlier copies.
- Refreshed context replaces stale account, project, and Git-status information.
- This is particularly relevant to eligible synced or managed sessions; background sessions are excluded.

Evidence: Session-refresh reasons and replacement messaging (search for `"Instruction files were re-read"` and `"after settings were synced onto this machine"`).

## Bug Fixes

- Safer handling for task-output temporary directories that have moved, become symlinks, or resolve unexpectedly. Claude Code now refuses unsafe output-path pinning, accepts verified same-directory aliases where appropriate, and gives recovery guidance to restart with a fresh `CLAUDE_CODE_TMPDIR`. Evidence: search for `"task output: pin of"` and `"restart Claude Code with CLAUDE_CODE_TMPDIR set to a fresh directory"`.


Generated with:
- tool: `harness-investigations@1a8fc5b-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/claude-code/changes/changes-v2.1.252.md` (filtered astdiff)
- string diff: `archive/claude-code/changes/string-diff-v2.1.252.txt`
- source modules: `archive/claude-code/original/cli-v2.1.252.modules.json`
- source normalization: `esbuild analysis snapshot; original module text retained`
