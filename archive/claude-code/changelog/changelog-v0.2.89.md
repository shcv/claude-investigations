# Changelog for version 0.2.89

## Overview
This update significantly restructures the internal codebase, removing 1,130 declarations and adding 176 new ones, resulting in a more streamlined implementation with 84.3% structural similarity to v0.2.86.


### AWS Credential Chain Management
- **New `createCredentialChain()` function**: Provides enhanced credential chain management for AWS SDK operations
  - **`expireAfter()` method**: Allows setting custom expiration times for credentials
  - Minimum expiration duration enforced at 5 minutes (300,000ms)
  - Example usage:
    ```javascript
    const credChain = createCredentialChain(provider1, provider2)
      .expireAfter(600000); // Set 10-minute expiration
    ```


### Property Provider Chain
- **New `propertyProviderChain()` function**: Implements a chain-of-responsibility pattern for property providers
  - Automatically tries next provider in chain if current provider fails with `tryNextLink` flag
  - Throws the last error if all providers fail


### Stream API Support
- Enhanced stream transformation capabilities with better error handling
- Added validation for `TransformStream` API availability
- Improved Blob-to-stream conversion with React Native compatibility warnings


### Error Handling
- Better error messages for unsupported APIs
- Specific guidance for React Native users regarding fetch streaming limitations


### AWS Configuration Components
The following AWS SDK configuration modules were removed in favor of the new credential chain system:
- Boolean selector utilities for environment/config parsing
- Dual-stack endpoint configuration options
- FIPS endpoint configuration options
- Various AWS region and endpoint resolution utilities
- Retry strategy implementations (StandardRetryStrategy, AdaptiveRetryStrategy)
- Multiple AWS signing and authentication modules


### HTTP Protocol Components
- HTTP request/response classes and utilities
- Content length middleware
- Host header middleware
- Logger middleware
- Recursion detection middleware


### UUID Generation
- Removed UUID v1, v3, v4, v5 generation utilities
- Removed UUID parsing and validation functions


### Code Organization
- Consolidated credential provider functionality into new chain-based architecture
- Simplified AWS SDK integration with fewer, more focused modules
- Removed redundant tslib helper functions across multiple modules


### Performance
- Reduced bundle size through removal of unused AWS SDK components
- More efficient credential caching and validation

## Migration Notes

- If you were using removed AWS SDK configuration features directly, you'll need to adapt to the new credential chain pattern
- UUID functionality that was removed can be replaced with external UUID libraries if needed
- The new credential chain system provides a more unified approach to managing AWS credentials across different sources

## Bug Fixes

- Improved handling of credential expiration edge cases
- Better error propagation in provider chains
- Fixed potential memory leaks in credential caching
