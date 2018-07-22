#!/bin/sh


# print HTTP header
# its best to print the header ASAP because 
# debugging is hard if an error stops a valid header being printed

echo Content-type: text/html
echo

# print page content

cat <<eof
<!DOCTYPE html>
<html lang="en">
<head>
<title></title>
</head>
<body>
Browser IP, Host and User Agent
<pre>
eof

# print all environment variables
# This is interpreted as HTML so we replace some chars by the equivalent HTML entity.
# Note this will not guarantee security in all contexts.

IP=$(env|
sed 's/&/\&amp;/;s/</\&lt;/g;s/>/\&gt;/g'|
egrep 'REMOTE_ADDR'|
sed 's/REMOTE_ADDR=//')
echo "Your browser is running at IP address:$IP"
echo ""
hostname=$(host $IP|
sed 's/.*pointer '//|
sed 's/ *.$//')
echo "Your browser is running on hostname:$hostname"
echo ""
agent=$(env|
sed 's/&/\&amp;/;s/</\&lt;/g;s/>/\&gt;/g'|
egrep 'HTTP_USER_AGENT'|
sed 's/HTTP_USER_AGENT=//')
echo "Your browser identifies as:$agent"
echo ""
cat <<eof
</pre>
</body>
</html>
eof
