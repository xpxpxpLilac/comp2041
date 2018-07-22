#!/bin/sh
if [ $# -eq 1 ]&&[ "$1" = "music/*" ]
then
	for file1 in $@
	do
		echo $file1       #"$@" "$file1"/$file1 all folder names get together
				  #$@ "$file1" same
				  #$@ $file1 seperate
	done	 
else
	for file in "$@"
	do
		echo $file
	done
fi | 
while read files
do
	 folder="$(ls "$files")"
         echo "$folder" |
         while read name
         do	
	 	title="$(echo "$name" | sed -E 's/ - /%/g'| cut -d'%' -f2)"
                artist="$(echo "$name" |sed -E 's/ - /%/g'| cut -d'%' -f3 | sed -E 's/.mp3//g')"
                track="$(echo "$name" |sed -E 's/ - /%/g'| cut -d'%' -f1)"
                album="$(echo "$files" | sed -E 's/.*music\///g;s/^ //g;s/\/$//g')"
                year="$(echo "$files" | sed -E 's/.*, //g')"
                id3 -t "$title" "$files/$name" >/dev/null
                id3 -T "$track" "$files/$name" >/dev/null
                id3 -a "$artist" "$files/$name" >/dev/null
                id3 -A "$album" "$files/$name" >/dev/null
                id3 -y "$year" "$files/$name" >/dev/null
         done
done

