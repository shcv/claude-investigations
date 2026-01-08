# Changelog for version 0.2.109

# Claude Code v0.2.109 Changelog

### Custom Model Selection
- Added support for specifying custom AI models via the `modelInput` parameter
- Users can now override the default model selection when running Claude Code
- The model specification is passed through the new `modelInput` field in the main execution function

### Configuration Management Enhancement
- Introduced `kq` function for dynamic configuration retrieval
- Respects environment variables: `CLAUDE_CODE_USE_BEDROCK`, `CLAUDE_CODE_USE_VERTEX`, and `DISABLE_TELEMETRY`
- Provides fallback to default configuration when telemetry is disabled or custom deployments are used

### Bash Command Timeout Configuration
- New `Sf` function allows customizing bash command timeouts via `BASH_DEFAULT_TIMEOUT_MS` environment variable
- Users can now set their preferred timeout for bash operations:
  ```bash
  export BASH_DEFAULT_TIMEOUT_MS=300000  # 5 minutes
  claude-code "run my long-running script"
  ```

### Exit Feedback System
- Implemented user feedback collection on exit with `Z10` and `G10` functions
- Shows feedback prompt for sessions longer than 10 characters
- Controlled by the "tengu-exit-feedback" feature flag

### Version Management
- Version now properly sourced from package.json (`y_2` variable)
- Centralized version retrieval through `_D5` function
- Version updated to 0.2.109

### System Prompt Enhancements
- System prompts now receive the model information as a parameter
- More accurate model context in the environment information
- Improved model awareness for better response generation

### IDE Integration
- Enhanced IDE integration function (`jD5`) now returns a promise
- Better error handling and cleanup for VS Code extension installation

### Code Organization
- Removed duplicate imports and unused variables
- Consolidated stream imports into a single location
- Better variable naming and function organization

### Performance
- Optimized file content truncation with dynamic limit calculation
- Improved memory usage in large file handling

## Bug Fixes

- Fixed duplicate import statements for stream and process modules
- Resolved undefined variable references in configuration handling
- Corrected function parameter passing in system prompt generation
