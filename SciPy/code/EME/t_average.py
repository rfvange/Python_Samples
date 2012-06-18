#import numpy as np
#import scipy.fftpack as my_fft
#import pylab

#f = open("unkn422-1.out")
#f = open("unkn422-1_conv_rev_flat_filt_kernel_65.out")
#f = open("unkn422-1_conv_rev_flat_filt_kernel_490.out")
#f = open("ke0b1.out")
f = open("ke0b2.out")
x1 = f.readlines()
f.close()

outf = open("ke0b2_avg.out","w")

# This doesn't work: x1 = float(x1)

for i in range(len(x1)):
  x1[i] = float(x1[i])

# Arguments are int(round(n*4096/freq)) where n = 0,1,2,...
for i in range(0,len(x1)-109):
  my_av = (x1[i] - x1[i+7] + x1[i+14] - x1[i+22] + x1[i+29] - x1[i+36] + x1[i+43] - x1[i+51])/8
#  my_av += (x1[i+1] - x1[i+8] + x1[i+15] - x1[i+23] + x1[i+30] - x1[i+37] + x1[i+44] - x1[i+52])/8
  my_av += (x1[i+58] - x1[i+65] + x1[i+72] - x1[i+79] + x1[i+87] - x1[i+94] + x1[i+101] - x1[i+108])/8
#  my_av += (x1[i+59] - x1[i+66] + x1[i+73] - x1[i+80] + x1[i+88] - x1[i+95] + x1[i+102] - x1[i+109])/8
#  my_av += (x1[i+116] - x1[i+123] + x1[i+130] - x1[i+137] + x1[i+144] - x1[i+152] + x1[i+159] - x1[i+166])
#  my_av /= 32
  my_av = int(round(my_av))
  out_val = "%d\n" % my_av
  outf.write(out_val)

outf.close()
