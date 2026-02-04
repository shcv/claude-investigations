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
  * If --cleanup is enabled: immediately clean each changelog after generation
  * If --post is enabled: immediately post each changelog after cleanup
- Phase 5: Generate detailed changes using Claude SDK (optional)
- Phase 6: Clean up changelog headers (optional, skipped if --changelog is enabled)
- Phase 7: Post changelogs to Discord (optional, skipped if --changelog is enabled)

Note: When --changelog is used with --cleanup and/or --post, each changelog is
processed completely (generate → clean → post) before moving to the next one.
This reduces the risk of losing work if the process is interrupted.
"""

import argparse
import json
import os
import re
import shutil
import sys
import tarfile
from dataclasses import dataclass
import tempfile
from pathlib import Path
from subprocess import run, PIPE, DEVNULL
from typing import List, Set, Optional, Tuple
import requests
from packaging import version

# Try to load .env file if python-dotenv is available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # python-dotenv not installed, skip loading .env file
    pass

# Claude changelog generation uses the claude CLI tool (Claude Code SDK)


class ProjectConfig:
    """Configuration for a specific project/package"""

    def __init__(
        self,
        name: str,
        npm_package: Optional[str] = None,
        github_repo: Optional[str] = None,
        github_tag_prefix: Optional[str] = None,
        use_astdiff: bool = False,
        changelog_prompt: Optional[str] = None,
        changes_prompt: Optional[str] = None,
        webhook_env_var: Optional[str] = None,
        source_subdir: Optional[str] = None,
        extract_files: Optional[List[Tuple[str, str]]] = None,
    ):
        self.name = name
        self.npm_package = npm_package
        self.github_repo = github_repo  # e.g., "openai/codex"
        self.github_tag_prefix = github_tag_prefix  # e.g., "rust-v" for rust-v0.46.0
        self.use_astdiff = use_astdiff
        self.changelog_prompt = changelog_prompt
        self.changes_prompt = changes_prompt
        self.webhook_env_var = webhook_env_var
        self.source_subdir = source_subdir  # Subdirectory containing main source (e.g., "codex-rs")
        # Files to extract: list of (archive_path, output_prefix) tuples
        # e.g., [("cli.js", "cli"), ("sdk.mjs", "sdk")] -> cli-v1.0.0.js, sdk-v1.0.0.mjs
        # If None, defaults to [("cli.js", "cli"), ("cli.mjs", "cli")] for backwards compat
        self.extract_files = extract_files
        # Primary file prefix for diff/changelog generation (first one if not specified)
        # Validate that at least one source is specified
        if not npm_package and not github_repo:
            raise ValueError(f"Project {name} must specify either npm_package or github_repo")

        self._primary_prefix = None
        if extract_files:
            self._primary_prefix = extract_files[0][1]  # Use first file's prefix as primary

    @property
    def primary_file_prefix(self) -> str:
        """Get the primary file prefix for diffs/changelogs"""
        return self._primary_prefix or "cli"

    @property
    def is_npm_based(self) -> bool:
        """Check if this project uses npm as its source"""
        return self.npm_package is not None

    @property
    def is_github_based(self) -> bool:
        """Check if this project uses GitHub releases as its source"""
        return self.github_repo is not None


# Predefined project configurations
PROJECTS = {
    "claude-code": ProjectConfig(
        name="claude-code",
        npm_package="@anthropic-ai/claude-code",
        use_astdiff=True,  # Use astdiff for minified Claude Code
        webhook_env_var="DISCORD_WEBHOOK_URL",  # Uses existing env var
    ),
    "claude-agent-sdk": ProjectConfig(
        name="claude-agent-sdk",
        npm_package="@anthropic-ai/claude-agent-sdk",
        use_astdiff=True,  # Use astdiff for bundled SDK code
        webhook_env_var="DISCORD_WEBHOOK_URL_AGENT_SDK",
        # Extract both CLI and SDK module files
        extract_files=[
            ("cli.js", "cli"),      # cli-v0.2.23.js
            ("sdk.mjs", "sdk"),     # sdk-v0.2.23.mjs
        ],
    ),
    "codex": ProjectConfig(
        name="codex",
        github_repo="openai/codex",
        github_tag_prefix="rust-v",  # Tags are like rust-v0.46.0
        source_subdir="codex-rs",  # Main Rust source is in codex-rs/
        use_astdiff=False,  # Regular diff for Rust source
        webhook_env_var="DISCORD_WEBHOOK_URL_CODEX",  # Separate webhook for Codex
    ),
}


from colors import Colors, colored, print_header, print_success, print_warning, print_error, print_info

# Common regex patterns
RE_DIFF_VERSION = re.compile(r"v([0-9.]+)(?:-\d+)?\.diff$")
RE_FILE_PREFIX_VERSION = re.compile(r"([a-z]+)-v([0-9.]+)\.[a-z]+$")


@dataclass
class SyncStats:
    """Track sync operation statistics"""
    total_versions: int = 0
    downloaded_count: int = 0
    prettified_count: int = 0
    diff_generated_count: int = 0
    changelog_generated_count: int = 0
    download_failures: int = 0
    prettier_failures: int = 0
    diff_generation_failures: int = 0
    changelog_generation_failures: int = 0
    changes_generated_count: int = 0
    changes_generation_failures: int = 0
    changelogs_cleaned_count: int = 0
    changelog_cleanup_failures: int = 0
    changelogs_posted_count: int = 0
    changelog_post_failures: int = 0


class ClaudeCodeSync:
    """Main sync tool implementation"""

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
        project: ProjectConfig,
        prettier: bool = False,
        diff: bool = False,
        changelog: bool = False,
        changes: bool = False,
        cleanup: bool = False,
        post: bool = False,
        latest: bool = False,
        since: Optional[str] = None,
        new_first: bool = False,
        redo: Optional[str] = None,
        dry_run: bool = False,
    ):
        self.base_dir = base_dir
        self.project = project
        self.prettier = prettier
        self.diff = diff
        self.changelog = changelog
        self.changes = changes
        self.do_cleanup = cleanup
        self.post = post
        self.latest = latest
        self.since = since
        self.new_first = new_first
        self.redo = redo
        self.dry_run = dry_run

        # Directory structure - now project-specific
        self.archive_dir = base_dir / "archive" / project.name

        # Source directory depends on project type
        if project.is_github_based:
            # GitHub projects: just a git clone
            self.source_dir = self.archive_dir / "source"
            self.original_dir = None  # Not used for GitHub projects
            self.pretty_dir = None  # Not used for GitHub projects
        else:
            # npm projects: original + prettified
            self.source_dir = None  # Not used for npm projects
            self.original_dir = self.archive_dir / "original"
            self.pretty_dir = self.archive_dir / "pretty"

        self.diff_dir = self.archive_dir / "diff"
        self.changelog_dir = self.archive_dir / "changelog"
        self.changes_dir = self.archive_dir / "changes"
        self.temp_dir = base_dir / f".sync-temp-{project.name}"

        self.stats = SyncStats()

    def setup_directories(self):
        """Create required directories"""
        directories = [self.archive_dir]

        # Add source directories based on project type
        if self.project.is_github_based:
            # GitHub: just source directory (will be git repo)
            directories.append(self.source_dir)
        else:
            # npm: original and pretty directories
            directories.append(self.original_dir)
            if self.prettier:
                directories.append(self.pretty_dir)

        if self.diff:
            directories.append(self.diff_dir)

        if self.changelog:
            directories.append(self.changelog_dir)

        if self.changes:
            directories.append(self.changes_dir)

        for directory in directories:
            if directory:  # Skip None directories
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

    def _is_before_since(self, version_str: str) -> bool:
        """Return True if version_str is before the --since cutoff."""
        if not self.since:
            return False
        try:
            return version.parse(version_str.lstrip("v")) < version.parse(self.since.lstrip("v"))
        except Exception:
            return False

    def get_github_releases(self) -> List[str]:
        """Get all available releases from GitHub, sorted oldest first by default"""
        print_info(f"Fetching all available releases from {self.project.github_repo}...")

        try:
            # Use GitHub API to get releases
            api_url = f"https://api.github.com/repos/{self.project.github_repo}/releases"
            response = requests.get(api_url)
            response.raise_for_status()

            releases = response.json()

            # Extract version numbers from tag names, excluding pre-releases
            versions = []
            for release in releases:
                # Skip pre-releases (alpha, beta, rc, etc.) for diff/changelog generation
                # We only want stable releases
                if release.get("prerelease", False):
                    continue

                tag_name = release.get("tag_name", "")
                # Remove prefix if specified
                if self.project.github_tag_prefix and tag_name.startswith(self.project.github_tag_prefix):
                    version_str = tag_name[len(self.project.github_tag_prefix):]
                    versions.append(version_str)
                elif not self.project.github_tag_prefix:
                    versions.append(tag_name)

            # Sort versions (oldest first by default, newest first if --new-first)
            sorted_versions = sorted(
                versions, key=version.parse, reverse=self.new_first
            )
            self.stats.total_versions = len(sorted_versions)

            if self.since:
                sorted_versions = [v for v in sorted_versions if not self._is_before_since(v)]
                print_info(f"Filtered to {len(sorted_versions)} versions since {self.since}")

            return sorted_versions

        except Exception as e:
            print_error(f"Failed to fetch releases from GitHub: {e}")
            sys.exit(1)

    def get_npm_versions(self) -> List[str]:
        """Get all available versions from npm registry, sorted oldest first by default"""
        print_info(f"Fetching all available versions of {self.project.npm_package}...")

        try:
            result = run(
                ["npm", "view", self.project.npm_package, "versions", "--json"],
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

            if self.since:
                sorted_versions = [v for v in sorted_versions if not self._is_before_since(v)]
                print_info(f"Filtered to {len(sorted_versions)} versions since {self.since}")

            return sorted_versions

        except Exception as e:
            print_error(f"Failed to fetch versions from npm: {e}")
            sys.exit(1)

    def get_existing_originals(self) -> Set[str]:
        """Get set of versions that already exist in original directory.

        For projects with multiple extract_files, a version is only considered
        'existing' if ALL required files are present.
        """
        # Determine which file prefixes we need
        extract_files = self.project.extract_files
        if extract_files is None:
            # Default: just need cli file
            required_prefixes = ["cli"]
        else:
            required_prefixes = [prefix for _, prefix in extract_files]

        # Count how many files exist for each version
        version_files: dict = {}  # version -> set of prefixes found

        for file_path in self.original_dir.glob("*-v*.*"):
            # Extract prefix and version from filename: cli-v1.0.63.js -> ("cli", "1.0.63")
            match = RE_FILE_PREFIX_VERSION.match(file_path.name)
            if match:
                prefix, ver = match.groups()
                if prefix in required_prefixes:
                    if ver not in version_files:
                        version_files[ver] = set()
                    version_files[ver].add(prefix)

        # Return versions that have ALL required files
        required_set = set(required_prefixes)
        return {ver for ver, found in version_files.items() if found >= required_set}

    def download_version(self, version_str: str) -> bool:
        """Download a specific version from npm. Returns True on success."""
        print(f"\n--- Downloading version {version_str} ---")

        try:
            # Get tarball URL
            print_info(f"Fetching tarball URL for version {version_str}...")
            result = run(
                ["npm", "view", f"{self.project.npm_package}@{version_str}", "dist.tarball"],
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

            tgz_file = self.temp_dir / f"{self.project.name}-{version_str}.tgz"
            with open(tgz_file, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            # Determine files to extract
            extract_files = self.project.extract_files
            if extract_files is None:
                # Default behavior: extract cli.js or cli.mjs
                extract_files = [("cli.js", "cli"), ("cli.mjs", "cli")]

            # Extract and save files
            print_info("Extracting files...")
            files_extracted = 0

            with tarfile.open(tgz_file, "r:gz") as tar:
                for archive_name, output_prefix in extract_files:
                    archive_path = f"package/{archive_name}"
                    try:
                        member = tar.getmember(archive_path)
                        tar.extract(member, self.temp_dir)
                        extracted_file = self.temp_dir / archive_path

                        # Determine output extension from archive name
                        ext = Path(archive_name).suffix or ".js"
                        original_file = self.original_dir / f"{output_prefix}-v{version_str}{ext}"
                        print_info(f"Saving: {original_file.name}")
                        shutil.copy2(extracted_file, original_file)
                        files_extracted += 1
                    except KeyError:
                        # File not in archive, skip (only warn if no files extracted at end)
                        continue

            if files_extracted == 0:
                print_warning(f"No files found in tarball for version {version_str}")
                tgz_file.unlink(missing_ok=True)
                shutil.rmtree(self.temp_dir / "package", ignore_errors=True)
                return False

            # Clean up temp files
            tgz_file.unlink(missing_ok=True)
            shutil.rmtree(self.temp_dir / "package", ignore_errors=True)

            print_success(f"Downloaded version {version_str} ({files_extracted} file(s))")
            return True

        except Exception as e:
            print_warning(f"Failed to download version {version_str}: {e}")
            return False

    def sync_github_repo(self, all_versions: List[str]):
        """Sync GitHub repository and checkout tags for all versions"""
        print_header("Phase 1: Syncing GitHub Repository")

        repo_url = f"https://github.com/{self.project.github_repo}.git"

        # Check if repo already cloned
        if not (self.source_dir / ".git").exists():
            print_info(f"Cloning {self.project.github_repo}...")
            result = run(
                ["git", "clone", repo_url, str(self.source_dir)],
                capture_output=True,
                text=True,
            )
            if result.returncode != 0:
                print_error(f"Failed to clone repository: {result.stderr}")
                sys.exit(1)
            print_success(f"Cloned {self.project.github_repo}")
        else:
            print_info(f"Repository already cloned, fetching updates...")
            result = run(
                ["git", "-C", str(self.source_dir), "fetch", "--tags"],
                capture_output=True,
                text=True,
            )
            if result.returncode != 0:
                print_warning(f"Failed to fetch updates: {result.stderr}")
            else:
                print_success("Fetched latest tags")

        # Get the latest version to checkout
        if self.latest:
            latest_version = all_versions[-1] if not self.new_first else all_versions[0]
            print_info(f"Checking out latest version: {latest_version}")
            tag_name = f"{self.project.github_tag_prefix}{latest_version}"
            result = run(
                ["git", "-C", str(self.source_dir), "checkout", tag_name],
                capture_output=True,
                text=True,
            )
            if result.returncode != 0:
                print_error(f"Failed to checkout {tag_name}: {result.stderr}")
            else:
                print_success(f"Checked out {tag_name}")
        else:
            print_info("Repository synced, ready for diff generation")

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
                # Get the second-latest version (versions are sorted oldest first)
                previous_version = all_versions[-2] if not self.new_first else all_versions[1]
                versions_to_check = [latest_version, previous_version]
                print_info(
                    f"Also checking previous version for diff: {previous_version}"
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

        # Determine file patterns based on extract_files config
        extract_files = self.project.extract_files
        if extract_files is None:
            # Legacy mode: use old naming convention (pretty-v*.js without prefix)
            patterns = [("cli-v*.js", r"cli-v([0-9.]+)\.js$", None)]  # None prefix = old naming
        else:
            # New mode: use prefix-based naming (pretty-{prefix}-v*.js)
            patterns = []
            for archive_name, prefix in extract_files:
                ext = Path(archive_name).suffix or ".js"
                pattern = f"{prefix}-v*{ext}"
                regex = rf"{prefix}-v([0-9.]+){re.escape(ext)}$"
                patterns.append((pattern, regex, prefix))

        for glob_pattern, regex_pattern, prefix in patterns:
            # Get all original files sorted by version
            original_files = list(self.original_dir.glob(glob_pattern))
            original_files.sort(
                key=lambda p, r=regex_pattern: version.parse(
                    re.match(r, p.name).group(1) if re.match(r, p.name) else "0"
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
                match = re.match(regex_pattern, original_file.name)
                if not match:
                    continue

                version_str = match.group(1)

                # Filter by --since if specified
                if self._is_before_since(version_str):
                    continue

                # Determine pretty file name based on prefix mode
                if prefix is None:
                    # Legacy mode: pretty-v{version}.js
                    pretty_file = self.pretty_dir / f"pretty-v{version_str}.js"
                else:
                    # New mode: pretty-{prefix}-v{version}.js
                    pretty_file = self.pretty_dir / f"pretty-{prefix}-v{version_str}.js"

                # Check if pretty version already exists
                if not pretty_file.exists():
                    files_to_prettify.append(original_file)

        return files_to_prettify

    def prettify_file(self, original_file: Path) -> bool:
        """Prettify a single file. Returns True on success."""
        # Extract prefix and version from filename: cli-v1.0.63.js -> ("cli", "1.0.63")
        match = RE_FILE_PREFIX_VERSION.match(original_file.name)
        if not match:
            return False

        prefix, version_str = match.groups()

        # Determine naming mode: legacy (no extract_files) vs new (with extract_files)
        if self.project.extract_files is None:
            # Legacy mode: pretty-v{version}.js
            pretty_file = self.pretty_dir / f"pretty-v{version_str}.js"
            print(f"\n--- Prettifying version {version_str} ---")
        else:
            # New mode: pretty-{prefix}-v{version}.js
            pretty_file = self.pretty_dir / f"pretty-{prefix}-v{version_str}.js"
            print(f"\n--- Prettifying {prefix} version {version_str} ---")

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

    def get_versions_to_diff_github(self, all_versions: List[str]) -> List[Tuple[str, str]]:
        """Get list of consecutive version pairs that need diffs generated (GitHub mode)"""
        versions_to_diff = []

        if self.latest:
            # For --latest, only diff the most recent pair
            if len(all_versions) >= 2:
                older_version = all_versions[-2] if not self.new_first else all_versions[1]
                newer_version = all_versions[-1] if not self.new_first else all_versions[0]

                diff_file = self.diff_dir / f"v{newer_version}.diff"
                if not diff_file.exists():
                    versions_to_diff.append((older_version, newer_version))
        else:
            # Create pairs of consecutive versions
            sorted_versions = sorted(all_versions, key=version.parse)
            for i in range(len(sorted_versions) - 1):
                older_version = sorted_versions[i]
                newer_version = sorted_versions[i + 1]

                # Filter by --since if specified (check newer version)
                if self._is_before_since(newer_version):
                    continue

                diff_file = self.diff_dir / f"v{newer_version}.diff"
                if not diff_file.exists():
                    versions_to_diff.append((older_version, newer_version))

            # Reverse to process newest first (when --new-first is specified)
            if self.new_first:
                versions_to_diff.reverse()

        return versions_to_diff

    def get_files_to_diff(self) -> List[Tuple[Path, Path]]:
        """Get list of consecutive version pairs that need diffs generated"""
        files_to_diff = []

        # Determine naming mode based on extract_files config
        if self.project.extract_files is None:
            # Legacy mode: use pretty-v*.js
            pretty_files = list(self.pretty_dir.glob("pretty-v*.js"))
            regex_pattern = r"pretty-v([0-9.]+)\.js$"
        else:
            # New mode: use pretty-{prefix}-v*.js with primary prefix
            prefix = self.project.primary_file_prefix
            pretty_files = list(self.pretty_dir.glob(f"pretty-{prefix}-v*.js"))
            regex_pattern = rf"pretty-{prefix}-v([0-9.]+)\.js$"

        if len(pretty_files) < 2:
            return files_to_diff

        # Sort by version (oldest first)
        pretty_files.sort(
            key=lambda p: version.parse(
                re.match(regex_pattern, p.name).group(1)
                if re.match(regex_pattern, p.name) else "0"
            )
        )

        if self.latest:
            # For --latest, only diff the most recent pair
            if len(pretty_files) >= 2:
                older_file = pretty_files[-2]
                newer_file = pretty_files[-1]

                newer_match = re.match(regex_pattern, newer_file.name)
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
                older_match = re.match(regex_pattern, older_file.name)
                newer_match = re.match(regex_pattern, newer_file.name)

                if not older_match or not newer_match:
                    continue

                newer_version = newer_match.group(1)

                # Filter by --since if specified (check newer version)
                if self._is_before_since(newer_version):
                    continue

                diff_file = self.diff_dir / f"v{newer_version}.diff"

                # Check if diff already exists
                if not diff_file.exists():
                    files_to_diff.append((older_file, newer_file))

            # Reverse to process newest first (when --new-first is specified)
            if self.new_first:
                files_to_diff.reverse()

        return files_to_diff

    def generate_diff_github(
        self, older_version: str, newer_version: str, iteration: int = 1
    ) -> bool:
        """Generate diff between two tags using git. Returns True on success."""
        # Add iteration suffix if > 1
        if iteration > 1:
            diff_file = self.diff_dir / f"v{newer_version}-{iteration}.diff"
        else:
            diff_file = self.diff_dir / f"v{newer_version}.diff"

        print(f"\n--- Generating diff: v{older_version} -> v{newer_version} ---")

        try:
            # Use git diff between tags
            older_tag = f"{self.project.github_tag_prefix}{older_version}"
            newer_tag = f"{self.project.github_tag_prefix}{newer_version}"

            # If source_subdir is specified, only diff that subdirectory
            path_spec = []
            if self.project.source_subdir:
                path_spec = ["--", self.project.source_subdir]

            result = run(
                ["git", "-C", str(self.source_dir), "diff", older_tag, newer_tag] + path_spec,
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

    def generate_diff(
        self, older_file: Path, newer_file: Path, iteration: int = 1
    ) -> bool:
        """Generate diff between two consecutive versions. Returns True on success."""
        # Determine naming mode based on extract_files config
        if self.project.extract_files is None:
            # Legacy mode
            regex_pattern = r"pretty-v([0-9.]+)\.js$"
        else:
            # New mode
            prefix = self.project.primary_file_prefix
            regex_pattern = rf"pretty-{prefix}-v([0-9.]+)\.js$"

        # Extract version from newer file
        match = re.match(regex_pattern, newer_file.name)
        if not match:
            return False

        newer_version = match.group(1)

        # Extract version from older file
        older_match = re.match(regex_pattern, older_file.name)
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
            # Use astdiff only if project configuration enables it
            use_astdiff = False
            if self.project.use_astdiff:
                astdiff_result = run(["which", "astdiff"], capture_output=True)
                use_astdiff = astdiff_result.returncode == 0

            if use_astdiff:
                # Use astdiff for better JavaScript-aware diffing (for minified code)
                result = run(
                    ["astdiff", str(older_file), str(newer_file)],
                    capture_output=True,
                    text=True,
                )
            else:
                # Use regular diff (for open-source or when astdiff not available)
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

    def generate_string_diff(self, version_str: str) -> Optional[str]:
        """
        Generate a string diff for a version using the AST-based string_diff.js tool.
        Returns the diff output as a string, or None if it fails.
        """
        # Find the string_diff.js tool - it's in the same directory as this script
        tools_dir = Path(__file__).parent
        string_diff_tool = tools_dir / "string_diff.js"

        if not string_diff_tool.exists():
            print_warning("string_diff.js not found, skipping string diff")
            return None

        # The string_diff.js tool has a built-in 'compare' command that handles version lookup
        try:
            result = run(
                ["node", str(string_diff_tool), "compare", version_str.lstrip("v"), "--filter"],
                capture_output=True,
                text=True,
                cwd=str(tools_dir.parent),  # Run from project root so paths resolve correctly
            )

            if result.returncode == 0:
                return result.stdout
            else:
                # If compare fails, try using the pretty_dir directly
                current_file = self.pretty_dir / f"pretty-v{version_str}.js"
                if not current_file.exists():
                    return None

                # Find previous version
                all_pretty_files = sorted(
                    self.pretty_dir.glob("pretty-v*.js"),
                    key=lambda p: version.parse(
                        re.match(r"pretty-v([0-9.]+)\.js$", p.name).group(1)
                    ),
                )
                prev_file = None
                for i, f in enumerate(all_pretty_files):
                    if f == current_file and i > 0:
                        prev_file = all_pretty_files[i - 1]
                        break

                if not prev_file:
                    return None

                result = run(
                    ["node", str(string_diff_tool), "diff", str(prev_file), str(current_file), "--filter"],
                    capture_output=True,
                    text=True,
                )

                if result.returncode == 0:
                    return result.stdout
                else:
                    print_warning(f"String diff failed: {result.stderr}")
                    return None

        except Exception as e:
            print_warning(f"String diff generation failed: {e}")
            return None

    def phase_3_generate_diffs(self, all_versions: Optional[List[str]] = None):
        """Phase 3: Generate diffs between consecutive versions"""
        if not self.diff:
            return

        print_header("Phase 3: Generating Diffs")
        print_info("Checking for diffs to generate...")

        if self.project.is_github_based:
            # GitHub mode: use git diff between tags
            if not all_versions:
                print_error("No versions provided for diff generation")
                return

            versions_to_diff = self.get_versions_to_diff_github(all_versions)

            if not versions_to_diff:
                print_info("All diffs already generated.")
                return

            order_desc = "newest first" if self.new_first else "oldest first"
            print_info(
                f"Found {len(versions_to_diff)} diffs to generate (processing {order_desc})"
            )

            for older_version, newer_version in versions_to_diff:
                if self.generate_diff_github(older_version, newer_version):
                    self.stats.diff_generated_count += 1
                else:
                    self.stats.diff_generation_failures += 1
        else:
            # npm mode: compare files
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

    def _get_versions_needing_output(self, output_dir: Path, filename_template: str) -> List[str]:
        """Get list of versions that have diffs but no corresponding output file.

        Args:
            output_dir: Directory to check for existing output files
            filename_template: Template with {version} placeholder, e.g. "changelog-v{version}.md"
        """
        versions_needed = []

        # Get all diff files
        diff_files = list(self.diff_dir.glob("v*.diff"))

        if self.latest and diff_files:
            # For --latest, only check the most recent diff
            valid_diff_files = [
                f for f in diff_files
                if RE_DIFF_VERSION.match(f.name)
            ]

            if valid_diff_files:
                valid_diff_files.sort(
                    key=lambda p: version.parse(
                        RE_DIFF_VERSION.match(p.name).group(1)
                    ),
                    reverse=True,
                )
                diff_files = [valid_diff_files[0]]
            else:
                diff_files = []

        for diff_file in diff_files:
            match = RE_DIFF_VERSION.match(diff_file.name)
            if not match:
                continue

            version_str = match.group(1)

            if self._is_before_since(version_str):
                continue

            output_file = output_dir / filename_template.format(version=version_str)

            if not output_file.exists():
                versions_needed.append(version_str)

        versions_needed.sort(key=version.parse, reverse=self.new_first)
        return versions_needed

    def get_versions_to_changelog(self) -> List[str]:
        """Get list of versions that need changelogs generated"""
        return self._get_versions_needing_output(
            self.changelog_dir, "changelog-v{version}.md"
        )

    def cleanup_single_changelog(self, changelog_file: Path, version_str: str) -> bool:
        """Clean up a single changelog file. Returns True on success."""
        try:
            import importlib.util
            cleanup_script = self.base_dir / "tools" / "cleanup_changelogs.py"

            if not cleanup_script.exists():
                print_warning("cleanup_changelogs.py not found, skipping cleanup")
                return False

            # Import the cleanup module
            spec = importlib.util.spec_from_file_location("cleanup_changelogs", cleanup_script)
            cleanup_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(cleanup_module)

            content = changelog_file.read_text()
            cleaned_content, was_modified = cleanup_module.cleanup_changelog(content, version_str)

            if was_modified:
                changelog_file.write_text(cleaned_content)
                orig_lines = len(content.split('\n'))
                new_lines = len(cleaned_content.split('\n'))
                print_success(f"Cleaned {changelog_file.name} ({orig_lines - new_lines} lines removed)")
                self.stats.changelogs_cleaned_count += 1
            else:
                print_info(f"No cleanup needed for {changelog_file.name}")

            return True

        except Exception as e:
            print_warning(f"Failed to clean {changelog_file.name}: {e}")
            self.stats.changelog_cleanup_failures += 1
            return False

    def post_single_changelog(self, changelog_file: Path, version_str: str) -> bool:
        """
        Post a single changelog to Discord using multi-webhook config.
        Returns True on success.

        NOTE: This posts immediately after generating each changelog (inline mode).
        The version is posted to all webhooks subscribed to this project's channel.
        """
        try:
            import subprocess
            post_script = self.base_dir / "tools" / "post.py"

            if not post_script.exists():
                print_warning("post.py not found, skipping post")
                return False

            # Post this specific version to all configured webhooks for this project
            cmd = [
                str(post_script),
                f"v{version_str}",  # Post this specific version
                "--project", self.project.name,
            ]

            if self.dry_run:
                cmd.append("--dry-run")

            result = subprocess.run(
                cmd,
                cwd=str(self.base_dir),
                capture_output=True,
                text=True,
                check=False
            )

            if result.returncode == 0:
                self.stats.changelogs_posted_count += 1
                print_success(f"Posted {changelog_file.name} to Discord")
                return True
            else:
                self.stats.changelog_post_failures += 1
                if result.stderr:
                    print_warning(f"post.py error: {result.stderr.strip()}")
                return False

        except Exception as e:
            print_warning(f"Failed to post {changelog_file.name}: {e}")
            self.stats.changelog_post_failures += 1
            return False

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

            # Generate string diff for additional context
            string_diff_output = self.generate_string_diff(version_str)
            if string_diff_output:
                print_info("Generated string diff for additional context")

            # Ensure system prompt file exists and read it
            self.ensure_changelog_prompt()
            system_prompt_file = self.changelog_dir / "system-prompt.md"
            with open(system_prompt_file, "r", encoding="utf-8") as f:
                system_prompt = f.read()

            # Use claude CLI to generate changelog
            claude_result = run(["which", "claude"], capture_output=True)
            if claude_result.returncode != 0:
                print_warning("claude CLI not found. Cannot generate changelog.")
                return False

            try:
                # Build prompt with optional string diff
                cli_prompt_parts = [f"Generate a changelog for version {version_str} based on this diff: @{diff_file}"]

                if string_diff_output:
                    cli_prompt_parts.append(f"""

