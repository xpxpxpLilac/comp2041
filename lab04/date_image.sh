#!/bin/sh
pat='.jpg$'
pat1='.png$'
for file in *
do	
	if [[ $file =~ $pat ]] || [[ $file =~ $pat1 ]]
	then
		ctime=$(echo `stat -c %y "$file"` | cut -d'.' -f1 | sed -E 's/-//g;s/://g;s/ //g;s/[0-9]{2}$//g;s/2017//g')
#		echo $ctime
		info=`ls -l "$file" | cut -d' ' -f 6-8`
		convert -gravity south -pointsize 36 -draw "text 0,10 '$info'" "$file" "$file"
		touch -m -t "$ctime" "$file"
	fi
done 

