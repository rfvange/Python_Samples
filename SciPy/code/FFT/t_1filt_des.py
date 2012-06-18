#import scipy
#import numpy as np
#import scipy.fftpack as my_fft
#from pprint import pprint
import numpy as np
import scipy.fftpack as my_fft
import scipy.signal

#print help(scipy)
#print help(scipy.fftpack)
#print help(scipy.signal)
print

# The REAL way to do this is to design for zero frequency
#  then convolve with shifted delta function <=> mult by cosine.

x1 = np.zeros(8,dtype=complex)
x1[0] = 1.0
x1[1] = 0.0
x1[2] = 1.0
x1[3] = 0.0
x1[4] = 0.0
x1[5] = 0.0
x1[6] = 0.0
x1[7] = 0.0

"""
x2 = np.zeros(8,dtype=float)
x2[0] = 1.0
x2[1] = 2.0
x2[2] = 1.0
x2[3] = 1.0
x2[4] = 0.0
x2[5] = 0.0
x2[6] = 0.0
x2[7] = 0.0
"""

print "x1 ="
print x1
print

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


