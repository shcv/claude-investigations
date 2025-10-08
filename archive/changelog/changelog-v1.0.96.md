# Changelog for version 1.0.96

## 🎯 Highlights
Version 1.0.96 introduces privacy controls that allow users to manage whether their usage data helps improve Claude, along with updated Consumer Terms and Privacy Policy notifications. This update also removes some internal telemetry code and makes minor improvements to the codebase.

## 🚀 New Features

### Privacy Settings Command
**What:** New `privacy-settings` command to view and manage data privacy preferences
**How to use:**
```bash
# Access privacy settings directly (only available for Pro/Max users)
claude privacy-settings
```
**Details:**
- Available exclusively for Pro and Max tier users
- Allows toggling "Help improve Claude" setting to control data usage for model improvement
- Provides direct link to web privacy settings at https://claude.ai/settings/data-privacy-settings
- Settings changes take effect immediately upon confirmation
- **Evidence**: `MN5` privacy-settings command at line 410235, `uM1()` tier check at line 355298

### Consumer Terms and Privacy Policy Notice
**What:** Interactive notice system for updated Consumer Terms and Privacy Policy taking effect September 28, 2025
**How to use:**
The notice appears automatically when starting Claude if you haven't made a privacy choice. You'll see options to:
- Accept terms with "Help improve Claude: ON"
- Accept terms with "Help improve Claude: OFF"  
- Defer decision (if in grace period before September 28, 2025)

**Details:**
- Grace period allows deferring the decision until September 28, 2025
- After the deadline, acceptance becomes mandatory to continue using Claude
- Domain-excluded users (certain email domains) automatically have data collection disabled
- Reminder frequency configurable to avoid notification fatigue
- **Evidence**: `Nh1()` notice component at line 409856, `KgB()` display logic at line 409841

### Privacy Notice on Non-Interactive Commands
**What:** Privacy policy reminder when running Claude commands without entering interactive mode
**Details:**
- Shows brief reminder about updated terms when executing commands directly
- Different messages for grace period vs. post-deadline
- Automatically marks notice as viewed to prevent repeated displays
- **Evidence**: `zgB()` function at line 410212, called in `$pB()` startup flow

## 🔧 Improvements

### Startup Flow Enhancement
**What:** Integrated privacy consent into the onboarding and startup process
**Details:**
- Privacy notice now appears during initial onboarding for new users
- Existing users see the notice on next startup if they haven't made a choice
- Graceful handling of escape/cancellation with proper telemetry tracking
- **Evidence**: Modified `NS5()` function at line 434069 (previously `DS5()`)

## 🗑️ Removed Features

### Statsig Analytics Removal
**What:** Removed Statsig telemetry client initialization code
**Details:**
- Removed Statsig client setup and configuration functions (`HN5`, `zN5`, `zh7`)
- Cleaned up related imports and dependencies
- Statsig tracking appears to be replaced with internal telemetry for privacy choices
- **Evidence**: Removed functions at lines 409748-409785 in v1.0.95

## 🔍 Technical Changes

### New Telemetry Events
The following analytics events were added for privacy feature tracking:
- `tengu_grove_policy_viewed` - When privacy notice is displayed
- `tengu_grove_policy_submitted` - When user makes a privacy choice
- `tengu_grove_policy_dismissed` - When user defers decision
- `tengu_grove_policy_escaped` - When user exits without choosing
- `tengu_grove_privacy_settings_viewed` - When privacy settings page is accessed
- `tengu_grove_policy_toggled` - When privacy setting is changed
- `tengu_grove_policy_exited` - When user exits during startup notice
- `tengu_grove_print_viewed` - When non-interactive reminder is shown
- **Evidence**: Event calls throughout `Nh1()`, `HgB()`, and `zgB()` functions

### API Endpoints
New API endpoints for privacy management:
- `GET /api/oauth/account/settings` - Fetch user privacy preferences
- `PATCH /api/oauth/account/settings` - Update privacy preferences
- `POST /api/oauth/account/grove_notice_viewed` - Mark notice as viewed
- `GET /api/claude_code_grove` - Get Grove configuration and status
- **Evidence**: API functions `V01()` at line 401393, `qM0()` at line 401406, `Bf1()` at line 401419
