# Changelog for version 1.0.57

Based on the analysis, here's the changelog for Claude Code v1.0.57:

# Claude Code v1.0.57 Changelog

## New Features

### pr-comments Prompt Optimization
The `pr-comments` prompt feature now uses Claude 3.5 Haiku model for improved performance when fetching and analyzing GitHub pull request comments. This optimization provides faster responses while maintaining quality for this specific use case.

**Example usage remains the same:**
```bash
# Fetch comments from the current PR
claude pr-comments

# With additional context
claude pr-comments "focus on security-related feedback"
```

## Internal Improvements

- **Code cleanup**: Removed numerous unused internal functions and variables, reducing bundle size and improving performance
- **Dependency updates**: Updated AWS SDK components for better compatibility
- **Infrastructure improvements**: Enhanced support for model-specific prompt configurations

## Technical Details

The primary change allows individual prompt features to specify which Claude model they use. The `pr-comments` feature now explicitly uses `claude-3-5-haiku-20241022` instead of the default model, optimizing for speed and cost-efficiency when processing pull request comments.

This update indicates a move toward task-specific model optimization, where different features can leverage the most appropriate Claude model based on their complexity and performance requirements.

## Notes

- No breaking changes
- No new CLI commands or flags
- Existing pr-comments functionality remains unchanged from a user perspective
- The model change is automatic and requires no configuration
