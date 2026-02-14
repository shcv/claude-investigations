# Changelog for version 0.2.34

# Claude Code v0.2.34 Changelog

## Import Optimizations

This release includes minor optimizations to module imports, focusing on more specific named imports rather than default imports. These changes improve code clarity and potentially reduce bundle size.


### Changes

#### Stream Module Updates
- **Optimized `stream` import**: Now imports only `Readable` as a named import instead of the entire stream module
  ```javascript
  // Before: import vR4 from "stream";
  // After:  import { Readable as qR4 } from "stream";
  ```

- **Added `PassThrough` stream utility**: Introduced named import for `PassThrough` from `node:stream`
  ```javascript
  import { PassThrough as so1 } from "node:stream";
  ```
  This suggests enhanced stream processing capabilities, potentially for piping data through transformations without modification.

#### Process Module Updates  
- **Optimized process import**: Changed from default import to named import of `cwd` function
  ```javascript
  // Before: import gb2 from "node:process";
  // After:  import { cwd as q00 } from "node:process";
  ```
  This indicates the CLI only needs the current working directory functionality from the process module.


### Summary

Version 0.2.34 is a minor optimization release that refactors module imports to use more specific named imports. This approach:
- Reduces memory footprint by importing only needed functions
- Improves code clarity by explicitly showing which functions are used
- Maintains 99.9% structural similarity with the previous version
- No functional changes to user-facing features

The addition of `PassThrough` stream support suggests potential improvements in how the CLI handles data streaming internally, though this doesn't introduce any new user-facing commands or features.
