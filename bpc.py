#! python3
# bpc.py [Bullet Point Compacter] - Removes the newlines between the bullet points

import pyperclip
import re

def remove_extra_newlines():
    text = pyperclip.paste()
    
    # Remove newlines between bullet points (assuming they start with '- ' or '* ')
    # cleaned_text = re.sub(r'([*-]\s.*)\n\s*\n([*-]\s)', r'\1\n\2', text)
    cleaned_text = re.sub(r'([*-]\s.*)\n\s*\n([*-]\s)', r'\1\n\2', text)
    
    # Additional ChatGPT content fixes
    cleaned_text = re.sub(r'#+\s\*\*Key [pP]oints\*\*', '**Key Points**', cleaned_text)    
    cleaned_text = re.sub(r'#+\sKey [pP]oints', '**Key Points**', cleaned_text)    
    cleaned_text = re.sub(r'#+\sOverview', '**Overview**', cleaned_text)    
    cleaned_text = re.sub(r'#+\s\*\*Example\*\*', '**Example**', cleaned_text)    
    cleaned_text = re.sub(r'#+\sNotes', '**Notes**', cleaned_text)    
    cleaned_text = re.sub(r'#+\s\*\*Output\*\*', '**Output**', cleaned_text)    
    cleaned_text = re.sub(r'#+\s\*\*Conclusion\*\*', '**Conclusion**', cleaned_text)    
    cleaned_text = re.sub(r'#+\sConclusion', '**Conclusion**', cleaned_text)    
    cleaned_text += "\n\n---\n\n" 

    pyperclip.copy(cleaned_text)
    print("Processed text copied to clipboard!")

if __name__ == "__main__":
    remove_extra_newlines()
