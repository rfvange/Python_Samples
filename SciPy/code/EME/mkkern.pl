#!/usr/local/bin/perl

binmode(STDOUT);
while(<>) {
  chomp;
  $out = pack("d",$_);
  print $out;
}
