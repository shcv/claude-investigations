# Changelog for version 2.1.5


## Summary

This is a maintenance release with no user-facing changes. The update consists entirely of internal code refactoring—specifically, modernizing import statements to use ES module named imports instead of default imports for Node.js built-in modules.

## New Features

None.

## Improvements

None.

## Bug Fixes

None.

## Internal Changes (Not User-Facing)

This release refactors how Node.js built-in modules are imported throughout the codebase:

- **Import modernization**: Changed from default imports (e.g., `import fs from "node:fs"`) to named imports (e.g., `import { readFileSync, existsSync } from "node:fs"`).

- **Affected modules**: `node:child_process`, `node:fs`, `node:os`, `node:path`, `node:process`, `node:util`, `crypto`, `https`, `stream`, `path`, `child_process`

**Evidence**: The diff shows 15 removed import statements and 15 added import statements with restructured named imports. Structural similarity is 99.9% with 8,487 internal variable renames typical of minification differences.

## Notes

Users upgrading from v2.1.4 should experience no behavioral differences. This release appears to be a housekeeping update to improve code consistency and potentially enable tree-shaking optimizations in the bundler.
