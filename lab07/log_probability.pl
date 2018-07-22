#!/usr/bin/perl
foreach $file (glob "lyrics/*.txt") {
        my $total=0;
        my $occur=0;
        open FILE ,'<',$file or die;
        @files=<FILE>;
        close FILE;
        $file =~ s/lyrics\///g;
        $file =~ s/.txt//g;
        $file =~ s/_/ /g;
        foreach $line (@files) {
                $line = lc $line;
                @all = $line =~ /[A-Za-z]+/g;
		$ARGV[0] = lc $ARGV[0];
                @array = $line =~ /\b$ARGV[0]\b/g;   #match a word boundary
                $total += $#all +1;
                $occur += $#array+1;
        }
        my $result=log(($occur+1)/$total);
        printf("log((%d+1)/%6d) = %8.4f %s\n","$occur","$total","$result","$file");
}


