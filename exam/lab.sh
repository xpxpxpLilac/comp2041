#!/bin/sh
newline=''
pat='<![^!<>]*>'
pat1='<[!<>]*>'
while read line
do
	echo "$line"
	if [[ $line =~ $pat ]]
	then
		echo "$line" | egrep '<![^!<>]*>'
	elif [[ $line =~ $pat1 ]]
	then
		echo "==================="
		$newline=$(echo "$line" | sed -E 's/<([^!<>]*)>/cat \1/g')
	fi
	echo "$newline"
done
