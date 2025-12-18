#!/usr/bin/env python3
"""
Test prevention hypotheses for emoji generation.
Creates subdirectories with different CLAUDE.md configurations and tests them.
"""

import os
import subprocess
import re
import json
import shutil
from pathlib import Path
from datetime import datetime

def has_emoji(text):
    """Check if text contains emoji characters."""
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002702-\U000027B0"  # dingbats
        u"\U000024C2-\U0001F251"
        u"\U0001F900-\U0001F9FF"  # supplemental symbols
        u"\U0001FA70-\U0001FAFF"  # symbols and pictographs extended-a
        "]+", 
        flags=re.UNICODE
    )
    return bool(emoji_pattern.search(text))

# Prevention hypotheses to test
PREVENTION_HYPOTHESES = {
    "explicit_no_emoji": {
        "name": "Explicit No Emoji Instruction",
        "claude_md": """# CLAUDE.md

## Code Generation Rules
- NEVER use emoji characters in code output
- Use only ASCII characters in all generated code
- Replace any visual symbols with text descriptions
""",
        "description": "Direct instruction to avoid emojis"
    },
    
    "ascii_only": {
        "name": "ASCII-Only Requirement",
        "claude_md": """# CLAUDE.md

## Output Constraints
- All code output must use ASCII characters only (codes 32-126)
- No Unicode characters beyond basic ASCII
- Use text representations instead of symbols
""",
        "description": "Restrict to ASCII character set"
    },
    
    "professional_context": {
        "name": "Professional Context Emphasis",
        "claude_md": """# CLAUDE.md

## Code Standards
- Generate professional, production-ready code
- Follow enterprise coding standards
- Avoid decorative or casual elements in code
- Use formal, business-appropriate representations
""",
        "description": "Emphasize professional/enterprise context"
    },
    
    "terminal_compatibility": {
        "name": "Terminal Compatibility Focus",
        "claude_md": """# CLAUDE.md

## Compatibility Requirements
- All code must work in basic terminal environments
- Ensure compatibility with legacy systems
- Use only characters available in standard terminals
- Avoid special Unicode that may not render properly
""",
        "description": "Focus on terminal/legacy system compatibility"
    },
    
    "accessibility_emphasis": {
        "name": "Accessibility-First Approach",
        "claude_md": """# CLAUDE.md

## Accessibility Guidelines
- All output must be screen reader friendly
- Use text descriptions instead of visual symbols
- Ensure code is accessible to users with visual impairments
- Prioritize clear, descriptive text over symbols
""",
        "description": "Emphasize accessibility concerns"
    },
    
    "debugging_focus": {
        "name": "Debugging/Testing Context",
        "claude_md": """# CLAUDE.md

## Code Generation Context
- Generate code suitable for debugging and testing
- Use simple, clear representations
- Avoid characters that might cause encoding issues
- Focus on functional clarity over visual appeal
""",
        "description": "Frame as debugging/testing scenario"
    },
    
    "plain_text_preference": {
        "name": "Plain Text Preference",
        "claude_md": """# CLAUDE.md

## Output Style
- Prefer plain text representations
- Use word descriptions instead of symbols
- Generate code that works well in plain text environments
- Avoid decorative or ornamental characters
""",
        "description": "General preference for plain text"
    },
    
    "substitute_suggestions": {
        "name": "Provide ASCII Substitutes",
        "claude_md": """# CLAUDE.md

## Symbol Representation
- When symbols are needed, use ASCII alternatives:
  - Happy: :) or :-) 
  - Celebration: * or !
  - Status: [OK], [DONE], [FAIL]
  - Progress: === or --- or ###
- Always provide text-based alternatives to Unicode symbols
""",
        "description": "Explicitly suggest ASCII alternatives"
    }
}

