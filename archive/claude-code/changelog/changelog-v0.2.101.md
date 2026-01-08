# Changelog for version 0.2.101

Based on the diff analysis, here is the changelog for Claude Code version 0.2.101:

### New Features

#### Model Selection and Configuration
- **Added model selection support**: Users can now choose between different Claude models or use the default
  - Claude 3.7 Sonnet (Fast and balanced · $3/$15 per Mtok)
  - Claude 3.5 Sonnet (Previous generation · $3/$15 per Mtok)  
  - Claude 3.5 Haiku (Quick responses · $0.80/$4 per Mtok)
  - Custom model configurations
- **Environment variable support**: Set your preferred model using `ANTHROPIC_MODEL` environment variable
- **Platform-specific model routing**: Automatic detection and routing for Bedrock (`CLAUDE_CODE_USE_BEDROCK`) and Vertex (`CLAUDE_CODE_USE_VERTEX`) platforms

#### Migration System
- **New migration framework**: Automated migration system for handling configuration and data migrations between versions
- **Bundled migration support**: Special handling for Bun runtime with embedded migration files
- **Version tracking**: Migration files are now included with version metadata (v0.2.101)

#### IDE Integration Improvements
- **IDE lock file management**: New functions for managing IDE integration lock files in `~/.claude/ide/`
- **Connection handling**: Enhanced TCP connection support for IDE integrations using Node.js `net` module

#### User Interface Enhancements
- **Relative time formatting**: New utility for displaying human-readable relative timestamps (e.g., "2 hours ago", "in 3 days")
- **Enhanced permission context**: Improved tool permission handling system

### Technical Improvements

#### Performance and Stability
- **React 18+ compatibility**: Removed legacy React components and updated to modern React 18+ APIs
- **Reduced bundle size**: Removed approximately 496 deprecated functions while adding only 119 new ones
- **Memory optimization**: Cleaned up unused signal handling and event management code

#### Code Quality
- **Structural similarity**: Maintained 92.7% structural similarity with previous version for stability
- **Modernized codebase**: Removed legacy polyfills and outdated compatibility layers

### Bug Fixes
- Fixed potential issues with Fast Refresh module reloading
- Improved cache invalidation for selectors returning inconsistent values
- Enhanced error handling for migration processes

### Developer Experience
- **Better error messages**: More descriptive error messages for migration failures
- **Issue reporting**: Direct links to GitHub issues (`https://github.com/anthropics/claude-code/issues`)
- **Documentation**: Updated references to documentation at `https://docs.anthropic.com/s/claude-code`

### Breaking Changes
- Removed legacy signal handling utilities (`$i0`, `Ui0`)
- Removed deprecated React lifecycle methods and compatibility layers
- Some internal APIs have been restructured (maintaining 92.7% compatibility)

### Usage Examples

#### Setting a preferred model:
```bash
# Via environment variable
export ANTHROPIC_MODEL="claude-3-7-sonnet"
claude "Help me write a Python script"

# The CLI will use Claude 3.7 Sonnet for this request
```

#### Using platform-specific routing:
```bash
# For AWS Bedrock
export CLAUDE_CODE_USE_BEDROCK=true
claude "Analyze this codebase"

# For Google Cloud Vertex
export CLAUDE_CODE_USE_VERTEX=true
claude "Review this pull request"
```

The model selection interface provides clear pricing information and performance characteristics to help users choose the most appropriate model for their needs.
