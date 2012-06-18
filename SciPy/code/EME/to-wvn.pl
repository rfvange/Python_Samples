$#ARGV >= 1 || die "Usage: to-wvn.pm <infile> <wavefile>\n";
$infile = shift; # Get input file size.
$wavfl = shift; # Get wave file from command line
#$wavfl = q/\tyvc\sp-f3\unkn422.wav/;
#$infile = q/t-filt.out/;

open(INFILE,"<$infile") || die "Can\'t open file $infile $!";
# Get the header
open(WFILE,"<$wavfl") || die "Can\'t open file $wavfl $!";
read(WFILE,$buf,40); # Up to size info
print $buf; # write header to stdout;
close WFILE;

$num = 0;
# Get filesize.
while(<INFILE>) { ++$num; }

seek(INFILE,0,0); # Rewind the input file.

# Put in the file size
&putsize();

#$i = 0;
# Now write the info
while(<INFILE>) {
  chomp;
  $a = pack("C",(int($_ + 0.5) + 128));
#  $as = unpack("C",$a);
#  print ASCF $as-128,"\n";
  print $a;
#  last if $i++==500;
}

close INFILE;

sub putsize {
  $i = 0;
  do {
    $n[$i++] = $num%256;
    $num = int($num/256);
  } until $num == 0;
  for($j=0;$j<$i;$j++) {
    $a = pack("C",$n[$j]);
    print $a;
  }
  $a = pack("C",0);
  for($k=$j;$k<4;$k++) {
    print $a;
  }
  1;
}
