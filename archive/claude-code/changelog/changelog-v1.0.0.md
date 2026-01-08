# Changelog for version 1.0.0

Based on my analysis of the diff file, here's the changelog for Claude Code version 1.0.0:

# Claude Code v1.0.0 Changelog

### New Models

#### Claude Opus 4
- **NEW**: Introduced Claude Opus 4 model for complex tasks
- Available across all providers:
  - First-party API: `claude-opus-4-20250514`
  - AWS Bedrock: `us.anthropic.claude-opus-4-20250514-v1:0`
  - Google Vertex: `claude-opus-4@20250514`
- Pricing: $15/$75 per million tokens
- Access Opus using `/model opus` command

#### Claude Sonnet 4
- **NEW**: Introduced Claude Sonnet 4 as the new default model for daily use
- Available across all providers:
  - First-party API: `claude-sonnet-4-20250514`
  - AWS Bedrock: `us.anthropic.claude-sonnet-4-20250514-v1:0`
  - Google Vertex: `claude-sonnet-4@20250514`
- Claude Sonnet 3.7 remains available for AWS Bedrock users

### User-Facing Features

#### Model Selection Improvements
- Enhanced `/model` command with better model descriptions:
  - **Opus**: "Claude Opus 4 for complex tasks"
  - **Sonnet**: "Claude Sonnet 4 for daily use"
- Model selection now accepts both "sonnet" and "opus" as valid options
- Improved model display showing "Claude Sonnet 4" or "Claude Sonnet 3.7" based on your provider

#### Enhanced Error Handling
- **NEW**: Smart fallback for rate-limited users when Opus experiences high load
- New error message: "Opus is experiencing high load, please use /model to switch to Sonnet"
- Improved handling of repeated 529 (overloaded) errors with clearer guidance

#### Visual Improvements
- **NEW**: Enhanced splash screen with Claude ASCII art (3 different variations based on terminal size)
- **NEW**: Setup warnings dialog for potential configuration issues
  - Shows clear warnings with actionable instructions
  - Press Enter to continue anyway or Ctrl+C to exit and fix issues

### CLI Improvements

#### Better IDE Integration
- Removed `ENABLE_IDE_INTEGRATION` environment variable requirement
- IDE integration now works automatically when supported IDEs are detected
- Improved VS Code and JetBrains plugin installation flow

#### Performance & Reliability
- Removed the experimental batch tool execution feature (`Call` tool)
- Streamlined tool execution for better reliability
- Improved handling of unified rate limits with automatic fallback

### Technical Changes

#### Model Architecture
- Added support for "interleaved-thinking-2025-05-14" capability
- Enhanced model selection logic with provider-specific defaults
- Improved model availability detection based on user permissions

#### Error Recovery
- Better handling of OAuth token revocation
- Improved credit balance error messages
- Enhanced prompt length error handling

### Removed Features
- Removed placeholder model used for testing
- Removed batch tool execution (`mX1`/batch tool)
- Removed several internal helper functions for cleaner codebase

### Bug Fixes
- Fixed duplicate model selection issues
- Improved error handling for overloaded servers
- Better handling of rate limit resets with unified fallback

### Setting Models
```bash
# Use the new Opus model for complex tasks
/model opus

# Switch back to Sonnet for daily use
/model sonnet

# Check current model
/model
```

### Handling Rate Limits
When you encounter rate limits with Opus during high load periods, Claude Code will now suggest switching to Sonnet automatically with a clear message.

### Visual Experience
The new splash screen adapts to your terminal size, showing different Claude ASCII art based on available space, creating a more polished first-run experience.
