# Changelog for version 1.0.40

# Claude Code v1.0.40 Changelog


### Enhanced Web Search Date Awareness
The WebSearch tool now includes improved guidance for handling date-sensitive queries. When searching for the latest documentation or time-sensitive content, the tool will now properly account for the current date provided in the environment context.

**Example**: If the environment indicates "Today's date: 2025-07-01" and you request "the latest docs", the search will use 2025 in the query instead of defaulting to 2024.


### Improved SSL/TLS Certificate Handling
The CLI now better supports Node.js's automatic certificate authority (CA) handling:

- When `NODE_EXTRA_CA_CERTS` is set, Claude Code will display an informative message that Node.js will automatically append these certificates to the built-in CAs
- The certificate configuration display has been simplified and clarified

Usage:
```bash
# Set additional CA certificates
export NODE_EXTRA_CA_CERTS=/path/to/ca-bundle.crt
claude-code
```

The API configuration info (shown via `claude-code --version` or during startup) will now display:
- `Additional CA cert(s): /path/to/ca-bundle.crt` when NODE_EXTRA_CA_CERTS is set
- Clearer labeling for mTLS client certificates and keys

## Technical Improvements

- Streamlined import statements for Node.js stream modules
- Added support for data structures related to GitHub issue/PR tracking (internal improvement for future features)
- Improved process working directory handling with explicit imports
- Code restructuring for better modularity

## Bug Fixes

- Removed redundant certificate configuration checks
- Fixed duplicate import statements for stream modules
- Cleaned up unnecessary conditional logic in certificate validation
