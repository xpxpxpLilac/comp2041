#!/bin/sh
folder=(\')$
song='^#'
year=1992
folder_name=""
num=1
mkdir "$2" 
wget -q -O- 'https://en.wikipedia.org/wiki/Triple_J_Hottest_100?action=raw' |
head -n 600 | tail -n 478 |
sed -E 's/\*.+//g' |
sed -E '/\#ffd\;\"$/,/^|$/d' |
sed -E 's/^\#.*\([0-9]{4}\)$//g' |
sed -E '/^$/d'| 
while read name
do
    if [[ $name =~ $folder ]]
    then 
	year=$(expr $year + 1)
	folder_name=$(echo $name | sed -E 's/.*\[\[//g;s/\|[0-9]{4}.*//g')
	mkdir "$2"/"$folder_name" 
    elif [[ $name =~ $song ]]
    then
	song_name=$(echo $name | sed -E 's/\[[^][|]+\|//g')
	title=$(echo $song_name | sed -E 's/\x20\xE2\x80\x93\x20/%/g' | cut -d'%' -f2 | sed -E 's/\"//g;s/\[//g;s/\]//g')   #deal with unicode
	singer=$(echo $song_name | sed -E 's/\x20\xE2\x80\x93\x20/%/g' | cut -d'%' -f1 | sed -E 's/#( )?//g;s/\[//g;s/\]//g;s/$/.mp3/g')
	track=$num
	num=$(expr $num + 1)
	if [ $num -eq 11 ] 
	then 
		num=$(expr $num - 10)
        fi
	old_name=$(echo "$track - $title - $singer")
	long_song_name=$(echo $old_name | sed -E 's/\//-/g')
	cp -b "$1" "$2"/"$folder_name"                                               #copy a file and put it into directory directly
	mv "$2"/"$folder_name"/"$1" "$2/$folder_name/$long_song_name"                #rename the file you have to tell the path where it is


    fi
done
