#import scipy
f = open("af9y.out")

x1 = f.readlines()

x1.reverse() # reverses lists is in place, not np.array objects.

print dir(x1)
print

print "x1 ="
print x1[0:20]
print x1[-10:]
print

print "x1 type is",type(x1)

print "x1 ="
print x1[0:20]
print

x2 = x1[::-1] # This also reverses np.array objects.
print "x2 ="
print x2[0:10]

#fout = open("af9y_rev.out","w")
#fout.writelines(x1)
f.close()
#fout.close()

