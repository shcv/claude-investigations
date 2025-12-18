#!/usr/bin/env python3
"""
Statistical test runner for emoji prevention hypotheses.
Runs each hypothesis multiple times and provides statistical analysis.
"""

import os
import subprocess
import re
import json
import shutil
import statistics
from pathlib import Path
from datetime import datetime
from collections import defaultdict

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

def test_hypothesis_multiple_trials(base_dir, hypothesis_key, hypothesis_data, test_prompt, num_trials=5):
    """Test a single prevention hypothesis multiple times."""
    
    # Create test directory
    test_dir = base_dir / f"test_{hypothesis_key}"
    test_dir.mkdir(exist_ok=True)
    
    # Write CLAUDE.md file
    claude_md_path = test_dir / "CLAUDE.md"
    with open(claude_md_path, 'w') as f:
        f.write(hypothesis_data['claude_md'])
    
    print(f"\n{'='*60}")
    print(f"Testing: {hypothesis_data['name']}")
    print(f"Running {num_trials} trials...")
    print(f"{'='*60}")
    
    trials = []
    successful_runs = 0
    prevented_emojis = 0
    unique_outputs = set()
    
    for trial in range(num_trials):
        print(f"  Trial {trial + 1}/{num_trials}...", end=" ", flush=True)
        
        result = run_test_in_directory(test_dir, test_prompt)
        
        if result['return_code'] != 0:
            print(f"❌ Error: {result['error']}")
            trials.append({
                'trial_number': trial + 1,
                'success': False,
                'output': result['output'],
                'error': result['error'],
                'contains_emoji': None,
                'prevented_emoji': None
            })
            continue
        
        # Check results
        successful_runs += 1
        contains_emoji = has_emoji(result['output'])
        prevented_emoji = not contains_emoji
        unique_outputs.add(result['output'].strip())
        
        if prevented_emoji:
            prevented_emojis += 1
            print("✅")
        else:
            print("❌")
        
        trials.append({
            'trial_number': trial + 1,
            'success': True,
            'output': result['output'],
            'error': result['error'],
            'contains_emoji': contains_emoji,
            'prevented_emoji': prevented_emoji
        })
    
    # Calculate statistics
    prevention_rate = (prevented_emojis / successful_runs * 100) if successful_runs > 0 else 0
    success_rate = (successful_runs / num_trials * 100)
    output_consistency = len(unique_outputs)
    
    print(f"\n  Results:")
    print(f"    Successful runs: {successful_runs}/{num_trials} ({success_rate:.1f}%)")
    print(f"    Prevention rate: {prevented_emojis}/{successful_runs} ({prevention_rate:.1f}%)")
    print(f"    Unique outputs: {output_consistency}")
    
    if successful_runs > 0:
        print(f"    Sample output: {list(unique_outputs)[0][:60]}{'...' if len(list(unique_outputs)[0]) > 60 else ''}")
    
    return {
        'hypothesis': hypothesis_key,
        'name': hypothesis_data['name'],
        'description': hypothesis_data['description'],
        'num_trials': num_trials,
        'successful_runs': successful_runs,
        'success_rate': success_rate,
        'prevented_emojis': prevented_emojis,
        'prevention_rate': prevention_rate,
        'unique_outputs': len(unique_outputs),
        'output_samples': list(unique_outputs),
        'trials': trials,
        'statistical_confidence': "High" if successful_runs >= 4 else "Medium" if successful_runs >= 2 else "Low"
    }

def run_baseline_trials(base_dir, test_prompt, num_trials=5):
    """Run baseline tests (no CLAUDE.md) multiple times."""
    print(f"\n{'='*60}")
    print(f"BASELINE TESTING (No CLAUDE.md)")
    print(f"Running {num_trials} trials...")
    print(f"{'='*60}")
    
    baseline_dir = base_dir / "test_baseline"
    baseline_dir.mkdir(exist_ok=True)
    
    # Ensure no CLAUDE.md exists
    claude_md_path = baseline_dir / "CLAUDE.md"
    if claude_md_path.exists():
        claude_md_path.unlink()
    
    trials = []
    successful_runs = 0
    contains_emoji_count = 0
    unique_outputs = set()
    
    for trial in range(num_trials):
        print(f"  Trial {trial + 1}/{num_trials}...", end=" ", flush=True)
        
        result = run_test_in_directory(baseline_dir, test_prompt)
        
        if result['return_code'] != 0:
            print(f"❌ Error")
            continue
        
        successful_runs += 1
        contains_emoji = has_emoji(result['output'])
        unique_outputs.add(result['output'].strip())
        
        if contains_emoji:
            contains_emoji_count += 1
            print("😊 (emoji)")
        else:
            print("📝 (no emoji)")
        
        trials.append({
            'trial_number': trial + 1,
            'success': True,
            'output': result['output'],
            'contains_emoji': contains_emoji
        })
    
    emoji_rate = (contains_emoji_count / successful_runs * 100) if successful_runs > 0 else 0
    
    print(f"\n  Baseline Results:")
    print(f"    Successful runs: {successful_runs}/{num_trials}")
    print(f"    Emoji generation rate: {contains_emoji_count}/{successful_runs} ({emoji_rate:.1f}%)")
    print(f"    Unique outputs: {len(unique_outputs)}")
    
    return {
        'num_trials': num_trials,
        'successful_runs': successful_runs,
        'contains_emoji_count': contains_emoji_count,
        'emoji_rate': emoji_rate,
        'unique_outputs': len(unique_outputs),
        'output_samples': list(unique_outputs),
        'trials': trials
    }

