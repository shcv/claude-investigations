# Changelog for version 1.0.64

Based on my analysis of the diff file, here's the changelog for Claude Code version 1.0.64:

## Claude Code v1.0.64 Changelog

### New Features

#### 🎯 Agent Model Configuration
- **Configurable AI models for agents**: Agents can now specify which Claude model they should use (Sonnet, Opus, or Haiku)
- **"Inherit" model option**: Agents can inherit the model from the parent conversation, allowing for flexible model usage
- **Environment variable override**: New `CLAUDE_CODE_SUBAGENT_MODEL` environment variable to globally override agent model selection
  ```bash
  export CLAUDE_CODE_SUBAGENT_MODEL=haiku
  claude # All agents will use Haiku regardless of their configuration
  ```

#### 🛠️ Enhanced Agent Management
- **Edit Model option**: New menu option "Edit model" when managing agents through the interactive UI
- **Model validation**: Agent files now validate model specifications against allowed values (sonnet, opus, haiku, inherit)
- **Agent file model syntax**: Agents can specify their model in the frontmatter:
  ```markdown
  ---
  name: my-agent
  description: Description of what this agent does
  model: opus  # New field
  tools: [Read, Write, Bash]
  ---
  ```

#### 🔧 MCP (Model Context Protocol) Improvements
- **Resource management**: Better handling of MCP resources with proper cleanup and state management
- **Tool namespacing**: MCP tools are now properly namespaced with `mcp__<server-name>__` prefix for better organization
- **Connection stability**: Improved reconnection logic for SSE (Server-Sent Events) based MCP connections

#### 📊 Status Hook Integration
- **External status monitoring**: New internal status hook system for external tools to monitor Claude Code's status
- **JSON-based status communication**: Status information can be passed to external commands via JSON
- **Configurable timeout**: Status hook operations have a 5-second default timeout

### Improvements

#### 🎨 UI/UX Enhancements
- **Model display in agent info**: Agent model selection is now displayed in the agent information
- **Better model descriptions**: Clear descriptions for each model option:
  - Sonnet: "Balanced performance - best for most agents"
  - Opus: "Most capable for complex reasoning tasks"
  - Haiku: "Fast and efficient for simple tasks"
  - Inherit: "Use the same model as the main conversation"

#### 🐛 Bug Fixes
- **Removed duplicate MCP management code**: Cleaned up redundant MCP server management implementation
- **Fixed agent file path handling**: Improved path resolution for agent files across different locations
- **Better error messages**: More descriptive error messages for invalid agent configurations

### Technical Changes

#### 🏗️ Architecture
- **Modular agent system**: Agents now have a more structured configuration with model preferences
- **Improved type safety**: Better validation of agent properties including model selection
- **Resource cleanup**: Proper cleanup of MCP resources when connections are terminated

#### 🔄 Compatibility
- **Backward compatible**: Existing agents without model specifications default to Sonnet
- **Survey system**: Added force display option via `CLAUDE_FORCE_DISPLAY_SURVEY` environment variable for testing

### Usage Examples

**Creating an agent with a specific model:**
```bash
# In your .claude/agents/fast-analyzer.md
---
name: fast-analyzer
description: Quick code analysis using Haiku for speed
model: haiku
tools: [Read, Grep, Glob]
---

Your agent prompt here...
```

**Using the inherit model option:**
```bash
# If you're using Opus in your main conversation
claude --model opus

# This agent will also use Opus when called
---
name: inherit-example
description: Uses the same model as the parent conversation
model: inherit
tools: [*]
---
```

**Global model override:**
```bash
# Force all agents to use Haiku for faster responses
export CLAUDE_CODE_SUBAGENT_MODEL=haiku
claude
```

This update focuses on giving users more control over agent behavior through model selection, improving the MCP integration, and enhancing the overall agent management experience.
