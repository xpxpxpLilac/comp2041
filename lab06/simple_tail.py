#!/usr/bin/python
import sys
for file in sys.argv[1:]:
	content = open(file,"r")
	lines = content.readlines()
	x = len(lines)
	for n in range(x):
		if((x - n)<=10):
			sys.stdout.write(lines[n])
	content.close()
	
