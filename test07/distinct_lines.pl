#!/usr/bin/perl
$target = $ARGV[0];
$count = 0;
$lines = 0;
foreach $line (<STDIN>){
	$line = lc $line;
	$line =~ s/ +/ /g;
	$line =~ s/^ //g;
	$lines++;
	if(!exists $hash{$line}){
		$hash{$line} = 1;
		$count++;
		last if($count == $target);
	}
}
if($count == $target){
	print "$target distinct lines seen after $lines lines read.\n";
} else {
	print "End of input reached after $lines lines read - $target different lines not seen.\n";
}
