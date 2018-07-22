#!/usr/bin/python
import re, sys
if((len(sys.argv)-1) != 2):
	print "Usage: ./echon.py <number of lines> <string>"
elif(sys.argv[1].isdigit() == False):
	print "./echon.py: argument 1 must be a non-negative integer"
elif(sys.argv[1] < 0):
	print "/echon.py: argument 1 must be a non-negative integer"
else:
	for x in range(int(sys.argv[1])):
    		print sys.argv[2]
