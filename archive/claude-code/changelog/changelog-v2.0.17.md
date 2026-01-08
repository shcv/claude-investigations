# Changelog for version 2.0.17

## Highlights

Version 2.0.17 introduces MCPB file format support for distributing packaged MCP servers, adds SOCKS5 proxy support for enhanced network sandboxing, includes support for the new Haiku 4.5 model, and enhances Windows path security validation.

### MCPB File Format Support

**What:** Full support for loading MCP servers from MCPB (`.mcpb` or `.dxt`) archive files, which are secure ZIP-based packages containing manifest, configuration, and server code.

**How to use:**
```bash
# Load an MCPB file from local path
claude --mcp-config path/to/server.mcpb

# Load an MCPB from URL (downloads and caches automatically)
claude --mcp-config https://example.com/servers/tool.mcpb
```

**Details:**
- Secure ZIP extraction with protection against zip bombs, path traversal, and excessive file sizes
- Automatic caching system (`.mcpb-cache` directory) with hash-based invalidation
- Support for downloading MCPB files from HTTP/HTTPS URLs with progress tracking
- Validates manifest.json against schema and generates MCP server configuration
- Security limits: max 512MB per file, max 1GB total uncompressed size, max 100k files, max 50:1 compression ratio
- Three structured error types for debugging: `mcpb-download-failed`, `mcpb-invalid-manifest`, `mcpb-extract-failed`
- **Evidence**: `PO0() at line 279621`, `_8B() at line 279846`, `x8B() at line 279926`, `mg1() at line 279587` in v2.0.17 (completely absent from v2.0.15)

### SOCKS5 Proxy Support in Network Sandbox

**What:** Complete SOCKS5 proxy server added alongside existing HTTP proxy for enhanced network sandboxing on Linux and macOS. Provides dual-proxy infrastructure on ports 1080 (SOCKS) and 3128 (HTTP).

**How to use:**
Automatic when network sandbox is enabled. The SOCKS proxy is configured via environment variables:
```bash
# Automatically set when sandbox is active
ALL_PROXY=socks5h://localhost:1080
```

**Details:**
- SOCKS5 server implementation with authentication and connection filtering
- Unix socket bridges for both HTTP and SOCKS proxies on Linux (`claude-socks-*.sock`, `claude-http-*.sock`)
- Environment variables automatically configured: `ALL_PROXY`, `all_proxy`, `GIT_SSH_COMMAND`, `FTP_PROXY`, `GRPC_PROXY`, etc.
- Function `QJ6()` wraps commands with dual proxy setup using socat
- Parallel initialization of both proxy servers in `HJ6()`
- **Evidence**: `QJ6() at line 207609`, `Bp2() at line 207346`, `KJ6()` and `HJ6() at line 207225` in v2.0.17 (SOCKS functionality completely absent from v2.0.15; only HTTP proxy existed)

### Haiku 4.5 Model Support

**What:** Support for the new Claude Haiku 4.5 model (`claude-haiku-4-5-20251001`), available across all platforms (direct API, Bedrock, Vertex).

**How to use:**
```bash
# Use Haiku 4.5 as your model
claude --model claude-haiku-4-5-20251001

# Or use model aliases
claude --model haiku45
```

**Details:**
- Model identifier: `claude-haiku-4-5-20251001`
- Display name: "Haiku 4.5"
- Platform mappings configured for firstParty, Bedrock (`global.anthropic.claude-haiku-4-5-20251001-v1:0`), and Vertex (`claude-haiku-4-5@20251001`)
- Vertex region environment variable: `VERTEX_REGION_CLAUDE_HAIKU_4_5`
- Haiku 4.5 used in plan mode when model preference is set to "haiku"
- **Evidence**: Model detection at `IOA() at line 83108`, platform mappings at lines 83142-83144, model selection logic at `x01() at line 144036` (model identifier "haiku-4-5" completely absent from v2.0.15)

### Windows Path Security Validation

**What:** Enhanced security check that detects suspicious Windows-specific path patterns and requires manual approval before allowing file access.

**How to use:**
Automatic protection when Claude attempts to access files with suspicious paths. You'll receive a prompt like:
> "Claude requested permissions to read/write to {path}, which contains a suspicious Windows path pattern that requires manual approval."

**Details:**
- Detects alternate data streams (`:` in paths beyond drive letter)
- Detects short/8.3 format names (`~1`, `~2` patterns used to bypass filters)
- Detects long path prefixes (`\\?\`, `\\.\`) that can bypass security checks
- Detects trailing dots or spaces that Windows ignores
- Detects reserved device names (CON, PRN, AUX, NUL, COM1-9, LPT1-9)
- Applies to both read and write permission checks
- **Evidence**: `ZMQ() at line 454449`, integrated into `b41() at line 454621` and `op() at line 454708` (function and security checks completely absent from v2.0.15)

### Enhanced Changelog Fetch Respects Traffic Control

The changelog fetching functionality now respects the `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` environment variable. While the variable existed in v2.0.15, v2.0.17 adds this check to the changelog download function `Gb0()`, preventing unnecessary network requests in restricted environments.

**Evidence**: `Gb0() at line 362735` adds the check (new location for this guard in v2.0.17)
