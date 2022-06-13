#! python3
# bpa.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()  # gets the text in the clipboard

# Separate lines and add stars.
lines = text.split("\n")

for i in range(len(lines)):  # loop through all indexes for "lines" list
    lines[i] = "* " + lines[i]  # add star to each string in "lines" list
text = "\n".join(lines)  # joins the list values into a string, seperated by '\n'
pyperclip.copy(text)  # puts the processed text into the clipboard
