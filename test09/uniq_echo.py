#!/usr/bin/python3
import sys,re
from collections import defaultdict
d=defaultdict(dict)
s=""
for ele in sys.argv[1:]:
	if ele not in d:
		s = s +ele+" "
		d[ele] = 1
print(s)
