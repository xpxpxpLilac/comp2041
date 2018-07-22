#!/usr/bin/perl
$url = "http://www.timetable.unsw.edu.au/current/$ARGV[0]KENS.html";
open F, "wget -q -O- $url|" or die;
while ($line = <F>) {
	if($line =~ />$ARGV[0]/){
		$line =~ s/\<[^<>]+>//g;
		$line =~ s/ *//g;
	print $line;
	}
}
