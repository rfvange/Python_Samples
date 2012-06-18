#!/usr/local/bin/perl
$err1 = "Usage: iirband.pm <BW> <freq> <sample freq> <ifile> <ofile>";
$#ARGV >= 4 || die "$err1\n";
$bw = shift; # Notch filter bandwidth
$freq = shift; # Waveform frequency
$f_sample = shift; # Sample frequency
$ifile = shift; # Input data file
$ofile = shift; # Final decimal output file

print "ofile is $ofile\n";
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

# Filter the input file
while(1) {
  last unless $_ = <IFILE>;
  $out = $a0*$_ + $a1*$u[1] + $a2*$u[0] + $b1*$out[1] + $b2*$out[0];
  $packv = pack("d",$out); # pack with double value
  push(@a,$packv);
#  print "out = $out\n";
  push(@u,$_); shift(@u);
  push(@out,$out); shift(@out);
}

close IFILE;

$u[0] = $u[1] = $out[0] = $out[1] = 0; # Reset the delay lines

$max = 0;
while(1) { # Go through the data in reverse order
  $_ = pop(@a) || last;
  $upack = unpack("d",$_);
#  print "upack2 = $upack\n";
  $_ = $out = $a0*$upack + $a1*$u[1] + $a2*$u[0] + $b1*$out[1] + $b2*$out[0];
  $packv = pack("d",$out); # pack with double value
  push(@b,$packv);
  push(@u,$upack); shift(@u);
  push(@out,$out); shift(@out);
# $max is used to scale the final output values  
  $_ = -$_ if ($_ < 0); # Absolute value
#  $_ = ($_ < 0) ? -$_ : $_; # Absolute value
  $max = $_ if ($max < $_); # Update $max
#  ($max < $_) ? $_ : $max; # Update $max
}

$adj = 120/$max;
print "max = $max, adj = $adj\n";
print "size of a = $#a, size of b = $#b\n";

open(OFILE, ">$ofile") || die "Can\'t open $ofile - $!";
while(1) {
  $rval = pop(@b) || last;
  $_ = unpack("d",$rval);
  $new = ($_ < 0) ? int($adj*$_ - 0.5) :  int($adj*$_ + 0.5);
#  print "$new\n";
  print OFILE "$new\n";
}

close OFILE;
