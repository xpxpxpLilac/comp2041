#!/usr/bin/python
import re, sys, glob
reg= r"\b"+re.escape(sys.argv[1])+r"\b"
for file in sorted(glob.glob("lyrics/*.txt")):
	count=0
	total=0
	content = open(file,"r")
	name = re.sub("lyrics/","",file)
	name = re.sub(".txt","",name)
	name = re.sub("_"," ",name)
	for line in content:
		line = line.lower()
		all = re.findall("[A-Za-z]+",line)
		array = re.findall(reg,line)
		total += len(all)
		count += len(array)
	value = float(count)/float(total)
	print("%4d/%6d = %.9f %s" %(count, total, value, name))
