#!/usr/bin/python3
import sys,re,os
file = sys.argv[1]
f = open(file,"r")
w = open("copy","w")
for line in f:
	line = re.sub("[AEIOUaeiou]*","",line)
	w.write(line)
#	f.write(line)
w.close
f.close
os.rename("copy", file)
