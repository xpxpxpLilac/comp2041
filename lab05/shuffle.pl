#!/usr/bin/perl -w
@list=<>;
while($#list != -1){
	$index=rand($#list);
	print "$list[$index]";
	$curr=$list[$#list];
	$list[$index]=$curr;
	pop @list;
}
