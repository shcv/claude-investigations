# Changelog for version 1.0.7

Now, based on the diff analysis, I can generate a comprehensive changelog for version 1.0.7:

### New Features

#### Plan Mode
- **New `/exit_plan_mode` command**: Exit planning mode and start coding immediately. When in plan mode, use this command to signal you're ready to begin implementation.
  ```bash
  # In an interactive session, after planning is complete:
  /exit_plan_mode
  ```
- Added visual indicator with a new `planMode` color theme (teal) to distinguish when Claude is in planning mode

#### Model Selection Enhancements
- **Improved model recommendations**: Claude now provides intelligent model suggestions based on your subscription tier
  - For Claude Pro users with >1x usage tier, Opus 4.0 is recommended when available
  - Automatically detects subscription level and suggests appropriate models
- **Enhanced `/model` command**: Now shows subscription-aware recommendations
  ```bash
  # Shows available models with smart recommendations
  /model
  ```

#### Logging and Observability
- **OpenTelemetry Logs Support**: Full integration with OpenTelemetry logging API
  - Set `OTEL_LOGS_EXPORTER` environment variable to enable log export
  - Support for multiple exporters: `otlp`, `console`
  - Configure with `OTEL_LOG_USER_PROMPTS=true` to include user prompts in logs (redacted by default)
  ```bash
  # Enable OTLP log export
  export OTEL_LOGS_EXPORTER=otlp
  
  # Include user prompts in logs (use with caution)
  export OTEL_LOG_USER_PROMPTS=true
  ```

#### Configuration Migration
- **Settings.json migration**: The `claude config` command now migrates settings to `settings.json`
  - `allowedTools` and `ignorePatterns` are automatically migrated
  - Warning shown when using deprecated config commands
  ```bash
  # These commands now show migration warnings:
  claude config add allowedTools bash
  claude config add ignorePatterns "*.log"
  ```

### Tool Improvements

#### Edit Tool Enhancement
- **Improved string normalization**: The Edit tool now automatically handles common formatting discrepancies
  - Fixes issues with XML-like tags (e.g., `<fnr>` → `<function_results>`)
  - Handles spacing variations in special markers
  - More robust matching for assistant/human message markers

#### Bash Tool Enhancement
- **Smart exit code handling**: Different commands now have appropriate error handling
  - `grep` returns useful results even with non-zero exit codes (no matches found)
  - `find` properly handles "file not found" scenarios
  - Generic commands provide clearer error messages

### Performance Improvements

- **Proxy support optimization**: Better handling of HTTP proxy configurations
  - Unified proxy handling across axios and undici HTTP clients
  - Improved `HTTPS_PROXY` environment variable support

### API Enhancements

- **Subscription-aware cost calculation**: Model costs now reflect Development Partner Program discounts
- **Enhanced retry logic**: Improved handling of context limit errors with automatic max_tokens adjustment
- **Better error messages**: More informative error responses for rate limits and quota issues

### Bug Fixes

- Fixed duplicate imports and removed unused dependencies
- Cleaned up legacy code for improved performance
- Fixed multiline editing issues in string replacement operations
- Improved file path resolution in various tools

### Developer Experience

- **New telemetry events**: Added tracking for plan mode usage and subscription recommendations
- **Better TypeScript support**: Improved type definitions for new features
- **Enhanced debugging**: More detailed logging for troubleshooting tool operations

### Deprecated Features

- `claude config add` commands for `allowedTools` and `ignorePatterns` are deprecated in favor of direct `settings.json` editing
