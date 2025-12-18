# Changelog for version 0.45.0

# Changelog - Version 0.45.0

## 🔐 Security & Authentication

### OAuth Support for MCP Servers (Experimental)
Added OAuth authentication for MCP servers with secure credential storage. To use OAuth:

```bash
# Authenticate with an MCP server
codex mcp login my-server

# Remove stored credentials
codex mcp logout my-server
```

OAuth credentials are stored securely using your operating system's credential manager:
- **macOS**: macOS Keychain
- **Windows**: Windows Credential Manager  
- **Linux**: DBus Secret Service and kernel keyutils
- Falls back to `~/.codex/.credentials.json` if keyring is unavailable

**Requirements**: Set `experimental_use_rmcp_client = true` in your `config.toml`. Only works with streamable HTTP MCP servers that support OAuth.

### 🚨 BREAKING: Secure API Key Login
The `--api-key` flag has been removed from `codex login` for security reasons. API keys must now be piped from stdin to prevent them from appearing in shell history or process listings.

```bash
# New secure method
printenv OPENAI_API_KEY | codex login --with-api-key

# Or from a file
cat api-key.txt | codex login --with-api-key

# Old method no longer works
# codex login --api-key sk-...  ❌
```

If you try using the old flag, you'll see: "The --api-key flag is no longer supported. Pipe the key instead, e.g. `printenv OPENAI_API_KEY | codex login --with-api-key`."

## 🛠️ Command Changes

### Sandbox Commands Renamed
The `codex debug` command has been renamed to `codex sandbox` for clarity, with platform-specific subcommands:

```bash
# New syntax
codex sandbox macos <command>   # Run command in macOS sandbox
codex sandbox linux <command>   # Run command in Linux sandbox

# Old syntax still works via aliases
codex debug seatbelt <command>
codex debug landlock <command>
```

The `debug` command remains as an alias for backward compatibility.

## ⚡ Performance & Execution

### Parallel Tool Calls
Models can now execute multiple independent tool calls simultaneously when supported by the prompt configuration. Previously, all tool calls were forced to execute sequentially. This enables faster execution when the model requests multiple unrelated operations.

Example: If the model wants to read three different files, all three read operations can now happen in parallel instead of waiting for each to complete.

## 🐛 Bug Fixes & Improvements

### Better Context Window Error Detection
Context window exceeded errors are now properly detected and reported. When the API returns a `context_length_exceeded` error, the system recognizes it as a `ContextWindowExceeded` error type, allowing for more graceful handling and clearer error messages.

### Improved System Prompt Guidance
Updated guidance for the `apply_patch` tool:

- The model now receives better instructions about when to use `apply_patch` vs other editing methods: "Try to use apply_patch for single file edits, but it is fine to explore other options to make the edit if it does not work well. Do not use apply_patch for changes that are auto-generated (i.e. generating package.json or running a lint or format command like gofmt) or when scripting is more efficient (such as search and replacing a string across a codebase)."

- Added explicit warning against destructive git commands: "**NEVER** use destructive commands like `git reset --hard` or `git checkout --` unless specifically requested or approved by the user."

These changes reduce the likelihood of accidental data loss and improve the model's decision-making about file editing approaches.

### Better Log Truncation
Improved string truncation in telemetry and logging to respect UTF-8 character boundaries, eliminating broken characters in log previews.

## 🏗️ Internal Improvements

### Tool System Refactoring
Major internal refactoring of the tool execution system introduces new abstractions (`ToolHandler` trait, `ToolRegistry`, `ToolRouter`) that provide better separation between tool specification and execution. This lays the foundation for future extensibility, including potential support for custom tools and plugins.

### Executor Refactoring
Introduced `PreparedExec` struct for staged execution and new `ExecError` enum for more consistent error handling. The executor logic has been better organized, providing clearer separation of sandbox decision logic and improved approval workflows.

### Token Usage Tracking
Enhanced token usage tracking with new methods to mark when the context window is full (`set_token_usage_full()`), enabling more accurate reporting of context limits.

### Async MCP Commands
All `codex mcp` subcommands now use async execution internally, enabling better I/O performance for configuration loading operations.
