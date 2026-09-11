# Changelog for version 2.1.263

## Summary

This release expands the effort-reduction prompt to support a second model and configurable messaging, with a gradual server-controlled rollout. It also recovers automatically when an API rejects the thinking-binding-controls beta instead of leaving the conversation failed.

## Improvements


### Model-specific effort prompts [Gradual Rollout]

Claude Code can now present a configurable prompt to lower the default effort setting for an additional model, tracking whether the prompt was seen per model rather than globally.

Details:

- The existing prompt was limited to a high-to-medium suggestion for one model.
- The new configuration supports `high`, `xhigh`, or `max` as the starting effort and can provide custom warning text.
- Availability is server-controlled through `tengu_steady_plum`; users who are not included in the rollout will not see the new prompt.

Evidence: Model-specific effort nudge configuration (search for `"tengu_steady_plum"` and `"Switch your default effort to {to}?"`).

## Bug Fixes

- Claude Code now retries a request without the thinking-binding-controls beta header and `block_binding` value when the server rejects that beta for the conversation. This prevents an otherwise unsupported beta control from blocking the request. Evidence: retry handling (search for `"retry:thinking-binding-controls"`).


Generated with:
- tool: `harness-investigations@5a7f523-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/claude-code/changes/changes-v2.1.263.md` (filtered astdiff)
- string diff: `archive/claude-code/changes/string-diff-v2.1.263.txt`
- source modules: `archive/claude-code/original/cli-v2.1.263.modules.json`
- source normalization: `esbuild analysis snapshot; original module text retained`
