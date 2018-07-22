#!/usr/bin/perl
my %hash = (
	'you'=>1,
	'me'=>4,
	'she'=>3,
	'he'=>2
);
$num = (sort {$hash{$a} <=> $hash{$b}} keys %hash)[0];
print "$num\n";
$num = sprintf("%.5f", 2.5577777);
print "$num\n";
my @days =qw/Mon Tue Wed Thu Fri/;
my $width = 6;
printf "%-${width}s", $session;
$command = date;
print eval $command;
