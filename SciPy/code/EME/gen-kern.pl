#$kernlen = 140;
#$fftlen = 1024;
$kernlen = 2000;
$fftlen = 2010;
$freq = 567/8192;
$pi = atan2(0,-1);
#print "pi = $pi\n";
for($i=0;$i<$kernlen;++$i) {
  $out = 120.0*cos(2*$pi*$freq*$i);
  print "$out\n";
}
for($i=$kernlen;$i<$fftlen;++$i) {
  print "0\n";
}
