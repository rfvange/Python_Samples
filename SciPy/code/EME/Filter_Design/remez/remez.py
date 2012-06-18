import scipy.signal as ss
import scipy.fftpack as my_fft
import pylab
import numpy as np

#print help(ss)

#out = ss.remez(64, [0.0, 0.05, 0.1, 0.13, 0.2, 0.5], [0, 1, 0], weight=[1,1,1])
#out = ss.remez(64, [0.0, 0.1, 0.2, 0.3, 0.4, 0.5], [0, 1, 0], weight=[1,1,1])
#out = ss.remez(256, [0.0, 0.06, 0.069, 0.071, 0.08, 0.5], [0, 1, 0], weight=[5,1,5])
#out = ss.remez(128, [0.0, 0.05, 0.1, 0.15, 0.18, 0.25, 0.3, 0.36, 0.41, 0.5], [0, 1, 0, 1, 0])
out = ss.remez(128, [0.0, 0.05, 0.1, 0.15, 0.20, 0.25, 0.3, 0.36, 0.41, 0.5], [0, 1, 0, 1, 0], weight=[1,1,1,1,1]) # , grid_density=32
#out = ss.remez(128, [0.0, 0.05, 0.1, 0.15, 0.18, 0.25, 0.3, 0.36, 0.41, 0.5], [0, 1, 0, 1, 0], type='differentiator') # , grid_density=32
#out = ss.remez(128, [0.0, 0.05, 0.1, 0.15, 0.18, 0.25, 0.3, 0.36, 0.41, 0.5], [1, 0, 1, 0, 1]) # Doesn't work

print "Out ="
print out
print

y1 = abs(my_fft.fft(out))

print "y1 ="
print y1

pylab.figure()
#pylab.plot(the_val,'k+',label='value')
pylab.plot(20.0*np.log10(y1),'b-',label="Spectrum") # [14:22]
#pylab.plot(y1,'b-',label="Spectrum") # [14:22]
#pylab.plot(20.0*np.log10(y2[7200:9800]),'b-',label=sys.argv[1]) # zoom in 5150:11750, 8000:9300
#pylab.plot(y2[3000:20000],'b-',label=sys.argv[1]) # zoom in
pylab.legend(loc='lower right')

#my_fig = sys.argv[1]+".png" # To save
#my_fig = "fdtd%d.png" % t
#pylab.savefig(my_fig,dpi=72) # To save

#my_fig = sys.argv[1]+".png"; pylab.savefig(my_fig,dpi=300) # To save

pylab.figure()
pylab.plot(out,'k-',label="coefficients")
pylab.legend(loc='lower right')
#pylab.plot(acc_est,'k-',label='acceleration')
#pylab.plot(vel_est,'b-',label='velocity')
#pylab.legend(loc='upper left')
pylab.show() # To show



