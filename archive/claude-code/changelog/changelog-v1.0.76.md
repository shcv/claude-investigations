# Changelog for version 1.0.76

## Highlights
Claude Code now supports Sonnet 4 with 1-million token context windows, allowing for much longer conversations and the ability to work with significantly larger codebases without hitting context limits. This premium feature provides 5x more context than the standard 200,000 token limit.


### Sonnet 4 with 1M Context Support
**What:** Added support for Claude Sonnet 4 model with 1-million token context window
**How to use:**
```bash
# Switch to the 1M context model through the model selector
# The model will appear as "Sonnet (1M context)" in your model options
# Note: This feature requires API access verification
```
**Details:**
- Available as "Sonnet (1M context)" or "Sonnet 4 (with 1M token context)" in the model selector
- Provides 1,000,000 tokens of context (5x the standard 200,000 limit)
- Perfect for working with large codebases, lengthy documents, or extended coding sessions
- Pricing: $6 per million input tokens, $22.50 per million output tokens
- Access is controlled via API verification - only available to eligible accounts
- Uses rate limits faster than standard Sonnet on long requests
- Context warnings are intelligently adjusted to avoid premature alerts when you still have hundreds of thousands of tokens available


### Optimized Import Statements
**What changed:** Refactored Node.js module imports to use named imports instead of default imports
**Impact:** Reduces memory footprint and improves code clarity by explicitly importing only the required functions from crypto, stream, and process modules


### Smart Context Warning System
**What changed:** Context warnings now adapt based on the model's maximum context size
**Impact:** Users with 1M context models won't receive premature "low context" warnings when they still have substantial tokens remaining, improving the experience for long-form conversations

## Bug Fixes

No bug fixes were included in this release.
