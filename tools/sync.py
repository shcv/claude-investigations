#!/usr/bin/env python3
"""
Claude Code Archive Sync Tool (Python Implementation)

This script automates the process of downloading, organizing, and optionally
processing all available versions of the @anthropic-ai/claude-code package
from the npm registry.

Architecture:
- Phase 1: Download missing versions from npm registry
- Phase 2: Prettify downloaded files using prettier (optional)
- Phase 3: Generate diffs between consecutive versions (optional)
- Phase 4: Generate changelogs using Claude SDK (optional)
"""

import argparse
import json
import os
import re
import shutil
import sys
import tarfile
import tempfile
from pathlib import Path
from subprocess import run, PIPE, DEVNULL
from typing import List, Set, Optional, Tuple
import requests
from packaging import version

# Try to import Claude SDK
try:
    from claude import Claude

    CLAUDE_SDK_AVAILABLE = True
except ImportError:
    CLAUDE_SDK_AVAILABLE = False


# ANSI color codes for output
class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    END = "\033[0m"

    @classmethod
    def disable(cls):
        """Disable colors for non-TTY output"""
        cls.RED = cls.GREEN = cls.YELLOW = cls.BLUE = cls.PURPLE = cls.CYAN = (
            cls.BOLD
        ) = cls.END = ""


def colored(text: str, color: str) -> str:
    """Apply color to text"""
    return f"{color}{text}{Colors.END}"


def print_header(title: str):
    """Print a colored section header"""
    print(f"\n{colored('=== ' + title + ' ===', Colors.BOLD + Colors.BLUE)}")


def print_success(message: str):
    """Print a green success message"""
    print(colored(f"✓ {message}", Colors.GREEN))


def print_warning(message: str):
    """Print a yellow warning message"""
    print(colored(f"⚠ Warning: {message}", Colors.YELLOW))


def print_error(message: str):
    """Print a red error message"""
    print(colored(f"✗ Error: {message}", Colors.RED), file=sys.stderr)


def print_info(message: str):
    """Print a cyan info message"""
    print(colored(message, Colors.CYAN))


class SyncStats:
    """Track sync operation statistics"""

    def __init__(self):
        self.total_versions = 0
        self.downloaded_count = 0
        self.prettified_count = 0
        self.diff_generated_count = 0
        self.changelog_generated_count = 0
        self.download_failures = 0
        self.prettier_failures = 0
        self.diff_generation_failures = 0
        self.changelog_generation_failures = 0
        self.changes_generated_count = 0
        self.changes_generation_failures = 0


