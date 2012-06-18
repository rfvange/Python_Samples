'''
from numpy import cos, sin, pi, absolute, arange
from scipy.signal import kaiserord, lfilter, firwin, freqz
from pylab import figure, clf, plot, xlabel, ylabel, xlim, ylim, title, grid, axes, show
'''
import sys

print "length sys.arv =",len(sys.argv)

if (len(sys.argv)) != 3:
  print "length sys.arv =",len(sys.argv)
  exit()
  

a = "1000 cuts"
b = 23
c = "skiddoo"

print a + "," + str(b) + "," + c

str1 = a + "%d"%b + c
print str1

print a + "," + "%d"%b + "," + c

print "Now is the time for " + "%d"%b + " men to come to the aid of their party."

