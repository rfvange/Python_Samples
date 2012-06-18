# Procedure that takes input:
# Extrinsic Le(c(k,1))
# Branch Table Entries c(k,j)
# Lc = 4*Es/N0
# Systematic bit - y(k,1,s), Parity bit i - y(k,i,p)
# and returns a tuple: (Partial Branch Metrics, Full Branch Metrics).

#from scipy import *
#from numpy import *
import numpy as np
from pprint import pprint


def Calc_Forward_Branch_Metrics(FB_Full_Branch_Metrics, FB_Forward_Branch_Metrics, FB_Norm_Forward_Branch_Metrics) :
# Calculates the forward branch metrics and the normalized forward branch metrics
# Needs to be customized for every code

  print "In Calc_Forward_Branch_Metrics"
#  pprint(FB_Full_Branch_Metrics)
#  print
#  print FB_Norm_Forward_Branch_Metrics
#  print
  
  for bit in range(7):
    
    print "bit =",bit
    print "FB_Norm_Forward_Branch_Metrics[0][bit] =",FB_Norm_Forward_Branch_Metrics[0][bit]
    print "FB_Full_Branch_Metrics[0][bit] =",FB_Full_Branch_Metrics[0][bit]
    print "FB_Norm_Forward_Branch_Metrics[1][bit] =",FB_Norm_Forward_Branch_Metrics[1][bit]
    print "FB_Full_Branch_Metrics[5][bit] =",FB_Full_Branch_Metrics[5][bit]
    print
    
    FB_Forward_Branch_Metrics[0][bit+1] = FB_Norm_Forward_Branch_Metrics[0][bit]*FB_Full_Branch_Metrics[0][bit] + \
                                          FB_Norm_Forward_Branch_Metrics[1][bit]*FB_Full_Branch_Metrics[5][bit]
    FB_Forward_Branch_Metrics[1][bit+1] = FB_Norm_Forward_Branch_Metrics[3][bit]*FB_Full_Branch_Metrics[3][bit] + \
                                          FB_Norm_Forward_Branch_Metrics[2][bit]*FB_Full_Branch_Metrics[6][bit]
    FB_Forward_Branch_Metrics[2][bit+1] = FB_Norm_Forward_Branch_Metrics[0][bit]*FB_Full_Branch_Metrics[4][bit] + \
                                          FB_Norm_Forward_Branch_Metrics[1][bit]*FB_Full_Branch_Metrics[1][bit]
    FB_Forward_Branch_Metrics[3][bit+1] = FB_Norm_Forward_Branch_Metrics[3][bit]*FB_Full_Branch_Metrics[7][bit] + \
                                          FB_Norm_Forward_Branch_Metrics[2][bit]*FB_Full_Branch_Metrics[2][bit]
    FB_Forward_Branch_Metrics[4][bit+1] = FB_Forward_Branch_Metrics[0][bit+1] + FB_Forward_Branch_Metrics[1][bit+1] + \
                                          FB_Forward_Branch_Metrics[2][bit+1] + FB_Forward_Branch_Metrics[3][bit+1]
    for i in range(4):
      FB_Norm_Forward_Branch_Metrics[i][bit+1] = FB_Forward_Branch_Metrics[i][bit+1] / FB_Forward_Branch_Metrics[4][bit+1]

def Calc_Norm_Backward_Branch_Metrics_Denom(BB_Full_Branch_Metrics, BB_Norm_Backward_Branch_Metrics, \
                                            BB_Norm_Forward_Branch_Metrics) :

  for bit in range(6,-1,-1): # 6-0

    BB_Norm_Backward_Branch_Metrics[4][bit] = BB_Norm_Forward_Branch_Metrics[0][bit]* \
                                              (BB_Full_Branch_Metrics[0][bit] + BB_Full_Branch_Metrics[4][bit]) + \
                                              BB_Norm_Forward_Branch_Metrics[1][bit]* \
                                              (BB_Full_Branch_Metrics[1][bit] + BB_Full_Branch_Metrics[5][bit]) + \
                                              BB_Norm_Forward_Branch_Metrics[2][bit]* \
                                              (BB_Full_Branch_Metrics[2][bit] + BB_Full_Branch_Metrics[6][bit]) + \
                                              BB_Norm_Forward_Branch_Metrics[3][bit]* \
                                              (BB_Full_Branch_Metrics[3][bit] + BB_Full_Branch_Metrics[7][bit])



def Calc_Backward_Branch_Metrics(BB_Full_Branch_Metrics, BB_Backward_Branch_Metrics, BB_Norm_Backward_Branch_Metrics, \
                                 BB_Norm_Forward_Branch_Metrics) :

