#!/usr/bin/perl
$format = 0;
$table = 0;
my %S1 =();
my %S2 = ();
foreach $course (@ARGV){
	if($course eq "-d"){$format = 1; next;}
	if($course eq "-t"){$table = 1; next;}
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
	if($format == 1 || $table == 1){
		foreach $ele (sort keys %hash){
			foreach $key (sort keys %{$hash{$ele}}){
				@array = split(/, /,$key);
				foreach $num (@array){
					$num =~ s/\(.*?\)//;
					if(!exists $check{$ele}{$num}){
						if($num =~ /(\w{3}) ([0-9]{2})\:[0-9]{2} \- ([0-9]{2})/){
							$check{$ele}{$num} = 1;
							$hr1 = $2;
						 	if($hr1 < 10){ $hr1 =~ s/0//; }
							while($hr1 < $3){
								if($table == 1){   
									if($ele eq 'S1'){
										if(exists $S1{$1}{$hr1}){
											$S1{$1}{$hr1}++;
										} else {
											$S1{$1}{$hr1} = 1;
										}
									} elsif($ele eq 'S2') {    
										 if(exists $S2{$1}{$hr1}){
                                                                                        $S2{$1}{$hr1}++;
                                                                                } else {
                                                                                        $S2{$1}{$hr1} = 1;
                                                                                }
									}
								} else {
									print "$ele $course $1 $hr1\n";
								} 
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
if($table == 1){
	if(%S1){
		print "S1	Mon 	Tue 	Wed 	Thu 	Fri\n";
		$time = 9;
		while($time <= 20){
			if($time == 9){$time = '09';}
			print "$time:00 	";
			if($time == 9){$time = 9;}
			$newline = join('	',$S1{Mon}{$time},$S1{Tue}{$time},$S1{Wed}{$time},$S1{Thu}{$time},$S1{Fri}{$time});
			print $newline;
			print "\n";
			$time++;
		}
	}
	if(%S2){
		print "S2      Mon     Tue     Wed     Thu     Fri\n";
        	$time = 9;
        	while($time <= 20){
                	if($time == 9){$time = '09';}
                	print "$time:00	";
                	if($time == 9){$time = 9;}
                	$newline = join('	',$S2{Mon}{$time},$S2{Tue}{$time},$S2{Wed}{$time},$S2{Thu}{$time},$S2{Fri}{$time});
                	print $newline;
                	print "\n";
                	$time++;
        	}
	}
}
