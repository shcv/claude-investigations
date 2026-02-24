#!/usr/bin/env python3
"""Variant B: Parallel Haiku annotation of change batches using Anthropic API.

Reads batches from archive/claude-code/changes/{version}/batches/
Writes batch-NNN-annotations.json alongside each batch file.

Usage: python3 annotate_changes.py [version]
  e.g.: python3 annotate_changes.py v2.1.48
"""
import asyncio
import json
import re
import sys
from pathlib import Path

from claude_agent_sdk import query, ResultMessage, ClaudeAgentOptions

SEMAPHORE_LIMIT = 4
MODEL = "claude-haiku-4-5-20251001"

ANNOTATION_PROMPT = """\
Analyze these changes to the Claude Code CLI source code and classify each one.
Return a JSON array between <result></result> tags.

CRITICAL — "removed" section semantics: Entries in the "removed" section mean those
specific code bodies had NO close match in the new version. This does NOT mean the
feature was deleted — it may have been reorganized, reimplemented, or renamed such
that the diff tool couldn't match it. Only use change_type="removal" if the code
content clearly indicates a capability is gone: e.g., a CLI flag literal removed,
a tool name constant that disappears, or a user-facing error string no longer present.
When uncertain, prefer change_type="refactor" over "removal".

For each change, output an object with:
- "name": identifier name (use the [name] from the diff header)
- "summary": 1-2 sentence plain-English description of what this change does
- "importance": integer 1-5:
    1 = internal refactoring, no user impact
    2 = minor internal change, unlikely visible to users
    3 = notable improvement or infrastructure indirectly affecting users
    4 = clear new user-facing feature or significant behavior change
    5 = major feature, breaking change, or release-defining capability
- "user_facing": true if change produces visible output, adds CLI flags/options,
    new tools, or changes behavior users observe directly
- "feature_flag": string name if gated by a tengu_* flag — look for calls like
    r8("tengu_foo", !1). Use null if no feature flag.
- "disabled": true ONLY if the flag default is explicitly !1 or false
    (r8("tengu_foo", !1) → disabled=true; r8("tengu_foo", !0) → disabled=false)
- "component": pick the MOST SPECIFIC category that applies:
    - models: model capability fields (supportsAdaptiveThinking, effortLevels),
               model version strings, thinking parameters, pricing
    - sdk: ClaudeAgentOptions fields, query() params, SDK-exposed APIs,
            promptSuggestions — things SDK callers configure
    - tools: built-in tool definitions and their schemas/descriptions
              (Bash, Read, Write, Grep, Glob, AskUserQuestion, Skill, TodoWrite,
               CreateWorktree, ListMcpResources, TaskCreate, TaskUpdate, etc.)
    - hooks: hook event types and handlers (PreToolUse, PostToolUse,
              ConfigChange, TaskCompleted, SubagentStop, HttpHook)
    - git: git integration, worktrees, commits, branches, diffs
    - mcp: Model Context Protocol servers, tool results, auth, resources
    - cli: command-line flags, REPL UI, startup flow, shell integration,
            slash commands, session management
    - auth: authentication, OAuth, API keys, login/logout flows
    - config: settings schemas, CLAUDE.md loading/excludes, policy enforcement
    - agent: agent coordination, task management, teams, background agents
    - shell: shell execution, bash/powershell providers, shell detection
    - transport: WebSocket, HTTP, SSE, network communication
    - telemetry: logging, analytics, event tracking
    - internal: refactoring with no user-visible effect (use as last resort)
- "change_type": new_feature | enhancement | bug_fix | removal | refactor |
    documentation | infrastructure
- "evidence": 1-2 key code fragments supporting your classification

Grouping: combine related sub-functions into one entry when clearly part of one feature.
Structural changes often represent feature wiring — a new field or parameter being passed
through usually enables a specific user-visible capability; identify what that is.
Skip 100%-similarity entries (pure minifier renames with no content change).

Section: {section}
Batch {batch_id} of changes:

{content}
"""


