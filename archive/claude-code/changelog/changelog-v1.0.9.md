# Changelog for version 1.0.9

# Claude Code v1.0.9 Changelog

## New Features

### Internal Metrics Export System
- Added new internal metrics exporter (`Nh1` class) that sends telemetry data to Anthropic's metrics endpoint
- Metrics are exported every 60 seconds to `https://api.anthropic.com/api/claude_code/otel/metrics`
- Includes service metadata, metric descriptions, and data points with timestamps
- Graceful shutdown support with configurable timeout

## Improvements

### Enhanced Telemetry System
- Restructured OpenTelemetry initialization to support both external and internal metrics collection
- Added conditional logic for enabling internal metrics export (controlled by `uB6()` function, currently disabled)
- Improved error handling and logging for telemetry operations

### Import Optimizations
- Replaced generic stream imports with more specific imports:
  - Changed from `import stream` to `import { PassThrough }` for better tree-shaking
  - Updated process import to use named import `{ cwd }` instead of default import
- Added new utility variables for internal operations

## Technical Changes

### Code Organization
- Refactored telemetry initialization function (renamed from `Mk0` to `Rk0`)
- Improved separation of concerns between external and internal metrics readers
- Better error messages for OpenTelemetry timeout scenarios

### Version Updates
- Bumped version from 1.0.8 to 1.0.9
- Updated all version references throughout the codebase

## Bug Fixes

- Fixed potential race conditions in metrics export by tracking pending exports
- Improved attribute conversion to handle undefined and null values properly
- Enhanced timestamp handling for metric data points

## Notes

The internal metrics feature appears to be prepared for future use but is currently disabled (the `uB6()` function returns `false`). When enabled, this feature will provide Anthropic with anonymous usage metrics to help improve Claude Code.
