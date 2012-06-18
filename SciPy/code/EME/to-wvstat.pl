#!/usr/local/bin/perl

@ARGV == 3 || die "Usage: to-wvstat.pl <infile> <wavfile> <outfile> - $!";
$infile = shift;
$wavfl = shift; # Get template wave file from command line
$outfile = shift; # Get output file from command line
open(INFILE, "<$infile") || die "Error opening $infile - $!";
open(OUTFILE, ">$outfile") || die "Error opening $outfile - $!";
binmode OUTFILE;

# Get file statistics
$lines = 0;
$size = 0;
$sqsum = 0;
$max = 0;
while(<INFILE>) {
  chomp;
  ++$size; # File size
  next if $_ < 0;
  ++$lines;
  $sumsq += $_**2;
  $max = $_ if($_ > $max);
}
print "max = $max\n";
print "lines = $lines\n";
print "size = $size\n";
$stdev = sqrt($sumsq/$lines);
print "stdev = $stdev\n";

# Get the wave file header
open(WFILE,"<$wavfl") || die "Error opening $wavfl $!";
read(WFILE,$buf,40); # Up to size info

# Write to the output file
print OUTFILE $buf; # write header to stdout;
close WFILE;

# Put in the file size
&putsize($size);

# Set up for data output
$omax = 120; # Limit output value - Absolute max is 128
$mult = $omax/(3.0*$stdev); # Multiplication factor

seek(INFILE,0,0);
while(<INFILE>) {
  chomp;
  $val = $_*$mult;
  $val = $omax if ($val>$omax);
  $val = -$omax if ($val<-$omax);
  $a = pack("C",(int($val + 0.5) + 128));
  print OUTFILE $a;
}
close OUTFILE;
close INFILE;
# All done!

# Subroutines
sub putsize {
  my $num = shift;
  my $i = 0;
  do {
    $n[$i++] = $num%256;
    $num = int($num/256);
  } until $num == 0;
  for($j=0;$j<$i;$j++) {
    $a = pack("C",$n[$j]);
    print OUTFILE $a;
  }
  $a = pack("C",0);
  for($k=$j;$k<4;$k++) {
    print OUTFILE $a;
  }
  1;
}