# Calculates the backward branch metrics and the normalized backward branch metrics
# Needs to be customized for every code

  print "In Calc_Backward_Branch_Metrics"
  for bit in range(5,-1,-1): # 5-0
#    print "bit =",bit

    BB_Backward_Branch_Metrics[0][bit] = BB_Norm_Backward_Branch_Metrics[0][bit+1]*BB_Full_Branch_Metrics[0][bit+1] + \
                                           BB_Norm_Backward_Branch_Metrics[2][bit+1]*BB_Full_Branch_Metrics[4][bit+1]
    BB_Backward_Branch_Metrics[1][bit] = BB_Norm_Backward_Branch_Metrics[0][bit+1]*BB_Full_Branch_Metrics[5][bit+1] + \
                                           BB_Norm_Backward_Branch_Metrics[2][bit+1]*BB_Full_Branch_Metrics[1][bit+1]
    BB_Backward_Branch_Metrics[2][bit] = BB_Norm_Backward_Branch_Metrics[1][bit+1]*BB_Full_Branch_Metrics[6][bit+1] + \
                                           BB_Norm_Backward_Branch_Metrics[3][bit+1]*BB_Full_Branch_Metrics[2][bit+1]
    BB_Backward_Branch_Metrics[3][bit] = BB_Norm_Backward_Branch_Metrics[3][bit+1]*BB_Full_Branch_Metrics[7][bit+1] + \
                                           BB_Norm_Backward_Branch_Metrics[1][bit+1]*BB_Full_Branch_Metrics[3][bit+1]
    BB_Norm_Backward_Branch_Metrics[0][bit] = BB_Backward_Branch_Metrics[0][bit]/BB_Norm_Backward_Branch_Metrics[4][bit]
    BB_Norm_Backward_Branch_Metrics[1][bit] = BB_Backward_Branch_Metrics[1][bit]/BB_Norm_Backward_Branch_Metrics[4][bit]
    BB_Norm_Backward_Branch_Metrics[2][bit] = BB_Backward_Branch_Metrics[2][bit]/BB_Norm_Backward_Branch_Metrics[4][bit]
    BB_Norm_Backward_Branch_Metrics[3][bit] = BB_Backward_Branch_Metrics[3][bit]/BB_Norm_Backward_Branch_Metrics[4][bit]

# Construct all relevant tables

#Sig_to_Noise = 3
Sig_to_Noise = 0.25 # Doesn't alter raw data


Received_Data = \
 [[2, 1, 3, -2, 2, -4, -5], # Intrinsic, y(1,s)
  [-5, 1, -1, -1, 1, -2, -1], # Parity 1, y(1,p)
  [3, 1, -1, -1, -3, -1, -6]] # Parity 2, y(2,p)

#Extrinsic_Value = [0, 0, 0, 0, 0, 0, 0] # Extrinsic
Extrinsic_Value = np.zeros(7,dtype=float) # Extrinsic

Lc = 4.0*Sig_to_Noise

Adj_Data = np.dot(Lc,Received_Data) # When a list, "*" means "replicate"

pprint(Received_Data)
print
print Extrinsic_Value
print
pprint(Adj_Data)
print

# Transition table: From, To, c(1,k), c(2,k), Uk
Transition_T = \
 [[1, 1, -1, -1, -1],
  [2, 3, -1, -1, -1],
  [3, 4, -1,  1, -1],
  [4, 2, -1,  1, -1],
  [1, 3,  1,  1,  1],
  [2, 1,  1,  1,  1],
  [3, 2,  1, -1,  1],
  [4, 4,  1, -1,  1]]

#pprint(Transition_T)
#print

Full_Branch_Metrics = np.zeros(8*7,dtype=float).reshape(8,7) # Columns, Rows
#pprint(Full_Branch_Metrics)
#print

Partial_Branch_Metrics = np.zeros(8*7,dtype=float).reshape(8,7) # Columns, Rows
#pprint(Partial_Branch_Metrics)
#print

Forward_Branch_Metrics = np.zeros(5*8,dtype=float).reshape(5,8)
#pprint(Forward_Branch_Metrics)
#print

Norm_Forward_Branch_Metrics = np.zeros(4*8,dtype=float).reshape(4,8)
#pprint(Norm_Forward_Branch_Metrics)
#print

Backward_Branch_Metrics = np.zeros(4*7,dtype=float).reshape(4,7)
#pprint(Backward_Branch_Metrics)
#print

