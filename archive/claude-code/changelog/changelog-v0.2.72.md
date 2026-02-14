# Changelog for version 0.2.72

# Claude Code v0.2.72 Changelog


### Parallel Agent Execution
- **New command**: `/parallel-agents [on|off|count]` - Toggle parallel agent execution or set the number of agents to run concurrently
  - `parallel-agents on` - Enable with default 3 agents
  - `parallel-agents off` - Disable parallel execution
  - `parallel-agents 5` - Enable with 5 parallel agents
  - `parallel-agents` or `parallel-agents status` - Show current status
  - Note: Using parallel agents will increase token usage by approximately (count + 1)x due to the synthesis agent


### Enhanced Progress Indicators
- **Offline indicator**: Progress spinner now shows "offline" status when internet connection is lost
- **Network connectivity monitoring**: Real-time detection of internet connectivity with visual feedback
- **Mode-specific spinners**: Different visual indicators for different operations:
  - `⚒` for tool use
  - `↓` for responding/thinking
  - `↑` for requesting


### Improved File Size Display
- New human-readable file size formatting (e.g., "1.5MB" instead of "1572864 bytes")
- Automatic unit conversion: bytes → KB → MB → GB


### Streamlined Command Output Display
- Simplified display of command execution results
- Cleaner separation of stdout and stderr output
- More concise "No output" message when commands produce no output


### Better Progress Tracking
- Token counting now updates smoothly during generation
- Elapsed time counter with 10ms precision
- Improved animation timing for character counting


### Enhanced Settings Display
- Local settings now show: `On this machine in <path>`
- Project settings now show: `Checked in at .claude/settings.json`
- Clearer distinction between local and project-wide settings


### Parallel Agent Architecture
When enabled, the Task tool can now:
1. Spawn multiple agents to work on different aspects of a problem simultaneously
2. Collect results from all agents
3. Use a synthesis agent to combine findings into a cohesive response
4. Display progress for each agent separately in the UI

Example output with parallel agents:
```
3 total tool uses across 3 agents

Agent 1:
  [tool use progress]

Agent 2:
  [tool use progress]

Synthesis (combining results):
  [synthesis progress]
```


### Stream Event Handling
- New `stream_request_start` event type for better request lifecycle tracking
- Improved mode detection for different content block types
- More granular control over UI updates during streaming


### Removed Legacy Features
- Removed persistent shell functionality and related classes
- Removed unused spinner configurations and animation styles
- Cleaned up deprecated utility functions

## Bug Fixes

- Fixed duplicate import statements
- Improved error handling for offline scenarios
- Better cleanup of temporary resources
