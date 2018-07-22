#!/usr/bin/perl
foreach $line(<STDIN>){
	if($line =~ /<!([^!<>]+)>/){
		$command = `$1`;
		$line =~ s/<![^!<>]+>/$command/g;
	}elsif($line =~ /<([^<>!]*)>/){
		$command = `cat $1`;
		$line =~ s/<[^!<>]*>/$command/g;				
	}
	print $line;



}
