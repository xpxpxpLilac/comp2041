#!/bin/sh
cat $1|
sed 's/[AEIOUaeiou]*//g' >> copy
mv copy $1
