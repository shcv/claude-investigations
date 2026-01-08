# Changelog for version 2.0.61

## Highlights

This is a maintenance release containing internal code refactoring only. There are no user-facing changes, new features, or bug fixes in this version.

### Import Statement Modernization
**What:** Internal code refactoring that reorganizes how Node.js modules are imported.

**Details:**
- Converted 16 default imports to named/destructured imports
- No runtime behavior changes
- No impact on CLI functionality or performance
- **Evidence**: `import@16646` at line 16647 in v2.0.60 changed from `import eD1 from "node:child_process"` to destructured `import { spawn as v84, spawnSync as b84 } from "child_process"` at line 47888 in v2.0.61

**Affected modules:**
- `node:child_process`
- `node:fs`
- `node:os`
- `node:path`
- `node:process`
- `node:util`
- `crypto`
- `https`
- `stream`


**Note:** Users do not need to take any action for this release. All existing commands, flags, and workflows continue to work identically to v2.0.60.
