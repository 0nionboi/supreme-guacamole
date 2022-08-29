#! python3

'''
ipParse.py v0.1 - takes input from a text file or clipboard, and returns a list of IPs from the file.
Created originally to parse IP outputs from Nessus scans.

TO DO: Add the ability to read copied text from the clipboard.
I will develop this at a later date if I'm not working from Multipass.

Release Notes:
v0.1 - first working version.
'''

import sys, re, os.path # removed pyperclip because multipass clipboard issues (HyperV?)

def ipCheck(fileName, ipAddress):
# ipCheck checks if the file exists.  If it doesn't it returns TRUE.  If it does,
# it checks for the IP in the list, returns TRUE if present, FALSE otherwise.
    if not os.path.exists(fileName):
        return True # Checks if file exists
    ipList = [] # Holds the existing IPs in the file
    checkFile = open(fileName, 'r') # Opens the file, assuming existance
    for line in checkFile:
        ipList.append(line.strip("\n")) # Appends each IP in the file to ipList
    checkFile.close() # done with file.
    if ipAddress in ipList: # If exists, return false
        return False
    else: # If exists, return true
        return True

# Regex pattern for finding the IP addresses. ipPattern is legacy, not actually
# used anymore.  lineRegex is used to tokenize strings from the pdf copy.
ipPattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
lineRegex = re.compile(r' |/|\(|\)|\\|\n|\,')

# Open the file that was passed in the argument.
file_text = open(sys.argv[1], 'r')
for line in file_text: # Goes through line by line.
    parsedLine = re.split(lineRegex, line) # parses the line with regex.
    while '' in parsedLine: # Removes emptyset from parsed lists.
        parsedLine.remove('')
    head, sep, tail = sys.argv[1].partition('.') # Parses the filename,
    # so that new filename can be created from it.
    x = 1 # Setup loop for all the ports in each line.
    while x < len(parsedLine): # Loops thru ports.
        fileName = "{}_{}_{}.txt".format(head,parsedLine[x],parsedLine[x+1])
        if ipCheck(fileName, parsedLine[0]): # gets T or F from ipCheck func
            writeFile = open(fileName, 'a')
            writeFile.write(parsedLine[0] + "\n")
            writeFile.close()
        x += 2 # Important to increment by 2 for IP/protocol pairs

# Close original file.
file_text.close()
