# Changelog for version 2.1.247

## Summary

This release adds configurable organization spinner tips and improves cloud-session startup from Git linked worktrees. It also contains substantial, currently unavailable infrastructure for local Artifact previews and for securely routing local tools into eligible cloud sessions.

## New Features

### Organization-supplied spinner tips

What: Administrators and users can add custom tips to Claude Code’s spinner rotation.

Usage:

```json
{
  "spinnerTipsOverride": {
    "label": "Acme Tip",
    "excludeDefault": false,
    "tips": [
      {
        "id": "acme-review",
        "text": "Run the project checks before requesting review.",
        "cooldownSessions": 5,
        "priority": 1
      }
    ],
    "tipsFile": "~/.config/acme/claude-tips.json"
  }
}
```

Details:

- `tips` accepts plain strings or objects with a stable `id`, `text`, optional `cooldownSessions`, and optional `priority`.
- Set `excludeDefault: true` to show only custom tips.
- `tipsFile` accepts a local absolute or `~/` path to a JSON array (or `{ "tips": [...] }`) and is read once per Claude Code process.
- Project settings may provide only plain-string tips; `label` and `tipsFile` are restricted to user or managed settings.

Evidence: New `spinnerTipsOverride` setting (search for `"Add your organization's own tips to the spinner tip rotation"` and `"spinnerTipsOverride.tipsFile"`).


## Improvements

### Cloud sessions can start from eligible Git linked worktrees

What: A cloud session can now upload the commits and uncommitted changes from an eligible `git worktree` checkout instead of refusing it outright.

Usage:

```bash
cd path/to/linked-worktree
claude --cloud
```

Details:

- This is an upload fallback, not bidirectional synchronization: changes do not sync back to the linked worktree and the cloud session cannot push to GitHub from that upload.
- Claude Code still refuses unsupported or unverifiable worktree layouts, and recommends the repository’s main checkout when file sync is required.

Evidence: Linked-worktree upload messaging (search for `"Started from an upload of this linked working tree"` and `"nothing syncs back here and it can't push to GitHub"`).


## In Development

Features with infrastructure added but not yet enabled. These are shipped dark and may become available in future versions.


### Local Artifact preview [In Development]

What: Artifact authors will be able to render a local HTML page in a locked-down headless browser before publishing, with desktop/mobile screenshots, light/dark rendering, and mechanical layout/load checks.

Status: Stubbed and feature-flagged.

Details:

- The intended tool action is `preview` with `file_path`, optional viewport widths, and themes.
- Preview is read-only and designed to block network access except Google Fonts, pop-ups, and WebRTC.
- This build hardcodes the preview implementation as unavailable (`"artifact preview is not compiled into this build"`); even where compiled, rollout is gated by `tengu_cobalt_plinth_aspen` with a false default.

Evidence: Preview tool description (search for `"Render a local page file in a headless browser to check it before publishing. Nothing is uploaded."`) and gate (search for `"tengu_cobalt_plinth_aspen"`).


### Local tools for cloud sessions [In Development]

What: Eligible cloud sessions will be able to discover and invoke tools served by an attached local Claude Code client, including native tools, MCP tools, and internal directory-sync plumbing.

Status: Feature-flagged.

Details:

- The protocol adds `remote_tools_announce`, liveness checks, delivery/error handling, and worker-epoch re-announcement after a cloud worker restart.
- It is gated by the server-controlled `tengu_violin_wood` flag, which defaults to disabled.
- Directory-sync plumbing is explicitly internal and never model-facing.

Evidence: Remote-tool protocol and gate (search for `"remote_tools_announce"` and `"tengu_violin_wood"`).


Generated with:
- tool: `harness-investigations@d83141a-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/claude-code/changes/changes-v2.1.247.md` (filtered astdiff)
- string diff: `archive/claude-code/changes/string-diff-v2.1.247.txt`
- source modules: `archive/claude-code/original/cli-v2.1.247.modules.json`
- source normalization: `esbuild analysis snapshot; original module text retained`
