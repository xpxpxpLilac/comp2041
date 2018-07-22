#!/usr/bin/perl
foreach $line(<>){
	$line =~ s/(\w+)/\$$1/g;
	print $line;
}
