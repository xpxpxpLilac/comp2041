#!/usr/bin/perl
%hash1=();
%hash2=();
foreach $whale (<STDIN>){
	chomp $whale;
	$whale = lc $whale;
	$whale =~ s/s$//g;
        $whale =~ s/ +/ /g;
	$whale =~ s/ *$//g;
#print "$whale^\n"; 
	if($whale =~ /(\d+) (.+)/){
		if(exists $hash1{$2}){
			$hash1{$2} += $1;
			$hash2{$2}++;
		} else {
			$hash1{$2} = $1;
			$hash2{$2} = 1;
		}	
	}
}
foreach $key (sort keys %hash1) {
	print "$key observations: $hash2{$key} pods, $hash1{$key} individuals\n";
}

