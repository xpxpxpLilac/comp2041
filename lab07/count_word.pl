#!/usr/bin/perl

my $total=0;
foreach $line (<STDIN>) {
	$line = lc $line;
        @array = $line =~ /\b$ARGV[0]\b/g;   #match a word boundary
        $total += $#array +1;
}
print "$ARGV[0] occurred $total times\n";

