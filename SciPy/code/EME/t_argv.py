#import scipy
import sys
import glob

print sys.argv

if len(sys.argv) < 2:
  print "need filename"

print glob.glob("*.txt")

'''
f = open("af9y.out")

x1 = f.readlines()

x1.reverse() # reverse is in place

print dir(x1)
print

print "x1 ="
print x1[0:20]
print x1[-10:]
print

#print "x2 type is",type(x2)

print "x1 ="
print x1[0:20]
print

fout = open("af9y_rev.out","w")
fout.writelines(x1)
f.close()
fout.close()
'''