def run_test_in_directory(test_dir, prompt, timeout=30):
    """Run claude -p in a specific directory and return results."""
    original_cwd = os.getcwd()
    
    try:
        os.chdir(test_dir)
        
        result = subprocess.run(
            ['claude', '-p', prompt],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        
        return {
            'output': result.stdout,
            'error': result.stderr,
            'return_code': result.returncode
        }
        
    except subprocess.TimeoutExpired:
        return {
            'output': '',
            'error': 'Timeout expired',
            'return_code': -1
        }
    except Exception as e:
        return {
            'output': '',
            'error': str(e),
            'return_code': -1
        }
    finally:
        os.chdir(original_cwd)

def test_hypothesis(base_dir, hypothesis_key, hypothesis_data, test_prompt):
    """Test a single prevention hypothesis."""
    
    # Create test directory
    test_dir = base_dir / f"test_{hypothesis_key}"
    test_dir.mkdir(exist_ok=True)
    
    # Write CLAUDE.md file
    claude_md_path = test_dir / "CLAUDE.md"
    with open(claude_md_path, 'w') as f:
        f.write(hypothesis_data['claude_md'])
    
    print(f"\n{'='*60}")
    print(f"Testing: {hypothesis_data['name']}")
    print(f"Directory: {test_dir}")
    print(f"{'='*60}")
    
    # Run the test
    result = run_test_in_directory(test_dir, test_prompt)
    
    if result['return_code'] != 0:
        print(f"❌ Error: {result['error']}")
        return {
            'hypothesis': hypothesis_key,
            'name': hypothesis_data['name'],
            'description': hypothesis_data['description'],
            'success': False,
            'output': result['output'],
            'error': result['error'],
            'contains_emoji': None,
            'prevented_emoji': None
        }
    
    # Check results
    contains_emoji = has_emoji(result['output'])
    prevented_emoji = not contains_emoji
    
    print(f"Output: {result['output'][:100]}{'...' if len(result['output']) > 100 else ''}")
    print(f"Contains emoji: {contains_emoji}")
    print(f"Prevention successful: {prevented_emoji}")
    
    if prevented_emoji:
        print("✅ SUCCESS: Emoji prevention worked!")
    else:
        print("❌ FAILED: Still generated emojis")
    
    return {
        'hypothesis': hypothesis_key,
        'name': hypothesis_data['name'],
        'description': hypothesis_data['description'],
        'success': True,
        'output': result['output'],
        'error': result['error'],
        'contains_emoji': contains_emoji,
        'prevented_emoji': prevented_emoji
    }

def main():
    base_dir = Path(__file__).parent
    results_dir = base_dir / 'prevention_results'
    
    # Clean and recreate results directory
    if results_dir.exists():
        shutil.rmtree(results_dir)
    results_dir.mkdir()
    
    # Test prompt that we know generates emojis
    test_prompt = "Write Python code that prints a happy face"
    
    print(f"Testing prevention hypotheses with prompt: '{test_prompt}'")
    print(f"Results will be saved in: {results_dir}")
    
    # Test baseline (no CLAUDE.md)
    print(f"\n{'='*60}")
    print(f"Testing: BASELINE (No CLAUDE.md)")
    print(f"{'='*60}")
    
    baseline_dir = results_dir / "test_baseline"
    baseline_dir.mkdir()
    baseline_result = run_test_in_directory(baseline_dir, test_prompt)
    baseline_contains_emoji = has_emoji(baseline_result['output']) if baseline_result['return_code'] == 0 else None
    
    print(f"Baseline output: {baseline_result['output'][:100]}{'...' if len(baseline_result['output']) > 100 else ''}")
    print(f"Baseline contains emoji: {baseline_contains_emoji}")
    
    # Test each hypothesis
    results = []
    successful_preventions = []
    
    for hypothesis_key, hypothesis_data in PREVENTION_HYPOTHESES.items():
        result = test_hypothesis(results_dir, hypothesis_key, hypothesis_data, test_prompt)
        results.append(result)
        
        if result['success'] and result['prevented_emoji']:
            successful_preventions.append(result)
    
    # Generate summary
    summary = {
        'test_prompt': test_prompt,
        'baseline_contains_emoji': baseline_contains_emoji,
        'baseline_output': baseline_result['output'],
        'total_hypotheses': len(PREVENTION_HYPOTHESES),
        'successful_runs': len([r for r in results if r['success']]),
        'successful_preventions': len(successful_preventions),
        'prevention_rate': len(successful_preventions) / len([r for r in results if r['success']]) * 100 if results else 0,
        'results': results,
        'timestamp': datetime.now().isoformat()
    }
    
    # Save detailed results
    with open(base_dir / 'prevention_results.json', 'w') as f:
        json.dump(summary, f, indent=2)
    
    # Print final summary
    print(f"\n{'='*60}")
    print(f"FINAL SUMMARY")
    print(f"{'='*60}")
    print(f"Test prompt: {test_prompt}")
    print(f"Baseline generated emoji: {baseline_contains_emoji}")
    print(f"Total hypotheses tested: {summary['total_hypotheses']}")
    print(f"Successful runs: {summary['successful_runs']}")
    print(f"Successful preventions: {summary['successful_preventions']}")
    print(f"Prevention success rate: {summary['prevention_rate']:.1f}%")
    
    if successful_preventions:
        print(f"\nSuccessful prevention methods:")
        for result in successful_preventions:
            print(f"  ✅ {result['name']}")
            print(f"     Description: {result['description']}")
    else:
        print(f"\n❌ No prevention methods were successful")
    
    print(f"\nDetailed results saved to: prevention_results.json")
    print(f"Individual test directories in: prevention_results/")

if __name__ == '__main__':
    main()