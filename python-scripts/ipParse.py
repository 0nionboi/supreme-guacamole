#! python3

'''
ipParse.py - takes input from a text file or clipboard, and returns a list of IPs from the file.
Created originally to parse IP outputs from Nessus scans.
'''

import sys, re # removed pyperclip because multipass

# Regex pattern for finding the IP addresses
ipPattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

ipAddresses = [] # Initialize the list for IPs to be stored

# Commenting this out, since it is old.
'''
for groups in ipPattern.findall():
    ipAddresses.append(groups[0])
'''
for i, line in enumerate(open(sys.argv[1])):
    for match in re.finditer(ipPattern, line):
        print(match.group())

