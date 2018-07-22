#!/usr/bin/python
import re, sys
ind={}
pod={}
for line in sys.stdin:
	line = line.lower()
	line = re.sub(r'( )*s *$','',line)
	line = re.sub(r' +',' ',line)
	line = re.sub(r' $','',line)                                   #why there is a space at the end? use autotest to check
	a = re.findall('(\d+) (.*)',line)				#(\d+) (.*) will let it return a two-dimension array(num,name)
	if a[0][1] in ind:						#other language(with regex) also applied
		ind[a[0][1]] += int(a[0][0])				#the returned array contains str not int
		pod[a[0][1]] += 1					#if a[][] in ind check whether the key exists!!!!!!!!!
	else:
		ind[a[0][1]] = int(a[0][0])
		pod[a[0][1]] = 1
for key in sorted(ind):							#sort hash
	p = str(pod[key])
	i = str(ind[key])
	print key + " observations: " + p + " pods, "+ str(ind[key])+" individuals"
