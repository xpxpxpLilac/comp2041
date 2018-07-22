#!/usr/bin/perl
my $total=0;
foreach $line (<STDIN>) {
	@array = $line =~ /[A-Za-z]+/g;
	$total += $#array +1; 
}
print "$total words\n";


