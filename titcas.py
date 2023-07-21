#! python3

import pyperclip, sys

if len(sys.argv) != 1:
    print("Usage: titcas")
    sys.exit()
text = pyperclip.paste()
newText = text.title()
pyperclip.copy(newText)
