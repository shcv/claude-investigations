# Changelog for version 2.1.56


## Summary

Version 2.1.56 is a maintenance release with internal refactoring only. The bundler output was updated to use named/destructured imports for Node.js core modules instead of default imports, simplifying several lazy initialization wrappers. There are no user-facing changes in this release.

## Notes

This release contains no new features, improvements, or bug fixes that affect users. The 99.9% structural similarity between v2.1.55 and v2.1.56 reflects purely internal changes:

- **Import modernization**: Default imports like `import X from "child_process"` were replaced with named imports like `import { execFile, spawn } from "child_process"` across 12 Node.js core modules (`child_process`, `crypto`, `https`, `node:child_process`, `node:fs`, `node:os`, `node:path`, `node:process`, `node:util`, `path`, `stream`, `url`).

- **Initialization simplification**: Several lazy initialization wrappers (e.g., for `promisify(execFile)`) were simplified or removed since named imports no longer require runtime extraction from default import objects.

Evidence: Import changes visible across the diff header; verified via counts of `tengu_` flags (933 each), `CLAUDE_CODE_` env vars (399 each), `.describe(` settings (385 each), slash commands (1,128 each), and CLI flags (129 unique each) — all identical between v2.1.55 and v2.1.56.
