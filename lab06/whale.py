#!/usr/bin/python
import re,sys
ind=0
pod=0
for line in sys.stdin:
	#p = re.compile('[0-9]+')
	if sys.argv[1] in line:        #search for string in a line
		pod += 1
		digit = re.findall('[0-9]+',line)                    #like pattern matching find all matched element, return an array
		ind += int(digit[0])		
print sys.argv[1] + " observations: " + str(pod) +" pods, " + str(ind) +" individuals"
