#! python3

# tic.py [Transform Into Code (HTML)] - Add opening and closing tags of the element code to the copied text.

import pyperclip

clipboard = pyperclip.paste()

clipboard = "<code>" + clipboard + "</code>"

pyperclip.copy(clipboard)