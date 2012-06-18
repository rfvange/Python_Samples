# Translate a Matlab program into a SciPy program.
# Same content: send-pdf.pdf, fec_conv.py
#from scipy import *
#from numpy import *
import numpy as np

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

for i in range(N):
  if i in d01[1]:
    d0[0][i] = 0
  else:
    d0[0][i] = 1
#  d0[0][i] = 1 for i in d02[1]
print "d0 ="
print d0
print

#g = [[1,1,1],[1,0,1]] # Doesn't work
g = array([[1,1,1],[1,0,1]]) # Generator polynomial for rate 1/2, m=2
'''
'''
Refer to hard_decision_Viterbi.m and soft_decision_Viterbi.m

antipodal_conv(find(antipodal_conv>=1)=1 %converion of encoded bits to antipodal signal
antipodal_conv(find(antipodal_conv<=0)=-1

Ltx = length(antipodal_conv)

Es_No = Eb_No + 10*log(1/2)

No = 1./(10.^(Es_No./10)) (?)

antipodal_conv = encode_block(g,d0) % output from convolutional encoder

function encode_block(g,x) % g is polynomial matrix above, x is stream to be encoded, d0
'''
'''
encode_block(g,d0)
'''

