#!/bin/bash

I="/Users/parrt/github/msan501/projects/regression"
O="/tmp/regression"

while true
do
	if test $I/css/article.css -nt $O/regression.html || \
           test $I/regression.xml -nt $O/regression.html
	then
		java -jar /Users/parrt/github/bookish/target/bookish-1.0-SNAPSHOT.jar -target html -o /tmp/regression $I/project.xml
	fi
	sleep .2s
done
