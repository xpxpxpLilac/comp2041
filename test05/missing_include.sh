#!/bin/sh
pat='#include.*.h'
pat1='<.*>'
for name in $@
do
    cat $name|
    while read line
    do
       	if [[ $line =~ $pat ]]
	then 
	    if ! [[ $line =~ $pat1 ]]
	    then
	        file=$(echo "$line"| cut -d' ' -f2| sed -E 's/\"//g' )
	        if ! [[ -f $file ]]
	        then 
		    echo "$file included into $name does not exist"
	        fi
	    fi
        fi
    done 
done
