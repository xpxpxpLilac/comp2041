#!/usr/bin/python3 
import sys,re
from collections import defaultdict
for line in sys.stdin.readlines():
	line = re.sub(' *\n$','',line)
	line = re.sub(' +',' ',line)
	a = line.split(' ')	
	for words in a:
		d = defaultdict(dict)
		word = words.lower()
		b = list(word)
		for char in b:
			if char in d:
				d[char] += 1
			else:
				d[char] = 1
		count = d[b[0]]
		last = 0
		for char in b:
			if count != d[char]:
				last = 1
				break
		if last != 0:
			line = re.sub(words+' ?','',line)
	print(line)
