#!/usr/bin/perl
open FILE, '<',$ARGV[0] or die;
@file = <FILE>;
close FILE;
my %map =(
	a => '$a',
	b => '$b',
	c => '$c',
	n => '$n'
);
foreach $line (@file){
	# group amount of indent spacing
	if($line =~ /^#!\//){print "#!/usr/bin/perl -w\n";}
        elsif($line =~ /(\s*)echo.*/){
                $line =~ s/echo */print "/g;
                $line =~ s/\n/\\n";\n/g;
                print $line;
	}elsif($line =~ /(\s*)(\w+) *= *(\d+|\$\w+)/){
		print "$1\$$2 = $3;\n";
	}elsif($line =~ /(\s*)while *\(\((\w+) *([\W]+) *(\d+)/){
		print "$1while (\$$2 $3$4) {\n";
	}elsif($line =~ /(\s*)while *\(\((\w+) *([\W]+) *(\w+)/){
		print "$1while (\$$2 $3\$$4) {\n";
	}elsif($line =~ /(\s*)if *\(\(.*\)\)/){
		$line =~ s/\(//;
		$line =~ s/\)//;
		$line =~ s/\n//;
		$line =~ s/([abcn])/$map{$1}/g;
		print "$line {\n";
	}elsif($line =~ /(\s*)(do|then)\n/){
		next;	
	}elsif($line =~ /(\s*)(done|fi)\n/){
		print "$1}\n";
	}elsif($line =~/(\s*)else/){
		print "$1\} else \{\n";
	}elsif($line =~ /(\s*)(\w+) *= *\$\(\((\w+) ?(\W+) ?(\d+)\)\)/){
		print "$1\$$2 = \$$3 $4$5;\n";
	}elsif($line =~ /(\s*)(\w+) *= *\$\(\((\w+) ?(\W+) ?(\w+)\)\)/){
		print "$1\$$2 = \$$3 $4\$$5;\n";
	}elsif($line =~ /(\s+)(\w+)=\$\(\(.*\)\)/){
		$line =~ s/\(//g;
		$line =~ s/\)//g;
		$line =~ s/\$//g;
		$line =~ s/=/ = /;
		$line =~ s/n/\$n/g;
		$line =~ s/\n/;\n/;
		print $line;
#	}elsif($line =~ /(\s*)echo.*/){
		#$line =~ s/echo */print "/g;
		#$line =~ s/\n/\\n";\n/g;
#		print $line;
	}else{print $line;}
}
