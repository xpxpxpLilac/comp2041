#!/usr/bin/perl -w
if( $#ARGV != 1 ){
     print "Usage: ./echon.pl <number of lines> <string>\n"
}elsif( $ARGV[0] =~ /^[0-9]+$/ ) {
    for($i = 0; $i < $ARGV[0]; $i++) {
        print "$ARGV[1]\n";
    }
} else {
    print "./echon.pl: argument 1 must be a non-negative integer\n"
}
#    $var = "hello bob";
#    if ($var =~ /$pattern/) {
        # EXECUTES IF PATTERN MATCHES
#    }
