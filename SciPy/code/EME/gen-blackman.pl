#$kernlen = 140;
#$fftlen = 1024;
$kernlen = 500;
$fftlen = 510;
$freq = 567/8192;
$pi = atan2(0,-1);
#print "pi = $pi\n";
for($i=0;$i<$kernlen;++$i) {
  $out = 120.0*cos(2*$pi*$freq*$i);
  $out = $out*(0.42 - 0.5*cos(2*$pi*$i/$kernlen) + 0.08*cos(4*$pi*$i/$kernlen));
  print "$out\n";
}
for($i=$kernlen;$i<$fftlen;++$i) {
  print "0\n";
}

__END__

Blackman window (slower rolloff, better stopband: -80dB): A smooth curve used in the
design of filters and spectral analysis, calculated
from : 0.42 - 0.5cos(2*pi*n/M) + 0.08cos(4*pi*n/M),
where n runs from 0 to M.