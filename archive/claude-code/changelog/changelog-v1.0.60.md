# Changelog for version 1.0.60

Based on my analysis of the diff file, here's the changelog for Claude Code v1.0.60:

### Major Features

#### Agent Management System (New!)
- **New `/agents` command**: Create and manage custom subagents that Claude can delegate tasks to
  - Create agents with specialized system prompts and tool access
  - Choose between AI-generated or manual agent configuration
  - Agents can be stored at project level (`.claude/agents/`) or personal level (`~/.claude/agents/`)
  - Built-in agents are always available and cannot be modified
  - Each agent can have a custom background color for visual distinction

**Example usage:**
```bash
# Open the agent management interface
/agents
```

#### Background Shell Management Tools (New!)
- **KillShell Tool**: Kill a running background shell by its ID
  - Use `/bashes` command to find shell IDs
  - Returns success/failure status
  
- **BashOutput Tool**: Retrieve output from background shells
  - Returns only new output since last check
  - Shows stdout, stderr, and shell status
  - Automatically truncates very long outputs

### Enhanced Features

#### Bash Output Summarization
- Claude now intelligently summarizes verbose command outputs
- Summaries are triggered for outputs over 5000 characters
- Original output is preserved and can be viewed in verbose mode
- Includes sections for: Overview, Detailed Summary, Errors, and Verbatim Output
- Particularly useful for build logs, test results, and repetitive debug output

**Example scenario:**
```bash
# Running a command with verbose output
npm run build

# Claude will automatically summarize if output is lengthy, showing:
[Summarized output]
Overview: Build completed successfully...
Detailed summary: ...
Errors: None encountered
Verbatim output: [key snippets preserved]
```

#### Spinner Tips
- Tips functionality has been made configurable
- Tips are now fetched dynamically based on user preferences
- Improved tip management system

### UI/UX Improvements

#### Enhanced Dialog Components
- New `bv1` component for better dialog presentation
- Improved escape key handling with "Press Esc again to exit" confirmation
- Consistent styling with rounded borders and proper spacing

#### OAuth Flow Improvements
- Added manual code entry support for OAuth authentication
- Better error handling with retry options
- Visual improvements during the authentication process
- Support for long-lived tokens (1 year expiry) for GitHub Actions

### Technical Improvements

#### ️ Command System Enhancements
- New agent type system with built-in types:
  - `general-purpose`: General multi-step task handling
  - `context-collector`: Codebase exploration and metrics
  - `tech-researcher`: Technical solution research
  - `test-engineer`: Test writing and maintenance
  - `spec-designer`: Specification refinement
  - `file-organizer`: File operations and organization
  - `comment-writer`: Code documentation
  - `investigator`: Deep code investigation
  - `refactoring-specialist`: Code improvement
  - `code-auditor`: Architecture and security analysis
  - `implementation-engineer`: Feature implementation
  - `documentation-specialist`: Comprehensive documentation
  - `style-fixer`: Code formatting and style

#### Aliases and Usability
- `/clear` command now also responds to `/reset` alias
- Improved permission handling for additional working directories
- Better path resolution and validation

### Developer Experience

#### Agent Creation Workflow
1. **Choose location**: Project or personal agents directory
2. **Creation method**: AI-generated or manual configuration
3. **Define purpose**: Describe what the agent should do
4. **Select tools**: Choose which tools the agent can access
5. **Customize appearance**: Optional background color
6. **Review and save**: Confirm configuration before saving

**Example agent creation:**
```bash
/agents
# Select "Create new agent"
# Choose location: Project
# Method: Generate with Claude
# Describe: "Expert code reviewer that checks for security vulnerabilities and best practices"
# Claude generates the configuration
# Select tools the agent should have access to
# Choose a background color
# Save the agent
```

### Bug Fixes and Cleanup
- Removed unused OAuth error classes and related error handling code
- Cleaned up shell snapshot cleanup functionality
- Removed various deprecated functions and imports
- Fixed issue with pasted text display (now shows "[Pasted text #X]" without "+0 lines")

### Breaking Changes
- None identified in this release

### Notes for Users
- Agents provide a powerful way to create specialized assistants for specific tasks
- Background shell management allows better handling of long-running processes
- Output summarization helps maintain context efficiency while preserving important information
- The new agent system is particularly useful for repetitive tasks like code reviews, testing, and documentation
