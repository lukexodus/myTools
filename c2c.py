#! python3
# c2c.py (Convert double colons) - Convert double colons `::` into
# their HTML entity counterparts `&colon;&colon;`

# Made for windows

import pyperclip
import re


def replace_colons_with_entities(input_string):
    # Use re.sub() to find and replace '::' with '&colon;&colon;'
    output_string = re.sub(
        r'(?<!\{\{c\d)::', ':&ZeroWidthSpace;:', input_string)
    return output_string


clipboard = pyperclip.paste()
clipboardStr = str(clipboard)

pocessedText = replace_colons_with_entities(clipboardStr)
pyperclip.copy(pocessedText)
