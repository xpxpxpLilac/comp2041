#!/usr/bin/perl
print "#!/usr/bin/python3\n";
$ARGV[0] =~ s/(\\\w+)/\\$1/g;    #using grouping get all match and $1 as reference ;
$ARGV[0] =~ s/(["'])/\\$1/g;
$ARGV[0] =~ s/
/\\n/;
print "print(\"$ARGV[0]\")\n";
