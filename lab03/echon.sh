#!/bin/sh

re='^[^0-9]+$'
str='^-[0-9]+$'

if test $# -ne 2  #numeric comparison is different from string 
then 	
	echo "Usage: ./echon.sh <number of lines> <string>"
	exit 1 
elif [[ $1 =~ $re ]]  #match a pattern
then	
	echo "./echon.sh: argument 1 must be a non-negative integer"
	exit 1

elif [[ $1 =~ $str ]]
then 
	echo "./echon.sh: argument 1 must be a non-negative integer"

else 
	n=0
        while test $1 -gt $n
	do
		echo $2	
	 	n=`expr $n + 1`  
	done

fi






