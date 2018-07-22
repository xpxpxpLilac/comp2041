#!/usr/bin/perl
$pattern=$ARGV[0];
$count=0;
$obse=0;
foreach $whale(<STDIN>) {
    if($whale =~ /$pattern/){
	$count++;
	my @num = $whale =~ /\d+/g;
	$obse += $num[0];
    }
}
print "$ARGV[0] observations: $count pods, $obse individuals\n";
