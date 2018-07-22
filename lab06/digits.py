#!/usr/bin/python
import re, sys

for line in sys.stdin.readlines():
	line = re.sub(r'[0-4]',"<",line)
	line = re.sub(r'[6-9]',">",line)
	sys.stdout.write(line)
	
