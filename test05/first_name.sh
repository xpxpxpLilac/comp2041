#!/bin/sh
cat $1|
egrep 'COMP[29]041'|
cut -d'|' -f3|
cut -d',' -f2 |
sed -E 's/^ //g;s/( )*$//g'|
sed -E 's/( [A-Za-z]+)*//g'|
sort|
uniq -c|
sort -n|
tail -1|
sed -E 's/^ *[ 0-9]+//g'
