# Changelog for version 0.153.1

## Summary

Codex 0.153.1 adds the GPT-6-Astra model to the API-supported catalog while keeping it out of the interactive model picker and preserving the picker’s default model. It also corrects experimental Guardian v2 behavior when a thread switches between models with different computer-use review requirements.

## Official Release Highlights

### GPT-6-Astra API model support

What: GPT-6-Astra can now be explicitly selected through an API-backed Codex configuration.

Usage:

```toml
model = "gpt-6-astra"
```

Details:

- GPT-6-Astra is configured for text and image input, verbosity controls, parallel tool calls, web search, and reasoning efforts from `low` through `ultra`.
- It is marked `supported_in_api: true`, so it is available to API-authenticated clients where the account has access.
- It is intentionally hidden from the model picker. The picker-default selection uses the first picker-visible model, so adding this hidden catalog entry does not replace the interactive default.
- The model requires automatic review for Node REPL-backed computer-use tools.

Code references:

- `gpt-6-astra` model catalog entry in `codex-rs/models-manager/models.json`
- `ModelPreset::filter_by_auth` and `ModelPreset::mark_default_by_picker_visibility` in `codex-rs/protocol/src/openai_models.rs`
- `ModelsManager::build_available_models` in `codex-rs/models-manager/src/manager.rs`

## Additional Changes Beyond Official Notes

The diff also includes the following correction for the opt-in Guardian v2 review system.

## In Development

### Guardian v2 model-switch review handling [Experimental]

What: Guardian v2 now follows the active turn’s model-specific Node REPL review requirement when a thread changes models.

Usage:

```toml
[features.guardianv2]
enabled = true
```

Details:

- Guardian v2 is disabled by default and requires the existing automatic-approval review flow.
- In computer-use-only mode, switching to a model that does not require Node REPL review now skips scoring and invalidates any older in-flight score.
- This prevents stale automatic-review scores from being reused after model changes, including when switching back to a model that does require review.

Status: Runtime-gated by `features.guardianv2`; `Feature::GuardianV2` is marked under development and defaults to disabled.

Code references:

- `GuardianV2Extension` in `codex-rs/ext/guardian-v2/src/async_scorer/extension.rs`
- `GuardianV2ReviewScope::ComputerUseOnly` in `codex-rs/ext/guardian-v2/src/async_scorer/config.rs`
- `Feature::GuardianV2` in `codex-rs/features/src/lib.rs`


Generated with:
- tool: `harness-investigations@c7c8b06-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/codex/diff/v0.153.1.diff` (raw diff)
- official release notes: `archive/codex/changes/release-notes-v0.153.1.md`
