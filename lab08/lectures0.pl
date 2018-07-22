#!/usr/bin/perl
foreach $course (@ARGV){
	$url = "http://www.timetable.unsw.edu.au/current/$course.html";
	open F, "wget -q -O- $url|" or die;
	$count = 100;
	my %hash=();
	while ($line = <F>) {
		if($line =~ /[0-9]\"\>Lecture/){
			$count = 0;
			next;
		}
		$count++;
		if($count == 1){
			$line =~ s/<.*?>//g;         #the least thing that matches
			$line =~ s/ {2,}//g;
			$line =~ s/\n//g;
			$line =~ s/T/S/g;
			if($line ne "\n"){
				$seme = $line;
			}
		} elsif($count == 6){
			$line =~ s/<.*?>//g;         #the least thing that matches
			$line =~ s/ {2,}//g;
			$line =~ s/\n//g;
			if($line ne ""){
				if(!exists $$course{$seme}{$line}){$hash{$seme}{$line} = 1;}
			}
		}

	}
	foreach $ele (sort keys %hash){
		foreach $key (sort keys %{$hash{$ele}}){
			print "$course: $ele $key\n"; 
		}
	}
}

