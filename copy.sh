
#!/bin/sh

if [ -z $1 ]
then
	echo "Input day missing!"
else
	day=`printf %02d $1`
	cp -nv "main/day00.py" "main/day$day.py"
fi
