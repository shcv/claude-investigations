#!/usr/bin/env python3
"""
Manual test to generate emoji-containing code for prevention testing.
"""

import subprocess
import re

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

# Test prompts that are likely to generate emojis
test_prompts = [
    "Write Python code that prints a happy face",
    "Create a function that returns celebration symbols",
    "Write code for a mood tracker with visual representations",
    "Generate code that displays weather conditions with symbols",
    "Create a status indicator function using visual symbols"
]

def test_prompt(prompt, timeout=15):
    """Test a single prompt and check for emoji output."""
    try:
        result = subprocess.run(
            ['claude', '-p', prompt],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        
        output = result.stdout
        print(f"\n{'='*60}")
        print(f"PROMPT: {prompt}")
        print(f"{'='*60}")
        print(output)
        print(f"{'='*60}")
        print(f"Contains emoji: {has_emoji(output)}")
        print(f"Return code: {result.returncode}")
        if result.stderr:
            print(f"Errors: {result.stderr}")
        
        return output, has_emoji(output)
        
    except subprocess.TimeoutExpired:
        print(f"TIMEOUT: {prompt}")
        return "", False
    except Exception as e:
        print(f"ERROR with '{prompt}': {e}")
        return "", False

if __name__ == "__main__":
    emoji_found = []
    
    for prompt in test_prompts:
        output, contains_emoji = test_prompt(prompt)
        if contains_emoji:
            emoji_found.append(prompt)
    
    print(f"\n\nSUMMARY:")
    print(f"Total prompts tested: {len(test_prompts)}")
    print(f"Prompts that generated emojis: {len(emoji_found)}")
    
    if emoji_found:
        print(f"Successful prompts:")
        for prompt in emoji_found:
            print(f"  - {prompt}")
    else:
        print("No prompts generated emoji characters.")