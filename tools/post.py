#!/usr/bin/env python3
"""
Discord Changelog Poster

Posts Claude Code changelogs to Discord via webhook, creating forum threads for each version.
Tracks the last posted version to enable automatic posting of new changelogs.
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import List, Optional, Tuple
import requests
from packaging import version

# Try to load .env file if python-dotenv is available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # python-dotenv not installed, skip loading .env file
    pass

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
    """Print a blue info message"""
    print(colored(f"ℹ {message}", Colors.CYAN))


# Constants
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL", "")
MAX_MESSAGE_LENGTH = 2000
LAST_POSTED_FILE = ".last_posted_version"
UPLOAD_STATE_FILE = ".upload_state.json"
CHANGELOG_DIR = Path("archive/changelog")

# Discord webhook rate limit: 5 requests per 2 seconds
# We'll be conservative and use 4 requests per 2 seconds to be safe
RATE_LIMIT_REQUESTS = 4
RATE_LIMIT_PERIOD = 2.0  # seconds


class RateLimiter:
    """Simple rate limiter for Discord webhook requests"""

    def __init__(self, max_requests: int, time_period: float):
        """
        Args:
            max_requests: Maximum number of requests allowed in time_period
            time_period: Time period in seconds
        """
        self.max_requests = max_requests
        self.time_period = time_period
        self.request_times: List[float] = []

    def wait_if_needed(self):
        """Wait if necessary to comply with rate limits"""
        now = time.time()

        # Remove requests older than the time period
        self.request_times = [t for t in self.request_times if now - t < self.time_period]

        # If we've hit the limit, wait until the oldest request expires
        if len(self.request_times) >= self.max_requests:
            oldest = self.request_times[0]
            sleep_time = self.time_period - (now - oldest)
            if sleep_time > 0:
                print_info(f"Rate limit: waiting {sleep_time:.1f}s before next request...")
                time.sleep(sleep_time)
                # Clean up again after sleeping
                now = time.time()
                self.request_times = [t for t in self.request_times if now - t < self.time_period]

        # Record this request
        self.request_times.append(time.time())


def get_project_root() -> Path:
    """Find the project root directory"""
    current = Path.cwd()
    while current != current.parent:
        # Check for various archive structures
        if (current / "archive" / "changelog").exists():
            return current
        if (current / "archive" / "claude-code" / "changelog").exists():
            return current
        if (current / "tools" / "post.py").exists():
            return current
        current = current.parent
    raise RuntimeError("Could not find project root")


def load_upload_state(project_root: Path, project_name: Optional[str] = None) -> dict:
    """Load the upload state from JSON file"""
    if project_name:
        state_file = project_root / f".upload_state_{project_name}.json"
    else:
        state_file = project_root / UPLOAD_STATE_FILE
    if not state_file.exists():
        return {}

    try:
        return json.loads(state_file.read_text())
    except Exception as e:
        print_warning(f"Could not load upload state: {e}")
        return {}


def save_upload_state(project_root: Path, state: dict, project_name: Optional[str] = None):
    """Save the upload state to JSON file"""
    if project_name:
        state_file = project_root / f".upload_state_{project_name}.json"
    else:
        state_file = project_root / UPLOAD_STATE_FILE
    try:
        state_file.write_text(json.dumps(state, indent=2) + "\n")
    except Exception as e:
        print_error(f"Could not save upload state: {e}")


def get_version_state(state: dict, version_str: str) -> Optional[dict]:
    """Get the upload state for a specific version"""
    return state.get(version_str)


def mark_version_complete(state: dict, version_str: str):
    """Mark a version as completely uploaded and remove from state"""
    if version_str in state:
        del state[version_str]


def update_version_state(state: dict, version_str: str, thread_id: str, chunks_posted: int, total_chunks: int):
    """Update the upload state for a version"""
    state[version_str] = {
        "thread_id": thread_id,
        "chunks_posted": chunks_posted,
        "total_chunks": total_chunks
    }


def extract_version_from_filename(filename: str) -> Optional[str]:
    """Extract version string from changelog filename"""
    match = re.match(r"changelog-v?(.+)\.md$", filename)
    return match.group(1) if match else None


def extract_version_from_path(path: Path) -> Optional[str]:
    """Extract version string from changelog file path"""
    return extract_version_from_filename(path.name)


def get_all_changelogs(changelog_dir: Path) -> List[Tuple[version.Version, Path]]:
    """Get all changelog files sorted by version"""
    changelogs = []
    for file_path in changelog_dir.glob("changelog-*.md"):
        ver_str = extract_version_from_path(file_path)
        if ver_str:
            try:
                ver = version.parse(ver_str)
                changelogs.append((ver, file_path))
            except Exception as e:
                print_warning(f"Could not parse version from {file_path.name}: {e}")

    changelogs.sort(key=lambda x: x[0])
    return changelogs


def get_last_posted_version(project_root: Path, project_name: Optional[str] = None) -> Optional[version.Version]:
    """Read the last posted version from tracking file"""
    if project_name:
        last_posted_file = project_root / f".last_posted_version_{project_name}"
    else:
        last_posted_file = project_root / LAST_POSTED_FILE
    if not last_posted_file.exists():
        return None

    try:
        ver_str = last_posted_file.read_text().strip()
        return version.parse(ver_str)
    except Exception as e:
        print_warning(f"Could not read last posted version: {e}")
        return None


def save_last_posted_version(project_root: Path, ver: version.Version, project_name: Optional[str] = None):
    """Save the last posted version to tracking file"""
    if project_name:
        last_posted_file = project_root / f".last_posted_version_{project_name}"
    else:
        last_posted_file = project_root / LAST_POSTED_FILE
    last_posted_file.write_text(str(ver) + "\n")


def parse_changelog_sections(content: str) -> List[Tuple[str, str]]:
    """
    Parse a changelog into semantic sections.

    Returns a list of (section_type, content) tuples where section_type is:
    - 'title': The # heading
    - 'summary': ## Summary section
    - 'section': ## New Features, ## Improvements, etc.
    - 'feature': ### Feature Name subsection
    - 'content': Non-header content belonging to previous section
    """
    sections = []
    lines = content.split('\n')
    current_section = []
    current_type = 'content'

    for line in lines:
        # Check what type of line this is
        if line.startswith('# ') and not line.startswith('## '):
            # Title (# Changelog for version X.X.X)
            if current_section:
                sections.append((current_type, '\n'.join(current_section)))
            current_section = [line]
            current_type = 'title'
        elif line.startswith('## '):
            # Major section header
            if current_section:
                sections.append((current_type, '\n'.join(current_section)))
            current_section = [line]
            if 'Summary' in line:
                current_type = 'summary'
            else:
                current_type = 'section'
        elif line.startswith('### '):
            # Feature/subsection header
            if current_section:
                sections.append((current_type, '\n'.join(current_section)))
            current_section = [line]
            current_type = 'feature'
        elif line.strip() == '---':
            # Horizontal rule - end of feature, include with current section
            current_section.append(line)
            sections.append((current_type, '\n'.join(current_section)))
            current_section = []
            current_type = 'content'
        else:
            # Regular content line
            current_section.append(line)

    # Don't forget the last section
    if current_section:
        sections.append((current_type, '\n'.join(current_section)))

    return sections


def smart_chunk_changelog(content: str, max_length: int = MAX_MESSAGE_LENGTH) -> List[str]:
    """
    Split a changelog into chunks at logical boundaries.

    Strategy:
    1. Parse into semantic sections (title, summary, features, etc.)
    2. Keep title + summary together in first chunk
    3. Start new chunks at major section headers (## headers)
    4. Split features to keep chunks focused but not too small
    5. Combine small trailing sections (Bug Fixes, Notes)
    """
    sections = parse_changelog_sections(content)

    if not sections:
        return [content] if content else []

    # Filter out empty content sections
    sections = [(t, c) for t, c in sections if c.strip()]

    chunks = []
    current_chunk_parts = []
    current_length = 0

    def flush_chunk():
        nonlocal current_chunk_parts, current_length
        if current_chunk_parts:
            chunk_text = '\n'.join(current_chunk_parts).strip()
            if chunk_text:
                chunks.append(chunk_text)
        current_chunk_parts = []
        current_length = 0

    for i, (section_type, section_content) in enumerate(sections):
        section_length = len(section_content) + 1  # +1 for newline

        # If this single section is too long, we need to split it
        if section_length > max_length:
            flush_chunk()

            # Fall back to line-by-line splitting for this oversized section
            lines = section_content.split('\n')
            for line in lines:
                line_length = len(line) + 1
                if current_length + line_length > max_length:
                    flush_chunk()
                current_chunk_parts.append(line)
                current_length += line_length
            continue

        # Decide whether to start a new chunk based on section type and size
        should_break = False

        # Title always starts the first chunk (don't break before it)
        # Summary should stay with title if they fit together
        if section_type == 'title':
            should_break = False
        elif section_type == 'summary':
            # Keep summary with title if possible
            should_break = False
        elif section_type == 'section':
            # Major section headers (## New Features, ## Bug Fixes, etc.)
            # Break before them UNLESS the current chunk is small
            # This allows combining small trailing sections
            if current_chunk_parts and current_length > max_length * 0.25:
                should_break = True
        elif section_type == 'feature':
            # Features (### Feature Name)
            # Break if current chunk is getting large (>50% full)
            if current_length > max_length * 0.5:
                should_break = True

        # Always break if adding this would exceed the limit
        if current_length + section_length > max_length:
            should_break = True

        if should_break:
            flush_chunk()

        current_chunk_parts.append(section_content)
        current_length += section_length

    # Flush any remaining content
    flush_chunk()

    # Post-process: merge very small trailing chunks
    if len(chunks) > 1:
        merged_chunks = []
        i = 0
        while i < len(chunks):
            chunk = chunks[i]

            # If this is a small chunk and we can merge with next
            while (i + 1 < len(chunks) and
                   len(chunk) < max_length * 0.3 and
                   len(chunk) + len(chunks[i + 1]) + 2 <= max_length):
                chunk = chunk + '\n\n' + chunks[i + 1]
                i += 1

            merged_chunks.append(chunk)
            i += 1

        chunks = merged_chunks

    return chunks


def chunk_message(content: str, max_length: int = MAX_MESSAGE_LENGTH) -> List[str]:
    """
    Split message into chunks that fit within Discord's character limit.

    For changelogs (detected by '# Changelog' header), uses smart semantic splitting.
    For other content, falls back to simple line-based splitting.
    """
    if len(content) <= max_length:
        return [content]

    # Use smart chunking for changelogs
    if content.strip().startswith('# Changelog'):
        return smart_chunk_changelog(content, max_length)

    # Fall back to simple line-based splitting for non-changelogs
    chunks = []
    current_chunk = ""

    lines = content.split("\n")

    for line in lines:
        # If a single line is too long, we need to split it
        if len(line) > max_length:
            if current_chunk:
                chunks.append(current_chunk)
                current_chunk = ""

            for i in range(0, len(line), max_length):
                chunks.append(line[i:i + max_length])
        else:
            if len(current_chunk) + len(line) + 1 > max_length:
                chunks.append(current_chunk)
                current_chunk = line
            else:
                if current_chunk:
                    current_chunk += "\n" + line
                else:
                    current_chunk = line

    if current_chunk:
        chunks.append(current_chunk)

    return chunks


def post_to_discord(
    thread_name: str,
    content: str,
    rate_limiter: RateLimiter,
    version_str: str,
    upload_state: dict,
    project_root: Path,
    dry_run: bool = False,
    resume_thread_id: Optional[str] = None,
    resume_from_chunk: int = 0,
    project_name: Optional[str] = None
) -> Tuple[bool, Optional[str], int]:
    """
    Post a message to Discord webhook, creating a forum thread or resuming an existing one.

    Args:
        thread_name: The name of the forum thread to create
        content: The message content
        rate_limiter: Rate limiter to prevent hitting Discord's limits
        version_str: Version string for tracking
        upload_state: Current upload state dictionary
        project_root: Project root path
        dry_run: If True, don't actually post (just simulate)
        resume_thread_id: Thread ID to resume posting to (if resuming)
        resume_from_chunk: Chunk index to resume from (0-based)

    Returns:
        Tuple of (success, thread_id, chunks_posted)
    """
    chunks = chunk_message(content)
    total_chunks = len(chunks)

    if dry_run:
        if resume_from_chunk > 0:
            print_info(f"DRY RUN: Would resume thread '{thread_name}' from chunk {resume_from_chunk + 1}/{total_chunks}")
        else:
            print_info(f"DRY RUN: Would create thread '{thread_name}' with {total_chunks} message(s)")
        for i, chunk in enumerate(chunks, 1):
            print_info(f"  Message {i}: {len(chunk)} characters")
        return (True, "dry_run_thread_id", total_chunks)

    thread_id = resume_thread_id
    start_chunk = resume_from_chunk

    try:
        # If not resuming, create the thread with the first chunk
        if start_chunk == 0:
            rate_limiter.wait_if_needed()

            first_payload = {
                "content": chunks[0],
                "thread_name": thread_name
            }

            response = requests.post(
                f"{WEBHOOK_URL}?wait=true",
                json=first_payload,
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()

            # Extract thread_id from response
            response_data = response.json()
            thread_id = response_data.get("channel_id")

            if not thread_id:
                print_error("Could not get thread_id from webhook response")
                return (False, None, 0)

            # Save state after first chunk
            update_version_state(upload_state, version_str, thread_id, 1, total_chunks)
            save_upload_state(project_root, upload_state, project_name)

            start_chunk = 1

        # Post remaining chunks
        for i in range(start_chunk, total_chunks):
            rate_limiter.wait_if_needed()

            chunk_payload = {"content": chunks[i]}
            chunk_response = requests.post(
                f"{WEBHOOK_URL}?thread_id={thread_id}",
                json=chunk_payload,
                headers={"Content-Type": "application/json"}
            )
            chunk_response.raise_for_status()

            # Update state after each chunk
            chunks_posted = i + 1
            update_version_state(upload_state, version_str, thread_id, chunks_posted, total_chunks)
            save_upload_state(project_root, upload_state, project_name)

        return (True, thread_id, total_chunks)

    except requests.exceptions.RequestException as e:
        print_error(f"Failed to post to Discord: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print_error(f"Response: {e.response.text}")
        # State has already been saved up to the last successful chunk
        chunks_posted = start_chunk if start_chunk > 0 else 0
        return (False, thread_id, chunks_posted)


def post_changelog(
    file_path: Path,
    rate_limiter: RateLimiter,
    upload_state: dict,
    project_root: Path,
    dry_run: bool = False,
    project_name: Optional[str] = None
) -> bool:
    """Post a single changelog file to Discord, resuming if partially uploaded"""
    ver_str = extract_version_from_path(file_path)
    if not ver_str:
        print_error(f"Could not extract version from {file_path.name}")
        return False

    thread_name = f"v{ver_str}"

    try:
        content = file_path.read_text()
    except Exception as e:
        print_error(f"Could not read {file_path}: {e}")
        return False

    # Check if we're resuming a partial upload
    version_state = get_version_state(upload_state, ver_str)
    resume_thread_id = None
    resume_from_chunk = 0

    if version_state:
        chunks_posted = version_state.get("chunks_posted", 0)
        total_chunks = version_state.get("total_chunks", 0)
        resume_thread_id = version_state.get("thread_id")

        if chunks_posted < total_chunks and resume_thread_id:
            print_info(f"Resuming {file_path.name} from chunk {chunks_posted + 1}/{total_chunks}...")
            resume_from_chunk = chunks_posted
        else:
            print_info(f"Posting {file_path.name} as '{thread_name}'...")
    else:
        print_info(f"Posting {file_path.name} as '{thread_name}'...")

    success, thread_id, chunks_posted = post_to_discord(
        thread_name,
        content,
        rate_limiter,
        ver_str,
        upload_state,
        project_root,
        dry_run,
        resume_thread_id,
        resume_from_chunk,
        project_name
    )

    if success:
        # Mark as complete and remove from state
        mark_version_complete(upload_state, ver_str)
        save_upload_state(project_root, upload_state, project_name)
        print_success(f"Posted {thread_name} ({chunks_posted} chunks)")
    else:
        print_error(f"Failed to complete {thread_name} (posted {chunks_posted} chunks)")

    return success


def parse_version_arg(arg: str, changelog_dir: Path) -> Optional[Path]:
    """Parse a version argument (either a file path or version string)"""
    # Check if it's a file path
    path = Path(arg)
    if path.exists() and path.is_file():
        return path

    # Try to interpret as version string
    # Remove 'v' prefix if present
    ver_str = arg[1:] if arg.startswith('v') else arg

    # Try to find the corresponding changelog file
    changelog_file = changelog_dir / f"changelog-v{ver_str}.md"
    if changelog_file.exists():
        return changelog_file

    return None


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Post Claude Code changelogs to Discord forum channel",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Environment Variables:
  DISCORD_WEBHOOK_URL    Discord webhook URL for posting (required)

Examples:
  # Set webhook URL
  export DISCORD_WEBHOOK_URL='https://discord.com/api/webhooks/...'

  # Post specific changelog files
  %(prog)s archive/changelog/changelog-v1.0.67.md

  # Post specific versions
  %(prog)s v1.0.67 v1.0.68

  # Post all new changelogs since last posted version
  %(prog)s --new

  # Post all changelogs (careful!)
  %(prog)s --all

  # Dry run (don't actually post)
  %(prog)s --dry-run --new
"""
    )

    parser.add_argument(
        "versions",
        nargs="*",
        help="Changelog files or version numbers to post (e.g., 'v1.0.67' or 'archive/changelog/changelog-v1.0.67.md')"
    )

    parser.add_argument(
        "--new",
        action="store_true",
        help="Post all changelogs newer than the last posted version"
    )

    parser.add_argument(
        "--all",
        action="store_true",
        help="Post all changelogs (use with caution!)"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate posting without actually sending to Discord"
    )

    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable colored output"
    )

    args = parser.parse_args()

    if args.no_color or not sys.stdout.isatty():
        Colors.disable()

    # Check for webhook URL
    if not WEBHOOK_URL:
        print_error("DISCORD_WEBHOOK_URL environment variable not set")
        print_info("Set it with: export DISCORD_WEBHOOK_URL='your-webhook-url'")
        return 1

    # Find project root
    try:
        project_root = get_project_root()
    except RuntimeError as e:
        print_error(str(e))
        return 1

    changelog_dir = project_root / CHANGELOG_DIR

    # Determine which changelogs to post
    files_to_post: List[Tuple[version.Version, Path]] = []

    if args.all:
        # Post all changelogs
        print_header("Posting All Changelogs")
        files_to_post = get_all_changelogs(changelog_dir)

    elif args.new:
        # Post changelogs newer than last posted
        print_header("Posting New Changelogs")
        last_posted = get_last_posted_version(project_root)
        all_changelogs = get_all_changelogs(changelog_dir)

        if last_posted is None:
            print_info("No last posted version found, will post all changelogs")
            files_to_post = all_changelogs
        else:
            print_info(f"Last posted version: v{last_posted}")
            files_to_post = [(v, p) for v, p in all_changelogs if v > last_posted]

    elif args.versions:
        # Post specific versions
        print_header("Posting Specific Changelogs")
        for ver_arg in args.versions:
            file_path = parse_version_arg(ver_arg, changelog_dir)
            if file_path:
                ver_str = extract_version_from_path(file_path)
                if ver_str:
                    try:
                        ver = version.parse(ver_str)
                        files_to_post.append((ver, file_path))
                    except Exception as e:
                        print_error(f"Could not parse version from {file_path}: {e}")
            else:
                print_error(f"Could not find changelog for: {ver_arg}")

    else:
        parser.print_help()
        return 0

    if not files_to_post:
        print_info("No changelogs to post")
        return 0

    # Sort by version
    files_to_post.sort(key=lambda x: x[0])

    print_info(f"Will post {len(files_to_post)} changelog(s)")

    # Load upload state
    upload_state = load_upload_state(project_root)

    # Create rate limiter
    rate_limiter = RateLimiter(RATE_LIMIT_REQUESTS, RATE_LIMIT_PERIOD)

    # Post each changelog
    posted_count = 0
    last_posted_ver = None

    for ver, file_path in files_to_post:
        if post_changelog(file_path, rate_limiter, upload_state, project_root, dry_run=args.dry_run):
            posted_count += 1
            last_posted_ver = ver
        else:
            print_error(f"Failed to post {file_path.name}, stopping")
            break

    # Update last posted version
    if last_posted_ver and not args.dry_run:
        save_last_posted_version(project_root, last_posted_ver)
        print_success(f"Updated last posted version to v{last_posted_ver}")

    print_header("Summary")
    print_success(f"Posted {posted_count} of {len(files_to_post)} changelog(s)")

    return 0 if posted_count == len(files_to_post) else 1


if __name__ == "__main__":
    sys.exit(main())
