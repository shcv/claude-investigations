# Changelog for version 0.153.3

## Summary

Codex 0.153.3 adds GPT-6-Astra to Amazon Bedrock model selection, including global and US cross-region Runtime routes. It also corrects GPT-6-Astra’s handling of asynchronous clarification questions and aligns Bedrock capability metadata with supported behavior.

## Official Release Highlights

### GPT-6-Astra for Amazon Bedrock

What: GPT-6-Astra is now available through Amazon Bedrock’s Mantle catalog and Bedrock Runtime global and US cross-region routes.

Usage:

```bash
# Amazon Bedrock Mantle
codex -m openai.gpt-6-astra

# Amazon Bedrock Runtime
codex -m global.openai.gpt-6-astra
codex -m us.openai.gpt-6-astra
```

Details:

- The interactive model picker now lists GPT-6-Astra for configured Bedrock providers.
- Runtime routes expose `global.openai.gpt-6-astra` and `us.openai.gpt-6-astra`.
- GPT-6-Astra is placed after GPT-5.6 Sol in the Bedrock picker and supports the available Bedrock reasoning-level choices through Max.

Code references:

- `AMAZON_BEDROCK_GPT_6_ASTRA_MODEL_ID` in `codex-rs/model-provider-info/src/lib.rs`
- `static_model_catalog()` and `GPT_6_ASTRA_OPENAI_MODEL_ID` in `codex-rs/model-provider/src/amazon_bedrock/catalog.rs`
- `static_runtime_model_catalog()` in `codex-rs/model-provider/src/amazon_bedrock/runtime_catalog.rs`


### Corrected asynchronous clarification guidance for GPT-6-Astra

What: GPT-6-Astra’s bundled instructions now direct it to use the supported clarification-question mechanism and account for its text-only response format.

Details:

- This corrects model behavior when it needs to ask a user an asynchronous clarification question.
- No configuration change is required.

Code references: `gpt-6-astra` `model_messages.instructions_template` in `codex-rs/models-manager/models.json`

## Additional Changes Beyond Official Notes

### Bedrock capability alignment

What: Codex now normalizes Bedrock model metadata to avoid advertising or sending capabilities that Amazon Bedrock does not support.

Usage:

```bash
codex -m openai.gpt-5.6-sol
```

Details:

- The Bedrock catalog clears unsupported speed and service-tier options, leaving the provider’s default tier.
- Web search uses the text-only Bedrock-compatible tool type.
- Bedrock models use multi-agent V1 because Bedrock does not support the response items required by multi-agent V2.
- Bedrock GPT-5.6-family entries, including GPT-6-Astra, remove the unsupported Ultra reasoning level.

Code references:

- `normalize_bedrock_catalog()` in `codex-rs/model-provider/src/amazon_bedrock/catalog.rs`
- `bedrock_model()` in `codex-rs/model-provider/src/amazon_bedrock/catalog.rs`


Generated with:
- tool: `harness-investigations@c7c8b06-dirty`
- provider: `codex`
- model: `gpt-5.6-terra`
- reasoning effort: `medium`
- primary diff: `archive/codex/diff/v0.153.3.diff` (raw diff)
- official release notes: `archive/codex/changes/release-notes-v0.153.3.md`
