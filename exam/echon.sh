#!/bin/sh
echo what?
read n
she=6
echo $n
echo $((she/2))
echo $2
echo "count is "$#
for file in $*
do
	echo $file
	echo finish
done
echo 'she is $she'
echo "she is $she"
echo $(date)
