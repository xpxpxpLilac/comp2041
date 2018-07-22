#!/usr/bin/python
import re, sys, glob,math


for file in sys.argv[1:]:
	content = open(file,"r")
	h = dict()
	copy= dict()
	singer = dict()

	for line in content:
		line = line.lower()
		line = line.rstrip()
	  	for word in re.split(r'[^a-z]+',line):
			if word !="":
				if word in h:
					h[word] += 1
				else:
					h[word] = 1
					copy[word] = 0
	#for x in h:
	#	print "For "+ x + " is "+ str(h[x])
	for musicfile in sorted(glob.glob("lyrics/*.txt")):
		total = 0
		for key in copy:
			copy[key]=0
	    	content = open(musicfile,"r")
	    	name = re.sub("lyrics/","",musicfile)
	    	name = re.sub(".txt","",name)
	    	name = re.sub("_"," ",name)
		for line in content:
			line = line.lower()
			all = re.findall("[A-Za-z]+",line)
			total += len(all)

			for key in h:
				reg= r"\b"+re.escape(key)+r"\b"
				array = re.findall(reg,line)
				copy[key] += len(array)

		result = 0

		for key in h:
			result += h[key]*math.log(float(copy[key]+1)/float(total))

		singer[name] = result

#	for w in sorted(singer, key=singer.get,reverse=True):   here is a way sort the value
	val = max(singer, key=singer.get)
	print file + " most resembles the work of "+val+ "(log-probability="+"{:.1f}".format(singer[val])+")"
