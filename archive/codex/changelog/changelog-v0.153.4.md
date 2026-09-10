# Changelog for version 0.153.4

## Summary

This hotfix makes `gpt-6-astra` visible in Codex’s bundled model picker and selects it as the bundled default when no model is configured. It also corrects Astra’s built-in guidance so it only uses asynchronous questions when that tool is available in the session.

## Official Release Highlights

### Astra is available from the bundled model picker

What: `gpt-6-astra` is now shown in the interactive model picker and becomes the bundled default for users without an explicit model selection.

Usage:

```bash
codex -m gpt-6-astra
```

Details:

- The bundled catalog changes Astra’s `visibility` from `"hide"` to `"list"`.
- Astra has priority `1`; the model catalog marks the first picker-visible model as the default.
- Existing explicit selections, such as `model = "gpt-5.6-sol"` in `config.toml` or `-m`, remain explicit choices.

Code references:

- `gpt-6-astra` entry in `codex-rs/models-manager/models.json`
- `ModelsManager::list_models` in `codex-rs/models-manager/src/manager.rs`
- `ModelPreset::mark_default_by_picker_visibility` in `codex-rs/protocol/src/openai_models.rs`


### Astra only asks asynchronous questions when supported

What: Astra’s bundled instruction template now conditions asynchronous questioning on the question tool being available in the active session.

Details:

- This prevents the model from attempting an unavailable interaction path.
- The change affects Astra’s supplied model guidance; it does not add a new CLI command, configuration key, or app-server protocol method.

Code references:

- `model_messages.instructions_template` for `gpt-6-astra` in `codex-rs/models-manager/models.json`


Generated with:
- tool: `harness-investigations@c7c8b06-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/codex/diff/v0.153.4.diff` (raw diff)
- official release notes: `archive/codex/changes/release-notes-v0.153.4.md`
