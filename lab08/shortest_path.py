#!/usr/bin/python
import sys,re      
from sets import Set                     #sys.argv[0] is ./short_path
from collections import defaultdict		#set has many useful functions, union intersection remove..
d=defaultdict(dict)				#defaultdict(dict) can define any dimension dict, but dict() cannot do that
shortest=defaultdict(dict)
route=defaultdict(dict)
start = sys.argv[1]
dest = sys.argv[2]

if len(sys.argv) != 3:
	sys.exit('Wrong number of arguments')
else:
	for line in sys.stdin.readlines():
		st,to,dis = line.split()
		d[st][to] = int(dis)
		d[to][st] = int(dis)
	unreach = Set(d.keys())
	shortest[start]=0
	route[start]=""
	current = start
	while current and current != dest:
		unreach.remove(current)
		for town in unreach:
			if current in d and town in d[current]:	
				l = shortest[current] + d[current][town]		#find from current, if any town can make its shortest path
				if town not in shortest or shortest[town] > l:		#then update this town route via current
					shortest[town] = l
					route[town] = route[current] +" "+current 	#all shortest[town] is shortest currently
		min = 10000000
		current = ""
		for town in unreach:							#find shortest distance among all shortest path to towns, make this town as current 
			if town in shortest and shortest[town] < min:
				min = shortest[town]
				current = town						#when set is empty, finish the loop

	if dest not in shortest:
		print "NO route"
	else:
		print "Shortest route is length = "+ str(shortest[dest])+":"+route[dest]+" "+dest+"."				
	






