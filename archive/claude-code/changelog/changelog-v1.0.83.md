# Changelog for version 1.0.83

## 🎯 Highlights
Advanced beta features including interleaved thinking and 1M token context windows are now available for users of the Anthropic API and Google Vertex AI. AWS Bedrock users maintain the previous feature set for compatibility.

## 🚀 New Features

### Extended Beta Features for First-Party and Vertex API Users
**What:** Users connecting through Anthropic's API or Google Vertex AI now have access to previously restricted beta features
**How to use:**
```bash
# For Anthropic API (default - no special configuration needed)
claude "Analyze this 800,000 token codebase"

# For Google Vertex AI
export CLAUDE_CODE_USE_VERTEX=true
claude "Use interleaved thinking to solve this complex problem"
```
**Details:**
- Enables "interleaved-thinking-2025-05-14" beta feature for enhanced reasoning capabilities
- Enables "context-1m-2025-08-07" beta feature supporting up to 1 million token context windows
- These features are automatically included in API requests when not using AWS Bedrock
- No additional flags or configuration needed - features activate automatically based on your backend

## 💪 Improvements

### Smart Beta Feature Detection Based on Backend
**What changed:** The CLI now intelligently enables or disables beta features based on your chosen backend provider
**Impact:** First-party API and Vertex users get access to cutting-edge features while AWS Bedrock maintains compatibility by excluding features that aren't supported on that platform

## 🐛 Bug Fixes

No bug fixes in this release.
