#!/usr/bin/perl
foreach $value (@ARGV){
	if(! $hash{$value}){
		print "$value ";
		$hash{$value} = 1;
	}
}
print "\n";
