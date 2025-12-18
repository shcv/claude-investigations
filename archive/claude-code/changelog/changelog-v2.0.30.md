# Changelog for version 2.0.30

## 🎯 Highlights

Version 2.0.30 introduces Language Server Protocol (LSP) support, enabling Claude to access code intelligence features like go-to-definition, find-references, and hover documentation. It also adds enhanced sandbox security controls and refactors the internal tool execution architecture for better concurrent processing.

## 🚀 New Features

### LSP (Language Server Protocol) Tool

**What:** A new tool that integrates Language Server Protocol servers to provide code intelligence features directly to Claude.

**How to use:**
```bash
# Claude can now use LSP operations when analyzing code
# The tool works automatically when LSP servers are configured
```

**Supported operations:**
- `goToDefinition`: Find where a symbol is defined
- `findReferences`: Find all references to a symbol  
- `hover`: Get hover information (documentation, type info) for a symbol
- `documentSymbol`: Get all symbols (functions, classes, variables) in a document
- `workspaceSymbol`: Search for symbols across the entire workspace

**Configuration:**
LSP servers can be configured in two ways:

1. **Plugin-based configuration:** Plugins can define LSP servers via `.lsp.json` files or in their manifest's `lspServers` property
2. **Project configuration:** LSP server settings include command, args, supported languages, transport type (stdio/socket), initialization options, and workspace settings

**Requirements:**
- All operations require `filePath`, `line` (0-indexed), and `character` (0-indexed) parameters
- LSP servers must be configured for the file type; operations will return an error if no server is available

**Details:**
- **Evidence**: LSP tool definition at `at1()` at line 455338, LSP server manager initialization at line 454707
- Plugin LSP configuration loading at `Ig2()` at line 454527
- Comprehensive error handling for LSP failures including: `lsp-config-invalid`, `lsp-server-start-failed`, `lsp-server-crashed`, `lsp-request-timeout`, `lsp-request-failed`
- LSP URI decoding support at line 205830 (`uO0()` function)

### Magic Docs Auto-Update System

**What:** An automated documentation maintenance system that updates project documentation files based on conversations with Claude.

**How it works:**
- When you work with Claude and learn new information about your codebase, the system can automatically update designated "Magic Doc" files
- Uses a specialized `magic-docs` agent type that reads existing documentation and incorporates new learnings
- Focuses on high-level architecture, patterns, and entry points rather than exhaustive code details

**Philosophy:**
- Keeps documentation CURRENT (not a changelog or history)
- Updates information in-place to reflect the current state
- Removes or replaces outdated information
- Emphasizes terseness: "High signal only. No filler words."

**Evidence**: `magic-docs` agent type at line 476091, documentation update prompt generator `Aa5()` at line 475984

### Enhanced Sandbox Security Policy

**What:** A new configuration option `allowUnsandboxedCommands` that provides policy-level control over the `dangerouslyDisableSandbox` parameter.

**How to use:**
```javascript
// In your settings
{
  "sandbox": {
    "allowUnsandboxedCommands": false  // Enforce sandbox-only mode
  }
}
```

**Details:**
- **Default:** `true` (maintains backward compatibility)
- **When set to `false`:** All commands run in sandbox mode regardless of the `dangerouslyDisableSandbox` parameter
- **Enforcement:** The security check at `Q9A()` at line 249229 validates both the parameter AND the policy setting
- **User communication:** Claude receives different system prompt instructions based on this setting (lines 208919-208942)
- **Evidence**: Configuration schema at line 473000, getter function `XP8()` at line 208521

## ⚡ Improvements

### Refactored Tool Execution Architecture

**What changed:** Internal tool execution system migrated from function-based approach to a class-based queue system with better concurrent execution support.

**Technical details:**
- New `Qr1` class manages tool execution queue with status tracking ("queued" → "executing" → "completed" → "yielded")
- Intelligent concurrency: Tools marked as concurrency-safe can execute in parallel, while non-concurrent-safe tools block subsequent processing
- Feature-flag controlled: Uses `tengu_streaming_tool_execution` flag to gradually roll out new architecture
- Backward compatible: Falls back to renamed legacy functions (`Ev5()` at line 429788) when feature flag is disabled

**User impact:**
- Better responsiveness when Claude uses multiple tools simultaneously
- More efficient parallel processing of independent operations
- Improved result streaming as tools complete

**Evidence**: `Qr1` class definition at line 429311, feature flag check at line 429499

### Command Redirection Safety

**What:** Enhanced validation and handling of shell command redirections for safer execution.

**Details:**
- Command parser `SP()` at line 208476 separates redirections from commands  
- Safety validation detects dangerous redirection patterns
- Already existed in v2.0.29 but continues to provide protection in v2.0.30

**Evidence**: Function `SP()` at line 208476 (v2.0.30), existed as `whA()` at line 204320 (v2.0.29)

## 📋 Other Changes

### TodoWrite Tool Documentation

The TodoWrite tool documentation remains unchanged between v2.0.29 and v2.0.30. All guidance on when to use the tool, task states, and management practices are identical.

**Evidence**: Documentation at lines 204989-205176 (v2.0.30), previously at lines 204886-205072 (v2.0.29)

### ExitPlanMode Tool

The ExitPlanMode tool continues to exist with the same functionality as in v2.0.29. This tool prompts users to exit plan mode after planning is complete.

**Evidence**: Tool description at line 432519 (v2.0.29), continues in v2.0.30 with updated variable names

### Internal Refactoring

- Removed several internal functions related to command history and UI components (non-user-facing)
- Added new internal error handling and validation classes for LSP protocol support
- Tool execution helper functions renamed but functionality preserved for backward compatibility

## 🔍 Summary Statistics

- **Structural similarity:** 98.0% (minimal breaking changes)
- **Declarations:** 8795 → 8948 (+153 net additions)
- **Changes:** 182 additions, 29 deletions, 28 modifications