## String Literal Changes (AST-Extracted)

The following shows all string literals that were added or removed between versions.
This uses AST parsing for accuracy and filters out noise (identifiers, code fragments).
Use this to identify user-facing message changes.

{string_diff_output}
""")

                cli_prompt = "".join(cli_prompt_parts)

                result = run(
                    [
                        "claude",
                        "--print",
                        "--system-prompt",
                        system_prompt,
                        cli_prompt,
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

            # Write changelog
            with open(changelog_file, "w", encoding="utf-8") as f:
                f.write(f"# Changelog for version {version_str}\n\n")
                f.write(changelog_content)

            print_success(f"Generated changelog for v{version_str}")

            # Immediately clean up if cleanup is enabled
            if self.do_cleanup:
                self.cleanup_single_changelog(changelog_file, version_str)

            # Immediately post if posting is enabled
            if self.post:
                self.post_single_changelog(changelog_file, version_str)

            return True

        except Exception as e:
            print_warning(f"Changelog generation failed for v{version_str}: {e}")
            changelog_file.unlink(missing_ok=True)
            return False

    def phase_4_generate_changelogs(self):
        """Phase 4: Generate changelogs using claude CLI"""
        if not self.changelog:
            return

        print_header("Phase 4: Generating Changelogs")

        # Ensure the system prompt file exists
        self.ensure_changelog_prompt()

        # Check if Claude CLI is available
        claude_result = run(["which", "claude"], capture_output=True)
        if claude_result.returncode != 0:
            print_warning(
                "claude CLI not found in PATH. Skipping changelog generation."
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
        return self._get_versions_needing_output(
            self.changes_dir, "changes-v{version}.diff"
        )

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
        # Create CLAUDE.md in the project's archive directory
        claude_md_path = self.archive_dir / "CLAUDE.md"

        # Determine naming mode based on extract_files config
        if self.project.extract_files is None:
            # Legacy mode: pretty-v*.js
            pretty_files = list(self.pretty_dir.glob("pretty-v*.js"))
            regex_pattern = r"pretty-v([0-9.]+)\.js$"
            file_prefix = "pretty-v"
        else:
            # New mode: pretty-{prefix}-v*.js
            prefix = self.project.primary_file_prefix
            pretty_files = list(self.pretty_dir.glob(f"pretty-{prefix}-v*.js"))
            regex_pattern = rf"pretty-{prefix}-v([0-9.]+)\.js$"
            file_prefix = f"pretty-{prefix}-v"

        if pretty_files:
            # Sort by version to find the actual latest
            pretty_files.sort(
                key=lambda p: version.parse(
                    re.match(regex_pattern, p.name).group(1)
                    if re.match(regex_pattern, p.name) else "0"
                ),
                reverse=True,
            )
            latest_file = pretty_files[0]
            latest_match = re.match(regex_pattern, latest_file.name)
            if latest_match:
                latest_version = latest_match.group(1)
            else:
                latest_version = version_str
        else:
            latest_version = version_str

        # Project display name
        project_display = self.project.name.replace("-", " ").title()

        # Content for CLAUDE.md (using relative paths from archive subdirectory)
        claude_md_content = f"""# CLAUDE.md

