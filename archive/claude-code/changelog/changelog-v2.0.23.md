# Changelog for version 2.0.23

## 🎯 Highlights

Version 2.0.23 is a maintenance release focused on internal code improvements and a new experimental security feature for API requests.

## 🔒 New Features

### Additional Protection Mode for API Requests

**What:** Added support for an experimental additional protection mode that can be enabled via environment variable.

**How to use:**
```bash
# Enable additional protection for API requests
export CLAUDE_CODE_ADDITIONAL_PROTECTION=true
claude --prompt "your prompt here"
```

**Details:**
- When enabled, sets the `x-anthropic-additional-protection` header on API requests
- This is an experimental security feature that may provide enhanced request validation
- Only affects requests to Anthropic's API (not Bedrock or Vertex)
- **Evidence**: Added at `bU() at line 203031-203032` in the API client initialization function

## 🔧 Internal Improvements

### Session Persistence Optimization

Improved the session persistence mechanism by adding request queuing and serialization to prevent race conditions when multiple session updates occur simultaneously. The system now uses a Map-based queue (`fTQ`) to ensure session persistence operations are processed sequentially per session.

**Evidence**: New function `hTQ() at line 457187` wraps session persistence calls with queue management, while `qM8() at line 457135` handles the actual persistence logic.

### Import Reorganization

Consolidated and optimized module imports throughout the codebase:
- Removed redundant stream module imports
- Reorganized child_process imports to use named imports (`execSync`, `spawn`) instead of default imports
- Better alignment with Node.js best practices for ES module imports

**Evidence**: 
- Removed generic `import tr from "stream"` at line 12593
- Removed generic `import j40 from "node:child_process"` at line 35801  
- Added specific `import { PassThrough as ET8 } from "stream"` at line 467265
- Added specific `import { execSync as IBB, spawn as gO6 } from "node:child_process"` at line 247798
