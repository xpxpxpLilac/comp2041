#!/usr/bin/perl
@upre=();
@pre=();
$url = "http://www.handbook.unsw.edu.au/undergraduate/courses/current/$ARGV[0].html";
$url2 = "http://www.handbook.unsw.edu.au/postgraduate/courses/current/$ARGV[0].html";
open F,"wget -q -O- $url|" or die;
while ($line = <F>) {
	if($line =~ /Prerequisite/){
    	$line =~ s/<\/p>.*//g;
		@upre = $line =~ /[A-Z0-9]{8}/g;                     #for all that match /[A-Z0-9]{8}/, put them into an array and return it!!!!!!!!!!!!!!!!!!!!
	}
}
$url = "http://www.handbook.unsw.edu.au/postgraduate/courses/current/$ARGV[0].html";
open F, "wget -q -O- $url|" or die;
while ($line = <F>) {
	if($line =~ /Prerequisite/){
    	$line =~ s/<\/p>.*//g;
		@pre = $line =~ /[A-Z0-9]{8}/g;
	}
}
push(@upre,@pre);
foreach $c(sort @upre){print "$c\n";};
