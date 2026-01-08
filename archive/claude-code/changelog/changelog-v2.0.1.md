# Changelog for version 2.0.1

## Highlights
Version 2.0.1 focuses on platform compatibility improvements and welcome screen refinements. The key changes include proper handling of Bedrock/Vertex platform configurations during model migrations, enhanced Apple Terminal support with custom rendering, and streamlined onboarding that emphasizes keyboard shortcuts over changelog history.

### Extended Thinking Detection for API Calls
**What:** Added automatic detection of extended thinking content in conversation history to ensure accurate token counting and proper API parameter configuration.

**How it works:** When Claude Code needs to count tokens for API calls, it now scans through the message history to detect if any assistant responses contain thinking or redacted_thinking blocks. If detected, it automatically includes the appropriate thinking parameters in the API call.

**Details:**
- Detects both `thinking` and `redacted_thinking` content types
- Automatically adjusts token counting for conversations with extended thinking
- Ensures API calls include proper thinking budget parameters (1024 tokens)
- Improves accuracy when estimating costs for conversations using extended thinking
- **Evidence**: `uS2() at line 376194` (new detection function), enhanced `TZ1() at line 376212` and `dS2() at line 376234`

### Apple Terminal Custom Welcome Banner
**What:** Apple Terminal users now see a specially designed welcome screen with optimized ASCII art rendering.

**How it works:** The CLI detects if you're running in Apple Terminal and displays a custom banner designed for that terminal's specific rendering characteristics.

**Details:**
- Automatically detects Apple Terminal environment
- Shows theme-appropriate ASCII art (different designs for light vs dark themes)
- Uses simplified character graphics (▗, ▖) for better rendering compatibility
- Early detection ensures custom banner appears before standard theme processing
- **Evidence**: `Pc1() at line 441323` checks `hA.terminal === "Apple_Terminal"`, custom banner rendered via `Ot5() at line 441581`

### Streamlined Welcome Screen
The welcome screen now focuses on keyboard shortcuts rather than recent changelog entries. Instead of displaying the latest features from the changelog, new users immediately see the most important keyboard shortcuts for getting started.

**What changed:**
- Removed the "What's new" section that displayed recent changelog entries
- Replaced with a "Shortcuts" section showing essential keybindings
- Simplified onboarding experience focusing on practical usage

**Evidence**: `fGB() at line 405662` (v2.0.0) removed, replaced with `PGB() at line 405481` (v2.0.1)

### Platform-Aware Model Migration
The Sonnet 4.5 model migration now intelligently skips execution for Bedrock and Vertex AI users, preserving their platform-specific model configurations.

**What changed:**
- Migration checks if you're using Bedrock (`CLAUDE_CODE_USE_BEDROCK`) or Vertex AI (`CLAUDE_CODE_USE_VERTEX`)
- Third-party platform users skip the migration entirely, keeping their existing model settings
- Only Anthropic API (firstParty) users have their model preferences reset

**Why it matters:** Bedrock and Vertex have different model catalogs and naming conventions. This prevents the migration from breaking configurations on those platforms.

**Evidence**: `v4Q() at line 443591` with platform check via `k8() at line 351873`

### Visual Consistency Fix
Updated ASCII art rendering to use consistent color naming throughout the welcome screen.

**What changed:**
- Claude logo ASCII art changed from `"claude"` color to `"clawd_body"` color
- Matches the color scheme introduced for the Clawd mascot in v2.0.0
- No visual change (both colors use identical RGB values)
- Improves code maintainability and semantic clarity

**Evidence**: Color changes in `Pc1() at lines 441437, 441462, 441474` and corresponding dark theme locations

### Import Statement Cleanup
Removed unused import statements and reorganized dependencies for cleaner code organization:
- Removed unused `stream` import (`import@338166`)
- Removed unused `node:process` import (`import@442305`)  
- Added focused imports: `cwd` from `node:process` (`import@357264`) and `PassThrough` from `stream` (`import@443814`)

**Evidence**: Diff lines 10-12, 73-75, 79-81, 408-410