This file provides guidance to Claude Code when working with the {self.project.name} archive.

## Current {project_display} Version

The latest prettified version available for analysis is **v{latest_version}**.

File location: `pretty/{file_prefix}{latest_version}.js`

## Archive Structure

- `original/` - Original CLI files from npm
- `pretty/` - Prettified versions for easier reading
- `diff/` - Diffs between consecutive versions
- `changelog/` - Generated changelogs for each version
- `changes/` - Detailed changes with semantic names

## Latest Version Information

When analyzing {project_display}'s source, please use the prettified version at:
`pretty/{file_prefix}{latest_version}.js`

Package: `{self.project.npm_package}`
"""

        # Write or update CLAUDE.md
        try:
            with open(claude_md_path, "w", encoding="utf-8") as f:
                f.write(claude_md_content)
            print_info(f"Updated {claude_md_path.relative_to(self.base_dir)} to reference v{latest_version}")
        except Exception as e:
            print_warning(f"Failed to update CLAUDE.md: {e}")

    def phase_6_cleanup_changelogs(self):
        """Phase 6: Clean up changelog headers"""
        if not self.do_cleanup:
            return

        # Skip if changelogs were already cleaned during phase 4
        if self.changelog:
            print_info("Changelogs already cleaned during generation phase")
            return

        print_header("Phase 6: Cleaning Up Changelogs")

        changelog_files = sorted(self.changelog_dir.glob("changelog-*.md"))

        if not changelog_files:
            print_info("No changelogs to clean up")
            return

        print_info(f"Processing {len(changelog_files)} changelog(s)...")

        for changelog_file in changelog_files:
            ver_match = re.match(r'changelog-v?(.+)\.md$', changelog_file.name)
            version_str = ver_match.group(1) if ver_match else "unknown"
            self.cleanup_single_changelog(changelog_file, version_str)

        if self.stats.changelogs_cleaned_count > 0:
            print_success(f"Cleaned {self.stats.changelogs_cleaned_count} changelog(s)")

    def phase_7_post_changelogs(self):
        """Phase 7: Post changelogs to Discord using multi-webhook config"""
        if not self.post:
            return

        # Skip if changelogs were already posted during phase 4
        if self.changelog:
            print_info("Changelogs already posted during generation phase")
            return

        print_header("Phase 7: Posting Changelogs to Discord")

        import subprocess
        post_script = self.base_dir / "tools" / "post.py"

        if not post_script.exists():
            print_error("post.py not found")
            return

        # Use post.py with --new flag to post to all configured webhooks
        # that subscribe to this project's channel
        try:
            cmd = [
                str(post_script),
                "--new",
                "--project", self.project.name,
            ]

            if self.dry_run:
                cmd.append("--dry-run")

            print_info(f"Running: {' '.join(cmd)}")

            result = subprocess.run(
                cmd,
                cwd=str(self.base_dir),
                capture_output=False,  # Let output go directly to terminal
                check=False
            )

            if result.returncode == 0:
                print_success("Successfully posted changelogs via post.py")
                # Note: post.py handles its own statistics and version tracking
            else:
                print_error(f"post.py exited with code {result.returncode}")
                self.stats.changelog_post_failures += 1

        except Exception as e:
            print_error(f"Failed to run post.py: {e}")
            self.stats.changelog_post_failures += 1

    def cleanup(self):
        """Clean up temporary files"""
        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)

    def print_summary(self):
        """Print final summary statistics"""
        print_header("Sync Complete")

        print(f"Total versions available: {self.stats.total_versions}")

        if self.project.is_github_based:
            # GitHub-based project summary
            print(f"Archive directory: {self.archive_dir}")
            print(f"Source repository: {self.source_dir}")
        else:
            # npm-based project summary
            archived_versions = len(list(self.original_dir.glob("cli-v*.js")))
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

        if self.do_cleanup:
            if self.stats.changelogs_cleaned_count > 0:
                print_success(
                    f"Cleaned {self.stats.changelogs_cleaned_count} changelog(s)"
                )

        if self.post:
            if self.stats.changelogs_posted_count > 0:
                print_success(
                    f"Posted {self.stats.changelogs_posted_count} changelog(s) to Discord"
                )

        # Print any failures
        total_failures = (
            self.stats.download_failures
            + self.stats.prettier_failures
            + self.stats.diff_generation_failures
            + self.stats.changelog_generation_failures
            + self.stats.changes_generation_failures
            + self.stats.changelog_cleanup_failures
            + self.stats.changelog_post_failures
        )
        if total_failures > 0:
            print_warning(f"Total failures: {total_failures}")

    def run(self):
        """Execute the sync process"""
        try:
            project_display = self.project.name.replace("-", " ").title()
            title = f"{project_display} Archive Sync Tool"
            print(colored(title, Colors.BOLD + Colors.PURPLE))
            print(colored("=" * len(title), Colors.PURPLE))

            # Setup
            self.setup_directories()
            self.check_dependencies()

            # Get all versions (from npm or GitHub)
            if self.project.is_github_based:
                all_versions = self.get_github_releases()
            else:
                all_versions = self.get_npm_versions()

            # Execute phases
            if self.project.is_github_based:
                # GitHub-based projects
                self.sync_github_repo(all_versions)
                # Skip prettify phase for GitHub projects (source is already readable)
                self.phase_3_generate_diffs(all_versions)
            else:
                # npm-based projects
                self.phase_1_download_originals(all_versions)
                self.phase_2_prettify_files()
                self.phase_3_generate_diffs(all_versions)

            # Common phases for both project types
            self.phase_4_generate_changelogs()
            self.phase_5_generate_changes()
            self.phase_6_cleanup_changelogs()
            self.phase_7_post_changelogs()

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

        # Get all available versions from diff files (works for both npm and GitHub projects)
        diff_files = list(self.diff_dir.glob("v*.diff"))
        available_versions = []
        for f in diff_files:
            # Extract version from diff filename (handle both v1.0.69.diff and v1.0.69-2.diff)
            match = RE_DIFF_VERSION.match(f.name)
            if match:
                ver = match.group(1)
                if ver not in available_versions:
                    available_versions.append(ver)

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
                if self.project.is_github_based:
                    # GitHub mode: use git tags
                    # Find all versions to determine the previous one
                    diff_versions = []
                    for f in self.diff_dir.glob("v*.diff"):
                        match = RE_DIFF_VERSION.match(f.name)
                        if match and match.group(1) not in diff_versions:
                            diff_versions.append(match.group(1))
                    all_versions_sorted = sorted(diff_versions, key=version.parse)
                    try:
                        version_index = all_versions_sorted.index(version_str)
                        if version_index > 0:
                            prev_version = all_versions_sorted[version_index - 1]
                            print_info(
                                f"Generating diff iteration {diff_iteration} for v{version_str}"
                            )
                            if self.generate_diff_github(prev_version, version_str, diff_iteration):
                                self.stats.diff_generated_count += 1
                            else:
                                self.stats.diff_generation_failures += 1
                        else:
                            print_warning(f"No previous version found for v{version_str}")
                    except ValueError:
                        print_warning(f"Version {version_str} not found in available versions")
                else:
                    # npm mode: use pretty files
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
        description="Multi-Project Archive Sync Tool - Download and process CLI versions from npm",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --project claude-code                    # Download Claude Code files (default)
  %(prog)s --project codex --prettier               # Download and prettify Codex files
  %(prog)s --project claude-code --prettier --diff  # Generate diffs for Claude Code
  %(prog)s --all                                    # Run all processing steps (includes cleanup and post)
  %(prog)s --all --latest                           # Process only the most recent version
  %(prog)s --changelog --cleanup                    # Generate and clean up changelogs
  %(prog)s --cleanup --post                         # Clean up existing changelogs and post to Discord
  %(prog)s --changelog --since v1.0.50              # Generate changelogs for v1.0.50 and newer
  %(prog)s --all --since 1.0.50                     # Process all steps for versions 1.0.50+
  %(prog)s --changelog --new-first                  # Generate changelogs (newest first)
  %(prog)s --prettier --diff --changelog            # Generate diffs and changelogs
  %(prog)s --diff --changes                         # Generate diffs and detailed changes
  %(prog)s --redo 69 --changelog                    # Redo changelog for v1.0.69
  %(prog)s --project codex --all                    # Process all Codex versions
        """,
    )

    parser.add_argument(
        "--project",
        type=str,
        choices=list(PROJECTS.keys()),
        default="claude-code",
        help=f"Project to sync (default: claude-code). Available: {', '.join(PROJECTS.keys())}",
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
        "--cleanup",
        action="store_true",
        help="Clean up changelog headers (remove duplicate headers and meta-commentary)",
    )

    parser.add_argument(
        "--post",
        action="store_true",
        help="Post new changelogs to Discord via webhook",
    )

    parser.add_argument(
        "--all",
        action="store_true",
        help="Run all processing steps (prettier, diff, changelog, cleanup, post - excludes changes)",
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

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate posting without actually sending to Discord (only affects --post)",
    )

    args = parser.parse_args()

    # Handle --all flag
    if args.all:
        args.prettier = True
        args.diff = True
        args.changelog = True
        args.cleanup = True
        args.post = True

    # --changelog will work independently and process available diffs

    # Disable colors if requested or if not a TTY
    if args.no_color or not sys.stdout.isatty():
        Colors.disable()

    # Find base directory (project root)
    script_path = Path(__file__).resolve()
    base_dir = script_path.parent.parent  # Go up from tools/ to project root

    # Get project configuration
    project = PROJECTS[args.project]

    # Create and run sync tool
    sync_tool = ClaudeCodeSync(
        base_dir=base_dir,
        project=project,
        prettier=args.prettier,
        diff=args.diff,
        changelog=args.changelog,
        changes=args.changes,
        cleanup=args.cleanup,
        post=args.post,
        latest=args.latest,
        since=args.since,
        new_first=args.new_first,
        redo=args.redo,
        dry_run=args.dry_run,
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
