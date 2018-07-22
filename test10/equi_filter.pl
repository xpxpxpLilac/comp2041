#!/usr/bin/perl
foreach $line (<STDIN>){
	$line =~ s/ +/ /g;
	$line =~ s/\n$//;
	@word = split(/ /,$line);
	foreach $chars (@word){
		%hash = ();
		$char = lc $chars;
		@digit = split(//,$char);
		foreach $d (@digit){
			if(exists $hash{$d}){
				$hash{$d}++;
			} else {
				$hash{$d} = 1;
			}
		}	
		$count = $hash{$digit[0]};
		$last = 0;
		foreach $m (@digit){
			if($count != $hash{$m}){ $last = 1;last;}
		}
		if($last == 1){$line =~ s/$chars ?//;}
	}	
	print "$line\n";
}
