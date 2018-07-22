#!/usr/bin/python3
import sys,re
from collections import defaultdict
for line in sys.stdin.readlines():
	d=defaultdict(dict)
	for word in line.split():
		if word not in d:
			d[word] = 1
		else:
			d[word] += 1
	for w in sorted(d.keys()):	
#for w in sorted(d, key=d.get, reverse=False):
#		print(w)
		for count in range(d[w]):
			print(w+" ",end="")
	print("")
