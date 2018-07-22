#!/bin/sh
pat='^.*jpg$'
for file in *
do
        if [[ $file =~ $pat ]]
        then
                new_name=`(echo $file | sed -E 's/.jpg/.png/g')`
                if [ -f "$new_name" ]  #test -f  file exists and is a regular file
                then
                        echo "$new_name already exists"
                else
                        convert "$file" "$new_name"
                        rm "$file"
                fi
        fi
done

