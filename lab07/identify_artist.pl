#!/usr/bin/perl
foreach $text (@ARGV){   #put all files in an array ???????
        %hash1=();
	%hash2=();
	%copy=();
	open DATA, '<',$text or die;
	@data=<DATA>;
	close DATA;
	foreach $sent (@data){
		$sent = lc $sent;
		@content= $sent =~ /[A-Za-z]+/g;
		foreach $word(@content){
			if(exists $hash1{$word}){
				$hash1{$word} += 1;
			}else {
				$hash1{$word} = 1;
				$copy{$word} = 0;
			}	
		}
	}
	foreach $file (glob "lyrics/*.txt") {
		%copy=();
        	my $total=0;
        	open FILE ,'<',$file or die;
        	@files=<FILE>;
        	close FILE;
        	$file =~ s/lyrics\///g;
        	$file =~ s/.txt//g;
        	$file =~ s/_/ /g;
        	foreach $line (@files) {
                	$line = lc $line;
                	@all = $line =~ /[A-Za-z]+/g;
			$total += $#all +1;
			foreach $key (keys %hash1){
                		@array = $line =~ /\b$key\b/g;   #match a word boundary
                		$copy{$key} += $#array+1;
			}
        	}
#foreach $key (keys %hash1){print "$file for key $key is $copy{$key}\n"};
		$result = 0;
		foreach $key (keys %copy){$result += log(($copy{$key}+1)/$total)*$hash1{$key};}
		$hash2{$file} = $result;
	}
	
	$name = (sort { $hash2{$b} <=> $hash2{$a} } keys %hash2)[0];
	$log = sprintf("%.1f",$hash2{$name});
	print "$text most resembles the work of $name (log-probability=$log)\n";
}
