#!/usr/local/bin/perl
print "before a is @a\n";
$a = unshift(@a,1,2,3,4,5);
print "a is $a\n";
print "after a is @a\n";
foreach (@a) {
  print "Out = ",$_,"\n";
}

push(@a,shift @a); # Circular shift
print "after a is @a\n";
$_ = shift @a; # Must be done explicitly
print "_ is $_","\n";
print "after a is @a\n";
