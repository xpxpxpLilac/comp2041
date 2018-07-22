#!/bin/sh
sf=""
mf=""
lf=""
for file in *
do
        set -- `wc -l $file`
        if test $1 -lt 10
        then
		sf+=" $file"
        elif test $1 -lt 100
        then
		mf+=" $file"
        else
		lf+=" $file"
        fi
done
echo "Small files:$sf"
echo "Medium-sized files:$mf"
echo "Large files:$lf"