async def annotate_batch(
    batch: dict,
    out_path: Path,
    semaphore: asyncio.Semaphore,
) -> dict | None:
    async with semaphore:
        print(f"  Batch {batch['id']:03d} ({batch['section']}, {batch['count']} items)...")
        prompt = ANNOTATION_PROMPT.format(
            section=batch["section"],
            batch_id=batch["id"],
            content=batch["content"],
        )

        options = ClaudeAgentOptions(
            model=MODEL,
            allowed_tools=[],
            permission_mode="bypassPermissions",
            cwd=str(Path.cwd()),
        )

        try:
            output = ""
            async for msg in query(prompt=prompt, options=options):
                if isinstance(msg, ResultMessage):
                    if msg.is_error:
                        raise RuntimeError(msg.result or "query failed")
                    output = msg.result or ""
        except Exception as e:
            print(f"  Batch {batch['id']:03d}: SDK error: {e}")
            return None

        m = re.search(r"<result>(.*?)</result>", output, re.DOTALL)
        if not m:
            print(f"  Batch {batch['id']:03d}: no <result> tag found")
            # Try to find a JSON array directly
            m2 = re.search(r"\[\s*\{.*\}\s*\]", output, re.DOTALL)
            annotations = json.loads(m2.group(0)) if m2 else []
        else:
            try:
                annotations = json.loads(m.group(1).strip())
            except json.JSONDecodeError as e:
                print(f"  Batch {batch['id']:03d}: JSON parse error: {e}")
                annotations = []

        result = {**batch, "annotations": annotations}
        out_path.write_text(json.dumps(result, indent=2))
        print(f"  Batch {batch['id']:03d}: {len(annotations)} annotations written")
        return result


async def collect_and_filter(
    batches_dir: Path, min_importance: int = 3
) -> list[dict]:
    """Load all annotation files and filter by importance."""
    all_annotations = []
    for ann_file in sorted(batches_dir.glob("batch-*-annotations.json")):
        data = json.loads(ann_file.read_text())
        for ann in data.get("annotations", []):
            ann["_batch_id"] = data["id"]
            ann["_section"] = data["section"]
            all_annotations.append(ann)

    filtered = [a for a in all_annotations if a.get("importance", 0) >= min_importance]
    print(f"\nTotal annotations: {len(all_annotations)}")
    print(f"After filtering (importance >= {min_importance}): {len(filtered)}")
    return filtered


async def main(version: str, batches_dir: Path | None = None):
    if batches_dir is None:
        batches_dir = Path(f"archive/claude-code/changes/{version}/batches")
    if not batches_dir.exists():
        print(f"Error: {batches_dir} not found. Run slice_changes.py first.")
        sys.exit(1)

    batch_files = sorted(
        f for f in batches_dir.glob("batch-*.json")
        if "-annotations" not in f.name
    )
    if not batch_files:
        print("No batch files found.")
        sys.exit(1)

    # Skip already-annotated batches
    to_annotate = []
    skipped = 0
    for f in batch_files:
        out_path = f.parent / (f.stem + "-annotations.json")
        if out_path.exists():
            skipped += 1
            continue
        to_annotate.append((json.loads(f.read_text()), out_path))

    if skipped:
        print(f"Skipping {skipped} already-annotated batches.")
    if not to_annotate:
        print("All batches already annotated.")
    else:
        print(f"Annotating {len(to_annotate)} batches "
              f"(concurrency={SEMAPHORE_LIMIT}, model={MODEL})...")

        semaphore = asyncio.Semaphore(SEMAPHORE_LIMIT)
        tasks = [
            annotate_batch(batch, out_path, semaphore)
            for batch, out_path in to_annotate
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        errors = [r for r in results if isinstance(r, Exception)]
        if errors:
            print(f"Errors encountered: {errors}")
        print(f"Done: {len(results) - len(errors)}/{len(results)} batches annotated.")

    # Collect and filter
    filtered = await collect_and_filter(batches_dir)

    # Write filtered summary alongside the batches dir's parent
    summary_path = batches_dir.parent / f"annotations-{version}.json"
    # For non-default dirs, name the summary after the dir
    if batches_dir.name != "batches":
        summary_path = batches_dir.parent / f"annotations-{version}-{batches_dir.name}.json"
    summary_path.write_text(json.dumps(filtered, indent=2))
    print(f"Filtered annotations written to {summary_path}")

    # Print component breakdown
    from collections import Counter
    comps = Counter(a.get("component", "?") for a in filtered)
    print("\nBy component:")
    for comp, count in comps.most_common():
        print(f"  {comp}: {count}")

    user_facing = [a for a in filtered if a.get("user_facing")]
    print(f"\nUser-facing changes: {len(user_facing)}")
    flagged = [a for a in filtered if a.get("feature_flag")]
    print(f"Feature-flagged: {len(flagged)}")
    disabled = [a for a in filtered if a.get("disabled")]
    print(f"Disabled by default: {len(disabled)}")
    return filtered


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("version", nargs="?", default="v2.1.48")
    p.add_argument("--batches-dir", help="Override default batches directory path")
    args = p.parse_args()
    bd = Path(args.batches_dir) if args.batches_dir else None
    asyncio.run(main(args.version, bd))
