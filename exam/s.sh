#!/bin/sh
cat $1|
while read line
do
	echo hello
	echo $line
done