Norm_Backward_Branch_Metrics = np.zeros(5*7,dtype=float).reshape(5,7)
#pprint(Norm_Backward_Branch_Metrics)
#print

Product_Of_Metrics = np.zeros(8*7,dtype=float).reshape(8,7)
#print "Product_Of_Metrics ="
#pprint(Product_Of_Metrics)
#print

def Initialize_Tables(IT_Forward_Branch_Metrics, IT_Norm_Forward_Branch_Metrics, \
                      IT_Backward_Branch_Metrics, IT_Norm_Backward_Branch_Metrics):
  IT_Forward_Branch_Metrics[0][0] = 1.0
  IT_Forward_Branch_Metrics[4][0] = 1.0
  IT_Norm_Forward_Branch_Metrics[0][0] = 1.0
  IT_Backward_Branch_Metrics[0][6] = 1.0
  IT_Norm_Backward_Branch_Metrics[0][6] = 1.0

Initialize_Tables(Forward_Branch_Metrics, Norm_Forward_Branch_Metrics, \
                  Backward_Branch_Metrics, Norm_Backward_Branch_Metrics)
pprint(Forward_Branch_Metrics)
print
pprint(Norm_Forward_Branch_Metrics)
print
pprint(Backward_Branch_Metrics)
print
pprint(Norm_Backward_Branch_Metrics)
print


def Calc_Metrics(CM_Extrinsic_Value, CM_Transition_T, CM_Received_Data,
                 CM_Full_Branch_Metrics, CM_Partial_Branch_Metrics) : #
#  print "In Calc_Metrics"
#  pprint(CM_Transition_T)
#  print
#  pprint(CM_Received_Data)
#  print
#  print CM_Full_Branch_Metrics
#  print
#  print CM_Partial_Branch_Metrics
#  print
  # In general, top loop is received bit, next is transition, and last is computation.
  for my_bit in range(7):
    for t_entry in range(8):
#  my_bit = 2
#  t_entry = 3
      cm_p_bits = (CM_Received_Data[1][my_bit],) # Parity. Col. index is bit.
      cm_entries = (CM_Transition_T[t_entry][3],) # Transition Table Parity. Row index is state.
      my_arg = 0
#      print "my_bit =",my_bit,"t_entry =",t_entry
      for term in zip(cm_p_bits, cm_entries):
#        print "term =",term
        my_arg += term[0]*term[1]
#        print "my_arg1 =",my_arg
      CM_Partial_Branch_Metrics[t_entry][my_bit] = np.exp(0.5*my_arg)
      my_arg = 0.5*(CM_Extrinsic_Value[my_bit]+CM_Received_Data[0][my_bit])* \
        CM_Transition_T[t_entry][2]
#      print "my_arg2 =",my_arg
#      print "data =",CM_Received_Data[0][my_bit],"transition =",CM_Transition_T[t_entry][2]
      CM_Full_Branch_Metrics[t_entry][my_bit] = np.exp(my_arg)*CM_Partial_Branch_Metrics[t_entry][my_bit]
#      print "pbm =",CM_Partial_Branch_Metrics[t_entry][my_bit]
#      print "fbm =",CM_Full_Branch_Metrics[t_entry][my_bit]
#      print

Extrinsic = 1
Calc_Metrics(Extrinsic_Value, Transition_T, Adj_Data,
             Full_Branch_Metrics, Partial_Branch_Metrics)

print "Done"
print "FBM ="
print Full_Branch_Metrics
print
print "PBM ="
print Partial_Branch_Metrics
print

# See C:\bob2\Python\SciPy\Cookbook\Indexing\t_1Indexing.py
# For more info on array and matrix indexing.

# Strategy is to populate the tables, then pass to procedures the entries to process.

Calc_Forward_Branch_Metrics(Full_Branch_Metrics, Forward_Branch_Metrics, Norm_Forward_Branch_Metrics)
print Forward_Branch_Metrics
print
print Norm_Forward_Branch_Metrics
print

Calc_Norm_Backward_Branch_Metrics_Denom(Full_Branch_Metrics, Norm_Backward_Branch_Metrics, Norm_Forward_Branch_Metrics)
#print "Norm_Backward_Branch_Metrics"
#print Norm_Backward_Branch_Metrics
#print

Calc_Backward_Branch_Metrics(Full_Branch_Metrics, Backward_Branch_Metrics, Norm_Backward_Branch_Metrics, \
                                 Norm_Forward_Branch_Metrics)
print "Backward_Branch_Metrics"
print Backward_Branch_Metrics
print
print "Norm_Backward_Branch_Metrics"
print Norm_Backward_Branch_Metrics
print

