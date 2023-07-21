#! python3
# rnn.py (Remove Newlines \n; Compact i.e. ignores \n\n) - Removes the newlines from the text from the clipboard.

# Made for windows

import pyperclip

clipboard = pyperclip.paste()
clipboard = str(clipboard)
clipboard = list(clipboard)

for j in range(2):
    clipboard.append(" ")
i = 0
while i < len(clipboard):
    if i == len(clipboard) - 2:
        break
    if (
        clipboard[i] == " "
        and clipboard[i + 1] == "\n"
        and clipboard[i + 2] == "\n"
    ):
        i += 1
        continue

    # Disregard two subsequent newlines
    elif clipboard[i] == "\n":
        if (
            (clipboard[i - 1] == "\n")
            or (clipboard[i + 1] == "\n")
        ):
            del clipboard[i]
            continue
        else:
            clipboard[i] = " "

    if clipboard[i] == " " and clipboard[i + 1] == "\n":
        del clipboard[i]
        clipboard[i] = " "

    i += 1
for k in range(2):
    clipboard.pop()


pocessedText = "".join(clipboard)
pyperclip.copy(pocessedText)
