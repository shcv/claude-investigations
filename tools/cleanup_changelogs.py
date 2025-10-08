#!/usr/bin/env python3
"""
Changelog Cleanup Tool

Removes redundant headers and LLM meta-commentary from changelogs.

Pattern to fix:
  # Changelog for version X.X.X

  [LLM commentary about generating changelog]

  # Changelog for version X.X.X  <-- Remove from here up

  ## Actual Content...

Result:
  # Changelog for version X.X.X

  ## Actual Content...
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List, Optional

# ANSI color codes
class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    END = "\033[0m"

    @classmethod
    def disable(cls):
        cls.RED = cls.GREEN = cls.YELLOW = cls.BLUE = cls.CYAN = cls.BOLD = cls.END = ""


def colored(text: str, color: str) -> str:
    return f"{color}{text}{Colors.END}"


def print_success(msg: str):
    print(colored(f"✓ {msg}", Colors.GREEN))


def print_warning(msg: str):
    print(colored(f"⚠ {msg}", Colors.YELLOW))


def print_error(msg: str):
    print(colored(f"✗ {msg}", Colors.RED), file=sys.stderr)


def print_info(msg: str):
    print(colored(f"ℹ {msg}", Colors.CYAN))


def cleanup_changelog(content: str, version: str) -> tuple[str, bool]:
    """
    Clean up changelog by removing duplicate headers and meta-commentary.

    Returns:
        tuple of (cleaned_content, was_modified)
    """
    lines = content.split('\n')

    # Pattern 1: Look for duplicate H1 headers
    # Find all lines that match "# Changelog for version X.X.X"
    h1_pattern = re.compile(r'^#\s+Changelog for version', re.IGNORECASE)
    h1_indices = [i for i, line in enumerate(lines) if h1_pattern.match(line)]

    if len(h1_indices) <= 1:
        # No duplicate headers, check for other issues
        return content, False

    # Find the second H1 header
    first_h1 = h1_indices[0]
    second_h1 = h1_indices[1]

    # Check if there's substantive content between the headers
    # (more than just blank lines or simple commentary)
    between_content = '\n'.join(lines[first_h1 + 1:second_h1]).strip()

    # If the content between is just meta-commentary (typically short),
    # remove everything from after first H1 to before second H1
    if len(between_content) < 500:  # Arbitrary threshold - real content is usually longer
        # Keep first H1, remove up to (but not including) second H1
        cleaned_lines = lines[:first_h1 + 1] + lines[second_h1:]

        # Remove the duplicate second H1 since we kept the first
        cleaned_lines = cleaned_lines[:first_h1 + 1] + cleaned_lines[first_h1 + 2:]

        # Clean up excessive blank lines at the start
        result_lines = []
        blank_count = 0
        for i, line in enumerate(cleaned_lines):
            if i <= first_h1:
                result_lines.append(line)
            elif line.strip() == '':
                blank_count += 1
                if blank_count <= 2:  # Allow max 2 blank lines
                    result_lines.append(line)
            else:
                blank_count = 0
                result_lines.append(line)

        return '\n'.join(result_lines), True

    return content, False


def process_file(file_path: Path, dry_run: bool = False) -> bool:
    """Process a single changelog file."""
    try:
        content = file_path.read_text()
    except Exception as e:
        print_error(f"Could not read {file_path.name}: {e}")
        return False

    # Extract version from filename
    match = re.match(r'changelog-v?(.+)\.md$', file_path.name)
    version = match.group(1) if match else "unknown"

    cleaned_content, was_modified = cleanup_changelog(content, version)

    if not was_modified:
        print_info(f"{file_path.name}: No changes needed")
        return True

    if dry_run:
        print_warning(f"{file_path.name}: Would be modified (dry run)")
        # Show what would change
        orig_lines = len(content.split('\n'))
        new_lines = len(cleaned_content.split('\n'))
        print_info(f"  Lines: {orig_lines} → {new_lines} ({orig_lines - new_lines} removed)")
        return True

    try:
        file_path.write_text(cleaned_content)
        orig_lines = len(content.split('\n'))
        new_lines = len(cleaned_content.split('\n'))
        print_success(f"{file_path.name}: Cleaned ({orig_lines - new_lines} lines removed)")
        return True
    except Exception as e:
        print_error(f"Could not write {file_path.name}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Clean up changelog files by removing redundant headers and meta-commentary"
    )

    parser.add_argument(
        "files",
        nargs="*",
        help="Specific changelog files to process (default: all in archive/changelog/)"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be changed without modifying files"
    )

    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable colored output"
    )

    args = parser.parse_args()

    if args.no_color or not sys.stdout.isatty():
        Colors.disable()

    # Determine files to process
    if args.files:
        files_to_process = [Path(f) for f in args.files]
    else:
        # Find all changelog files
        changelog_dir = Path("archive/changelog")
        if not changelog_dir.exists():
            # Try from project root
            project_root = Path.cwd()
            while project_root != project_root.parent:
                test_dir = project_root / "archive" / "changelog"
                if test_dir.exists():
                    changelog_dir = test_dir
                    break
                project_root = project_root.parent
            else:
                print_error("Could not find archive/changelog directory")
                return 1

        files_to_process = sorted(changelog_dir.glob("changelog-*.md"))

    if not files_to_process:
        print_warning("No changelog files found")
        return 0

    print_info(f"Processing {len(files_to_process)} file(s){'...' if not args.dry_run else ' (dry run)...'}")
    print()

    success_count = 0
    modified_count = 0

    for file_path in files_to_process:
        if not file_path.exists():
            print_error(f"File not found: {file_path}")
            continue

        # Track original content to count modifications
        try:
            original = file_path.read_text()
            if process_file(file_path, args.dry_run):
                success_count += 1
                # Check if actually modified
                if not args.dry_run:
                    current = file_path.read_text()
                    if current != original:
                        modified_count += 1
        except Exception as e:
            print_error(f"Error processing {file_path.name}: {e}")

    print()
    print(colored("=== Summary ===", Colors.BOLD + Colors.BLUE))
    print_success(f"Processed {success_count} of {len(files_to_process)} file(s)")
    if not args.dry_run and modified_count > 0:
        print_success(f"Modified {modified_count} file(s)")

    return 0 if success_count == len(files_to_process) else 1


if __name__ == "__main__":
    sys.exit(main())
