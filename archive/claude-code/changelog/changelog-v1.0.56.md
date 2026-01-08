# Changelog for version 1.0.56

Based on my analysis of the diff for version 1.0.56, here's the changelog:

### New Features and Improvements

#### Enhanced AWS SDK Integration
- **New AWS authentication schemes**: Added support for multiple authentication methods including SigV4, SigV4A, and bearer token authentication
- **Improved credential providers**: 
  - Added HTTP credential provider for containerized environments (ECS/EKS)
  - Enhanced SSO credential provider with automatic token refresh
  - Added support for environment variable-based credentials with account ID and credential scope
- **New authentication configuration**: Users can now specify authentication scheme preferences via:
  - Environment variable: `AWS_AUTH_SCHEME_PREFERENCE`
  - Config file setting: `auth_scheme_preference`
  - Bearer tokens: `AWS_BEARER_TOKEN_<SERVICE_NAME>`

#### Protocol and Serialization Enhancements
- **Added comprehensive protocol support**:
  - AWS JSON RPC (1.0 and 1.1)
  - AWS Query protocol
  - AWS EC2 Query protocol  
  - AWS REST JSON
  - AWS REST XML
- **New serialization/deserialization infrastructure**: Added schema-based serialization with support for complex data types including big integers, big decimals, and timestamps

#### Improved Error Handling
- **Service exceptions**: New base `ServiceException` class with better error metadata
- **Protocol-specific error handling**: Each AWS protocol now has specialized error deserialization
- **Enhanced error messages**: More descriptive error messages with request IDs and extended metadata

#### Performance and Reliability
- **Request retry enhancements**: Improved retry strategies with configurable retry modes
- **Connection timeout configuration**: Different timeout settings based on deployment mode (standard, in-region, cross-region, mobile)
- **Middleware improvements**: Added recursion detection for Lambda environments to prevent infinite loops

#### Developer Experience
- **Command builder pattern**: New fluent API for building commands:
  ```javascript
  Command.classBuilder()
    .n("ServiceClient", "OperationCommand")
    .f(inputFilter, outputFilter)
    .ser(serializer)
    .de(deserializer)
    .build()
  ```
- **Aggregated client support**: Automatically generate convenience methods for all service operations
- **Improved logging**: Better structured logging with sensitive data filtering

### Bug Fixes
- Fixed duplicate comment issue in generated code
- Improved URL validation for credential providers
- Better handling of missing or invalid credentials

### Breaking Changes
- Node.js 16.x deprecation warning: Support will end on January 6, 2025
- Some internal functions have been removed or refactored

### Technical Improvements
- Added support for endpoint URL resolution with proper protocol handling
- Enhanced XML and JSON parsing with better error recovery
- Improved support for streaming responses and event streams
- Better handling of binary data with proper base64 encoding/decoding

This version represents a significant enhancement to the AWS SDK integration capabilities, making it easier to work with AWS services through Claude Code's CLI interface.
