#!/usr/bin/perl
foreach $ele (@ARGV){
	push @array, int($ele);
}
$size = @array;      #size of array
$median = ($size-1 )/2;
@result = sort{ $a <=> $b } @array;    
#if only use sort, it will sort by alphabet
print "$result[$median]\n";
