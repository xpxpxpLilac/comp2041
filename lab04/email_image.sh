#!/bin/sh
for arg2 in "$@"
do
	info="$(echo "$arg2" | sed -E 's/.png//g;s/.jpg//g')"
	#echo $info
	display $arg2
	echo "Address to e-mail this image to?"
	read address   #read from line

	echo "Message to accompany image?"
	read content
    echo "$content"|mutt -s "$info" -e 'set copy=no' -a $arg2 -- $address
	
	echo "$arg2" sent to $address
done
