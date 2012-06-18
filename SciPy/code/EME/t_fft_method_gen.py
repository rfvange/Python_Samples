import numpy as np
import scipy.fftpack as my_fft
import pylab

#f = open("unkn422-1.out")
#f = open("unkn422-1_conv_rev_flat_filt_kernel_65.out")
f = open("unkn422-1_filt490.out")
#f = open("unkn422-1_filt.out")
#f = open("ke0b2.out")
x1 = f.readlines()
f.close()
x1 = np.array(x1)
y1 = []
my_ema = []

#f_val = 1000.0 # normal
chunk = 256
#ema_val = chunk*float(x1[0])*0.2
#ema_val = 6000.0
ema_val = 1.2*abs(my_fft.fft(x1[0:chunk]))[18]
for i in range(0,len(x1) - chunk,chunk/2):
#  print i
  fft_chunk = my_fft.fft(x1[i:i+chunk]) # 0 - 64 goes to index 63.
  fft_chunk = abs(fft_chunk)
#  print "length of fft_chunk =",len(fft_chunk)
  avg_chunk = fft_chunk[18]
#  avg_chunk = 0.25*fft_chunk[17] + 0.5*fft_chunk[18] + 0.25*fft_chunk[19]
  ema_val = 0.05*avg_chunk + 0.95*ema_val # EMA
  f_val = avg_chunk
#  print "ema_val =",ema_val
#  print "f_val =",f_val
#  print
  y1.append(f_val) # f = 576 Hz (17 ~ 544, 19 ~ 608) for chunk = 256
  my_ema.append(ema_val)

print "length of y1 =",len(y1)

outf = open("unkn422-1_filt490_gen.out","w")

def dot(my_file):
# Generate sine waves
#$pi = atan2(0.0,-1.0); # use np.pi
  r_samp = 8192
  t_dot = 0.020
  t_dash = 3*t_dot
  t_space = t_dot
  t_idle = 2.5*t_dot
  t_word = 3*t_dot
  freq = 567 # could be changed
#  print "in dot"
#$f = 572

# Number of samples per symbol

  s_dot = int(r_samp*t_dot*2)
  s_dash = r_samp*t_dash
  s_space = r_samp*t_space
  s_idle = r_samp*t_idle
  s_word = r_samp*t_word

  twopif = 2*np.pi*freq/r_samp

  for k in range(s_dot):
    out_val = "%d" % int(round(120.0*np.sin(twopif*k)))
#    print 120.0*np.sin(twopif*k)
#    print out_val
    my_file.write(out_val)
    my_file.write("\n")
#    print "k =",k
# End of dot

for i in range(len(y1)):
  if(y1[i] > 2.0*my_ema[i]):
    dot(outf)
  else:
    for k in range(int(8192*0.020*2)):
      outf.write("0")
      outf.write("\n")

outf.close()


'''
#pylab.figure()
#my_line, = pylab.plot(y1,'b-',label="signal") # zoom in


pylab.figure()
#pylab.plot(the_val,'k+',label='value')
#pylab.plot(y1,'b-',label="signal")
pylab.plot(y1[1800:2200],'b-',label="signal") # zoom in
pylab.legend(loc='lower right')

my_fig = "filt_kernel_65_test_.png"
#my_fig = "fdtd%d.png" % t
pylab.savefig(my_fig,dpi=72)
'''

'''
for i in range(23):
  pylab.figure()
#pylab.plot(the_val,'k+',label='value')
#pylab.plot(y1,'b-',label="signal")
  my_mult = i*200
  my_label = "filt_kernel_65_test_%d" % my_mult
  pylab.plot(y1[200*i:400+200*i],'b-',label=my_label) # zoom in
  pylab.plot(my_ema[200*i:400+200*i],'r-')
  pylab.legend(loc='upper center')

  my_fig = "filt_kernel_65_test%d.png" % i
#  my_line.set_ydata(y1[1800+i:2200+i])
#my_fig = "fdtd%d.png" % t
  pylab.savefig(my_fig,dpi=72)

#pylab.figure()
#pylab.plot(acc_est,'k-',label='acceleration')
#pylab.plot(vel_est,'b-',label='velocity')
#pylab.legend(loc='upper left')
#pylab.show()
'''








