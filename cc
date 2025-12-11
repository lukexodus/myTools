#!/usr/bin/env python3
# c2c.py (Convert double colons) - Convert double colons `::` into
# their HTML entity counterparts `&colon;&colon;`

# Made for Linux (Windows version commented out below)

import subprocess
import re

# ========== ORIGINAL WINDOWS VERSION (COMMENTED OUT) ==========
# import pyperclip
# import re
#
# def replace_colons_with_entities(input_string):
#     # Use re.sub() to find and replace '::' with '&colon;&colon;'
#     output_string = re.sub(
#         r'(?<!\{\{c\d)::', ':&ZeroWidthSpace;:', input_string)
#     return output_string
#
# clipboard = pyperclip.paste()
# clipboardStr = str(clipboard)
#
# pocessedText = replace_colons_with_entities(clipboardStr)
# pyperclip.copy(pocessedText)
# ===============================================================


# ========== LINUX VERSION (using wl-clipboard) ==========
def replace_colons_with_entities(input_string):
    """Convert double colons to use zero-width space separator"""
    # Use re.sub() to find and replace '::' with ':&ZeroWidthSpace;:'
    output_string = re.sub(
        r'(?<!\{\{c\d)::', ':&ZeroWidthSpace;:', input_string)
    return output_string


def get_clipboard():
    """Get clipboard content using wl-paste"""
    try:
        result = subprocess.run(
            ['wl-paste'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError:
        print("Error: Could not read from clipboard.")
        return ""
    except FileNotFoundError:
        print("Error: wl-paste not found. Please install wl-clipboard:")
        print("  sudo apt install wl-clipboard  (Debian/Ubuntu)")
        print("  sudo dnf install wl-clipboard  (Fedora)")
        print("  sudo pacman -S wl-clipboard    (Arch)")
        return ""


def set_clipboard(text):
    """Set clipboard content using wl-copy"""
    try:
        subprocess.run(
            ['wl-copy'],
            input=text,
            text=True,
            check=True
        )
        return True
    except subprocess.CalledProcessError:
        print("Error: Could not write to clipboard.")
        return False
    except FileNotFoundError:
        print("Error: wl-copy not found. Please install wl-clipboard first.")
        return False


if __name__ == "__main__":
    # Get clipboard content
    clipboard = get_clipboard()
    
    if clipboard:
        # Strip trailing newline added by wl-paste
        clipboard = clipboard.rstrip('\n')
        
        # Process the text
        processed_text = replace_colons_with_entities(clipboard)
        
        # Copy back to clipboard
        if set_clipboard(processed_text):
            print("✓ Text processed and copied to clipboard successfully!")
        else:
            print("✗ Failed to copy to clipboard.")
    else:
        print("✗ No text found in clipboard or error reading clipboard.")
