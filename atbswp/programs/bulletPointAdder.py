#! python3

'''
bulletPointAdder.py - Adds wikipedia bullet points to the start of each line of text on the clipboard.
'''

import pyperclip
text = pyperclip.paste()

# Separate text lines and add stars.
lines = text.split('\n')
for i in range(len(lines)): #loop through all indexes in the "lines" list
	lines[i] = '* ' + lines[i] # adds star to each string in "lines" list

text = '\n'.join(lines)

pyperclip.copy(text)