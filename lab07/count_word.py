#!/usr/bin/python
import re,sys,glob
count=0
reg= r"\b"+re.escape(sys.argv[1])+r"\b"
for line in sys.stdin:
	line = line.lower()
	array = re.findall(reg,line)
	count += len(array)
print sys.argv[1] + " occurred " + str(count) + " times"
