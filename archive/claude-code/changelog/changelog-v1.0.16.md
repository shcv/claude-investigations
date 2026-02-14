# Changelog for version 1.0.16

# Claude Code v1.0.16 Changelog


### Plan Mode Support
- **New `ExitPlanMode` tool**: Users can now work in a "plan mode" where Claude Code presents implementation plans before executing them. When ready to proceed with coding, this tool prompts the user to exit plan mode.
  - Example usage: After Claude Code presents a plan for implementing a feature, it will use this tool to get user approval before proceeding with the actual implementation.
  - The plan parameter supports markdown formatting for clear, structured presentations.


### Non-Interactive Session Support
- **New session mode detection**: Claude Code can now detect and handle non-interactive sessions differently from interactive ones.
  - Two new functions manage this state: `z0A()` to check if the session is non-interactive, and `w0A(A)` to set the non-interactive state.
  - This affects API key authentication behavior - non-interactive sessions have different authentication requirements.


### Authentication and API Key Handling
- **Enhanced API key source detection**: The authentication check now considers whether the API key comes from `ANTHROPIC_API_KEY` environment variable or the `apiKeyHelper`.
  - The `iP()` function (formerly `BV()`) now checks the source of authentication more granularly.
  - Non-interactive sessions are handled differently in authentication flows.


### Cloud Provider Detection
- **Simplified cloud provider checks**: New `Hv()` function provides a cleaner way to detect if Claude Code is using AWS Bedrock or Google Vertex AI.
  - Returns `true` if either `CLAUDE_CODE_USE_BEDROCK` or `CLAUDE_CODE_USE_VERTEX` environment variables are set.


### Token Limits and Management
- **Updated token limits**: 
  - Maximum token limit increased from 180,000 to 200,000 tokens
  - New 20,000 token threshold introduced for certain operations
  - New `Ow2()` function calculates remaining tokens available in the current context


### Performance
- **Optimized imports**: Streamlined import statements, using more specific imports like `{ cwd as dI0 }` and `{ PassThrough as uK5 }` instead of default imports.

## Internal Changes

- Added new constant `po1 = 3000` (likely a timeout or delay value)
- Removed unused `KfA()` function that checked authentication source
- Removed empty object schema `q75` 
- Added `HA1` variable for internal module management

## Breaking Changes

None - this version maintains backward compatibility with v1.0.15.
