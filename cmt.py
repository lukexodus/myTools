#! python3
import pyperclip, sys

if len(sys.argv) != 2:
    print('Usage: cmt <COMMENT_TYPE>')
    sys.exit()

commentType = sys.argv[1]
text = pyperclip.paste()
lines = text.split("\n")

if commentType == '/':
    for i in range(len(lines)):
        lines[i] = "// " + lines[i]
    text = "\n".join(lines)
    pyperclip.copy(text)
elif commentType == '#':
    for i in range(len(lines)):
        lines[i] = "# " + lines[i]
    text = "\n".join(lines)
    pyperclip.copy(text)
else:
    print('! Comment type not implemented !')
    sys.exit()