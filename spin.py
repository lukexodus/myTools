#! python3
# spin.py - Adds spaces to the start
# of each line of text on the clipboard.

import pyperclip, sys

numTimes = int(sys.argv[1])

text = pyperclip.paste() 

lines = text.split("\n")

for i in range(len(lines)):
    lines[i] = " " * numTimes + lines[i]
text = "\n".join(lines)
pyperclip.copy(text)