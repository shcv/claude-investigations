"""Shared color utilities for CLI output."""


class Colors:
    """ANSI color codes for output"""
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
    import sys
    print(colored(f"✗ Error: {message}", Colors.RED), file=sys.stderr)


def print_info(message: str):
    """Print a cyan info message"""
    print(colored(message, Colors.CYAN))
