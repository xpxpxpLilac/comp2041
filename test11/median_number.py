#!/usr/bin/python3
import sys
array = []
for ele in sys.argv[1:]:
	array.append(int(ele))
array = sorted(array)
size = len(array)//2
print(array[size])
