#import scipy
import numpy as np
import scipy.fftpack as my_fft
import scipy.signal as my_signal
from pprint import pprint

#print help(scipy)
#print help(scipy.fftpack)
#print

x1 = np.zeros(16,dtype=float)
x1[0] = 1.0
x1[1] = 1.0
x1[2] = 2.0
x1[3] = 1.0
x1[4] = 4.0
x1[5] = 2.0
x1[6] = 4.0
x1[7] = 3.0
x1[8] = 2.0
x1[9] = 0.0
x1[10] = 0.0
x1[11] = 0.0
x1[12] = 0.0
x1[13] = 0.0
x1[14] = 0.0
x1[15] = 0.0

x2 = np.zeros(16,dtype=float)
x2[0] = 0.0
x2[1] = 0.0
x2[2] = 0.0
x2[3] = 0.0
x2[4] = 0.0
x2[5] = 0.0
x2[6] = 0.0
x2[7] = 0.0
x2[8] = 1.0
x2[9] = 2.0
x2[10] = 3.0
x2[11] = 2.0
x2[12] = 1.0
x2[13] = 2.0
x2[14] = 1.0
x2[15] = 2.0

y1 = my_fft.fft(x1)
y2 = my_fft.fft(x2)

z1 = y1*y2

#print z1
#print

x3 = my_fft.ifft(z1)

print x3
print

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

x2 = np.zeros(8,dtype=float)
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


"""
print x
print

print np.pi
y = [np.sin(2*np.pi*i/8) for i in range(16)]

#print y
pprint(y)
print

z = my_fft.fft(y)
print z
print
x1 = my_fft.ifft(z)
#pprint(x1)
print x1
print
"""

