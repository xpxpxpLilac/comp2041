#!/usr/bin/perl -w
$var=10;
if( $#ARGV < 0){
     @list=<>;
     if($#list > 9){
          for($i=$var;$i > 0;$i--){
              $index=$#list - $i + 1;
              print "$list[$index]"
          }
     }else{print "@list";}
} else {
    foreach $arg (@ARGV){
        if($arg =~ /-[0-9]+/){
	    $arg=~s/-//g;
	    $var=$arg;
        } else {
	    if($ARGV[0] !~ /-[0-9]+/ && $#ARGV > 1){
	        print "==> $arg <==\n";
	    }
            open Data ,'<',$arg or die "tail.pl: can't open $arg\n";
	    @answer=<Data>;
            close Data;
	    if($#answer > 9){        
	        for($i=$var;$i > 0;$i--){
		    $index=$#answer - $i + 1;
		    print "$answer[$index]"
                }
            }else{
	        print "@answer";
            }
        } 
    }
}
