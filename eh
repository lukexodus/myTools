#!/usr/bin/env python3
"""
eh [Extract Headers] - Extract module titles from clipboard and format them.
Uses wl-clipboard for clipboard operations.
"""

import subprocess
import re
import sys


def get_clipboard():
    """Get text from clipboard using wl-paste."""
    try:
        result = subprocess.run(
            ['wl-paste'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error reading from clipboard: {e}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print("Error: wl-paste not found. Please install wl-clipboard.", file=sys.stderr)
        sys.exit(1)


def set_clipboard(text):
    """Set text to clipboard using wl-copy."""
    try:
        subprocess.run(
            ['wl-copy'],
            input=text,
            text=True,
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error writing to clipboard: {e}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print("Error: wl-copy not found. Please install wl-clipboard.", file=sys.stderr)
        sys.exit(1)


def extract_module_titles(text):
    """
    Extract module titles from text.
    Matches pattern: ## Module N: Title
    Returns list of titles (text after '## Module N: ')
    """
    # Pattern matches ## followed by optional whitespace, then text ending with :, then captures the title
    pattern = r'^#+\s+[^:]+:\s+(.+)$'
    
    titles = []
    for line in text.split('\n'):
        match = re.match(pattern, line.strip())
        if match:
            titles.append(match.group(1))
    
    return titles


def format_output(titles):
    """
    Format titles as markdown headers separated by horizontal rules.
    """
    if not titles:
        return ""
    
    formatted_parts = []
    for title in titles:
        formatted_parts.append(f"# {title}\n\n\n\n---")
    
    return '\n\n'.join(formatted_parts)


def main():
    # Get clipboard content
    clipboard_text = get_clipboard()
    
    if not clipboard_text.strip():
        print("Clipboard is empty.", file=sys.stderr)
        sys.exit(1)
    
    # Extract module titles
    titles = extract_module_titles(clipboard_text)
    
    if not titles:
        print("No module titles found in clipboard.", file=sys.stderr)
        sys.exit(1)
    
    # Format output
    output = format_output(titles)
    
    # Set to clipboard
    set_clipboard(output)
    
    print(f"Extracted {len(titles)} module titles and copied to clipboard.")


if __name__ == '__main__':
    main()
