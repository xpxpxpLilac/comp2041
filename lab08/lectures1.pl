#!/usr/bin/perl
$format = 0;
foreach $course (@ARGV){
	if($course eq "-d"){$format = 1; next;}
	$url = "http://www.timetable.unsw.edu.au/current/$course.html";
	open F, "wget -q -O- $url|" or die;
	$count = 100;
	my %hash=();
	my %check=();
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
			if($line ne ""){
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
	if($format == 1){
		foreach $ele (sort keys %hash){
			foreach $key (sort keys %{$hash{$ele}}){
				@array = split(/, /,$key);
				foreach $num (@array){
					$num =~ s/\(.*?\)//;
					if(!exists $check{$ele}{$num}){
#	print "ele is $ele.num is $num\n";
						if($num =~ /(\w{3}) ([0-9]{2})\:[0-9]{2} \- ([0-9]{2})/){
							$check{$ele}{$num} = 1;
							$hr1 = $2;
							if($hr1 < 10){ $hr1 =~ s/0//; }
							while($hr1 < $3){
								print "$ele $course $1 $hr1\n"; 
								$hr1++;
							}
						}
					}
				}
			}
		}
	} else {
		foreach $ele (sort keys %hash){
			foreach $key (sort keys %{$hash{$ele}}){
				print "$course: $ele $key\n"; 
			}
		}
	}
}

