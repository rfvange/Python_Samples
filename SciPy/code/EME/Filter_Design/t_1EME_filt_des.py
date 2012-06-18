#import scipy
#import numpy as np
#from pprint import pprint
import numpy as np
import scipy.fftpack as my_fft
import scipy.signal as my_signal
import pylab

#print help(scipy)
#print help(scipy.fftpack)
#print help(scipy.signal)
print

# The base file is FFT\t1_filt_des.py
# This methodology is from Ch 16 of dspguide.
# Filter roll-off M-value is calculated from the relationship M ~ 4/BW where BW is the
#  fraction bandwidth of the transition region, delta f/sample rate.
# M must be even so the length of the kernel is odd.

M = 100
fc = 0.05

#h[i] = K*sin(2*pi*fc*(i-M/2))/(i-M/2)*(0.42 - 0.5*cos(2*pi*i)/M + 0.08*cos(4*pi*i)/M

h = []
for i in range(M):
  if i-M/2 == 0: h.append(2*np.pi*fc)
  else: h.append(np.sin(2*np.pi*fc*(i-M/2))/(i-M/2))

h = np.array(h)
h_brick = my_signal.fftconvolve(h, h)
#h_brick = h_brick[M/2:-M/2]
x1 = 20.0*np.log10(abs(my_fft.fft(h)))
x2 = 20.0*np.log10(abs(my_fft.fft(h_brick)))

'''
h_br_shift = complex_mult*np.array(h)



n=20
complex_mult = [2*np.cos(n*2.0*i*np.pi/len(h)) for i in range(len(h))]
h_shift = complex_mult*np.array(h)

h_brick = my_signal.fftconvolve(h_shift[M/4:-M/4], h_shift[M/4:-M/4])

x1 = 20.0*np.log10(abs(my_fft.fft(h_shift)))
x2 = 20.0*np.log10(abs(my_fft.fft(h_brick)))
'''

pylab.figure()
#pylab.plot(the_val,'k+',label='value')
pylab.plot(x1,'r-',label="kernel") # [0:70]
pylab.plot(x2,'b-',label="kernel")
#pylab.plot(x4[200000:300000],'b-',label='convolved_out') # zoom in
pylab.legend(loc='upper right')

#my_fig = sys.argv[2]+".png"
#my_fig = "fdtd%d.png" % t
#pylab.savefig(my_fig,dpi=72)

#pylab.figure()
#pylab.plot(acc_est,'k-',label='acceleration')
#pylab.plot(vel_est,'b-',label='velocity')
#pylab.legend(loc='upper left')
pylab.show()






'''

n = 1
complex_mult = [np.exp(n*2.0*i*np.pi*1j/len(x1)) for i in range(len(x1))] # shifts it right by n
#complex_mult = [2*np.cos(n*2.0*i*np.pi/len(x1)) for i in range(len(x1))]
#complex_mult = [np.exp(2*2.0*i*np.pi*1j/8) for i in range(8)] # shifts it right by two
#complex_mult = [np.exp(2.0*i*np.pi*1j/8) for i in range(8)] # shifts it right by one
print "complex_mult"
print complex_mult
print

"""
Does nothing
shift_filt = x1*complex_mult
print shift_filt
print
"""

rect_filt = y1 = my_fft.ifft(x1)
print "rect_filt"
print rect_filt
print
print abs(rect_filt)
print

# At this point, you have the entire kernel which, in practice, should now be
#  trimmed, windowed, shifted, and zero-filled to final fft length.
# For a "brick wall" filter, fft it, square it, and ifft.

#shift_kern = rect_filt*np.cos(np.pi/4) # shift in freq domain
shift_kern = rect_filt*complex_mult # shift in freq domain
#print shift_kern
#print
print "my_shift"
my_shift = my_fft.fft(shift_kern) # should be shifted
print abs(my_shift)
print

#my_win = scipy.signal.get_window("hamming", 8)
my_win = scipy.signal.get_window(("gaussian",3.0), 8)
# The larger the std-dev, the narrower the filter.

print "gaussian"
print my_win
print

win_filt = rect_filt*my_win # window it
print "windowed_window"
print win_filt
print
print abs(win_filt)
print

x3 = my_fft.fft(win_filt)
print "freq_resp"
print abs(x3)
print

x4 = x3**2
print "freq_resp**2"
print abs(x4)
print

x5 = my_fft.ifft(x4)
print "final kernel ="
print x5
print
print abs(x5)
print
'''

