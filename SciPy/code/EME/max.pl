#!/usr/local/bin/perl
$#ARGV >= 0 || die "Usage: max.pm <file-name> - $!";
$bin = 0;
$max = 0;
while(<>) {
  ++$bin;
  $_ = -$_ if ($_ < 0);
  if ($_ > $max) {
    $bmax = $bin;
    $max = $_;
  }
}
print "$max in bin = $bmax\n";
