#!/usr/bin/env python3
"""Generate a changelog from pre-computed Haiku annotations.

Takes the filtered annotations-{version}.json (output of annotate_changes.py)
and uses a Sonnet agent to generate the final changelog.

Usage: python3 generate_annotated_changelog.py [version] [--min-importance N]
  e.g.: python3 generate_annotated_changelog.py v2.1.48
"""
import asyncio
import json
import sys
from collections import defaultdict
from pathlib import Path

from claude_agent_sdk import query, ResultMessage, ClaudeAgentOptions

MIN_IMPORTANCE = 2
MODEL = "claude-sonnet-4-6"

SYSTEM_PROMPT_PATH = Path("archive/claude-code/changelog/system-prompt.md")


def format_annotations_for_prompt(annotations: list[dict], version: str) -> str:
    """Format annotations compactly, tiered by importance.

    Format per line:
      [component/change_type] IMP name: summary (evidence)
    Flags and disabled status are appended inline.
    """
    # Tier 1: importance 4-5
    tier1 = sorted(
        [a for a in annotations if a.get("importance", 0) >= 4],
        key=lambda a: (-a.get("importance", 0), not a.get("user_facing", False))
    )
    # Tier 2: importance 3
    tier2 = sorted(
        [a for a in annotations if a.get("importance", 0) == 3],
        key=lambda a: (not a.get("user_facing", False), a.get("component", ""))
    )
    # Tier 3: importance 1-2
    tier3 = sorted(
        [a for a in annotations if a.get("importance", 0) <= 2],
        key=lambda a: a.get("component", "")
    )

    def fmt(ann: dict) -> str:
        comp = ann.get("component", "?")
        ct = ann.get("change_type", "?")[:8]
        imp = ann.get("importance", "?")
        name = ann.get("name", "?")
        summary = ann.get("summary", "")
        evidence = ann.get("evidence", "") or ""
        if isinstance(evidence, list):
            evidence = "; ".join(str(e) for e in evidence)
        uf = "★" if ann.get("user_facing") else " "
        flag = ann.get("feature_flag", "")
        dis = ann.get("disabled", False)
        flag_str = f" [{flag}{'!disabled' if dis else ''}]" if flag else ""
        # Truncate for compactness
        ev_short = evidence[:60].split("\n")[0] if evidence else ""
        sum_short = summary[:80]
        return f"  [{comp}/{ct}]{uf}i={imp} {name}: {sum_short} | {ev_short}{flag_str}"

    lines = [
        f"# Pre-analyzed Changes for {version}",
        f"# Total: {len(annotations)} entries across 3 tiers",
        "#",
        "# Format: [component/type]★=user-facing i=importance | evidence [FLAG if gated]",
        "# Tiers: HIGH=4-5 (lead features), NOTABLE=3 (improvements), LOW=1-2 (internal)",
        "#",
        "# INSTRUCTIONS:",
        "# - HIGH items: include all user-facing (★) ones; summarize patterns for non-★",
        "# - NOTABLE: include if clearly user-visible, skip pure infrastructure",
        "# - LOW: use for context only; mention patterns (e.g. 'several internal refactors')",
        "# - feature_flag items: if disabled, put in 'In Development' section",
        "# - For removal/refactor items: the feature may still exist (reorganized code)",
        "#   Only call it a removal if it makes sense from the user's perspective",
        "",
        f"## HIGH IMPORTANCE (i=4-5, {len(tier1)} items)",
    ]
    for ann in tier1:
        lines.append(fmt(ann))

    lines.append("")
    lines.append(f"## NOTABLE (i=3, {len(tier2)} items)")
    for ann in tier2:
        lines.append(fmt(ann))

    lines.append("")
    lines.append(f"## LOW / INTERNAL (i=1-2, {len(tier3)} items — use for context)")
    for ann in tier3:
        lines.append(fmt(ann))

    return "\n".join(lines)


async def generate(version: str, min_importance: int = MIN_IMPORTANCE):
    changes_dir = Path(f"archive/claude-code/changes/{version}")
    annotations_file = changes_dir / f"annotations-{version}.json"
    changelog_dir = Path("archive/claude-code/changelog")
    output_file = changelog_dir / f"changelog-{version}-annotated.md"

    if not annotations_file.exists():
        print(f"Error: {annotations_file} not found. Run annotate_changes.py first.")
        sys.exit(1)

    annotations = json.loads(annotations_file.read_text())
    filtered = [a for a in annotations if a.get("importance", 0) >= min_importance]
    print(f"Loaded {len(annotations)} annotations, {len(filtered)} at importance >= {min_importance}")

    system_prompt = SYSTEM_PROMPT_PATH.read_text() if SYSTEM_PROMPT_PATH.exists() else ""

    user_prompt = f"""Generate a changelog for Claude Code {version}.

{format_annotations_for_prompt(filtered, version)}

Generate the changelog following the standard format from the system prompt.
You do NOT need to read source files — the pre-analyzed changes above are your primary input.
However, you may read the prettified source file (pretty/pretty-{version}.js) if you want to
verify specific details or find additional context for important changes.
"""

    print(f"\nGenerating annotated changelog for {version}...")
    options = ClaudeAgentOptions(
        system_prompt=system_prompt,
        allowed_tools=["Read"],  # Allow reading source for verification only
        permission_mode="bypassPermissions",
        cwd=str(Path("archive/claude-code").resolve()),
    )

    result = ""
    async for msg in query(prompt=user_prompt, options=options):
        if isinstance(msg, ResultMessage):
            if msg.is_error:
                raise RuntimeError(msg.result or "query failed")
            result = msg.result or ""

    output_file.write_text(f"# Changelog for version {version}\n\n{result}")
    print(f"Written to {output_file}")


if __name__ == "__main__":
    version = sys.argv[1] if len(sys.argv) > 1 else "v2.1.48"
    min_imp = int(sys.argv[2]) if len(sys.argv) > 2 else MIN_IMPORTANCE
    asyncio.run(generate(version, min_imp))
