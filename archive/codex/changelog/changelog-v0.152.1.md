# Changelog for version 0.152.1

## Official Release Highlights

Guardian approval review now honors Node REPL policies supplied through the selected Guardian review model’s metadata. This fixes reviews that previously always used Codex’s bundled Node REPL policy.

## Summary

This patch fixes Guardian’s handling of approval-review instructions for `node_repl` and `cua_repl` actions. The effective Guardian reviewer model can now supply its own policy; if it does not, Codex retains the bundled default.

## Bug Fixes

### Guardian review honors model-provided Node REPL policy

What: Approval reviews for Node and CUA REPL actions now inject the policy from the Guardian reviewer model’s `auto_review.node_repl_policy` metadata instead of unconditionally injecting the built-in policy.

Usage: No CLI flag or local configuration is required. The behavior applies automatically when the active Guardian reviewer model catalog provides this metadata.

Details:

- `GuardianNodeReplPolicy::from_model_messages` reads the reviewer model’s policy and falls back to the bundled policy when none is provided.
- An explicitly empty metadata policy suppresses policy injection, rather than being replaced with the default.
- Cached Guardian review sessions include the effective policy in their reuse key, preventing a reviewer session configured with one policy from being reused after the policy changes.
- Model activation rejects an unsafe parent-fallback transition when it would change the effective Node REPL policy.

Code references:

- `AutoReviewMessages::node_repl_policy` in `codex-rs/protocol/src/openai_models.rs`
- `GuardianNodeReplPolicy::from_model_messages` in `codex-rs/core/src/context/guardian_node_repl_policy.rs`
- `ensure_guardian_node_repl_policy` and `GuardianReviewSessionReuseKey::with_node_repl_policy` in `codex-rs/core/src/guardian/review_session.rs`
- `check_legacy_model_safety` in `codex-rs/core/src/session/step_activation.rs`


Generated with:
- tool: `harness-investigations@c7c8b06-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/codex/diff/v0.152.1.diff` (raw diff)
- official release notes: `archive/codex/changes/release-notes-v0.152.1.md`
