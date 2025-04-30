#! python3

# pdh.py [Push Down Header]

import pyperclip

def main():
    text = pyperclip.paste()
    
    cleaned_text = text.replace("# ", "## ");

    pyperclip.copy(cleaned_text)
    print("Processed text copied to clipboard!")

if __name__ == "__main__":
    main()