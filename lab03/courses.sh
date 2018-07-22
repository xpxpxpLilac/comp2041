#!/bin/sh
init=$1
fir=${init::1}
wget -q -O- "http://www.handbook.unsw.edu.au/vbook2017/brCoursesByAtoZ.jsp?StudyLevel=Undergraduate&descr=$fir" "http://www.handbook.unsw.edu.au/vbook2017/brCoursesByAtoZ.jsp?StudyLevel=Postgraduate&descr=$fir"|
grep $1|
cat -A|
sed -E 's/<p>.*<\/p>//'|
sed -E 's/(\^I)+//'|
sed -E 's/(<[^<>]+>)+//'|
sed -E 's/(<[^<>]+>)*\$//'|
egrep -v '^$'|
sed 'N;s/\n/ /'|
cat -A|
sed -E 's/ \$/$/'|
sed -E 's/\$//'|
sort |
uniq 

 
