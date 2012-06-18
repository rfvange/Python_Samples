# The intent is to make an AM detector

#print "entering\n";
#print "$#ARGV";
#print "\n";
$#ARGV == 0 or die "supply input - $!";

while(<>) {
#  print "enter\n";
#  print;
  $_ = -$_ if $_ < 0;
#  print;
#  print "\n";
  $out = $_;
#  print "out = $out\n";
  printf "%d\n",$out+0.5;
  last;
}

while(<>) {
#  print "main\n";
#  print;
  $_ = -$_ if $_ < 0;
#  print;
#  print "\n";
  if($_ > $out) {
    $out = $_;
  } else {
    $out -= $out/4;
  }
#  print "out = $out\n";
#  print "out = ";
  printf "%d\n",$out+0.5;
#  print "\n";
}
