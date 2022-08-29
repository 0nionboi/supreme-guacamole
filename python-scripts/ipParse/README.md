# ipParsy.py
Requires python3.
## Usage
```
$ python3 ipParse.py <filename.txt>
```
ipParse.py will take a file with a list of IP addresses and ports, and sort them into seperate files with the port numbers appended to the file names.  For use with nmap.  See sample.txt for an example of what the input file needs to look like.  Don't try it with files that aren't formatted like this.  This format comes from nessus and similar network scanners.
See the sample-output folder to see what the output will look like.