class ClaudeCodeSync:
    """Main sync tool implementation"""

    NPM_PACKAGE = "@anthropic-ai/claude-code"

    # Default changelog system prompt
    DEFAULT_CHANGELOG_PROMPT = """Give me a changelog based on the diff provided in the prompt. Return only the changelog contents. Be detailed and clear in your explanations. Investigate the newer file as needed. Focus on and prioritize user-facing (interactive and cli argument) features. If there is a new command, argument, flag, or other user-facing feature, give explanations and examples for how a user could use it. Note that this is an interactive CLI application, not a library; user's won't interact with the code directly, so present usage from the perspective of an interaction or command-line arguments, not function calls. If you want to explain the code, reproduce the relevant snippet with semantic names."""

    # Default changes system prompt
    DEFAULT_CHANGES_PROMPT = """You are analyzing a code diff to make it more understandable. Your task is to process one specific change from the diff.

## Your Task

Given a specific change (addition, removal, or modification), you should:

1. **Preserve the exact function names and line numbers** where the change occurred
2. **Rewrite the changed code using meaningful variable and parameter names** instead of minified names
3. **Match related additions and removals** that should be grouped together (e.g., a function being moved or renamed)
4. **Classify if this change is unimportant** (e.g., whitespace, formatting, build artifacts)

## Output Format

Return a JSON object with this structure:

```json
{
  "location": "functionName() at line 123",
  "type": "addition|removal|modification|move",
  "original": "original minified code snippet",
  "rewritten": "code with meaningful names",
  "related_changes": ["line numbers of related changes"],
  "importance": "high|medium|low|trivial",
  "reason": "brief explanation if marked as low importance or trivial"
}
```

## Guidelines

- Focus on making the change understandable, not on classifying the kind of change
- Use descriptive names that explain what the code does
- Keep the output concise but informative
- Group related changes (e.g., function moved to different location)
- Mark build artifacts, whitespace changes, or auto-generated code as trivial"""

    def __init__(
        self,
        base_dir: Path,
        prettier: bool = False,
        diff: bool = False,
        changelog: bool = False,
        changes: bool = False,
        latest: bool = False,
        since: Optional[str] = None,
        new_first: bool = False,
        redo: Optional[str] = None,
    ):
        self.base_dir = base_dir
        self.prettier = prettier
        self.diff = diff
        self.changelog = changelog
        self.changes = changes
        self.latest = latest
        self.since = since
        self.new_first = new_first
        self.redo = redo

        # Directory structure
        self.archive_dir = base_dir / "archive"
        self.original_dir = self.archive_dir / "original"
        self.pretty_dir = self.archive_dir / "pretty"
        self.diff_dir = self.archive_dir / "diff"
        self.changelog_dir = self.archive_dir / "changelog"
        self.changes_dir = self.archive_dir / "changes"
        self.temp_dir = base_dir / ".sync-temp"

        self.stats = SyncStats()

    def setup_directories(self):
        """Create required directories"""
        directories = [self.archive_dir, self.original_dir]

        if self.prettier:
            directories.append(self.pretty_dir)

        if self.diff:
            directories.append(self.diff_dir)

        if self.changelog:
            directories.append(self.changelog_dir)

        if self.changes:
            directories.append(self.changes_dir)

        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)

        # Create temp directory
        self.temp_dir.mkdir(exist_ok=True)

    def check_dependencies(self):
        """Check for required system dependencies"""
        # Check prettier if needed
        if self.prettier:
            print_info("Checking prettier command...")
            result = run(["which", "prettier"], capture_output=True)
            if result.returncode != 0:
                print_error("'prettier' command not found in PATH")
                print_error(
                    "Please ensure the prettier tool is installed and available"
                )
                sys.exit(1)

    def get_npm_versions(self) -> List[str]:
        """Get all available versions from npm registry, sorted oldest first by default"""
        print_info(f"Fetching all available versions of {self.NPM_PACKAGE}...")

        try:
            result = run(
                ["npm", "view", self.NPM_PACKAGE, "versions", "--json"],
                capture_output=True,
                text=True,
                check=True,
            )

            versions = json.loads(result.stdout)
            if isinstance(versions, str):
                versions = [versions]  # Handle single version case

            # Sort versions (oldest first by default, newest first if --new-first)
            sorted_versions = sorted(
                versions, key=version.parse, reverse=self.new_first
            )
            self.stats.total_versions = len(sorted_versions)

            # Filter versions if --since is specified
            if self.since:
                since_version = self.since.lstrip("v")  # Remove 'v' prefix if present
                try:
                    since_parsed = version.parse(since_version)
                    filtered_versions = []
                    for v in sorted_versions:
                        v_clean = v.lstrip("v")
                        if version.parse(v_clean) >= since_parsed:
                            filtered_versions.append(v)

                    print_info(
                        f"Filtered to {len(filtered_versions)} versions since {self.since}"
                    )
                    return filtered_versions
                except Exception as e:
                    print_warning(f"Invalid --since version '{self.since}': {e}")
                    print_info("Processing all versions...")

            return sorted_versions

        except Exception as e:
            print_error(f"Failed to fetch versions from npm: {e}")
            sys.exit(1)

    def get_existing_originals(self) -> Set[str]:
        """Get set of versions that already exist in original directory"""
        existing = set()

        for file_path in self.original_dir.glob("cli-v*.js"):
            # Extract version from filename: cli-v1.0.63.js -> 1.0.63
            match = re.match(r"cli-v([0-9.]+)\.js$", file_path.name)
            if match:
                existing.add(match.group(1))

        return existing

    def download_version(self, version_str: str) -> bool:
        """Download a specific version from npm. Returns True on success."""
        print(f"\n--- Downloading version {version_str} ---")

        try:
            # Get tarball URL
            print_info(f"Fetching tarball URL for version {version_str}...")
            result = run(
                ["npm", "view", f"{self.NPM_PACKAGE}@{version_str}", "dist.tarball"],
                capture_output=True,
                text=True,
                check=True,
            )

            tarball_url = result.stdout.strip()
            if not tarball_url:
                print_warning(f"Could not get tarball URL for version {version_str}")
                return False

            # Download tarball
            print_info(f"Downloading {tarball_url}...")
            response = requests.get(tarball_url, stream=True)
            response.raise_for_status()

            tgz_file = self.temp_dir / f"claude-code-{version_str}.tgz"
            with open(tgz_file, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            # Extract CLI file
            print_info("Extracting CLI file...")
            cli_file = None

            with tarfile.open(tgz_file, "r:gz") as tar:
                # Try to extract cli.js first, then cli.mjs
                for filename in ["package/cli.js", "package/cli.mjs"]:
                    try:
                        member = tar.getmember(filename)
                        tar.extract(member, self.temp_dir)
                        cli_file = self.temp_dir / filename
                        break
                    except KeyError:
                        continue

            if not cli_file or not cli_file.exists():
                print_warning(f"No CLI file found in tarball for version {version_str}")
                tgz_file.unlink(missing_ok=True)
                return False

            # Save original file
            original_file = self.original_dir / f"cli-v{version_str}.js"
            print_info(f"Saving original file: cli-v{version_str}.js")
            shutil.copy2(cli_file, original_file)

            # Clean up temp files
            tgz_file.unlink(missing_ok=True)
            shutil.rmtree(self.temp_dir / "package", ignore_errors=True)

            print_success(f"Downloaded version {version_str}")
            return True

        except Exception as e:
            print_warning(f"Failed to download version {version_str}: {e}")
            return False

    def phase_1_download_originals(self, all_versions: List[str]):
        """Phase 1: Download missing original files"""
        print_header("Phase 1: Downloading Original Files")

        if self.latest:
            # For --latest, only process the most recent version
            if not all_versions:
                print_warning("No versions available to download.")
                return

            latest_version = all_versions[-1] if not self.new_first else all_versions[0]  # Get appropriate latest version
            print_info(f"Processing latest version only: {latest_version}")

            # Also download the previous version for diff generation
            if self.diff and len(all_versions) > 1:
                versions_to_check = [latest_version, all_versions[1]]
                print_info(
                    f"Also checking previous version for diff: {all_versions[1]}"
                )
            else:
                versions_to_check = [latest_version]

            existing_originals = self.get_existing_originals()
            missing_versions = [
                v for v in versions_to_check if v not in existing_originals
            ]
        else:
            # Normal behavior: check all versions
            print_info("Checking for missing original files...")
            existing_originals = self.get_existing_originals()
            missing_versions = [v for v in all_versions if v not in existing_originals]

        if not missing_versions:
            print_info("All required original files are present.")
            return

        print_info(f"Missing original versions: {', '.join(missing_versions)}")
        print_info("Downloading missing versions...")

        for version_str in missing_versions:
            if self.download_version(version_str):
                self.stats.downloaded_count += 1
            else:
                self.stats.download_failures += 1

        print_info(f"\nDownloaded {self.stats.downloaded_count} new files.")
        if self.stats.download_failures > 0:
            print_warning(f"{self.stats.download_failures} downloads failed.")

    def get_files_to_prettify(self) -> List[Path]:
        """Get list of original files that need prettification"""
        files_to_prettify = []

        # Get all original files sorted by version (oldest first by default, newest first if --new-first)
        original_files = list(self.original_dir.glob("cli-v*.js"))
        original_files.sort(
            key=lambda p: version.parse(
                re.match(r"cli-v([0-9.]+)\.js$", p.name).group(1)
            ),
            reverse=self.new_first,
        )

        if self.latest and original_files:
            # For --latest, only check the most recent version
            files_to_check = [original_files[0]]
            # Also check previous version for diff
            if self.diff and len(original_files) > 1:
                files_to_check.append(original_files[1])
        else:
            files_to_check = original_files

        for original_file in files_to_check:
            # Extract version from filename
            match = re.match(r"cli-v([0-9.]+)\.js$", original_file.name)
            if not match:
                continue

            version_str = match.group(1)

            # Filter by --since if specified
            if self.since:
                since_version = self.since.lstrip("v")
                try:
                    if version.parse(version_str) < version.parse(since_version):
                        continue
                except Exception:
                    pass  # If version parsing fails, include the file

            pretty_file = self.pretty_dir / f"pretty-v{version_str}.js"

            # Check if pretty version already exists
            if not pretty_file.exists():
                files_to_prettify.append(original_file)

        return files_to_prettify

    def prettify_file(self, original_file: Path) -> bool:
        """Prettify a single file. Returns True on success."""
        # Extract version from filename
        match = re.match(r"cli-v([0-9.]+)\.js$", original_file.name)
        if not match:
            return False

        version_str = match.group(1)
        pretty_file = self.pretty_dir / f"pretty-v{version_str}.js"

        print(f"\n--- Prettifying version {version_str} ---")

        try:
            # Run prettier with babel parser and custom ignore-path to handle gitignored files
            result = run(
                [
                    "prettier",
                    "--ignore-path",
                    ".prettierignore",
                    "--parser",
                    "babel",
                    str(original_file),
                ],
                capture_output=True,
                text=True,
                check=True,
            )

            # Write output to pretty file
            with open(pretty_file, "w", encoding="utf-8") as f:
                f.write(result.stdout)

            # Check if prettier succeeded (non-empty output)
            if pretty_file.stat().st_size == 0:
                print_warning(
                    f"prettier produced empty output for version {version_str}"
                )
                pretty_file.unlink(missing_ok=True)
                return False

            print_success(f"Prettified version {version_str}")

            # Update CLAUDE.md with the current version
            self.update_claude_md(version_str)

            return True

        except Exception as e:
            print_warning(f"prettier failed for version {version_str}: {e}")
            pretty_file.unlink(missing_ok=True)
            return False

    def phase_2_prettify_files(self):
        """Phase 2: Prettify files if requested"""
        if not self.prettier:
            return

        print_header("Phase 2: Prettifying Files")
        print_info("Checking for files to prettify...")

        files_to_prettify = self.get_files_to_prettify()

        if not files_to_prettify:
            print_info("All files already prettified.")
            return

        order_desc = "newest first" if self.new_first else "oldest first"
        print_info(
            f"Found {len(files_to_prettify)} files to prettify (processing {order_desc})"
        )

        for original_file in files_to_prettify:
            if self.prettify_file(original_file):
                self.stats.prettified_count += 1
            else:
                self.stats.prettier_failures += 1

        print_info(f"\nPrettified {self.stats.prettified_count} new files.")
        if self.stats.prettier_failures > 0:
            print_warning(f"{self.stats.prettier_failures} prettifications failed.")

    def get_files_to_diff(self) -> List[Tuple[Path, Path]]:
        """Get list of consecutive version pairs that need diffs generated"""
        files_to_diff = []

        # Get all pretty files sorted by version (oldest first for pairing)
        pretty_files = list(self.pretty_dir.glob("pretty-v*.js"))
        if len(pretty_files) < 2:
            return files_to_diff

        # Sort by version (oldest first)
        pretty_files.sort(
            key=lambda p: version.parse(
                re.match(r"pretty-v([0-9.]+)\.js$", p.name).group(1)
            )
        )

        if self.latest:
            # For --latest, only diff the most recent pair
            if len(pretty_files) >= 2:
                older_file = pretty_files[-2]
                newer_file = pretty_files[-1]

                newer_match = re.match(r"pretty-v([0-9.]+)\.js$", newer_file.name)
                if newer_match:
                    newer_version = newer_match.group(1)
                    diff_file = self.diff_dir / f"v{newer_version}.diff"

                    if not diff_file.exists():
                        files_to_diff.append((older_file, newer_file))
        else:
            # Create pairs of consecutive versions
            for i in range(len(pretty_files) - 1):
                older_file = pretty_files[i]
                newer_file = pretty_files[i + 1]

                # Extract versions
                older_match = re.match(r"pretty-v([0-9.]+)\.js$", older_file.name)
                newer_match = re.match(r"pretty-v([0-9.]+)\.js$", newer_file.name)

                if not older_match or not newer_match:
                    continue

                newer_version = newer_match.group(1)

                # Filter by --since if specified (check newer version)
                if self.since:
                    since_version = self.since.lstrip("v")
                    try:
                        if version.parse(newer_version) < version.parse(since_version):
                            continue
                    except Exception:
                        pass  # If version parsing fails, include the file

                diff_file = self.diff_dir / f"v{newer_version}.diff"

                # Check if diff already exists
                if not diff_file.exists():
                    files_to_diff.append((older_file, newer_file))

            # Reverse to process newest first (when --new-first is specified)
            if self.new_first:
                files_to_diff.reverse()

        return files_to_diff

    def generate_diff(
        self, older_file: Path, newer_file: Path, iteration: int = 1
    ) -> bool:
        """Generate diff between two consecutive versions. Returns True on success."""
        # Extract version from newer file
        match = re.match(r"pretty-v([0-9.]+)\.js$", newer_file.name)
        if not match:
            return False

        newer_version = match.group(1)

        # Extract version from older file
        older_match = re.match(r"pretty-v([0-9.]+)\.js$", older_file.name)
        if not older_match:
            return False

        older_version = older_match.group(1)

        # Add iteration suffix if > 1
        if iteration > 1:
            diff_file = self.diff_dir / f"v{newer_version}-{iteration}.diff"
        else:
            diff_file = self.diff_dir / f"v{newer_version}.diff"

        print(f"\n--- Generating diff: v{older_version} -> v{newer_version} ---")

        try:
            # Check if astdiff is available
            astdiff_result = run(["which", "astdiff"], capture_output=True)
            use_astdiff = astdiff_result.returncode == 0

            if use_astdiff:
                # Use astdiff for better JavaScript-aware diffing
                result = run(
                    ["astdiff", str(older_file), str(newer_file)],
                    capture_output=True,
                    text=True,
                )
            else:
                # Fall back to regular diff
                result = run(
                    ["diff", "-u", str(older_file), str(newer_file)],
                    capture_output=True,
                    text=True,
                )

            # Write diff output (even if empty - that means no changes)
            with open(diff_file, "w", encoding="utf-8") as f:
                if result.stdout:
                    f.write(result.stdout)
                else:
                    f.write(
                        f"No changes between v{older_version} and v{newer_version}\n"
                    )

            print_success(f"Generated diff for v{newer_version}")
            return True

        except Exception as e:
            print_warning(f"Diff generation failed for v{newer_version}: {e}")
            diff_file.unlink(missing_ok=True)
            return False

    def phase_3_generate_diffs(self):
        """Phase 3: Generate diffs between consecutive versions"""
        if not self.diff:
            return

        print_header("Phase 3: Generating Diffs")
        print_info("Checking for diffs to generate...")

        files_to_diff = self.get_files_to_diff()

        if not files_to_diff:
            print_info("All diffs already generated.")
            return

        order_desc = "newest first" if self.new_first else "oldest first"
        print_info(
            f"Found {len(files_to_diff)} diffs to generate (processing {order_desc})"
        )

        for older_file, newer_file in files_to_diff:
            if self.generate_diff(older_file, newer_file):
                self.stats.diff_generated_count += 1
            else:
                self.stats.diff_generation_failures += 1

        print_info(f"\nGenerated {self.stats.diff_generated_count} new diffs.")
        if self.stats.diff_generation_failures > 0:
            print_warning(
                f"{self.stats.diff_generation_failures} diff generations failed."
            )

    def get_versions_to_changelog(self) -> List[str]:
        """Get list of versions that need changelogs generated"""
        versions_to_changelog = []

        # Get all diff files
        diff_files = list(self.diff_dir.glob("v*.diff"))

        if self.latest and diff_files:
            # For --latest, only check the most recent diff
            # Filter out files that don't match our pattern first
            valid_diff_files = []
            for f in diff_files:
                if re.match(r"v([0-9.]+)(?:-\d+)?\.diff$", f.name):
                    valid_diff_files.append(f)

            if valid_diff_files:
                valid_diff_files.sort(
                    key=lambda p: version.parse(
                        re.match(r"v([0-9.]+)(?:-\d+)?\.diff$", p.name).group(1)
                    ),
                    reverse=True,
                )  # Always get the latest for --latest flag
                diff_files = [valid_diff_files[0]]
            else:
                diff_files = []

        for diff_file in diff_files:
            # Extract version from filename (handle both v1.0.69.diff and v1.0.69-2.diff)
            match = re.match(r"v([0-9.]+)(?:-\d+)?\.diff$", diff_file.name)
            if not match:
                continue

            version_str = match.group(1)

            # Filter by --since if specified
            if self.since:
                since_version = self.since.lstrip("v")
                try:
                    if version.parse(version_str) < version.parse(since_version):
                        continue
                except Exception:
                    pass  # If version parsing fails, include the file

            changelog_file = self.changelog_dir / f"changelog-v{version_str}.md"

            # Check if changelog already exists
            if not changelog_file.exists():
                versions_to_changelog.append(version_str)

        # Sort by version (oldest first by default, newest first if --new-first)
        versions_to_changelog.sort(key=version.parse, reverse=self.new_first)

        return versions_to_changelog

    def generate_changelog(self, version_str: str, iteration: int = 1) -> bool:
        """Generate changelog for a specific version. Returns True on success."""
        # Use the appropriate diff file based on iteration
        if iteration > 1:
            diff_file = self.diff_dir / f"v{version_str}-{iteration}.diff"
            # If the iteration-specific diff doesn't exist, fall back to the original
            if not diff_file.exists():
                diff_file = self.diff_dir / f"v{version_str}.diff"
        else:
            diff_file = self.diff_dir / f"v{version_str}.diff"

        # Add iteration suffix to changelog if > 1
        if iteration > 1:
            changelog_file = (
                self.changelog_dir / f"changelog-v{version_str}-{iteration}.md"
            )
        else:
            changelog_file = self.changelog_dir / f"changelog-v{version_str}.md"

        print(f"\n--- Generating changelog for version {version_str} ---")

        if not diff_file.exists():
            print_warning(
                f"Diff file not found for version {version_str}. Run with --diff to generate diffs first."
            )
            return False

        try:
            # Read the diff
            with open(diff_file, "r", encoding="utf-8") as f:
                diff_content = f.read()

            # Ensure system prompt file exists and read it
            self.ensure_changelog_prompt()
            system_prompt_file = self.changelog_dir / "system-prompt.md"
            with open(system_prompt_file, "r", encoding="utf-8") as f:
                system_prompt = f.read()

            # Use Claude SDK to generate changelog
            if CLAUDE_SDK_AVAILABLE:
                claude = Claude()

                # Prepare the prompt
                prompt = f"Generate a changelog for version {version_str} based on this diff:\n\n{diff_content}"

                # Generate changelog
                response = claude.completions.create(
                    prompt=prompt,
                    system=system_prompt,
                    max_tokens_to_sample=4000,
                    model="sonnet",
                )

                changelog_content = response.completion
            else:
                # Fallback: use claude CLI if available
                claude_result = run(["which", "claude"], capture_output=True)
                if claude_result.returncode == 0:
                    try:
                        # Use claude CLI with --system-prompt and file reference
                        prompt = f"Generate a changelog for version {version_str} based on this diff: @{diff_file}"

                        result = run(
                            [
                                "claude",
                                "--print",
                                "--system-prompt",
                                system_prompt,
                                prompt,
                            ],
                            capture_output=True,
                            text=True,
                        )

                        if result.returncode == 0:
                            changelog_content = result.stdout
                        else:
                            print_warning(f"Claude CLI failed: {result.stderr}")
                            return False
                    except Exception as e:
                        print_warning(f"Claude CLI execution failed: {e}")
                        return False
                else:
                    print_warning("Neither Claude SDK nor claude CLI is available")
                    return False

            # Write changelog
            with open(changelog_file, "w", encoding="utf-8") as f:
                f.write(f"# Changelog for version {version_str}\n\n")
                f.write(changelog_content)

            print_success(f"Generated changelog for v{version_str}")
            return True

        except Exception as e:
            print_warning(f"Changelog generation failed for v{version_str}: {e}")
            changelog_file.unlink(missing_ok=True)
            return False

    def phase_4_generate_changelogs(self):
        """Phase 4: Generate changelogs using Claude SDK"""
        if not self.changelog:
            return

        print_header("Phase 4: Generating Changelogs")

        # Ensure the system prompt file exists
        self.ensure_changelog_prompt()

        # Check if Claude is available
        if not CLAUDE_SDK_AVAILABLE:
            # Check for claude CLI as fallback
            claude_result = run(["which", "claude"], capture_output=True)
            if claude_result.returncode != 0:
                print_warning(
                    "Claude SDK not installed and claude CLI not found. Skipping changelog generation."
                )
                print_info(
                    "Install with: pip install claude-sdk or ensure claude CLI is in PATH"
                )
                return

        print_info("Checking for changelogs to generate...")

        versions_to_changelog = self.get_versions_to_changelog()

        if not versions_to_changelog:
            print_info("All changelogs already generated.")
            return

        order_desc = "newest first" if self.new_first else "oldest first"
        print_info(
            f"Found {len(versions_to_changelog)} changelogs to generate (processing {order_desc})"
        )

        for version_str in versions_to_changelog:
            if self.generate_changelog(version_str):
                self.stats.changelog_generated_count += 1
            else:
                self.stats.changelog_generation_failures += 1

        print_info(
            f"\nGenerated {self.stats.changelog_generated_count} new changelogs."
        )
        if self.stats.changelog_generation_failures > 0:
            print_warning(
                f"{self.stats.changelog_generation_failures} changelog generations failed."
            )

    def get_versions_to_changes(self) -> List[str]:
        """Get list of versions that need changes files generated"""
        versions_to_changes = []

        # Get all diff files
        diff_files = list(self.diff_dir.glob("v*.diff"))

        if self.latest and diff_files:
            # For --latest, only check the most recent diff
            # Filter out files that don't match our pattern first
            valid_diff_files = []
            for f in diff_files:
                if re.match(r"v([0-9.]+)(?:-\d+)?\.diff$", f.name):
                    valid_diff_files.append(f)

            if valid_diff_files:
                valid_diff_files.sort(
                    key=lambda p: version.parse(
                        re.match(r"v([0-9.]+)(?:-\d+)?\.diff$", p.name).group(1)
                    ),
                    reverse=True,
                )
                diff_files = [valid_diff_files[0]]
            else:
                diff_files = []

        for diff_file in diff_files:
            # Extract version from filename (handle both v1.0.69.diff and v1.0.69-2.diff)
            match = re.match(r"v([0-9.]+)(?:-\d+)?\.diff$", diff_file.name)
            if not match:
                continue

            version_str = match.group(1)

            # Filter by --since if specified
            if self.since:
                since_version = self.since.lstrip("v")
                try:
                    if version.parse(version_str) < version.parse(since_version):
                        continue
                except Exception:
                    pass

            changes_file = self.changes_dir / f"changes-v{version_str}.diff"

            # Check if changes file already exists
            if not changes_file.exists():
                versions_to_changes.append(version_str)

        # Sort by version
        versions_to_changes.sort(key=version.parse, reverse=self.new_first)

        return versions_to_changes

    def generate_changes(self, version_str: str, iteration: int = 1) -> bool:
        """Generate changes file for a specific version. Returns True on success."""
        # Use the appropriate diff file based on iteration
        if iteration > 1:
            diff_file = self.diff_dir / f"v{version_str}-{iteration}.diff"
            if not diff_file.exists():
                diff_file = self.diff_dir / f"v{version_str}.diff"
        else:
            diff_file = self.diff_dir / f"v{version_str}.diff"

        # Add iteration suffix to changes file if > 1
        if iteration > 1:
            changes_file = self.changes_dir / f"changes-v{version_str}-{iteration}.diff"
        else:
            changes_file = self.changes_dir / f"changes-v{version_str}.diff"

        print(f"\n--- Generating changes for version {version_str} ---")

        if not diff_file.exists():
            print_warning(
                f"Diff file not found for version {version_str}. Run with --diff to generate diffs first."
            )
            return False

        try:
            # Read the diff
            with open(diff_file, "r", encoding="utf-8") as f:
                diff_content = f.read()

            # Parse the diff to extract individual changes
            changes = self.parse_diff_changes(diff_content)

            if not changes:
                print_warning(f"No changes found in diff for v{version_str}")
                return False

            # Ensure system prompt file exists and read it
            self.ensure_changes_prompt()
            system_prompt_file = self.changes_dir / "changes-prompt.md"
            with open(system_prompt_file, "r", encoding="utf-8") as f:
                system_prompt = f.read()

            processed_changes = []
            print_info(f"Processing {len(changes)} changes with Sonnet...")

            # Process each change with Sonnet
            for i, change in enumerate(changes, 1):
                print(f"  Processing change {i}/{len(changes)}...", end="\r")

                # Use claude CLI with Sonnet model for each change
                claude_result = run(["which", "claude"], capture_output=True)
                if claude_result.returncode == 0:
                    try:
                        prompt = (
                            f"Analyze this specific change from the diff:\n\n{change}"
                        )

                        # Use Sonnet for better structured output following the prompt
                        result = run(
                            [
                                "claude",
                                "--print",
                                "--model",
                                "sonnet",
                                "--system-prompt",
                                system_prompt,
                                prompt,
                            ],
                            capture_output=True,
                            text=True,
                            timeout=60,  # Increased timeout to 60 seconds
                        )

                        if result.returncode == 0:
                            processed_changes.append(result.stdout)
                        else:
                            processed_changes.append(
                                f"# Failed to process change:\n{change}"
                            )
                    except Exception as e:
                        processed_changes.append(
                            f"# Error processing change: {e}\n{change}"
                        )
                else:
                    print_warning("Claude CLI not available for processing changes")
                    return False

            print()  # Clear the progress line

            # Combine all processed changes
            changes_content = f"# Changes for version {version_str}\n\n"
            changes_content += "## Processed Changes\n\n"
            changes_content += "\n---\n\n".join(processed_changes)

            # Add a section for unimportant changes
            changes_content += "\n\n## Unimportant Changes\n\n"
            changes_content += (
                "Changes marked as trivial or low importance are moved here.\n"
            )

            # Write changes file
            with open(changes_file, "w", encoding="utf-8") as f:
                f.write(changes_content)

            print_success(f"Generated changes file for v{version_str}")
            return True

        except Exception as e:
            print_warning(f"Changes generation failed for v{version_str}: {e}")
            changes_file.unlink(missing_ok=True)
            return False

    def parse_diff_changes(self, diff_content: str) -> List[str]:
        """Parse diff content into individual changes"""
        changes = []
        current_change = []
        in_change = False

        # Check if this is an astdiff output or unified diff
        is_astdiff = "=== Removed" in diff_content or "=== Added" in diff_content

        if is_astdiff:
            # Parse astdiff format
            lines = diff_content.split("\n")
            i = 0
            while i < len(lines):
                line = lines[i]
                # Look for section headers like "--- Removed function 'xyz'"
                if (
                    line.startswith("--- Removed")
                    or line.startswith("--- Added")
                    or line.startswith("--- Modified")
                ):
                    # Start of a change block
                    change_block = [line]
                    i += 1
                    # Collect the file path line
                    if i < len(lines) and lines[i].startswith("/"):
                        change_block.append(lines[i])
                        i += 1
                    # Collect the actual code lines (prefixed with - or +)
                    while i < len(lines) and (
                        lines[i].startswith("-")
                        or lines[i].startswith("+")
                        or lines[i].strip() == ""
                    ):
                        if lines[i].strip():  # Skip empty lines
                            change_block.append(lines[i])
                        i += 1
                    if len(change_block) > 1:
                        changes.append("\n".join(change_block))
                else:
                    i += 1
        else:
            # Parse unified diff format
            for line in diff_content.split("\n"):
                # Detect start of a new change block
                if line.startswith("@@"):
                    if current_change:
                        changes.append("\n".join(current_change))
                        current_change = []
                    in_change = True
                    current_change.append(line)
                elif in_change and (
                    line.startswith("+") or line.startswith("-") or line.startswith(" ")
                ):
                    current_change.append(line)
                elif in_change and not line:
                    # Empty line might separate changes
                    if current_change:
                        changes.append("\n".join(current_change))
                        current_change = []
                    in_change = False

            # Add the last change if any
            if current_change:
                changes.append("\n".join(current_change))

        return changes

    def phase_5_generate_changes(self):
        """Phase 5: Generate changes files using Claude subagents"""
        if not self.changes:
            return

        print_header("Phase 5: Generating Changes Files")

        # Ensure the system prompt file exists
        self.ensure_changes_prompt()

        # Check if Claude CLI is available
        claude_result = run(["which", "claude"], capture_output=True)
        if claude_result.returncode != 0:
            print_warning("Claude CLI not found. Skipping changes generation.")
            print_info("Ensure claude CLI is in PATH")
            return

        print_info("Checking for changes files to generate...")

        versions_to_changes = self.get_versions_to_changes()

        if not versions_to_changes:
            print_info("All changes files already generated.")
            return

        order_desc = "newest first" if self.new_first else "oldest first"
        print_info(
            f"Found {len(versions_to_changes)} changes files to generate (processing {order_desc})"
        )

        for version_str in versions_to_changes:
            if self.generate_changes(version_str):
                self.stats.changes_generated_count += 1
            else:
                self.stats.changes_generation_failures += 1

        print_info(
            f"\nGenerated {self.stats.changes_generated_count} new changes files."
        )
        if self.stats.changes_generation_failures > 0:
            print_warning(
                f"{self.stats.changes_generation_failures} changes generations failed."
            )

    def ensure_changelog_prompt(self):
        """Ensure the changelog system prompt file exists"""
        system_prompt_file = self.changelog_dir / "system-prompt.md"

        if not system_prompt_file.exists():
            print_info("Creating default changelog system prompt file...")
            with open(system_prompt_file, "w", encoding="utf-8") as f:
                f.write(self.DEFAULT_CHANGELOG_PROMPT)
            print_success(f"Created {system_prompt_file}")
            print_info("You can edit this file to customize changelog generation")

    def ensure_changes_prompt(self):
        """Ensure the changes system prompt file exists"""
        system_prompt_file = self.changes_dir / "changes-prompt.md"

        if not system_prompt_file.exists():
            print_info("Creating default changes system prompt file...")
            with open(system_prompt_file, "w", encoding="utf-8") as f:
                f.write(self.DEFAULT_CHANGES_PROMPT)
            print_success(f"Created {system_prompt_file}")
            print_info("You can edit this file to customize changes generation")

    def update_claude_md(self, version_str: str):
        """Update CLAUDE.md file to indicate the current version for analysis"""
        claude_md_path = self.base_dir / "CLAUDE.md"

        # Get the latest version from all pretty files
        pretty_files = list(self.pretty_dir.glob("pretty-v*.js"))
        if pretty_files:
            # Sort by version to find the actual latest
            pretty_files.sort(
                key=lambda p: version.parse(
                    re.match(r"pretty-v([0-9.]+)\.js$", p.name).group(1)
                ),
                reverse=True,
            )
            latest_file = pretty_files[0]
            latest_match = re.match(r"pretty-v([0-9.]+)\.js$", latest_file.name)
            if latest_match:
                latest_version = latest_match.group(1)
            else:
                latest_version = version_str
        else:
            latest_version = version_str

        # Use the latest version for the file path
        latest_pretty_file_path = self.pretty_dir / f"pretty-v{latest_version}.js"

        # Content for CLAUDE.md
        claude_md_content = f"""# CLAUDE.md

This file provides guidance to Claude Code when working with the claude-code archive.

## Current Claude Code Version

The latest prettified version available for analysis is **v{latest_version}**.

File location: `{latest_pretty_file_path.relative_to(self.base_dir)}`

## Archive Structure

- `archive/original/` - Original CLI files from npm
- `archive/pretty/` - Prettified versions for easier reading
- `archive/diff/` - Diffs between consecutive versions
- `archive/changelog/` - Generated changelogs for each version

## Latest Version Information

When analyzing Claude Code's source, please use the prettified version at:
`{latest_pretty_file_path.relative_to(self.base_dir)}`
"""

        # Write or update CLAUDE.md
        try:
            with open(claude_md_path, "w", encoding="utf-8") as f:
                f.write(claude_md_content)
            print_info(f"Updated CLAUDE.md to reference v{latest_version}")
        except Exception as e:
            print_warning(f"Failed to update CLAUDE.md: {e}")

    def cleanup(self):
        """Clean up temporary files"""
        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)

    def print_summary(self):
        """Print final summary statistics"""
        print_header("Sync Complete")

        archived_versions = len(list(self.original_dir.glob("cli-v*.js")))

        print(f"Total versions available: {self.stats.total_versions}")
        print(f"Total versions archived: {archived_versions}")
        print(f"Archive directory: {self.original_dir}")

        if self.stats.downloaded_count > 0:
            print_success(f"Downloaded {self.stats.downloaded_count} new versions")

        if self.prettier:
            prettified_count = len(list(self.pretty_dir.glob("pretty-v*.js")))
            print(f"Prettified versions: {prettified_count}")
            if self.stats.prettified_count > 0:
                print_success(f"Prettified {self.stats.prettified_count} new files")

        if self.diff:
            diff_count = len(list(self.diff_dir.glob("v*.diff")))
            print(f"Version diffs: {diff_count}")
            if self.stats.diff_generated_count > 0:
                print_success(f"Generated {self.stats.diff_generated_count} new diffs")

        if self.changelog:
            changelog_count = len(list(self.changelog_dir.glob("changelog-v*.md")))
            print(f"Version changelogs: {changelog_count}")
            if self.stats.changelog_generated_count > 0:
                print_success(
                    f"Generated {self.stats.changelog_generated_count} new changelogs"
                )

        if self.changes:
            changes_count = len(list(self.changes_dir.glob("changes-v*.diff")))
            print(f"Version changes: {changes_count}")
            if self.stats.changes_generated_count > 0:
                print_success(
                    f"Generated {self.stats.changes_generated_count} new changes files"
                )

        # Print any failures
        total_failures = (
            self.stats.download_failures
            + self.stats.prettier_failures
            + self.stats.diff_generation_failures
            + self.stats.changelog_generation_failures
            + self.stats.changes_generation_failures
        )
        if total_failures > 0:
            print_warning(f"Total failures: {total_failures}")

    def run(self):
        """Execute the sync process"""
        try:
            print(colored("Claude Code Archive Sync Tool", Colors.BOLD + Colors.PURPLE))
            print(colored("=" * 35, Colors.PURPLE))

            # Setup
            self.setup_directories()
            self.check_dependencies()

            # Get all versions
            all_versions = self.get_npm_versions()

            # Execute phases
            self.phase_1_download_originals(all_versions)
            self.phase_2_prettify_files()
            self.phase_3_generate_diffs()
            self.phase_4_generate_changelogs()
            self.phase_5_generate_changes()

            # Summary
            self.print_summary()

        except KeyboardInterrupt:
            print_warning("\nSync interrupted by user")
            sys.exit(1)
        except Exception as e:
            print_error(f"Unexpected error: {e}")
            sys.exit(1)
        finally:
            self.cleanup()

    def parse_version_range(self, version_spec: str) -> List[str]:
        """Parse version range specification and return list of versions.

        Supports:
        - Single version: "1.0.69" or "v1.0.69"
        - Range: "1.0.69-1.0.71" or "v1.0.69-v1.0.71"
        - Open range: "1.0.69-" (from 1.0.69 to latest)
        - Shorthand: "69" -> "1.0.69", "69-71" -> "1.0.69-1.0.71"
        """
        versions = []

        # Get all available versions from the pretty directory
        pretty_files = list(self.pretty_dir.glob("pretty-v*.js"))
        available_versions = []
        for f in pretty_files:
            match = re.match(r"pretty-v([0-9.]+)\.js$", f.name)
            if match:
                available_versions.append(match.group(1))

        # Sort versions
        available_versions.sort(key=version.parse)

        # Remove 'v' prefix if present
        version_spec = version_spec.lstrip("v")

        # Handle shorthand notation
        if re.match(r"^\d+$", version_spec):
            # Single shorthand version like "69"
            target = f"1.0.{version_spec}"
            if target in available_versions:
                return [target]
        elif re.match(r"^\d+-\d+$", version_spec):
            # Range shorthand like "69-71"
            start_num, end_num = version_spec.split("-")
            start_version = f"1.0.{start_num}"
            end_version = f"1.0.{end_num}"
            for v in available_versions:
                if (
                    version.parse(start_version)
                    <= version.parse(v)
                    <= version.parse(end_version)
                ):
                    versions.append(v)
            return versions
        elif re.match(r"^\d+-$", version_spec):
            # Open range shorthand like "69-"
            start_num = version_spec.rstrip("-")
            start_version = f"1.0.{start_num}"
            for v in available_versions:
                if version.parse(v) >= version.parse(start_version):
                    versions.append(v)
            return versions

        # Handle full version notation
        if "-" in version_spec:
            # Range notation
            parts = version_spec.split("-")
            if len(parts) == 2:
                start_version = parts[0]
                end_version = parts[1] if parts[1] else None

                for v in available_versions:
                    if version.parse(v) >= version.parse(start_version):
                        if end_version and version.parse(v) > version.parse(
                            end_version
                        ):
                            break
                        versions.append(v)
        else:
            # Single version
            if version_spec in available_versions:
                versions.append(version_spec)

        return versions

    def redo_versions(self):
        """Redo diff and changelog generation for specified versions."""
        if not self.redo:
            return

        print_header("Redoing Diffs and Changelogs")

        # Parse version range
        versions_to_redo = self.parse_version_range(self.redo)

        if not versions_to_redo:
            print_warning(f"No matching versions found for: {self.redo}")
            return

        print_info(
            f"Redoing {len(versions_to_redo)} version(s): {', '.join(versions_to_redo)}"
        )

        for version_str in versions_to_redo:
            # Find the next iteration number for this version
            diff_iteration = 1
            changelog_iteration = 1

            # Check existing diff files
            existing_diffs = list(self.diff_dir.glob(f"v{version_str}*.diff"))
            for diff_file in existing_diffs:
                match = re.match(
                    rf"v{re.escape(version_str)}(?:-(\d+))?\.diff$", diff_file.name
                )
                if match:
                    iter_num = int(match.group(1)) if match.group(1) else 1
                    diff_iteration = max(diff_iteration, iter_num + 1)

            # Check existing changelog files
            existing_changelogs = list(
                self.changelog_dir.glob(f"changelog-v{version_str}*.md")
            )
            for changelog_file in existing_changelogs:
                match = re.match(
                    rf"changelog-v{re.escape(version_str)}(?:-(\d+))?\.md$",
                    changelog_file.name,
                )
                if match:
                    iter_num = int(match.group(1)) if match.group(1) else 1
                    changelog_iteration = max(changelog_iteration, iter_num + 1)

            # Generate diff if requested
            if self.diff:
                # Find the pretty files for this version and the previous one
                pretty_file = self.pretty_dir / f"pretty-v{version_str}.js"
                if not pretty_file.exists():
                    print_warning(f"Pretty file not found for v{version_str}")
                    continue

                # Find previous version
                all_pretty_files = sorted(
                    self.pretty_dir.glob("pretty-v*.js"),
                    key=lambda p: version.parse(
                        re.match(r"pretty-v([0-9.]+)\.js$", p.name).group(1)
                    ),
                )
                prev_file = None
                for i, f in enumerate(all_pretty_files):
                    if f == pretty_file and i > 0:
                        prev_file = all_pretty_files[i - 1]
                        break

                if prev_file:
                    print_info(
                        f"Generating diff iteration {diff_iteration} for v{version_str}"
                    )
                    if self.generate_diff(prev_file, pretty_file, diff_iteration):
                        self.stats.diff_generated_count += 1
                    else:
                        self.stats.diff_generation_failures += 1
                else:
                    print_warning(f"No previous version found for v{version_str}")

            # Generate changelog if requested
            if self.changelog:
                print_info(
                    f"Generating changelog iteration {changelog_iteration} for v{version_str}"
                )
                # Use the latest diff iteration if we just created one, otherwise use the latest existing
                if self.diff:
                    effective_iteration = diff_iteration
                else:
                    effective_iteration = 1  # Use base diff if not regenerating diffs

                if self.generate_changelog(version_str, changelog_iteration):
                    self.stats.changelog_generated_count += 1
                else:
                    self.stats.changelog_generation_failures += 1

            # Generate changes if requested
            if self.changes:
                changes_iteration = changelog_iteration  # Use same iteration tracking
                print_info(
                    f"Generating changes iteration {changes_iteration} for v{version_str}"
                )
                if self.generate_changes(version_str, changes_iteration):
                    self.stats.changes_generated_count += 1
                else:
                    self.stats.changes_generation_failures += 1

        print_info(
            f"\nRedo complete: {self.stats.diff_generated_count} diffs, {self.stats.changelog_generated_count} changelogs"
        )
        if (
            self.stats.diff_generation_failures > 0
            or self.stats.changelog_generation_failures > 0
        ):
            print_warning(
                f"Failures: {self.stats.diff_generation_failures} diffs, {self.stats.changelog_generation_failures} changelogs"
            )


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Claude Code Archive Sync Tool - Download and process Claude Code CLI versions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                        # Download only original files
  %(prog)s --prettier             # Download and prettify files
  %(prog)s --prettier --diff      # Generate diffs between versions
  %(prog)s --all                  # Run all processing steps
  %(prog)s --all --latest         # Process only the most recent version
  %(prog)s --changelog --since v1.0.50    # Generate changelogs for v1.0.50 and newer
  %(prog)s --all --since 1.0.50   # Process all steps for versions 1.0.50+
  %(prog)s --changelog --new-first        # Generate changelogs in reverse chronological order (newest first)
  %(prog)s --prettier --diff --changelog  # Generate diffs and changelogs
  %(prog)s --diff --changes               # Generate diffs and detailed changes
  %(prog)s --redo 69 --changelog          # Redo changelog for v1.0.69 (creates changelog-v1.0.69-2.md)
  %(prog)s --redo 69-71 --diff --changelog # Redo diffs and changelogs for v1.0.69 through v1.0.71
  %(prog)s --redo 1.0.69- --changelog     # Redo changelogs for v1.0.69 and later
        """,
    )

    parser.add_argument(
        "--prettier",
        action="store_true",
        help="Create prettified versions of CLI files",
    )

    parser.add_argument(
        "--diff",
        action="store_true",
        help="Generate diffs between consecutive versions",
    )

    parser.add_argument(
        "--changelog",
        action="store_true",
        help="Generate changelogs using Claude SDK (processes available diffs)",
    )

    parser.add_argument(
        "--changes",
        action="store_true",
        help="Generate detailed changes files with meaningful names using Claude subagents",
    )

    parser.add_argument(
        "--all",
        action="store_true",
        help="Run main processing steps (prettier, diff, changelog - excludes changes)",
    )

    parser.add_argument(
        "--latest", action="store_true", help="Process only the most recent version"
    )

    parser.add_argument(
        "--since",
        type=str,
        help="Only process versions at or after this version (e.g., --since v1.0.50)",
    )

    parser.add_argument(
        "--new-first",
        action="store_true",
        help="Process versions in reverse chronological order (newest first) instead of chronological order",
    )

    parser.add_argument(
        "--no-color", action="store_true", help="Disable colored output"
    )

    parser.add_argument(
        "--redo",
        type=str,
        help='Redo diff/changelog for specific version(s). Examples: "1.0.69", "69-71", "1.0.69-1.0.71", "69-"',
    )

    args = parser.parse_args()

    # Handle --all flag
    if args.all:
        args.prettier = True
        args.diff = True
        args.changelog = True

    # --changelog will work independently and process available diffs

    # Disable colors if requested or if not a TTY
    if args.no_color or not sys.stdout.isatty():
        Colors.disable()

    # Find base directory (project root)
    script_path = Path(__file__).resolve()
    base_dir = script_path.parent.parent  # Go up from tools/ to project root

    # Create and run sync tool
    sync_tool = ClaudeCodeSync(
        base_dir=base_dir,
        prettier=args.prettier,
        diff=args.diff,
        changelog=args.changelog,
        changes=args.changes,
        latest=args.latest,
        since=args.since,
        new_first=args.new_first,
        redo=args.redo,
    )

    # If --redo is specified, run the redo process instead
    if args.redo:
        # For redo, we need at least one of diff, changelog, or changes
        if not args.diff and not args.changelog and not args.changes:
            print_error(
                "--redo requires at least one of --diff, --changelog, or --changes"
            )
            sys.exit(1)
        sync_tool.setup_directories()
        sync_tool.check_dependencies()
        sync_tool.redo_versions()
    else:
        sync_tool.run()


if __name__ == "__main__":
    main()
