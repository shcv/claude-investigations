# Changelog for version 2.1.267

## Summary

This release adds per-model effort caps, making it possible to limit expensive reasoning levels for selected models. It also tightens goal safety, improves subagent-report delivery, and adds dark-launched plugin UI surface support.

## New Features


### Per-model effort caps

What: Configure a maximum reasoning effort for individual models.

Usage:

```json
{
  "modelSettings": {
    "claude-sonnet-4-5": {
      "maxEffortLevel": "high"
    }
  }
}
```

Details:

- `modelSettings.<model>.maxEffortLevel` overrides the top-level `maxEffortLevel` for that model.
- The lowest applicable cap across settings sources still wins.
- Use `"max"` to exempt a model from the top-level cap.

Evidence: Per-model setting documentation (search for `"Maximum effort level for this model."`)


## Improvements


### Safer `/goal` activation

`/goal` now requires a trusted workspace and is unavailable when hooks are restricted by settings or organization policy. Accept the workspace trust dialog and restart before setting a goal.

Evidence: Goal guard messages (search for `"/goal is only available in trusted workspaces"`)


### More reliable subagent hand-back

Subagents now have an enforced final-report delivery path, reducing cases where a task completes without its result reaching the calling agent. No configuration is required.

Evidence: Subagent delivery contract (search for `"SubagentHandback"`)


## Bug Fixes

- Prevented deleted shared-memory content from being silently restored unchanged. Recreate it only with changed content if it is genuinely needed. Evidence: tombstone-conflict message (search for `"This memory was recently deleted from shared memory"`)


## In Development

Features with infrastructure added but not yet enabled. These are shipped “dark” and may become available in future versions.


### Plugin UI surface modules [In Development]

What: Plugin hook modules can declare a companion surface module that draws the hook module’s `Client` elements in Claude Code.

Status: Feature-flagged

Details:

- `hooks.json` accepts a new `surface` path alongside a hook `modules` entry.
- The surface module is loaded next to the hook module and supplies UI rendering without access to the hook API object.
- Function-hook modules remain gated by `tengu_plugin_hooks_modules`, which defaults to disabled unless enabled through the rollout or `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS`.

Evidence: Plugin manifest schema (search for `"hooks.json \`surface\` names the surface module"`) and rollout gate (search for `"tengu_plugin_hooks_modules"`)


Generated with:
- tool: `harness-investigations@5a7f523-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/claude-code/changes/changes-v2.1.267.md` (filtered astdiff)
- string diff: `archive/claude-code/changes/string-diff-v2.1.267.txt`
- source modules: `archive/claude-code/original/cli-v2.1.267.modules.json`
- source normalization: `esbuild analysis snapshot; original module text retained`