exit()






"""
#print np.math.pi
extrinsic = 1.0 # Lc
entry = -1.0
entries = (-1.0,)
#entries = (5.0, 6.0)
s_bit = 2.0
#s_bit = 15.0
p_bits = (-5.0,)
#p_bits = (7.0, 8.0)
partial_met, full_met = Calc_Metrics(extrinsic, entry, entries, s_bit, p_bits)
print "metrics are =", partial_met, full_met
print
print np.modf(3.75)
#print help(np.math)
"""
"""
This is the np.math help content
FUNCTIONS
    acos(...)
        acos(x)

        Return the arc cosine (measured in radians) of x.

    acosh(...)
        acosh(x)

        Return the hyperbolic arc cosine (measured in radians) of x.

    asin(...)
        asin(x)

        Return the arc sine (measured in radians) of x.

    asinh(...)
        asinh(x)

        Return the hyperbolic arc sine (measured in radians) of x.

    atan(...)
        atan(x)

        Return the arc tangent (measured in radians) of x.

    atan2(...)
        atan2(y, x)

        Return the arc tangent (measured in radians) of y/x.
        Unlike atan(y/x), the signs of both x and y are considered.

    atanh(...)
        atanh(x)

        Return the hyperbolic arc tangent (measured in radians) of x.

    ceil(...)
        ceil(x)

        Return the ceiling of x as a float.
        This is the smallest integral value >= x.

    copysign(...)
        copysign(x,y)

        Return x with the sign of y.

    cos(...)
        cos(x)

        Return the cosine of x (measured in radians).

    cosh(...)
        cosh(x)

        Return the hyperbolic cosine of x.

    degrees(...)
        degrees(x) -> converts angle x from radians to degrees

    exp(...)
        exp(x)

        Return e raised to the power of x.

    fabs(...)
        fabs(x)

        Return the absolute value of the float x.

    factorial(...)
        factorial(x) -> Integral

        Find x!. Raise a ValueError if x is negative or non-integral.

    floor(...)
        floor(x)

        Return the floor of x as a float.
        This is the largest integral value <= x.

    fmod(...)
        fmod(x,y)

        Return fmod(x, y), according to platform C.  x % y may differ.

    frexp(...)
        frexp(x)

        Return the mantissa and exponent of x, as pair (m, e).
        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.

    fsum(...)
        sum(iterable)

        Return an accurate floating point sum of values in the iterable.
        Assumes IEEE-754 floating point arithmetic.

    hypot(...)
        hypot(x,y)

        Return the Euclidean distance, sqrt(x*x + y*y).

    isinf(...)
        isinf(x) -> bool
        Checks if float x is infinite (positive or negative)

    isnan(...)
        isnan(x) -> bool
        Checks if float x is not a number (NaN)

    ldexp(...)
        ldexp(x, i) -> x * (2**i)

    log(...)
        log(x[, base]) -> the logarithm of x to the given base.
        If the base not specified, returns the natural logarithm (base e) of x.

    log10(...)
        log10(x) -> the base 10 logarithm of x.

    log1p(...)
        log1p(x)

        Return the natural logarithm of 1+x (base e).
              The result is computed in a way which is accurate for x near zero.

    modf(...)
        modf(x)

        Return the fractional and integer parts of x.  Both results carry the si
gn
        of x and are floats.

    pow(...)
        pow(x,y)

        Return x**y (x to the power of y).

    radians(...)
        radians(x) -> converts angle x from degrees to radians

    sin(...)
        sin(x)

        Return the sine of x (measured in radians).

    sinh(...)
        sinh(x)

        Return the hyperbolic sine of x.

    sqrt(...)
        sqrt(x)

        Return the square root of x.

    tan(...)
        tan(x)

        Return the tangent of x (measured in radians).

    tanh(...)
        tanh(x)

        Return the hyperbolic tangent of x.

    trunc(...)
        trunc(x:Real) -> Integral

        Truncates x to the nearest Integral toward 0. Uses the __trunc__ magic m
ethod.

DATA
    e = 2.7182818284590451
    pi = 3.1415926535897931
"""



