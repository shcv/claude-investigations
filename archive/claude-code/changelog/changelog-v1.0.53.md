# Changelog for version 1.0.53

Based on my analysis of the diff for version 1.0.53, here is the detailed changelog:


### New Features

#### AWS Authentication Enhancements
- **AWS Auth Refresh Command**: Added `awsAuthRefresh` configuration option that allows users to specify a command to run when AWS credentials need refreshing. This command is automatically executed when AWS authentication fails.
  ```bash
  # In ~/.claude.json or settings:
  {
    "awsAuthRefresh": "aws sso login --profile myprofile"
  }
  ```

- **AWS Credential Export**: Added `awsCredentialExport` configuration option for dynamically providing AWS credentials from external sources.
  ```bash
  # In ~/.claude.json or settings:
  {
    "awsCredentialExport": "aws sts assume-role --role-arn arn:aws:iam::123456789012:role/MyRole --role-session-name claude-session"
  }
  ```
  The command must return AWS STS-compatible JSON output with `Credentials.AccessKeyId`, `Credentials.SecretAccessKey`, and `Credentials.SessionToken`.

#### OpenTelemetry Support
- **Custom OTEL Headers**: Added `otelHeadersHelper` configuration option to dynamically set OpenTelemetry headers for tracing and monitoring.
  ```bash
  # In ~/.claude.json or settings:
  {
    "otelHeadersHelper": "echo '{\"x-trace-id\": \"'$(uuidgen)'\", \"x-org-id\": \"myorg\"}'"
  }
  ```

#### MCP (Model Context Protocol) Enhancements
- **Server Instructions**: MCP servers can now provide custom instructions that are automatically included in the system prompt, helping Claude understand how to use specific tools and resources.
- **Batch Connection Size**: Added `MCP_SERVER_CONNECTION_BATCH_SIZE` environment variable to control concurrent MCP server connections (default: 3).
- **Improved MCP Command Parsing**: MCP commands are now properly identified with "(MCP)" suffix in command names.

#### Enhanced Conversation Management
- **Restore Options**: When jumping to a previous message (Cmd+L), users can now choose what to restore:
  - **Both**: Restore both conversation history and workspace state
  - **Conversation only**: Keep current workspace, restore chat history
  - **Workspace only**: Keep current chat, restore workspace state

#### Terminal Improvements
- **Dynamic Terminal Resizing**: Improved handling of terminal window resizing with proper event listeners and state management.
- **Better TTY Detection**: Enhanced checks for interactive terminal environments.


### User Experience Improvements

#### Command Processing
- **Enhanced Slash Command Parsing**: Improved parsing of slash commands with better argument extraction and MCP command recognition.
  ```bash
  # Regular command
  /search keyword
  
  # MCP command (automatically detected)
  /tool-name (MCP) arguments
  ```

- **User Prompt Submit Hooks**: Added support for hooks that can intercept and modify user prompts before they're sent to Claude. Hooks can:
  - Block prompts with error messages
  - Add additional context to prompts
  - Run preprocessing steps

#### Error Handling
- **AWS Credential Errors**: Better error messages and automatic retry mechanisms for AWS authentication failures.
- **Hook Error Display**: Clear error messages when prompt submission is blocked by hooks.


### Configuration

#### New Settings
- `awsAuthRefresh`: Command to run when AWS credentials need refreshing
- `awsCredentialExport`: Command to export AWS credentials dynamically
- `otelHeadersHelper`: Command to generate OpenTelemetry headers
- `MCP_SERVER_CONNECTION_BATCH_SIZE`: Environment variable for MCP connection concurrency


### API and Integration Updates
- Added support for the `DecodeAuthorizationMessage` AWS STS operation
- Enhanced AWS SDK integration with proper credential provider error handling
- Improved TypeScript helper imports and exports


### Performance and Stability
- **Connection Management**: Better handling of concurrent MCP server connections
- **Memory Management**: Improved caching mechanisms for AWS credentials and system state
- **Event Handling**: More robust terminal resize event management


### Developer Features
- **Client Type Configuration**: Added ability to set client type for telemetry
- **Enhanced Logging**: Better structured logging for AWS operations and MCP interactions
- **Improved Type Safety**: Additional TypeScript utilities and error classes

This update focuses on improving integration capabilities, particularly with AWS services and MCP servers, while enhancing the overall user experience with better error handling and configuration options.
