#!/usr/bin/python3
import sys,re
from collections import defaultdict
d=defaultdict(dict)
count=int(sys.argv[1])
length = 0
now = 0
for line in sys.stdin.readlines():
	copy = line
	length += 1
	line = line.lower()
	line = re.sub(r'^ *','',line)
	line = re.sub(r' +',' ',line)
	if line not in d:
		d[line] = 1
		now += 1
#	print(copy, end="")
	if ( now == count ):
		break
if ( now == count ):
	print(str(now)+ " distinct lines seen after "+str(length)+" lines read.")
else:
	print("End of input reached after "+str(length)+" lines read -  "+ str(count)+" different lines not seen.") 
