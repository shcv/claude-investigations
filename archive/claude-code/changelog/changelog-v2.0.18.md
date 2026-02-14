# Changelog for version 2.0.18

## Highlights

Version 2.0.18 adds **OpenTelemetry distributed tracing infrastructure** (disabled by default), introduces **settings source restriction** capability for enterprise use cases, and includes a **background task summarization fix** that prevents unnecessary processing.


### OpenTelemetry Tracing Support (Opt-In)

**What:** Comprehensive distributed tracing infrastructure for monitoring Claude Code's internal operations, API calls, and performance metrics. This feature is **disabled by default** and requires explicit opt-in.

**How to use:**
```bash
# Enable telemetry
export CLAUDE_CODE_ENABLE_TELEMETRY=true

# Configure where traces are exported (optional)
export OTEL_TRACES_EXPORTER=console  # or "otlp" for OpenTelemetry collectors

# Privacy controls (optional - both default to redacted)
export OTEL_LOG_USER_PROMPTS=true     # Log user prompts in traces
export OTEL_LOG_MODEL_RESPONSE=true   # Log model responses in traces
```

**Details:**
- Tracks user interactions, LLM API requests/responses, and tool executions
- **Privacy-conscious by default**: User prompts and model responses are redacted unless explicitly enabled via `OTEL_LOG_USER_PROMPTS` and `OTEL_LOG_MODEL_RESPONSE`
- Supports multiple export formats:
  - `console` - Output traces to console for debugging
  - `otlp` - Export to OpenTelemetry Protocol collectors (supports gRPC, HTTP/JSON, HTTP/Protobuf)
- Records detailed metrics: token counts (input, output, cache read, cache creation), latency, success/failure rates
- Full OpenTelemetry specification compliance with 15+ configuration environment variables
- Configurable sampling strategies via `OTEL_TRACES_SAMPLER` (defaults to `parentbased_always_on`)
- Batch span processor with tunable performance parameters
- **Evidence**: `DiB() at line 2314`, `JiB() at line 2048`, `Jb0() at line 2087`, `cL5() at line 2277`

**Supported Environment Variables:**

*Telemetry Control:*
- `CLAUDE_CODE_ENABLE_TELEMETRY` - Master switch (default: disabled)
- `OTEL_LOG_USER_PROMPTS` - Include user prompts in traces (default: redacted)
- `OTEL_LOG_MODEL_RESPONSE` - Include model responses in traces (default: redacted)

*Export Configuration:*
- `OTEL_TRACES_EXPORTER` - Exporters: "console", "otlp" (comma-separated)
- `OTEL_EXPORTER_OTLP_TRACES_PROTOCOL` - Protocol: "grpc", "http/json", "http/protobuf"
- `OTEL_EXPORTER_OTLP_PROTOCOL` - Default protocol for all signals

*Sampling:*
- `OTEL_TRACES_SAMPLER` - Sampler type (default: "parentbased_always_on")
- `OTEL_TRACES_SAMPLER_ARG` - Sampler configuration (e.g., ratio for TraceIdRatioBased)

*Span Limits:*
- `OTEL_ATTRIBUTE_VALUE_LENGTH_LIMIT` - Max attribute value length (unlimited by default)
- `OTEL_ATTRIBUTE_COUNT_LIMIT` - Max attributes per span (default: 128)
- `OTEL_SPAN_ATTRIBUTE_VALUE_LENGTH_LIMIT` - Span-specific attribute value limit
- `OTEL_SPAN_ATTRIBUTE_COUNT_LIMIT` - Span-specific attribute count (default: 128)
- `OTEL_SPAN_LINK_COUNT_LIMIT` - Max links per span (default: 128)
- `OTEL_SPAN_EVENT_COUNT_LIMIT` - Max events per span (default: 128)
- `OTEL_SPAN_ATTRIBUTE_PER_EVENT_COUNT_LIMIT` - Max attributes per event (default: 128)
- `OTEL_SPAN_ATTRIBUTE_PER_LINK_COUNT_LIMIT` - Max attributes per link (default: 128)

*Batch Processor:*
- `OTEL_BSP_MAX_EXPORT_BATCH_SIZE` - Batch size (default: 512)
- `OTEL_BSP_MAX_QUEUE_SIZE` - Queue size (default: 2048)
- `OTEL_BSP_SCHEDULE_DELAY` - Export delay in ms (default: 5000)
- `OTEL_BSP_EXPORT_TIMEOUT` - Timeout in ms (default: 30000)


### Settings Source Restriction

**What:** New capability to restrict which sources can provide settings, useful for enterprise deployments or security-sensitive environments where configuration should only come from approved sources.

**Details:**
- Programmatic API for controlling allowed settings sources
- Likely to be exposed via command-line flags or environment variables in future versions
- **Evidence**: `s0A() at line 3770`


### Background Task Summarization Guard

**What:** Fixed unnecessary processing when background task summarization is disabled.

**Details:**
- Added early-return check to skip summarization logic when the feature is disabled
- Prevents wasted CPU cycles and potential side effects
- Improves performance for users who don't use background task features
- **Evidence**: Check added in `tjQ()` function (formerly `bRQ`)


### Skills Display Enhancement

**What:** Skills now display without the "/" prefix, distinguishing them visually from regular slash commands.

**Details:**
- Regular commands: `/command-name`
- Skills: `The Skill Name` (no "/" prefix)
- Improves UI consistency and helps users understand the difference between commands and skills
- **Evidence**: `JoB() at line 3143` (formerly `pnB`), checks for "The " prefix

## Internal Changes

The following changes have no user-visible impact:

- **Import optimizations**: Consolidated imports for better tree-shaking (e.g., `import { cwd } from "node:process"` instead of importing entire modules)
- **Code organization**: 8000+ function and variable renames for improved code maintainability
- **Debug logging**: Enhanced logging for command processing and message creation (development-only)
- **Shell execution refactoring**: Internal parameter handling improvements
- **Skills infrastructure**: Stub implementations added for upcoming skills feature (currently disabled)
- **Plan editing UI**: Infrastructure added for future plan editing capability (not yet active)
- **Dead code removal**: Removed unused rendering function `HqQ`


**Note for Enterprise Users:** The new telemetry infrastructure provides deep observability into Claude Code's behavior and performance. When enabled, it can help diagnose issues, track API usage patterns, and monitor system health in production deployments. All telemetry respects privacy by default through content redaction controls.
