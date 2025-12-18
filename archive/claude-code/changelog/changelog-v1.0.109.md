# Changelog for version 1.0.109

## 🎯 Highlights
Version 1.0.109 introduces asynchronous hook support, enabling long-running hooks to execute in the background without blocking conversation flow, along with improved API error tracking for better debugging.

## 🚀 New Features

### Asynchronous Hook Execution
**What:** Hooks can now run asynchronously in the background, allowing long-running operations without blocking the main conversation
**How to use:**
```json
{
  "async": true,
  "asyncTimeout": 30000
}
```
**Details:**
- Background process management for async hooks
- Configurable timeout settings (default 15 seconds)
- Automatic response collection and delivery
- Process cleanup when hooks complete or timeout
- **Evidence**: `D$A() at line 362558`, `s10() at line 362783`, `U$A() at line 362581`

### Enhanced API Error Tracking
**What:** Improved error reporting with gateway and infrastructure tracking for API failures
**How to use:** Automatic - enhanced error information appears in debug logs and telemetry
**Details:**
- Extracts gateway information from API response headers
- Better visibility into which infrastructure components handled requests
- Enhanced debugging capabilities for API failures
- **Evidence**: `JE0() header extraction function`, `VE0() at line 393771` (renamed from `XE0`)

## 🔧 Improvements

### Hook Registry Management
Enhanced hook execution with background process tracking, timeout management, and response collection system for better reliability and performance.

### Rewind Feature UI
Improved checkpoint and rewind interface with better display of code changes, timestamps, and checkpoint status for enhanced user feedback.

### Code Organization
Function renaming and reorganization (`XE0` → `VE0`) as part of ongoing code maintenance and improved structure.

## 🐛 Bug Fixes

### Stream Import Cleanup
Removed redundant stream import (`o7Q`) that was no longer needed, reducing bundle size and potential conflicts.

### Dead Code Removal
Removed unused functions (`eP5()`, `e$0()`) that served no purpose, improving code cleanliness and maintainability.
