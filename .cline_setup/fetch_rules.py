#!/usr/bin/env python3
import urllib.request
import json

# Additional files to fetch
files_to_fetch = [
    'testing-strategy.md',
    'codebase-onboarding.md',
    'baby-steps.md',
    'code-review.md',
    'sequential-thinking.md'
]

base_url = 'https://raw.githubusercontent.com/cline/prompts/main/.clinerules/'

for filename in files_to_fetch:
    url = base_url + filename.replace(' ', '%20')
    try:
        print(f"\n{'='*60}")
        print(f"=== {filename} ===")
        print(f"{'='*60}")
        response = urllib.request.urlopen(url)
        content = response.read().decode()
        print(content)
        print(f"\n--- END {filename} ---\n")
    except Exception as e:
        print(f"Error fetching {filename}: {e}")
