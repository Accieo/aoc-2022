#!/bin/sh

cookie="$(<cookie.txt)"

if [ -z $1 ]
then
	echo "Input day missing!"
else
	day=`printf %02d $1`
	curl --cookie "session=$cookie" "https://adventofcode.com/2022/day/$1/input" > "input/day$day.txt"
fi
