#!/usr/bin/env python3
# sp [Space Indenter] - Adds spaces to the start of each line of text on the clipboard.

# Made for Linux (Windows version commented out below)

import subprocess
import sys

# ========== ORIGINAL WINDOWS VERSION (COMMENTED OUT) ==========
# import pyperclip, sys
#
# numTimes = int(sys.argv[1])
#
# text = pyperclip.paste() 
#
# lines = text.split("\n")
#
# for i in range(len(lines)):
#     lines[i] = " " * numTimes + lines[i]
# text = "\n".join(lines)
# pyperclip.copy(text)
# ===============================================================


# ========== LINUX VERSION (using wl-clipboard) ==========
def get_clipboard():
    """Get clipboard content using wl-paste"""
    try:
        result = subprocess.run(['wl-paste'], capture_output=True, text=True, check=True)
        return result.stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: Could not read clipboard. Install wl-clipboard: sudo pacman -S wl-clipboard")
        return ""


def set_clipboard(text):
    """Set clipboard content using wl-copy"""
    try:
        subprocess.run(['wl-copy'], input=text, text=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: Could not write to clipboard.")
        return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: sp <number_of_spaces>")
        sys.exit(1)
    
    try:
        numTimes = int(sys.argv[1])
    except ValueError:
        print("Error: Argument must be a number")
        sys.exit(1)
    
    text = get_clipboard()
    if not text:
        sys.exit(1)
    
    # Strip trailing newline added by wl-paste
    text = text.rstrip('\n')
    
    lines = text.split("\n")
    
    for i in range(len(lines)):
        lines[i] = " " * numTimes + lines[i]
    
    text = "\n".join(lines)
    
    if set_clipboard(text):
        print(f"✓ Added {numTimes} spaces to {len(lines)} lines")
    else:
        sys.exit(1)
