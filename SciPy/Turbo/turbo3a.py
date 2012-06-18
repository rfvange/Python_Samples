# Translate a Matlab program into a SciPy program.
# Same content: send-pdf.pdf, fec_conv.py
from scipy import *
from numpy import *

iterat = 3
#N = 10000
N = 10

Eb_No = arange(2,8,1) # Eb_No = [2:1:7] % produces [2 3 4 5 6 7]

print "Eb_No ="
print Eb_No
print

da = []
da.append(1)
da.append(0)
da.append(1)
da.append(0)
da.append(1)
da.append(0)
da.append(0)

print "da ="
print da # Has commas
print

d0 = array(da) # Really don't need to do
print "d0 ="
print d0 # No commas in a numpy.ndarray.  A Python array has commas.
print

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

print bitwise_and(next_state[input][present_state],1) # Gets LSB
print bitwise_and(next_state[input][present_state],2) >> 1 # Gets MSB
print bitwise_and(output[input][present_state],1) # Gets LSB
print bitwise_and(output[input][present_state],2) >> 1 # Gets MSB
print

# Generate output of ENC1
output_stream_r = []
output_stream = []
parity_stream1_r = []
parity_stream1 = []

state = 0
for bit in da:
  print bit
  print "Output is", output[bit][state]
  bit_out = bitwise_and(output[bit][state],2) >> 1 # Gets MSB
  output_stream_r.append(bit_out)
  if bit_out == 0:
    bit_out = -1
  print "bit_out =",bit_out
  output_stream.append(bit_out)
  bit_out = bitwise_and(output[bit][state],1) # Gets LSB
  parity_stream1_r.append(bit_out)
  if bit_out == 0:
    bit_out = -1
  parity_stream1.append(bit_out)
  print "parity =",bit_out
  state = next_state[bit][state]
  print "Next state =",state

print

print "Encoder 1 output"
print "output_stream_r =",output_stream_r
print "output_stream (not transmitted) =",output_stream
print "parity_stream1_r =",parity_stream1_r
print "parity_stream1 =",parity_stream1
print

# Now work out how to interleave
# Just hard code it
db = [1,1,1,1,1,1,1]
db[2] = da[0]
db[3] = da[1]
db[0] = da[2]
db[4] = da[3]
db[1] = da[4]
db[5] = da[5]
db[6] = da[6]

print "interleave_out ="
print db
print

# Generate output of ENC2
output_stream_r2 = []
output_stream2 = []
parity_stream1_r2 = []
parity_stream12 = []

state = 0
for bit in db:
  print bit
  print "Output is", output[bit][state]
  bit_out = bitwise_and(output[bit][state],2) >> 1 # Gets MSB
  output_stream_r2.append(bit_out)
  if bit_out == 0:
    bit_out = -1
  print "bit_out =",bit_out
  output_stream2.append(bit_out)
  bit_out = bitwise_and(output[bit][state],1) # Gets LSB
  parity_stream1_r2.append(bit_out)
  if bit_out == 0:
    bit_out = -1
  parity_stream12.append(bit_out)
  print "parity =",bit_out
  state = next_state[bit][state]
  print "Next state =",state

print

print "Encoder 2 (interleaved input) out"
print "output_stream_r2 =",output_stream_r2
print "output_stream2 =",output_stream2
print "parity_stream1_r2 =",parity_stream1_r2
print "parity_stream12 =",parity_stream12
print

'''
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
# Separator
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
#separator
'''
encode_block(g,d0)
'''

