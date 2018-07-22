#!/usr/bin/perl
sub find{
	@upre=();
	@pre=();
	my ($x) = @_;
	$url = "http://www.handbook.unsw.edu.au/undergraduate/courses/current/$x.html";
	open F, "wget -q -O- $url|" or die;
	while ($line = <F>) {
		if($line =~ /Prerequisite/){
    		$line =~ s/<\/p>.*//g;
			@upre = $line =~ /[A-Z0-9]{8}/g;
		}
	}
	$url = "http://www.handbook.unsw.edu.au/postgraduate/courses/current/$x.html";
	open F, "wget -q -O- $url|" or die;
	while ($line = <F>) {
		if($line =~ /Prerequisite/){
    		$line =~ s/<\/p>.*//g;									#any good way to reduce the repeat?
			@pre = $line =~ /[A-Z0-9]{8}/g;
		}
	}
	push(@pre,@upre);
	return @pre;
}
sub recursive{
	(@re) = @_;
	@c=();
	return() if(!@re);
	foreach $course(@re) {
	    @a=find($course);
    	    push(@c,@a);
	    my %hash = map { $_ => 1 } @c;       #delete the duplicates
	    @c = keys %hash;			 #delete the duplicates
	}
	if($req[0] eq $ARGV[1]){ pop @req; }  
	push(@req,@c);                           #have to push to the real array not the parameter    why not push(@re,@c);how to write if want to use @re?
	recursive(@c);
}
@req=();
if($ARGV[0] eq "-r"){
	@req=($ARGV[1]);
	recursive(@req);
	my %hash = map { $_ => 1 } @req;
	@req = keys %hash;
	@req=sort(@req);
} else {
	@req=find($ARGV[0]);
}
foreach $c (@req){print "$c\n";}
