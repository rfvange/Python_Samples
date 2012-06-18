import numpy as np
import scipy.fftpack as my_fft
import pylab




#f = open("unkn422-1.out")
#f = open("unkn422-1_conv_rev_flat_filt_kernel_65.out")
f = open("unkn422-1_filt490.out")
#f = open("ke0b1.out")
#f = open("ke0b2.out")
x1 = f.readlines()
f.close()
x1 = np.array(x1)
y1 = []
my_ema = []

#f_val = 1000.0 # normal
#ema_val = 2.0e7 # for 65.out
chunk = 256
ema_val = 1.2*abs(my_fft.fft(x1[0:chunk]))[18]
for i in range(0,len(x1) - chunk,chunk/2):
#  print i
  fft_chunk = my_fft.fft(x1[i:i+chunk]) # 0 - 64 goes to index 63.
  fft_chunk = abs(fft_chunk)
#  print "length of fft_chunk =",len(fft_chunk)
  avg_chunk = fft_chunk[18]
#  avg_chunk = 0.25*fft_chunk[17] + 0.5*fft_chunk[18] + 0.25*fft_chunk[19]
  ema_val = 0.01*avg_chunk + 0.99*ema_val # EMA
  f_val = avg_chunk
#  print "f_val =",f_val
  y1.append(f_val) # f = 576 Hz (17 ~ 544, 19 ~ 608) for chunk = 256
  my_ema.append(ema_val)

print "length of y1 =",len(y1)

#pylab.figure()
#my_line, = pylab.plot(y1,'b-',label="signal") # zoom in

'''
pylab.figure()
#pylab.plot(the_val,'k+',label='value')
#pylab.plot(y1,'b-',label="signal")
pylab.plot(y1[1800:2200],'b-',label="signal") # zoom in
pylab.legend(loc='lower right')

my_fig = "filt_kernel_65_test_.png"
#my_fig = "fdtd%d.png" % t
pylab.savefig(my_fig,dpi=72)
'''


for i in range(23):
  pylab.figure() # Create a new figure
#pylab.plot(the_val,'k+',label='value')
#pylab.plot(y1,'b-',label="signal")
  my_mult = i*200
  my_label = "unkn422-1_filt490_%d" % my_mult
  pylab.plot(y1[200*i:400+200*i],'b-',label=my_label) # zoom in
  pylab.plot(my_ema[200*i:400+200*i],'r-')
  pylab.legend(loc='upper center')

  my_fig = "unkn422-1_filt490_test%d.png" % i
#  my_line.set_ydata(y1[1800+i:2200+i])
#my_fig = "fdtd%d.png" % t
  pylab.savefig(my_fig,dpi=72)

#pylab.figure()
#pylab.plot(acc_est,'k-',label='acceleration')
#pylab.plot(vel_est,'b-',label='velocity')
#pylab.legend(loc='upper left')
#pylab.show()









