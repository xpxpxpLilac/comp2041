#!/usr/bin/perl
print "#!/usr/bin/python3\n";
#$ARGV[1] =~ s/(\\\w+)/\\$1/g;    #using grouping get all match and $1 as refere$
#$ARGV[1] =~ s/(["'])/\\$1/g;
$sub = "";
for($i=0;$i<2**(2*$ARGV[0]);$i++){
	$sub .= "\\";
}
$sub .="n";
$ARGV[0] =~ s/(\\\w+)/$sub$1/g;
$ARGV[0] =~ s/(["'])/$sub$1/g;
$ARGV[1] =~ s/
/$sub/;
#print "print(\"#!/usr/bin/perl\")\n";
#print "print(\"print \\\"#!/usr/bin/python3\\\\n\\\";\")\n";
#print "print(\"$ARGV[0]\")\n";
#print "print(\"print \\\"$ARGV[0]\\\\n\\\";\")\n";
#print "print(\"print \\\"print(\\\\\\\"$ARGV[1]\\\\\\\")\\\\n\\\";\")\n";
#print "print(\"print \\\"print(\\\\\\\"print \\\\\\\\\\\\\\\"$ARGV[1]\\\\\\\\\\\\\\\\n\\\\\\\\\\\\\\\";\\\\\\\")\\\\n\\\";\")\n";
#print "print(\"print \\\"print(\\\\\\\"print \\\\\\\\\\\\\\\"print(\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"$ARGV[1]\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")\\\\\\\\\\\\\\\\n\\\\\\\\\\\\\\\";\\\\\\\")\\\\n\\\";\")\n";
$strB = "print(\"";
$strE = "\")";
$count = $ARGV[0];
$backslash = "";
$back = 1;
for($i=0;$i<2*$count;$i++){
	$back = 2** $i;
	for($j=0;$j<$back;$j++){
		$backslash .= "\\";
	}
	if($i % 2 == 0){
		if($i == 0){ $n = "\\\\";}else{
		$n = "";
		for($z=0;$z<2**($i+1);$z++){
                        $n .= "\\";
                }
		}
		$strB .= "print " . $backslash . "\"";
		$strE = "$n" . "n" . $backslash . "\";" . $strE;
	} else {
		$strB .= "print(" . $backslash . "\"";
		$strE = "$backslash" . "\")" . $strE; 
	}
}
$final = "$strB$ARGV[1]$strE";
print "$final\n";
