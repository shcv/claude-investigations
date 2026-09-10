# Changelog for version 0.153.2

## Summary

This maintenance release corrects the displayed description of the GPT-6-Astra Fast service tier. It does not change request behavior, pricing, usage limits, or available commands.

## Official Release Highlights


### Corrected GPT-6-Astra Fast-tier description

What: The Fast tier’s UI/catalog description now states “2x speed, increased usage,” replacing the inaccurate “1.5x speed, increased usage.”

Usage: No action is required. The corrected wording appears wherever Codex presents this model tier.

Details:

- This is a display-text correction only; selecting the Fast tier works the same as before.
- No CLI flags, configuration keys, API methods, or model-tier behavior changed.

Code references:

- Updated Fast-tier `description` entry in `codex-rs/models-manager/models.json`


Generated with:
- tool: `harness-investigations@c7c8b06-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/codex/diff/v0.153.2.diff` (raw diff)
- official release notes: `archive/codex/changes/release-notes-v0.153.2.md`
