#! python3

# 1c.py [One Cloze number] - Sets all cloze number within the text with the specified number (this is for Anki cloze cards)

import pyperclip, sys, re

if len(sys.argv) == 1:
    sub = "1"
elif len(sys.argv) == 2:
    sub = sys.argv[1]
else:
    print("Usage: 1c <number to substitute (default is '1')> ")
    sys.exit()
text = pyperclip.paste()
clozeRegex = re.compile(r"(({{c)\d+(::))")
substitutedText = clozeRegex.sub(f"{{{{c{sub}::", text)
pyperclip.copy(substitutedText)
