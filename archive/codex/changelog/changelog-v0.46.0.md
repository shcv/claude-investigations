# Changelog for version 0.46.0

## MCP (Model Context Protocol) Enhancements

### Streamable HTTP Authentication Improvements

**Breaking Change**: The MCP server configuration format for streamable HTTP servers has changed to improve security.

- **Replaced `bearer_token` with `bearer_token_env_var`**: Instead of storing bearer tokens directly in config files (which was insecure), you now specify an environment variable name that contains the token.

  **Old format** (no longer supported):
  ```toml
  [mcp_servers.github]
  url = "https://example.com/mcp"
  bearer_token = "secret-token"  # Rejected with error
  ```

  **New format**:
  ```toml
  [mcp_servers.github]
  url = "https://example.com/mcp"
  bearer_token_env_var = "GITHUB_TOKEN"  # Reads token from environment
  ```

  **Usage**: Set the environment variable before running Codex:
  ```bash
  export GITHUB_TOKEN="your-token-here"
  codex
  ```

  If the environment variable is not set, empty, or contains invalid Unicode, Codex will report a clear error message.

### MCP Server Enable/Disable Control

- **New `enabled` field**: You can now disable MCP servers without removing them from your configuration.

  ```toml
  [mcp_servers.docs]
  command = "docs-server"
  enabled = false  # Server won't be initialized
  ```

  When omitted, `enabled` defaults to `true` for backward compatibility. Disabled servers are skipped during initialization.

### MCP Authentication Status Display

- **`codex mcp list` now shows authentication status**: The output includes two new columns:
  - **Status**: Shows whether the server is `enabled` or `disabled`
  - **Auth**: Shows the authentication status for the server:
    - `unsupported` - Server doesn't use authentication (e.g., stdio servers)
    - `authenticated` - OAuth credentials are stored
    - `unauthenticated` - OAuth required but no credentials found
    - `misconfigured` - Configuration error

  **Example output**:
  ```
  Name    Command       Args         Env          Status    Auth
  docs    docs-server   --port 4000  TOKEN=secret enabled   Unsupported
  
  Name     Url                        Bearer Token Env Var  Status   Auth
  github   https://example.com/mcp    GITHUB_TOKEN          enabled  authenticated
  ```

- **`codex mcp list --json` includes auth status**: The JSON output now includes `auth_status` and `enabled` fields for each server.

- **`codex mcp get` shows enabled status**: The human-readable output now displays `enabled: true/false`.

### OAuth Credentials Storage Mode

- **New configuration option**: `mcp_oauth_credentials_store` controls where OAuth credentials are stored.

  ```toml
  # In config.toml
  mcp_oauth_credentials_store = "keyring"  # or "file" or "auto" (default)
  ```

  **Options**:
  - `keyring` (recommended): Uses OS-specific keyring (Keychain on macOS, Credential Manager on Windows, Secret Service on Linux). Most secure option.
  - `file`: Stores credentials in `$CODEX_HOME/.credentials.json`. Readable by any process running as your user.
  - `auto` (default): Tries keyring first, falls back to file if keyring is unavailable.

  This setting can be managed via MDM on supported platforms.

### MCP Server Addition Improvements

- **`codex mcp add` now supports streamable HTTP servers**:

  ```bash
  # Add HTTP server without authentication
  codex mcp add github --url https://example.com/mcp

  # Add HTTP server with bearer token from environment variable
  codex mcp add issues --url https://example.com/issues \
    --bearer-token-env-var GITHUB_TOKEN
  ```

- **Mutual exclusivity enforced**: You cannot specify both `--url` and a command. Use `--url` for HTTP servers or provide a command for stdio servers.

- **Environment variables restricted to stdio**: The `--env` flag is now only valid with stdio servers (command-based), not with `--url`.

## Interactive Mode Improvements

### Device Code Authentication

- **`codex login --device-auth` now generally available**: The device code OAuth flow is no longer experimental.

  **Usage**:
  ```bash
  codex login --device-auth
  ```

  This flow is useful for:
  - Remote development environments where you can't open a browser on the same machine
  - Headless systems
  - SSH sessions

  The previous flag `--experimental_use-device-code` is removed.

### Exit Messages

- **Exit messages displayed on quit**: When you exit the interactive TUI, Codex now displays any important messages (such as warnings or notifications) before returning to the shell.

## Tool Execution Changes

### Parallel Tool Execution Redesign

**Internal change**: The runtime now uses a more robust concurrency model for handling parallel and serial tool calls:

- **Parallel-safe tools** can run concurrently with other parallel-safe tools
- **Non-parallel tools** block until all other tools complete before starting
- All pending tool calls are automatically cancelled if the stream encounters an error
- Uses `AbortOnDropHandle` to ensure proper cleanup when tool execution is interrupted

