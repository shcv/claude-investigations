# Changelog for version 0.149.1

## Release Status

> **Not yet released:** `rust-v0.149.1` is present in Git, but no published GitHub Release was found at sync time. This may be an intermediate development snapshot or a release prepared ahead of publication.


## Summary

This intermediate development snapshot adds a `codex exec` option for labeling newly created and forked threads. It also introduces an experimental remote-compaction mode that accounts for retained images in the context budget. No published GitHub Release was available for this tag.

## New Features

### Thread-source classification for non-interactive runs

What: `codex exec` can now attach a source classification to newly created or forked threads.

Usage:

```bash
codex exec --thread-source automated_review "Review this repository for regressions"
```

Details:

- The global `--thread-source SOURCE` option applies to new threads and to threads created by `codex exec fork`.
- With no option supplied, Codex continues to classify the thread as `user`.
- `user`, `subagent`, and `memory_consolidation` are recognized names; other values are preserved as feature-specific source labels, such as `automated_review`.
- This is chiefly useful for automation and integrations that need thread provenance in the app-server and persisted rollout metadata.

Code references:

- `Cli::thread_source` in `codex-rs/exec/src/cli.rs`
- `thread_start_params_from_config` and `ThreadForkParams` handling in `codex-rs/exec/src/lib.rs`
- `ThreadSource` in `codex-rs/protocol/src/protocol.rs`


## In Development

### Image-aware remote compaction budgets [Experimental]

What: Remote compaction can optionally count retained input images against its context-token budget.

Usage:

```toml
[features]
compaction_image_budget = true
```

Details:

- The setting affects the Remote Compaction v2 path and is disabled by default.
- When enabled, image-containing boundary messages are trimmed according to estimated image cost during compaction, rather than retaining images outside the text budget.
- An image and its adjacent harness labels are kept or removed atomically; later message content is favored, while audio remains uncharged.
- This can reduce the images carried into follow-up requests after compaction, trading retained visual context for tighter budget adherence.

Status: Runtime-gated by `[features].compaction_image_budget = true`; `Feature::CompactionImageBudget` is `UnderDevelopment` and defaults to disabled.

Code references:

- `Feature::CompactionImageBudget` in `codex-rs/features/src/lib.rs`
- `truncate_retained_messages` in `codex-rs/core/src/compact_remote_v2.rs`
- `truncate_message_to_token_budget` in `codex-rs/core/src/compact_remote_v2_images.rs`
- Config schema entry in `codex-rs/core/config.schema.json`


## Notes

This is a source-tag snapshot (`rust-v0.149.1`), not a published release with official binaries or assets.


Generated with:
- tool: `harness-investigations@a3dcf1c-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/codex/diff/v0.149.1.diff` (raw diff)
- release status: `unreleased Git tag; no published GitHub Release found at sync time`
