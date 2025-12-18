#!/usr/bin/env python3
"""
Test runner for the prevent-emoji experiment.
Runs prompts through claude -p and checks for emoji characters in the output.
"""

import os
import subprocess
import re
import json
from pathlib import Path
from datetime import datetime

def has_emoji(text):
    """Check if text contains emoji characters using Unicode ranges."""
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

def run_claude_prompt(prompt_file):
    """Run a prompt through claude -p and return the output."""
    try:
        with open(prompt_file, 'r') as f:
            prompt = f.read().strip()
        
        result = subprocess.run(
            ['claude', '-p', prompt],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        return {
            'prompt': prompt,
            'output': result.stdout,
            'error': result.stderr,
            'return_code': result.returncode
        }
    except subprocess.TimeoutExpired:
        return {
            'prompt': prompt,
            'output': '',
            'error': 'Timeout expired',
            'return_code': -1
        }
    except Exception as e:
        return {
            'prompt': prompt,
            'output': '',
            'error': str(e),
            'return_code': -1
        }

def main():
    base_dir = Path(__file__).parent
    prompts_dir = base_dir / 'prompts'
    results_dir = base_dir / 'results'
    
    results_dir.mkdir(exist_ok=True)
    
    # Get all prompt files
    prompt_files = sorted(prompts_dir.glob('*.txt'))
    
    results = []
    emoji_found = []
    
    print(f"Running {len(prompt_files)} prompts...\n")
    
    for i, prompt_file in enumerate(prompt_files, 1):
        print(f"[{i}/{len(prompt_files)}] Testing: {prompt_file.name}")
        
        result = run_claude_prompt(prompt_file)
        
        if result['return_code'] != 0:
            print(f"  ❌ Error: {result['error']}")
            continue
            
        # Save the output
        output_file = results_dir / f"{prompt_file.stem}_output.py"
        with open(output_file, 'w') as f:
            f.write(result['output'])
        
        # Check for emojis
        contains_emoji = has_emoji(result['output'])
        if contains_emoji:
            emoji_found.append(prompt_file.name)
            print(f"  🎯 EMOJI FOUND!")
        else:
            print(f"  ⚪ No emoji detected")
        
        results.append({
            'prompt_file': prompt_file.name,
            'prompt': result['prompt'],
            'output_file': output_file.name,
            'contains_emoji': contains_emoji,
            'output_length': len(result['output']),
            'timestamp': datetime.now().isoformat()
        })
    
    # Save summary
    summary = {
        'total_prompts': len(prompt_files),
        'successful_runs': len(results),
        'emoji_found_count': len(emoji_found),
        'emoji_found_files': emoji_found,
        'results': results,
        'timestamp': datetime.now().isoformat()
    }
    
    with open(base_dir / 'experiment_results.json', 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"\n=== SUMMARY ===")
    print(f"Total prompts: {summary['total_prompts']}")
    print(f"Successful runs: {summary['successful_runs']}")
    print(f"Prompts that generated emoji: {summary['emoji_found_count']}")
    
    if emoji_found:
        print(f"\nSuccessful prompts:")
        for filename in emoji_found:
            print(f"  - {filename}")
    else:
        print("\nNo prompts generated emoji characters.")
    
    print(f"\nResults saved to: experiment_results.json")

if __name__ == '__main__':
    main()