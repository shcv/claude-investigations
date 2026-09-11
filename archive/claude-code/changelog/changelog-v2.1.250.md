# Changelog for version 2.1.250

## Summary

This maintenance release improves the reliability and predictability of live Artifact watching. It adds more deliberate handling for stalled or transiently rejected live connections and prevents unnecessary re-watching when live updates have been switched off. No new CLI commands, flags, or settings were added.

## Improvements

### More resilient live Artifact watching

What: Claude Code now uses a longer retry window for stalled live Artifact subscriptions and recognizes transient connection failures such as server errors, rate limits, request timeouts, and Cloudflare mitigation.

Details:

- Stalled watches can use a longer randomized retry interval rather than the standard stall interval.
- Transient HTTP conditions—including 5xx responses, `429`, and `408`—are classified separately when deciding whether a live connection remains unavailable.
- This affects the live Artifact workflow; there is no new command or configuration required.

Evidence: Long-stall timing is newly present in `longStallMinMs` / `longStallMaxMs`; live connection handling checks `"cf_mitigated"` and upgrade-rejection status codes.


### Clearer stop behavior for live updates

What: When a live Artifact subscription is no longer available, Claude Code now explicitly avoids reconnecting on its own unless the user asks or the current task still depends on future republishes.

Details:

- If live updates are disabled, the agent is instructed that there is nothing to re-watch.
- This reduces unintended background re-subscriptions after a watch has ended or been disabled.

Evidence: Search for `"it will not reconnect on its own"` and `"there is nothing to re-watch while live updates are switched off"`.


Generated with:
- tool: `harness-investigations@1a8fc5b-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/claude-code/changes/changes-v2.1.250.md` (filtered astdiff)
- string diff: `archive/claude-code/changes/string-diff-v2.1.250.txt`
- source modules: `archive/claude-code/original/cli-v2.1.250.modules.json`
- source normalization: `esbuild analysis snapshot; original module text retained`
