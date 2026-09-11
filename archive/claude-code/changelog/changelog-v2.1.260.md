# Changelog for version 2.1.260

## Summary

This release adds a safer cleanup path for completed background-agent worktrees. It also ships feature-flagged Remote Control host-profile controls that are not enabled by default.

## Improvements


### Safely remove a background worktree with unpushed commits

`claude rm` can now explicitly remove a completed background session’s worktree even when it contains unpushed commits or uncommitted changes. The command requires a commit-and-worktree token supplied by a prior refusal, helping prevent deletion after the worktree has changed.

Usage:

```bash
claude rm <id> --discard-unpushed <commit>@<worktree-id>
```

Details:

- Run `claude rm <id>` first.
- If cleanup is blocked because commits are unpushed, Claude Code prints the exact protected value to pass.
- The deletion path verifies both the recorded commit and worktree identity before discarding content.

Evidence: background-session cleanup accepts `"--discard-unpushed"` and reports `Usage: claude rm <id> [--discard-unpushed <commit>@<worktree-id>]`.

## In Development

Features with infrastructure added but not yet enabled. These are shipped dark and may become available in future versions.


### Remote Control host-profile sharing [In Development]

What: Remote Control can be configured to control how much machine information it reports when registering a session.

Status: Feature-flagged. The implementation is gated by `tengu_bridge_host_profile`, whose source default is `"off"`.

Usage:

```json
{
  "remoteControl": {
    "shareHostProfile": "basic"
  }
}
```

Details:

- `"off"` reports no machine profile.
- `"basic"` reports the operating system, architecture, and detected developer tools.
- `"full"` additionally reports names of machine-configured MCP servers; repository `.mcp.json` servers are excluded.
- User, managed, and `--settings` configuration can set the level; project and local settings can only make it more restrictive.
- Changes are applied when Remote Control registers or starts, depending on whether the level is lowered or raised.

Evidence: `remoteControl.shareHostProfile` is described in settings as controlling “What a Remote Control environment reports about this machine,” while activation reads `tengu_bridge_host_profile` with default `"off"`.


Generated with:
- tool: `harness-investigations@5a7f523-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/claude-code/changes/changes-v2.1.260.md` (filtered astdiff)
- string diff: `archive/claude-code/changes/string-diff-v2.1.260.txt`
- source modules: `archive/claude-code/original/cli-v2.1.260.modules.json`
- source normalization: `esbuild analysis snapshot; original module text retained`
