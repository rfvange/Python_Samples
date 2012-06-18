$pi = atan2(0.0,-1.0);
$r_samp = 8192;
$t_dot = 0.05;
$t_dash = 3*$t_dot;
$t_space = $t_dot;
$t_idle = 2.5*$t_dot;
$t_word = 3*$t_dot;
$f = 572;

# Number of samples per symbol

$s_dot = $r_samp*$t_dot;
$s_dash = $r_samp*$t_dash;
$s_space = $r_samp*$t_space;
$s_idle = $r_samp*$t_idle;
$s_word = $r_samp*$t_word;

$twopif = 2*$pi*$f/$r_samp;

#print "pi = $pi, twopif = $twopif\n";
#print "s_dot = $s_dot, s_dash = $s_dash, s_space = $s_space, s_idle = $s_idle\n";

  &idle;
  &idle;
  &idle;

for($i=0;$i<1;++$i) {
#  &v;
  &a;
  &idle;
  &f;
  &idle;
  &nine;
  &idle;
  &y;
  &word;
#  print "From main\n";
}

&word;
&word;
  
sub v {
  &dot;
  &space;
  &dot;
  &space;
  &dot;
  &space;
  &dash;
#  print "From v\n";
}

sub a {
  &dot;
  &space;
  &dash;
}

sub b {
  &dash;
  &space;
  &dot;
  &space;
  &dot;
  &space;
  &dot;
}

sub e {
  &dot;
}

sub f {
  &dot;
  &space;
  &dot;
  &space;
  &dash;
  &space;
  &dot;
}

sub k {
  &dash;
  &space;
  &dot;
  &space;
  &dash;
}

sub y {
  &dash;
  &space;
  &dot;
  &space;
  &dash;
  &space;
  &dash;
}

sub nine {
  &dash;
  &space;
  &dash;
  &space;
  &dash;
  &space;
  &dash;
  &space;
  &dot;
}

sub zero {
  &dash;
  &space;
  &dash;
  &space;
  &dash;
  &space;
  &dash;
  &space;
  &dash;
}

sub dot {
  my $i;
  for($i=0;$i<$s_dot;++$i) {
    $val = sin($twopif*$i);
    printf "%8.5f\n",$val;
  }
#  print "From dot\n";
}

sub dash {
  my $i;
  for($i=0;$i<$s_dash;++$i) {
    $val = sin($twopif*$i);
    printf "%8.5f\n",$val;
  }
#  print "From dash\n";
}

sub space {
  my $i;
  for($i=0;$i<$s_space;++$i) { print "0\n"}
#  print "From space\n";
}

sub idle {
  my $i;
  for($i=0;$i<$s_idle;++$i) { print "0\n"}
#  print "From idle\n";
}

sub word {
  my $i;
  for($i=0;$i<$s_word;++$i) { print "0\n"}
}

