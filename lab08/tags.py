#!/usr/bin/python 
import sys, re, subprocess
flag = 0
table={}
for arg in sys.argv[1:]:
	if arg == "-f":
		flag = 1
		continue				    #continue in python
	webpage = subprocess.check_output(["wget", "-q", "-O-", arg], universal_newlines=True)
	webpage = re.sub(r'>[^<>]+<','>\n<',webpage)
	webpage = re.sub(r'<![^<>]+>','',webpage)
	a = re.findall('<\w+',webpage)
	for line in a:
		line = line.lower()			    #transform tolower case
		line = re.sub(r'<','',line)
		#print line
		if line in table:
			table[line] += 1
		else:
			table[line] = 1	
	#sys.stdout.write(webpage)
if flag == 0:
	for key in sorted(table):
		print key + " " + str(table[key])
else:
	for key in sorted(sorted(table), key=table.get):    #sorted(table) first sort table by key, then sort by value
		print key + " " + str(table[key])	    #such that when the value is same it's shown in 								    #alphabet
