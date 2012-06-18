#import scipy
import numpy as np
import scipy.fftpack as my_fft
import scipy.signal as my_signal
from pprint import pprint

#print help(scipy)
#print help(scipy.fftpack)
#print

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

# Now do overlap/save
# Let n = 4
# Kernel
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

x4 = my_signal.fftconvolve(x1, x2)

print "convolved"
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





