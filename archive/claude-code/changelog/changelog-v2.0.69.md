# Changelog for version 2.0.69

## Highlights
This release fixes a significant bug in the prompt suggestion system where the token limit was too restrictive, and includes internal code refactoring for better maintainability.


### Prompt Suggestion Token Limit Fix
**What:** Fixed the prompt suggestion feature's `maxOutputTokens` limit, which was set far too low at 50 tokens, potentially causing truncated or failed suggestions.

**Details:**
- The `maxOutputTokens` was increased from 50 to 16,000 tokens
- This provides the model adequate headroom to generate suggestions without hitting token limits
- The prompt still requests brief 3-8 word suggestions, but the model now has sufficient capacity to reason and respond reliably
- **Evidence**: `nH8()` function at line 366252 - `maxOutputTokens` changed from `iH8` (value: 50) to hardcoded `16000`


### Prompt Suggestion Code Refactoring
**What:** The prompt suggestion function was refactored for better code organization and maintainability.

**Details:**
- The system prompt text was extracted from inline to a module-level constant (`iH8` at line 366298)
- The function was converted from promise-chain style to explicit async/await
- Response parsing changed from `.then()` chain with `.find()` to a `for...of` loop with early return
- Variables were extracted for better readability (`cacheSafeParams` to `Q`, `canUseTool` callback to `B`)
- **Evidence**: `nH8()` at lines 366252-366273 in v2.0.69 vs lines 366252-366280 in v2.0.68


### Import Statement Reorganization
**What:** Several import statements were reorganized and consolidated across the codebase.

**Details:**
- Node.js built-in imports (`node:fs`, `node:child_process`, `node:path`, `node:os`, `node:util`, `node:process`) were restructured
- Crypto imports consolidated to use named imports (`randomBytes`, `randomUUID`, `timingSafeEqual`)
- Stream import changed from default to named import (`PassThrough`)
- These are purely organizational changes with no functional impact
- **Evidence**: Import changes at multiple locations throughout the codebase (see diff lines 10-72, 76-170)
