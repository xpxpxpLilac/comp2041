#!/usr/bin/perl
$file = $ARGV[0];
open FILE,'<', $file;
@f= <FILE>;
close FILE;
foreach $line (@f){
	$line =~ s/[AEIOUaeiou]*//g;
}
open $ff, '>' ,$file;
foreach(@f){
	print $ff "$_";
}
close $ff;