def main():
    base_dir = Path(__file__).parent
    results_dir = base_dir / 'statistical_results'
    
    # Clean and recreate results directory
    if results_dir.exists():
        shutil.rmtree(results_dir)
    results_dir.mkdir()
    
    # Configuration
    test_prompt = "Write Python code that prints a happy face"
    num_trials = 10  # Increased for better statistics
    
    print(f"STATISTICAL EMOJI PREVENTION TESTING")
    print(f"{'='*60}")
    print(f"Test prompt: '{test_prompt}'")
    print(f"Trials per hypothesis: {num_trials}")
    print(f"Results directory: {results_dir}")
    
    # Test baseline first
    baseline_results = run_baseline_trials(results_dir, test_prompt, num_trials)
    
    # Test each hypothesis
    hypothesis_results = []
    highly_effective = []
    moderately_effective = []
    ineffective = []
    
    for hypothesis_key, hypothesis_data in PREVENTION_HYPOTHESES.items():
        result = test_hypothesis_multiple_trials(
            results_dir, hypothesis_key, hypothesis_data, test_prompt, num_trials
        )
        hypothesis_results.append(result)
        
        # Categorize effectiveness
        if result['prevention_rate'] >= 90:
            highly_effective.append(result)
        elif result['prevention_rate'] >= 50:
            moderately_effective.append(result)
        else:
            ineffective.append(result)
    
    # Generate comprehensive summary
    summary = {
        'test_configuration': {
            'test_prompt': test_prompt,
            'trials_per_hypothesis': num_trials,
            'total_tests_run': (len(PREVENTION_HYPOTHESES) + 1) * num_trials,
            'timestamp': datetime.now().isoformat()
        },
        'baseline_results': baseline_results,
        'hypothesis_results': hypothesis_results,
        'statistical_summary': {
            'highly_effective': len(highly_effective),
            'moderately_effective': len(moderately_effective), 
            'ineffective': len(ineffective),
            'overall_success_rate': statistics.mean([r['prevention_rate'] for r in hypothesis_results if r['successful_runs'] > 0])
        },
        'effectiveness_categories': {
            'highly_effective': [r['name'] for r in highly_effective],
            'moderately_effective': [r['name'] for r in moderately_effective],
            'ineffective': [r['name'] for r in ineffective]
        }
    }
    
    # Save detailed results
    with open(base_dir / 'statistical_results.json', 'w') as f:
        json.dump(summary, f, indent=2)
    
    # Print comprehensive summary
    print(f"\n{'='*60}")
    print(f"STATISTICAL ANALYSIS SUMMARY")
    print(f"{'='*60}")
    print(f"Total tests executed: {summary['test_configuration']['total_tests_run']}")
    print(f"Baseline emoji rate: {baseline_results['emoji_rate']:.1f}%")
    print(f"Average prevention rate: {summary['statistical_summary']['overall_success_rate']:.1f}%")
    
    print(f"\nEFFECTIVENESS BREAKDOWN:")
    print(f"  Highly effective (≥90%): {len(highly_effective)} methods")
    print(f"  Moderately effective (50-89%): {len(moderately_effective)} methods")
    print(f"  Ineffective (<50%): {len(ineffective)} methods")
    
    if highly_effective:
        print(f"\n🏆 HIGHLY EFFECTIVE METHODS:")
        for result in sorted(highly_effective, key=lambda x: x['prevention_rate'], reverse=True):
            print(f"  • {result['name']}: {result['prevention_rate']:.1f}% prevention rate")
            print(f"    ({result['prevented_emojis']}/{result['successful_runs']} trials, {result['unique_outputs']} unique outputs)")
    
    if moderately_effective:
        print(f"\n⚠️  MODERATELY EFFECTIVE METHODS:")
        for result in sorted(moderately_effective, key=lambda x: x['prevention_rate'], reverse=True):
            print(f"  • {result['name']}: {result['prevention_rate']:.1f}% prevention rate")
    
    if ineffective:
        print(f"\n❌ INEFFECTIVE METHODS:")
        for result in ineffective:
            print(f"  • {result['name']}: {result['prevention_rate']:.1f}% prevention rate")
    
    print(f"\n📊 STATISTICAL CONFIDENCE:")
    for result in hypothesis_results:
        print(f"  • {result['name']}: {result['statistical_confidence']} confidence")
        print(f"    ({result['successful_runs']}/{result['num_trials']} successful runs)")
    
    print(f"\nDetailed results: statistical_results.json")
    print(f"Individual test directories: statistical_results/")

if __name__ == '__main__':
    main()