'''
#a = np.zeros((1,24),dtype=float).reshape(8,3)
a = np.array([[ -1.,  -1.,  -1. ], # c1, c2, u(k)
              [ -1.,  -1.,  -1. ],
              [ -1.,   1.,  -1. ],
              [ -1.,   1.,  -1. ],
              [  1.,   1.,   1. ],
              [  1.,   1.,   1. ],
              [  1.,  -1.,   1. ],
              [  1.,  -1.,   1. ]])
print "a ="
print a
print
# Orig 1.0,-1.0, 1.0, -1.0, 1.0, -1.0, -1.0
da = [ 2.0, 1.0, 3.0, -2.0, 2.0, -4.0, -5.0 ] # Corrupted input data
print "da ="
print da
print

#Orig 1.0, 1.0, -1.0, 1.0, 1.0, -1.0, -1.0
pa1 = [ -5.0, 2.0, -1.0, -2.0, 1.0, -2.0, -1.0 ] # Corrupted p1 data
print "pa1 ="
print pa1
print

# Orig 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, -1.0]
pa2 = [ 3.0, 1.0, -1.0, -1.0, -3.0, -1.0, -6.0 ] # Corrupted p2 data
print "pa2 ="
print pa2
print
'''
'''
input = 1
present_state = 3
next_state = { 0 : {0 : 0 , 1 : 2 , 2 : 3 , 3 : 1} ,
               1 : {0 : 2 , 1 : 0 , 2 : 1 , 3 : 3}
             }

output = { 0 : {0 : 0 , 1 : 0 , 2 : 1 , 3 : 1} ,
           1 : {0 : 3 , 1 : 3 , 2 : 2 , 3 : 2}
         }

print "next_state"
print next_state
print

print "output"
print output
print

print next_state[input][present_state]
print output[input][present_state]
print

print np.bitwise_and(next_state[input][present_state],1) # Gets LSB
print np.bitwise_and(next_state[input][present_state],2) >> 1 # Gets MSB
print np.bitwise_and(output[input][present_state],1) # Gets LSB, data bit
print np.bitwise_and(output[input][present_state],2) >> 1 # Gets MSB, parity bit
print
'''


'''
Forward_Error_Correction_Technique.m
iterat = 3
N = 10000
# Eb_No = [2:1:7] % [2 3 4 5 6 7]
'''
'''
def encode_bit(g,input,state):
  print "Encoding"
  print "g is"
  print g
  print
#  [n,k] = size(g) % Matlab "shape" function
  g_shape = g.shape
  print "g_shape ="
  print g_shape
  n = g_shape[0]
  K = g_shape[1]
  print "n =",n
  print "K =",K
  print
  m = K-1 # Number of states is 2**m
  print "input state ="
  print state
  print
  out = []
  out.append(state[0][0])
  out.append(state[0][1])
  print "out ="
  print out
  print
  for i in range(n): # Each row of g
    print "i =",i
    for j in range(K):
      print "j=",j
      out[i] = bitwise_xor(out[i],g[i][j])
  print "out is"
  print out
  print
  print "returning"
  print
  return (1,state) # this returns output and next state

def encode_block(g,x): #g = generation matrix, x is stream to be encoded
  print "encode_block"
  g_shape = g.shape
  print "g_shape ="
  print g_shape
  n = g_shape[0]
  K = g_shape[1]
  print "n =",n
  print "K =",K
  print
  m = K-1 # Number of states is 2**m
  x_shape = x.shape
  print "x_shape ="
  print x_shape
  print
  temp = x_shape[0]
  L_info = x_shape[1]
  print "temp =",temp
  print "L_info =",L_info
  print
  state = zeros((1,m),dtype=int)
#  state = []
#  state.append(0)
#  state.append(0)
  print "state ="
  print state
  print
  x = column_stack((x,state)) # Appends m zeros to get back to initial state
  print "x ="
  print x
  print
  L_total=L_info+m # Total length of stream
  for i in range(L_total):
    input_bit = x[0,i]
    (output_bits,state) = encode_bit(g,input_bit,state)
    print "input_bit =",input_bit
    print "output_bits =",output_bits,", state =",state

iterat = 3
#N = 10000
N = 10

Eb_No = arange(2,8,1) # Eb_No = [2:1:7] % produces [2 3 4 5 6 7]

print "Eb_No ="
print Eb_No
print
'''

'''
Matlab code
for kk=1,iterat
 kk
 d0=rand(1,N)
 d0(find(d0>=0.5)=1 % convert values >=1 to 1
 d0(find(d0<0.5)=0 % convert values <1 to 0
 d0
'''
'''
d0 = random.rand(1,N) # Column vector

print "d0 ="
print d0
print
print d0*100
print

#print "help random"
#print help(d0)
#print

# Generate a random stream of 0s and 1s
d01 = nonzero(d0<0.5)
d02 = nonzero(d0>=0.5)
print "d01 ="
print d01[1]
print "d02 ="
print d02[1]
print

'''


