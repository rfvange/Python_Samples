#import scipy
import numpy as np
import scipy.fftpack as my_fft
#import scipy.signal as my_signal
import pylab
import sys
#from pprint import pprint

#print help(scipy)
#print help(scipy.fftpack)
#print

# Now do overlap/save
# Let n = 4
# Kernel

num_args = 1
if (len(sys.argv)) != num_args+1: # One more than the number of command-line arguments.
  print "supply <test signal file>"
  exit()

'''
x1 = np.zeros(8,dtype=float)
x2 = np.zeros(8,dtype=float)

print "x1 ="
print x1
print
'''

f = open(sys.argv[1]) # load the signal file

x3 = f.readlines() # read input file to a list

x3 = np.array(x3) # must be of type np.array for fftconvolve() to work

y1 = my_fft.fft(x3)

y2 = np.abs(y1)

print "fft length =",len(y2)

'''
fout = open("spectrum_"+sys.argv[1]+".out","w")
length = len(y2)
for i in range(length):
    out = "%s\n" % y2[i]
    fout.write(out)
fout.close()
'''

pylab.figure()
#pylab.plot(the_val,'k+',label='value')
pylab.plot(20.0*np.log10(y2),'b-',label=sys.argv[1])
#pylab.plot(20.0*np.log10(y2[7200:9800]),'b-',label=sys.argv[1]) # zoom in 5150:11750, 8000:9300
#pylab.plot(y2[3000:20000],'b-',label=sys.argv[1]) # zoom in
pylab.legend(loc='lower center')

#my_fig = sys.argv[1]+".png" # To save
#my_fig = "fdtd%d.png" % t
#pylab.savefig(my_fig,dpi=72) # To save

my_fig = sys.argv[1]+".png"; pylab.savefig(my_fig,dpi=300) # To save

#pylab.figure()
#pylab.plot(acc_est,'k-',label='acceleration')
#pylab.plot(vel_est,'b-',label='velocity')
#pylab.legend(loc='upper left')
#pylab.show() # To show




#print "dir(x3)"
#print dir(x3)
#print

#print "x3 ="
#print x3
#print

'''
x1[0] = 1.0
x1[1] = 1.0
x1[2] = 2.0
x1[3] = 1.0
x1[4] = 0.0
x1[5] = 0.0
x1[6] = 0.0
x1[7] = 0.0

# Data Stream
x2[0] = 2.0
x2[1] = 3.0
x2[2] = 4.0
x2[3] = 1.0
x2[4] = 1.0
x2[5] = 2.0
x2[6] = 1.0
x2[7] = 1.0
'''
'''
x4 = my_signal.fftconvolve(xkern, x3)

print "size is",x4.size
print

print "convolved"
print x4[0:20] # first 20
print

print x4[-10:] # last 10
print
'''
'''
fout = open("af9y_convolved.out","w")
length = len(x4)
for i in range(length):
  if i%10 == 0:
    out = "%s\n" % x4[i]
    fout.write(out)
fout.close()
'''
'''
f.close()
fkern.close()

pylab.figure()
#pylab.plot(the_val,'k+',label='value')
pylab.plot(x4,'b-',label=sys.argv[2])
#pylab.plot(x4[200000:300000],'b-',label='convolved_out') # zoom in
pylab.legend(loc='lower right')

my_fig = sys.argv[2]+".png"
#my_fig = "fdtd%d.png" % t
pylab.savefig(my_fig,dpi=72)

#pylab.figure()
#pylab.plot(acc_est,'k-',label='acceleration')
#pylab.plot(vel_est,'b-',label='velocity')
#pylab.legend(loc='upper left')
#pylab.show()
'''
'''

# Both starting at index 0
x1 = np.zeros(8,dtype=float)
x1[0] = 1.0
x1[1] = 1.0
x1[2] = 2.0
x1[3] = 1.0
x1[4] = 0.0
x1[5] = 0.0
x1[6] = 0.0
x1[7] = 0.0

x2 = np.zeros(8,dtype=float)
x2[0] = 1.0
x2[1] = 2.0
x2[2] = 1.0
x2[3] = 1.0
x2[4] = 0.0
x2[5] = 0.0
x2[6] = 0.0
x2[7] = 0.0

y1 = my_fft.fft(x1)
y2 = my_fft.fft(x2)

z1 = y1*y2 # Convolution
#z1 = y1*y2.conj() # Correlation

#print z1
#print

x3 = my_fft.ifft(z1)

print x3
print

# One starting at index 4
x1[0] = 1.0
x1[1] = 1.0
x1[2] = 2.0
x1[3] = 1.0
x1[4] = 0.0
x1[5] = 0.0
x1[6] = 0.0
x1[7] = 0.0

x2[0] = 0.0
x2[1] = 0.0
x2[2] = 0.0
x2[3] = 0.0
x2[4] = 1.0
x2[5] = 2.0
x2[6] = 1.0
x2[7] = 1.0

y1 = my_fft.fft(x1)
y2 = my_fft.fft(x2)

z1 = y1*y2 # Convolution
#z1 = y1*y2.conj() # Correlation

#print z1
#print

x3 = my_fft.ifft(z1)

print x3
print

# fftconvolve takes two vectors of length n1 and n2
#  and produces an output vector of length n1+n2-1
# This is a nice test of overlap add / overlap
x4 = my_signal.fftconvolve(x1, x2)

print x4
print

fftbuf = np.zeros(8,dtype=float)
fftbuf[0] = 0.0
fftbuf[1] = 0.0
fftbuf[2] = 0.0
fftbuf[3] = 2.0
fftbuf[4] = 3.0
fftbuf[5] = 4.0
fftbuf[6] = 1.0
fftbuf[7] = 1.0

y1 = my_fft.fft(fftbuf)
y2 = my_fft.fft(x1) # kernel

z1 = y1*y2 # Convolution
#z1 = y1*y2.conj() # Correlation

#print z1
#print

print "ovl-saved"
x3 = my_fft.ifft(z1)
print x3
print
print x3[3:]
print


fftbuf[0] = 4.0
fftbuf[1] = 1.0
fftbuf[2] = 1.0
fftbuf[3] = 2.0
fftbuf[4] = 1.0
fftbuf[5] = 1.0
fftbuf[6] = 0.0
fftbuf[7] = 0.0

y1 = my_fft.fft(fftbuf)
y2 = my_fft.fft(x1) # kernel

z1 = y1*y2 # Convolution
#z1 = y1*y2.conj() # Correlation

#print z1
#print

print "ovl-saved"
x3 = my_fft.ifft(z1)

print x3
print
print x3[3:]
print

fftbuf[0] = 1.0
fftbuf[1] = 0.0
fftbuf[2] = 0.0
fftbuf[3] = 0.0
fftbuf[4] = 0.0
fftbuf[5] = 0.0
fftbuf[6] = 0.0
fftbuf[7] = 0.0

y1 = my_fft.fft(fftbuf)
y2 = my_fft.fft(x1) # kernel

z1 = y1*y2 # Convolution
#z1 = y1*y2.conj() # Correlation

#print z1
#print

print "ovl-saved"
x3 = my_fft.ifft(z1)

print x3
print
print x3[3:]
print

'''





