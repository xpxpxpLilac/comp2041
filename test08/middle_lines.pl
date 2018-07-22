#!/usr/bin/perl

open DATA, '<',$ARGV[0] or die;
@data=<DATA>;
close DATA;
$count = 0;
foreach $line (@data){
	$count++;
}
$mid = int($count/2);
if($count != 0){
	if($count %2 != 1){
		print "$data[$mid-1]";
		print "$data[$mid]";
	}else{
		
		print "$data[$mid]";
	}
}
