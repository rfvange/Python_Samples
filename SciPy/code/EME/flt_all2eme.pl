#!/usr/local/bin/perl
#$#ARGV >= 0 || die "Usage: max.pm <file-name> - $!";
$infile = 'all2eme.txt';
#$infile = glob("all2eme*"); # gets it from re
print "infile is $infile\n\nresult is:\n";
open(INFILE,"<$infile") or die "Error opening $infile - $!";
while($line = <INFILE>) {
  next unless $line =~ /Q/;
#  next unless $line =~ /4/;
  next unless $line =~ /AA/;
#  next unless $line =~ /AA/ and $line =~ /Q/; # same thing
  print $line;
}
