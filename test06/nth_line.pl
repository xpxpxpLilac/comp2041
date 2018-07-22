#!/usr/bin/perl
open FILE, '<', $ARGV[1] or die;
@array=<FILE>;
close(FILE);
if($ARGV[0] != 0){print $array[$ARGV[0]-1];}
