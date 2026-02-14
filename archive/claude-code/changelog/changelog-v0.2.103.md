# Changelog for version 0.2.103


### New Features

#### Parallel Agent Execution
- **Multiple concurrent agents**: Introduced a new parallel agent system that allows launching multiple agents simultaneously to work on the same task
- **Configurable agent count**: Users can control the number of parallel agents through settings
- **Automatic synthesis**: When using parallel agents, responses are automatically combined into a unified solution
- **Performance improvement**: Significantly faster execution for complex, multi-faceted tasks

#### Enhanced Edit Capabilities
- **Jupyter Notebook support**: Added `NotebookEdit` tool for editing Jupyter notebook cells
  - Use `edit_mode=insert` to add new cells
  - Use `edit_mode=delete` to remove cells
  - Use `edit_mode=replace` to update existing cells (default)
  - Example: `notebook_path="/path/to/notebook.ipynb", cell_number=0, new_source="print('Hello')", edit_mode="insert"`

#### Improved Thinking Mode
- **Dynamic thinking tokens**: Thinking capacity now adjusts based on user prompts
  - "think" → 4,000 tokens
  - "think hard/deeply/more" → 10,000 tokens  
  - "think harder/longer/really hard" → 31,999 tokens
- **Environment variable control**: Set `MAX_THINKING_TOKENS` to override automatic detection

#### Development Partner Program Integration
- **Data sharing notifications**: Organizations enrolled in the Development Partner Program receive clear notifications about data sharing
- **Discounted pricing**: Automatic cost adjustments for qualifying organizations
- **Visual indicators**: Special UI elements show enrollment status


### User-Facing Improvements

#### Tool Enhancements
- **MCP content size validation**: Added protection against oversized MCP tool responses exceeding token limits
- **IDE integration improvements**: Better handling of IDE-specific tools when `ENABLE_IDE_INTEGRATION=true`
- **Tool filtering**: Certain IDE tools are now properly filtered based on environment settings

#### Usage Tracking
- **Rate limit visibility**: Enhanced display of Claude AI usage limits with reset times
- **Token usage display**: More detailed token counting across parallel agent operations
- **Cost tracking**: Improved cost calculations including cache tokens


### CLI Arguments & Commands

#### Session Management
- **Auto-save sessions**: Sessions are now automatically saved with proper naming conventions
- **Session recovery**: Better handling of session restoration after crashes or interruptions

#### Error Handling
- **Clearer error messages**: More descriptive errors for:
  - API authentication issues
  - OAuth token revocation
  - Credit balance problems
  - Context length exceeded
  

### Performance & Stability

- **Request retry logic**: Improved retry mechanism with better backoff strategies
- **Abort handling**: More graceful cancellation of in-progress operations
- **Memory optimization**: Better cleanup of completed agent tasks


### Bug Fixes

- Fixed duplicate imports and variable declarations
- Removed obsolete IDE integration code
- Cleaned up unused configuration variables
- Improved file path handling across different operating systems


### Breaking Changes

- Removed several internal-only functions and variables that were not user-facing
- Changed internal message ID generation to use UUIDs consistently

This release focuses on performance improvements through parallel execution, better notebook support, and enhanced thinking capabilities while maintaining backward compatibility for existing workflows.
