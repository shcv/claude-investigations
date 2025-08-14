# Changelog for version 1.0.79

## 🎯 Summary
v1.0.79 updates the GitHub Actions integration documentation URLs and adds enhanced telemetry tracking for subscription types.

## 📚 Documentation Updates

### GitHub Actions Documentation Reorganization
**What changed:** Updated all GitHub Actions setup documentation links to point to new dedicated documentation files
**Previous:** Links pointed to README hash fragments like `#manual-setup-direct-api`
**New:** Links now point to dedicated docs at `https://github.com/anthropics/claude-code-action/blob/main/docs/setup.md`
**Impact:** Users get more comprehensive setup instructions in a dedicated documentation structure

## 💪 Improvements

### Enhanced Telemetry
**What changed:** Added subscription type and first token timestamp tracking to the identity provider
**New data collected:**
- `subscriptionType`: Tracks user's subscription tier (enterprise/team/pro/max/free)
- `firstTokenTime`: Records when user first authenticated with Claude Code
- `organizationUUID`: Added to custom IDs for better org-level analytics
**Impact:** Better understanding of user segments and engagement patterns while maintaining privacy

### GitHub Actions Environment Detection
**What changed:** Enhanced telemetry when running in GitHub Actions environment
**New data collected when `GITHUB_ACTIONS=true`:**
- `githubEventName`: The event that triggered the workflow
- `githubActionsRunnerEnvironment`: Runner environment details
- `githubActionsRunnerOs`: Operating system of the runner
- `githubActor`: User who triggered the action
- `githubRepositoryOwner`: Repository owner information
**Impact:** Better support and debugging for Claude Code running in CI/CD pipelines

## 🔧 Technical Changes

### Module Import Optimization
**What changed:** Switched from default imports to named imports for Node.js built-in modules
**Changes:**
- `import crypto from "crypto"` → `import { createHash, randomBytes } from "crypto"`
- `import stream from "stream"` → `import { PassThrough } from "stream"`
- `import process from "node:process"` → `import { cwd } from "node:process"`
**Impact:** Slightly improved tree-shaking and bundle optimization

### Output Style Function Addition
**What changed:** Added new function `L8B()` for retrieving output style configurations
**Purpose:** Supports future output style customization features
**Impact:** Foundation for customizable Claude response styles

## 📝 Notes
- The GitHub Actions feature (`/install-github-app` command) existed in v1.0.78 and remained functionally unchanged
- Variable names in minified code changed due to the build process (e.g., `zgB` → `WgB`, `EgB` → `JgB`)
- Version bump primarily for documentation updates and telemetry enhancements
