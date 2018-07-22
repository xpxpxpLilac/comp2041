#!/usr/bin/python
import re,sys
count=0
for line in sys.stdin:
	array = re.findall('[a-zA-Z]+',line)	
	count += len(array)
print str(count) + "words"
