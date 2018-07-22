#!/bin/sh
pat='htm$'
for file in *
do
    if [[ $file =~ $pat ]]
    then
	name=$(echo "$file" | sed -E 's/.htm/.html/g')
	if [ -f "$name" ]
	then
		echo "$name exists"
		exit 1
	else
		mv "$file" "$name"
	fi
    fi
done
