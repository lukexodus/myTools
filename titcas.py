#! python3

# titcas.py [Transform into TITle CASe] - Sets first letter of every word to uppercase and the rest of the letters as lowercase

import pyperclip, sys

if len(sys.argv) != 1:
    print("Usage: titcas")
    sys.exit()
text = pyperclip.paste()
newText = text.title()
pyperclip.copy(newText)
