#!/bin/sh
echo "Using \"\$@\""
for var in "$@"
do
    echo $var
done

echo
echo 'Using $@'
for var in $@
do
    echo $var
done

echo
echo "Using \"\$*\""
for var in "$*"
do
    echo $var
done

echo
echo 'Using $*'
for var in $*
do
    echo $var
done
