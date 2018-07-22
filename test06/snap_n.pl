#!/usr/bin/perl
%hash={};
$snap="";
foreach $line (<STDIN>){
	if(exists $hash{$line}){
		$hash{$line}++;
		if($hash{$line} == $ARGV[0]){$snap = $line; last;};
	}else{
		$hash{$line} = 1;
	}
}
if($snap ne ""){
print "Snap: $snap";
}
