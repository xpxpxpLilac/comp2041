#!/usr/bin/perl
foreach $line (<STDIN>){
	$line =~ s/ +/ /g;
	$line =~ s/\n//g;
	@array = split(/ /,$line);	
	@new = sort @array;
	print "@new";
	print "\n";
}
