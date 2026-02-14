# Changelog for version 2.0.45

## Highlights

Version 2.0.45 adds support for Azure AI Foundry deployments with Azure AD authentication, refactors the image processing system to use pure Sharp implementation for better reliability, and includes numerous internal improvements to terminal handling and error management.


### Azure AI Foundry Support
**What:** Claude Code now supports connecting to Claude models deployed on Azure AI Foundry with Azure AD token authentication

**How to use:**
```bash
# Enable Foundry mode
export CLAUDE_CODE_USE_FOUNDRY=true

# Option 1: Use API key authentication
export ANTHROPIC_FOUNDRY_API_KEY=your-api-key
export ANTHROPIC_FOUNDRY_BASE_URL=https://your-resource.services.ai.azure.com/anthropic/

# Option 2: Use resource name (automatically constructs URL)
export ANTHROPIC_FOUNDRY_RESOURCE=your-resource-name

# Option 3: Use Azure AD authentication (no API key needed)
# Azure AD token provider is automatically configured
```

**Details:**
- Supports both API key and Azure AD token provider authentication methods
- Can specify either a full `baseURL` or a `resource` name (which constructs the Azure services URL automatically)
- Azure AD authentication uses the `https://cognitiveservices.azure.com/.default` scope
- For testing/debugging, you can skip authentication with `CLAUDE_CODE_SKIP_FOUNDRY_AUTH=true`
- Foundry deployments are now recognized as a first-party environment alongside standard Anthropic deployments
- **Evidence**: `dsA class at line 202345`, Foundry client initialization in `xw() at line 243262`, environment detection via `j3() at line 86382`


### Experimental Features Flag Check
**What:** New internal function to check if experimental beta features should be enabled based on deployment environment

**Details:**
- Experimental features are automatically enabled for `firstParty` and `foundry` deployments
- Can be disabled with `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=true` environment variable
- **Evidence**: `mq4() at line 86382`


### Image Processing System Refactored
**What:** Replaced optional native image processor module with pure Sharp-based implementation for more reliable and consistent image handling

**Details:**
- Previous versions attempted to use a compiled native module (`image-processor.node`) with Sharp as a fallback, often showing warnings like "Native image processor not available, falling back to sharp"
- New implementation uses Sharp exclusively with a sophisticated multi-stage compression strategy:
  1. Multi-scale resizing (100%, 75%, 50%, 25% of original dimensions)
  2. PNG-specific palette compression (64 colors at 800x800)
  3. Progressive JPEG quality reduction (starting at quality 50 for 600x600)
  4. Final fallback (400x400 at quality 20)
- Eliminates dependency on native compilation, improving reliability across different platforms
- More predictable behavior with deterministic compression strategies
- **Evidence**: Removed `UqQ() at line 280470`, `$qQ at line 280527`, `qqQ() at line 280537` in v2.0.44; Added `K5A() at line 156002`, `_P8() at line 156053`, `xP8() at line 156081`, `vP8() at line 156089`, `bP8() at line 156097` in v2.0.45


### Terminal Cursor Movement Enhanced
**What:** Terminal cursor positioning now uses semantic event types instead of raw ANSI control sequences

**Details:**
- Replaced raw stdout strings (like `\r` for carriage return, ` \b` for wrap handling) with semantic event types
- New event types: `resolvePendingWrap`, `carriageReturn`, `cursorMove`
- Supports returning multiple terminal events per transaction for more complex operations
- Improves code maintainability and testability while producing identical terminal output
- **Evidence**: Replaced `Hk0() at line 77408` with `Ii0() at line 77184`, updated supporting class from `zk0` to `Yi0`


### Model Name Display for Foundry
**What:** Model name display logic now recognizes Foundry deployments and adjusts accordingly

**Details:**
- Foundry deployments skip the friendly model name display to show raw model identifiers
- Ensures consistent behavior across different deployment environments
- **Evidence**: `Y6Q() at line 86439` includes foundry environment check


### LSP Server Manager Refactored
- Language Server Protocol support remains fully functional with comprehensive code reorganization
- Main manager function renamed and restructured for improved maintainability
- All LSP features (initialization, diagnostics, workspace configuration) preserved
- **Evidence**: `_MQ() at line 288094` renamed to `C62() at line 314954`


### Semver Regex Module Relocated
- Semantic versioning regex patterns module moved to a different location in the bundled code
- All regex patterns remain functionally identical
- Pure internal refactoring with no user-facing impact
- **Evidence**: `s0A at line 80963` in v2.0.44 moved to `Z5A at line 150649` in v2.0.45


### Dependency Management
- Updated @azure/msal-node to v3.8.1
- Updated @azure/msal-common to v15.13.1
- Added support for Azure identity authentication flows
- Internal version identifier updated from 0.68.0 to 0.70.0


### Telemetry Server Shutdown
- Added graceful shutdown handler for telemetry operations
- **Evidence**: `wj1() at line 148844`

## ️ Technical Notes

- Structural similarity between v2.0.44 and v2.0.45: 89.7%
- Total changes: 1,069 additions, 52 deletions, 24 modifications
- Significant internal variable renaming (9,301 renames) due to minification changes
- No breaking changes to public APIs or command-line interface
