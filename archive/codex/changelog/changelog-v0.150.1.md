# Changelog for version 0.150.1

## Summary

This bug-fix release makes remote compaction account for retained images in its context-token budget by default. Long image-heavy conversations now trim older retained images as needed instead of preserving them outside that budget.

## Official Release Highlights

### Retained-image budgeting for remote compaction

What: Remote compaction now includes retained images when calculating its token budget by default.

Usage:

```toml
# config.toml — opt out to retain the previous behavior
[features]
compaction_image_budget = false
```

Details:

- The existing `compaction_image_budget` feature flag is now stable and enabled by default; it was previously under development and disabled by default.
- During remote compaction, Codex passes the enabled budget to compacted-history construction, so retained images consume the available context budget and older images can be removed when necessary.
- No action is needed for the corrected default. Users who explicitly need the prior behavior can disable the feature in `config.toml`.

Code references:

- `Feature::CompactionImageBudget` and its `FeatureSpec` in `codex-rs/features/src/lib.rs`
- `build_v2_compacted_history` and `RetainedImageBudget` selection in `codex-rs/core/src/compact_remote_v2.rs`


Generated with:
- tool: `harness-investigations@c7c8b06-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/codex/diff/v0.150.1.diff` (raw diff)
- official release notes: `archive/codex/changes/release-notes-v0.150.1.md`