This change improves reliability when the model requests multiple tool calls in a single turn, especially when mixing parallel-safe tools (like `read_file`) with serial tools (like shell commands).

### New Experimental Tools

Two new tools have been added for GPT-5 models (when enabled via model configuration):

#### `grep_files` Tool

**Purpose**: Search for files containing specific patterns, sorted by modification time.

**Parameters**:
- `pattern` (required): Regular expression to search for
- `include` (optional): Glob pattern to filter files (e.g., `"*.rs"`, `"*.{ts,tsx}"`)
- `path` (optional): Directory to search (defaults to working directory)
- `limit` (optional): Maximum results to return (default: 100, max: 2000)

**Implementation details**:
- Uses ripgrep (`rg`) under the hood
- 30-second timeout per search
- Returns file paths sorted by modification time
- Returns `success: false` when no matches found

**Requires**: ripgrep must be installed and available in PATH.

#### `list_dir` Tool

**Purpose**: List directory contents recursively with depth control and pagination.

**Parameters**:
- `dir_path` (required): Absolute path to directory
- `offset` (optional): 1-indexed entry number to start from (default: 1)
- `limit` (optional): Maximum entries to return (default: 25)
- `depth` (optional): Maximum directory depth to traverse (default: 2)

**Output format**:
- Directories marked with `/` suffix
- Symlinks marked with `@` suffix
- Unknown file types marked with `?` suffix
- Nested entries indented with 2 spaces per level
- Sorted alphabetically within each directory
- Shows "More than N entries found" when results are truncated

**Example output**:
```
Absolute path: /home/user/project
src/
  main.rs
  lib.rs
  utils/
    helper.rs
tests/
  integration.rs
README.md
```

## Transcript Rendering Improvements

### Tab Character Handling

- **Tabs expanded to spaces in transcripts**: Tab characters in tool outputs (like from `nl` command) are now replaced with 4 spaces when rendered in the TUI or CLI transcript views.

  This prevents visual artifacts that could occur when tabs interacted with line number prefixes in transcript mode. The change is purely cosmetic and doesn't affect the actual tool output sent to the model.

## Compaction Improvements

### Context Window Error Recovery

- **Auto-retry with history trimming**: When compaction fails due to context window limits, Codex now automatically retries after removing the oldest conversation item.

  **How it works**:
  1. Compaction attempts to summarize conversation history
  2. If the model returns a `context_length_exceeded` error
  3. Codex removes the oldest history item and retries
  4. Repeats until compaction succeeds or no more items can be removed
  5. Displays notification: "Trimmed N older conversation item(s) before compacting so the prompt fits the model context window"

  This allows compaction to succeed even when the accumulated history is very large, by progressively reducing the context until it fits.

## Observability and Telemetry

### SSE Event Timing

**Internal change**: OpenTelemetry logging now accurately tracks the duration of SSE (Server-Sent Events) responses. Previously, the timing measurement wrapped the logging call itself; now it correctly measures the actual timeout/response time.

## Configuration and Dependency Updates

- **Version bump**: 0.45.0 → 0.46.0
- **tree-sitter**: 0.25.9 → 0.25.10
- **tree-sitter-highlight**: Added as new dependency (0.25.10)
- **rmcp**: 0.8.0 → 0.8.1
- **rmcp-macros**: 0.8.0 → 0.8.1
- **unicode-width**: 0.1.14 → 0.2.1 (workspace-wide update)
- **tokio-util**: Added `rt` feature flag
- **tokio-stream**: Added `futures-util` dependency
- **Cargo.toml cleanup**: cloud-tasks dependencies now use workspace versions consistently

## Testing Enhancements

- **New test infrastructure**: Added `ResponseMock` helper for cleaner API request inspection in tests
- **MCP server tests**: Expanded test coverage for streamable HTTP servers with authentication
- **Compaction tests**: Added test for context window error recovery during manual compaction
- **Tool tests**: New test suites for `grep_files` and `list_dir` tools

---

## Migration Guide

### If you use MCP streamable HTTP servers with bearer tokens:

1. **Update your config**: Replace `bearer_token = "value"` with `bearer_token_env_var = "ENV_VAR_NAME"`
2. **Set environment variable**: Export the token value in your shell or add to your shell profile
3. **Restart Codex**: The old `bearer_token` field will cause an error on startup

### If you use managed configuration (MDM):

- You can now control OAuth credential storage via the `mcp_oauth_credentials_store` setting in managed config files

### If you maintain scripts that parse `codex mcp list --json`:

- The JSON output now includes `enabled` and `auth_status` fields for each server
- Update your scripts to handle these new fields if needed
