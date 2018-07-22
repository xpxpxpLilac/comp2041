#!/usr/bin/perl
$count=0;
foreach $line (<STDIN>){
	@array = $line =~ /(-?[0-9.]{2,})/g;
	if(@array){
		$max = $array[0];
		foreach $ele(@array){
			if($ele > $max){ $max = $ele ;}
		}
		$line = "$count $line";
		$hash{$line}= $max;
		$count++;
	}
}
if(%hash){

	$name = (sort { $hash{$b} <=> $hash{$a} } keys %hash)[0];
	$maxi = $hash{$name};
	foreach $key (sort keys %hash){
		if(exists $hash{$key}){
			if($hash{$key} == $maxi){ $key =~s/^[0-9]+ //; print $key;} 
		}
	}
} 

