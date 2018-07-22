#!/usr/bin/perl
foreach $line (<STDIN>){
	$line =~ s/[0-9]//g;
	print $line;
}
