#! python 3

'''
reModule.py - a working python program with examples from the py_regex pdf.
'''
import re

sentence = "This is a sample string."
print(sentence)

# This section shows how to use re.search to check for a string.
# Using bool() before it returns a bool.
check = bool(re.search(r'is',sentence))
print("Is 'is' in the sentence?", check)
check = bool(re.search(r'xyz', sentence))
print("Is 'xyz' in the sentence?", check)

# Case-sensitive check
check = bool(re.search(r'this', sentence))
print("Is 'this' in the sentence?", check)
check = bool(re.search(r'this', sentence, flags = re.I))
print("Is 'this' in the sentence (case-insensitive)?", check)

# Re.search in conditional expressions
if re.search(r'ring', sentence):
    print("'ring' present")
if not re.search(r'xyz', sentence):
    print("'xyz' not present")


