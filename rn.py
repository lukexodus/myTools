#! python3
# rn.py (Remove Newlines) - Removes the newlines in the text from the clipboard.

# Made for windows

import pyperclip

clipboard = pyperclip.paste()
clipboard = str(clipboard)
clipboard = list(clipboard)
for j in range(4):
    clipboard.append(" ")
i = 0
while i < len(clipboard):
    if i == len(clipboard) - 4:
        break
    if (
        clipboard[i] == " "
        and clipboard[i + 1] == "\r"
        and clipboard[i + 2] == "\n"
        and clipboard[i + 3] == "\r"
        and clipboard[i + 4] == "\n"
    ):
        i += 1
        continue

    elif clipboard[i] == "\r" and (
        (clipboard[i - 1] == "\n" and clipboard[i - 2] == "\r")
        or (
            clipboard[i + 1] == "\n"
            and clipboard[i + 2] == "\r"
            and clipboard[i + 3] == "\n"
        )
    ):
        i += 1
        continue

    elif clipboard[i] == "\n" and (
        (
            clipboard[i - 1] == "\r"
            and clipboard[i - 2] == "\n"
            and clipboard[i - 3] == "\r"
        )
        or (clipboard[i + 1] == "\r" and clipboard[i + 2] == "\n")
    ):
        i += 1
        continue

    if clipboard[i] == " " and clipboard[i + 1] == "\r" and clipboard[i + 2] == "\n":
        del clipboard[i]
        del clipboard[i]
        clipboard[i] = " "

    if clipboard[i] == "\r" and clipboard[i + 1] == "\n":
        clipboard[i] = " "
        del clipboard[i + 1]
    i += 1
for k in range(4):
    clipboard.pop()


pocessedText = "".join(clipboard)
pyperclip.copy(pocessedText)
