#!/usr/local/bin/perl
$err1 = "Usage: iirband.pm <BW> <freq> <sample freq> <ifile> <ofile>";
$#ARGV >= 4 || die "$err1\n";
$bw = shift; # Notch filter bandwidth
$freq = shift; # Waveform frequency
$f_sample = shift; # Sample frequency
$ifile = shift; # Input data file
$ofile = shift; # Final decimal output file
$tfileb = "t-tempb.bin"; # Binary results of first filter
$tfileb1 = "t-tempb1.bin"; # Binary reverse of t-tempb

$cos = 2*atan2(0,-1); # 2*pi
printf "%10.4f\n",$cos;

$cos = cos($cos*$freq/$f_sample); # Used for calculating filter coefficients
printf "cos = %10.4f\n",$cos;

$r = 1-3*$bw;
$rs = $r**2;
$k = (1-2*$r*$cos+$rs)/(2-2*$cos);
printf "r = %10.4f, k = %10.4f\n",$r,$k;

$a0 = 1-$k;
$a1 = 2*($k-$r)*$cos;
$a2 = $rs - $k;
$b1 = 2*$r*$cos;
$b2 = -$rs;

printf "a0 = %10.6f, a1 = %10.6f, a2 = %10.6f\n",$a0,$a1,$a2;
printf "b1 = %10.6f, b2 = %10.6f\n",$b1,$b2;

$u[0] = $u[1] = $out[0] = $out[1] = 0;

open(IFILE, "<$ifile") || die "Can\'t open $ifile - $!";
open(TFILEB, "+>$tfileb") || die "Can\'t open $tfileb - $!";
open(TFILEB1, "+>$tfileb1") || die "Can\'t open $tfileb1 - $!";
binmode(TFILEB); binmode(TFILEB1);

# Filter the input file
while(1) {
  last unless $_ = <IFILE>;
  $out = $a0*$_ + $a1*$u[1] + $a2*$u[0] + $b1*$out[1] + $b2*$out[0];
  $packv = pack("d",$out); # pack with double value
  print TFILEB $packv;
#  print "out = $out\n";
  push(@u,$_); shift(@u);
  push(@out,$out); shift(@out);
}

close IFILE;

$u[0] = $u[1] = $out[0] = $out[1] = 0; # Reset the delay lines

$max = 0;
seek(TFILEB,-8,2); # Read TFILEB in reverse order
while(1) { # Go through the data in reverse
  sysread(TFILEB,$_,8);
  $upack = unpack("d",$_);
#  print "upack2 = $upack\n";
  $_ = $out = $a0*$upack + $a1*$u[1] + $a2*$u[0] + $b1*$out[1] + $b2*$out[0];
  $packv = pack("d",$out); # pack with double value
  print TFILEB1 $packv; # Processed results in TFILEB1
  push(@u,$upack); shift(@u);
  push(@out,$out); shift(@out);
# $max is used to scale the final output values  
  $_ = -$_ if ($_ < 0); # Absolute value
#  $_ = ($_ < 0) ? -$_ : $_; # Absolute value
  $max = $_ if ($max < $_); # Update $max
#  ($max < $_) ? $_ : $max; # Update $max
  seek(TFILEB,-16,1) || last;
}

close TFILEB;

# TFILEB1 now has processed data in reverse order
$adj = 120/$max;
print "max = $max, adj = $adj\n";

# Finally, output the adjusted result

seek(TFILEB1,-8,2); # First item at end of TFILEB1
open(OFILE, ">$ofile") || die "Can\'t open $ofile - $!";

while(1) {
  sysread(TFILEB1,$rval,8);
  $_ = unpack("d",$rval);
  $new = ($_ < 0) ? int($adj*$_ - 0.5) : int($adj*$_ + 0.5);
  print OFILE "$new\n";
  seek(TFILEB1,-16,1) || last;
} 

close TFILEB1;
close OFILE;
unlink $tfileb;
unlink $tfileb1;
