#import scipy
#import numpy as np
#import scipy.fftpack as my_fft
#from pprint import pprint
import scipy.signal

#print help(scipy)
#print help(scipy.fftpack)
#print help(scipy.signal)
print

#my_win = scipy.signal.get_window("hamming", 16)
my_win = scipy.signal.get_window(("gaussian",2), 16)

print my_win
