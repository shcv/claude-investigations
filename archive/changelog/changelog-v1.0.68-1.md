# Changelog for version 1.0.68

Based on my analysis of the diff, here's the detailed changelog for Claude Code v1.0.68:

## Claude Code v1.0.68 Changelog

### Major Changes

#### 🚫 Removed Features

1. **NotebookRead Tool Removed**
   - The `NotebookRead` tool for extracting and reading source code from Jupyter notebooks has been completely removed
   - All associated functionality for reading `.ipynb` files as a dedicated tool has been deprecated
   - Note: Notebooks can still be read using the standard Read tool

2. **Claude CLI Diagnostic Command Removed**
   - The diagnostic functionality that showed installation status, paths, and configuration has been removed
   - This included checks for installation type, version, update permissions, and multiple installation warnings

3. **Alias Setup Helper Removed**
   - The automatic shell alias setup helper function has been removed
   - This previously helped users set up the `claude` alias in their shell configuration files

#### ✨ New Features

1. **Enhanced Process Execution Library (Execa)**
   - Added comprehensive process execution capabilities with the Execa library
   - New template literal syntax for executing commands:
     ```javascript
     // Example usage (internal):
     const result = await $`ls -la`;
     ```
   - Features include:
     - Advanced stream handling for stdin, stdout, stderr
     - IPC (Inter-Process Communication) support
     - Graceful cancellation with AbortSignal
     - Timeout management with force kill options
     - Better error handling with detailed error messages

2. **Stream Processing Enhancements**
   - New stream utilities for handling various data types:
     - `oJ1` - Array stream processing
     - `tJ1` - ArrayBuffer stream processing  
     - `AX1` - Text/string stream processing
   - Support for async iterables and web streams
   - Better memory management with configurable buffer limits

3. **IPC Communication**
   - Advanced IPC messaging system for subprocess communication
   - Deadlock detection and prevention
   - Strict mode for ensuring message delivery
   - Cancel signal propagation between parent and child processes

4. **Enhanced Error Reporting**
   - More detailed error messages with context
   - Better signal descriptions using human-readable names
   - Improved max buffer error reporting with specific stream information
   - Force termination tracking and reporting

### Technical Improvements

1. **Process Management**
   - Better signal handling with comprehensive signal definitions
   - Support for real-time signals (SIGRT)
   - Improved process cleanup and resource management
   - Reference counting for IPC channels

2. **Performance Optimizations**
   - Resizable ArrayBuffer support for better memory efficiency
   - Streaming data processing with backpressure handling
   - Optimized buffer allocation strategies

3. **Cross-Platform Enhancements**
   - Better Windows support for command escaping
   - Platform-specific PATH handling improvements
   - Consistent signal behavior across operating systems

### Breaking Changes

- Users relying on the `NotebookRead` tool must now use the standard `Read` tool for Jupyter notebooks
- The diagnostic command functionality is no longer available
- Shell alias setup must be done manually

### Internal Changes

- Removed unused stream imports
- Consolidated subprocess execution logic
- Better TypeScript-style error handling patterns
- Enhanced validation for tool inputs

This version focuses on improving the robustness of subprocess execution and stream handling while streamlining the tool interface by removing the specialized notebook reading functionality in favor of the unified Read tool approach.
