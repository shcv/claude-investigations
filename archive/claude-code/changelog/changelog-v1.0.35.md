# Changelog for version 1.0.35


### Bug Fixes & Improvements

- **Fixed Function Permission Handling**: Removed the `oU5` function that was handling tool permission messages for allowed/denied tools and workspace access
- **Updated Version References**: Updated internal version string from 1.0.34 to 1.0.35 across all configuration files


### Dependency Updates

- **AWS SDK Updates**: 
  - Updated AWS SDK dependencies to version 3.797.0
  - Updated middleware packages for better authentication and request handling
  - Enhanced security token and authorization header handling

- **MCP Protocol Enhancements**:
  - Improved MCP (Model Communication Protocol) authentication flow
  - Added better protocol version header handling (`mcp-protocol-version`)
  - Enhanced SSE (Server-Sent Events) client transport with authentication support


### Tool System Improvements

- **TodoWrite Tool Enhancements**:
  - Improved guidance for when to use the todo list tool
  - Added clearer examples for complex multi-step tasks vs simple tasks
  - Enhanced the tool's proactive usage recommendations
  - Better empty todo list reminder handling

- **ExitPlanMode Tool**:
  - Added clearer distinction between planning implementation tasks vs research tasks
  - Improved examples for when to use/not use the exit plan mode tool

- **Edit Tools**:
  - Enhanced error messages for duplicate old_string/new_string values
  - Improved line number prefix handling in edit operations
  - Better guidance for preserving exact indentation


### Internal Architecture Changes

- **URI Handling**: Added new URI parsing and manipulation library (`bo0` module) with comprehensive URL/URI support
- **JSON Schema Validation**: Enhanced with better const keyword support and improved error messages
- **Semver Support**: Added semantic versioning utilities for better version management
- **Error Handling**: Improved error messages for various edge cases including invalid arguments and authentication failures


### User Experience Improvements

- **Better Error Feedback**: More descriptive error messages for tool rejections and failures
- **Enhanced Tool Documentation**: Clearer descriptions of when to use specific tools
- **Improved Authentication Flow**: Better handling of 401 errors and authentication retries


### Technical Updates

- **Code Organization**: Restructured several internal modules for better maintainability
- **Type Safety**: Enhanced TypeScript type definitions for better development experience
- **Performance**: Various optimizations in request handling and protocol communication

This version focuses on stability improvements, better error handling, and enhanced guidance for tool usage, making the CLI more reliable and user-friendly.
