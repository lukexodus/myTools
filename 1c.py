#! python3

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
