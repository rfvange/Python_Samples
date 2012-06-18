# Procedure that takes input:
# Extrinsic Le(c(k,1))
# Branch Table Entries c(k,j)
# Lc = 4*Es/N0
# Systematic bit - y(k,1,s), Parity bit i - y(k,i,p)
# and returns a tuple: (Partial Branch Metrics, Full Branch Metrics).

#from scipy import *
#from numpy import *
#import numpy as np
#from pprint import pprint
from Turbo_Procedures import *

# Construct all relevant tables

#Sig_to_Noise = 3
Sig_to_Noise = 0.25 # Doesn't alter raw data

"""
# All correct without noise
Received_Data = \
 [[1, -1, 1, -1, 1, -1, -1], # Intrinsic, y(1,s) - Bit 1 is an error
  [1, 1, -1, 1, 1, -1, -1], # Parity 1, y(1,p) - Bits 3 & 5 are errors
  [1, -1, 1, -1, -1, -1, -1]] # Parity 2, y(2,p) - Bit 1 is an error
"""

"""
# Original
Received_Data = \
 [[2, 1, 3, -2, 2, -4, -5], # Intrinsic, y(1,s) - Bit 1 is an error
  [-5, 1, -1, -1, 1, -2, -1], # Parity 1, y(1,p) - Bits 3 & 5 are errors
  [3, 1, -1, -1, -3, -1, -6]] # Parity 2, y(2,p) - Bit 1 is an error
"""

Received_Data = \
 [[1, -2.1, 1, -1, -0.5, -2, -2], # Intrinsic, y(1,s) - Bit 1 is an error
  [2, 2, -1, 1, -1, -2, -2], # Parity 1, y(1,p) - Bits 3 & 5 are errors
  [2, -1, 2, -1, 1, -1, -1]] # Parity 2, y(2,p) - Bit 1 is an error

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

Iter_Data = np.zeros(2*7,dtype=float).reshape(2,7)
Iter_Data[0] = Adj_Data[0]
Iter_Data[1] = Adj_Data[1]

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

Extrinsic = 1
Calc_Metrics(Extrinsic_Value, Transition_T, Iter_Data,
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

print "Before Calc_Forward_Branch_Metrics"
print "Full_Branch_Metrics ="
print Full_Branch_Metrics
print
print "Forward_Branch_Metrics ="
print Forward_Branch_Metrics
print
print "Norm_Forward_Branch_Metrics ="
print Norm_Forward_Branch_Metrics
print

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

Calc_Product_Of_Metrics(Product_Of_Metrics, Norm_Forward_Branch_Metrics, \
                        Partial_Branch_Metrics, Norm_Backward_Branch_Metrics)
print "Product_Of_Metrics ="
print Product_Of_Metrics
print

Detection_Ratio = np.zeros(3*7,dtype = float).reshape(3,7)
Calc_Ratio(Product_Of_Metrics, Detection_Ratio, Received_Data, Extrinsic_Value)
print "Detection_Ratio ="
print Detection_Ratio
print

Extrinsic_Value = Detection_Ratio[0]
print "Extrinsic_Value ="
print Extrinsic_Value
print

# Decoder 2

Iter_Data[1] = Adj_Data[2]

Calc_Metrics(Extrinsic_Value, Transition_T, Iter_Data,
             Full_Branch_Metrics, Partial_Branch_Metrics)

print "Done"
print "FBM ="
print Full_Branch_Metrics
print
print "PBM ="
print Partial_Branch_Metrics
print

print "Before Calc_Forward_Branch_Metrics"
print "Full_Branch_Metrics ="
print Full_Branch_Metrics
print
print "Forward_Branch_Metrics ="
print Forward_Branch_Metrics
print
print "Norm_Forward_Branch_Metrics ="
print Norm_Forward_Branch_Metrics
print

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

Calc_Product_Of_Metrics(Product_Of_Metrics, Norm_Forward_Branch_Metrics, \
                        Partial_Branch_Metrics, Norm_Backward_Branch_Metrics)
print "Product_Of_Metrics ="
print Product_Of_Metrics
print

Detection_Ratio = np.zeros(3*7,dtype = float).reshape(3,7)
Calc_Ratio(Product_Of_Metrics, Detection_Ratio, Received_Data, Extrinsic_Value)
print "Detection_Ratio ="
print Detection_Ratio
print

Extrinsic_Value = Detection_Ratio[0]
print "Extrinsic_Value ="
print Extrinsic_Value
print

# Iteration 2 Through Decoder 1

Iter_Data[1] = Adj_Data[1]

Calc_Metrics(Extrinsic_Value, Transition_T, Iter_Data,
             Full_Branch_Metrics, Partial_Branch_Metrics)

print "Done"
print "FBM ="
print Full_Branch_Metrics
print
print "PBM ="
print Partial_Branch_Metrics
print

print "Before Calc_Forward_Branch_Metrics"
print "Full_Branch_Metrics ="
print Full_Branch_Metrics
print
print "Forward_Branch_Metrics ="
print Forward_Branch_Metrics
print
print "Norm_Forward_Branch_Metrics ="
print Norm_Forward_Branch_Metrics
print

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

Calc_Product_Of_Metrics(Product_Of_Metrics, Norm_Forward_Branch_Metrics, \
                        Partial_Branch_Metrics, Norm_Backward_Branch_Metrics)
print "Product_Of_Metrics ="
print Product_Of_Metrics
print

Detection_Ratio = np.zeros(3*7,dtype = float).reshape(3,7)
Calc_Ratio(Product_Of_Metrics, Detection_Ratio, Received_Data, Extrinsic_Value)
print "Detection_Ratio ="
print Detection_Ratio
print

Extrinsic_Value = Detection_Ratio[0]
print "Extrinsic_Value ="
print Extrinsic_Value
print

# Iteration 2 Through Decoder 2

Iter_Data[1] = Adj_Data[2]

Calc_Metrics(Extrinsic_Value, Transition_T, Iter_Data,
             Full_Branch_Metrics, Partial_Branch_Metrics)

print "Done"
print "FBM ="
print Full_Branch_Metrics
print
print "PBM ="
print Partial_Branch_Metrics
print

print "Before Calc_Forward_Branch_Metrics"
print "Full_Branch_Metrics ="
print Full_Branch_Metrics
print
print "Forward_Branch_Metrics ="
print Forward_Branch_Metrics
print
print "Norm_Forward_Branch_Metrics ="
print Norm_Forward_Branch_Metrics
print

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

Calc_Product_Of_Metrics(Product_Of_Metrics, Norm_Forward_Branch_Metrics, \
                        Partial_Branch_Metrics, Norm_Backward_Branch_Metrics)
print "Product_Of_Metrics ="
print Product_Of_Metrics
print

Detection_Ratio = np.zeros(3*7,dtype = float).reshape(3,7)
Calc_Ratio(Product_Of_Metrics, Detection_Ratio, Received_Data, Extrinsic_Value)
print "Detection_Ratio ="
print Detection_Ratio
print

Extrinsic_Value = Detection_Ratio[0]
print "Extrinsic_Value ="
print Extrinsic_Value
print

# Iteration 3 Through Decoder 1

Iter_Data[1] = Adj_Data[1]

Calc_Metrics(Extrinsic_Value, Transition_T, Iter_Data,
             Full_Branch_Metrics, Partial_Branch_Metrics)

print "Done"
print "FBM ="
print Full_Branch_Metrics
print
print "PBM ="
print Partial_Branch_Metrics
print

print "Before Calc_Forward_Branch_Metrics"
print "Full_Branch_Metrics ="
print Full_Branch_Metrics
print
print "Forward_Branch_Metrics ="
print Forward_Branch_Metrics
print
print "Norm_Forward_Branch_Metrics ="
print Norm_Forward_Branch_Metrics
print

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

Calc_Product_Of_Metrics(Product_Of_Metrics, Norm_Forward_Branch_Metrics, \
                        Partial_Branch_Metrics, Norm_Backward_Branch_Metrics)
print "Product_Of_Metrics ="
print Product_Of_Metrics
print

Detection_Ratio = np.zeros(3*7,dtype = float).reshape(3,7)
Calc_Ratio(Product_Of_Metrics, Detection_Ratio, Received_Data, Extrinsic_Value)
print "Detection_Ratio ="
print Detection_Ratio
print

Extrinsic_Value = Detection_Ratio[0]
print "Extrinsic_Value ="
print Extrinsic_Value
print

# Iteration 3 Through Decoder 2

Iter_Data[1] = Adj_Data[2]

Calc_Metrics(Extrinsic_Value, Transition_T, Iter_Data,
             Full_Branch_Metrics, Partial_Branch_Metrics)

print "Done"
print "FBM ="
print Full_Branch_Metrics
print
print "PBM ="
print Partial_Branch_Metrics
print

print "Before Calc_Forward_Branch_Metrics"
print "Full_Branch_Metrics ="
print Full_Branch_Metrics
print
print "Forward_Branch_Metrics ="
print Forward_Branch_Metrics
print
print "Norm_Forward_Branch_Metrics ="
print Norm_Forward_Branch_Metrics
print

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

Calc_Product_Of_Metrics(Product_Of_Metrics, Norm_Forward_Branch_Metrics, \
                        Partial_Branch_Metrics, Norm_Backward_Branch_Metrics)
print "Product_Of_Metrics ="
print Product_Of_Metrics
print

Detection_Ratio = np.zeros(3*7,dtype = float).reshape(3,7)
Calc_Ratio(Product_Of_Metrics, Detection_Ratio, Received_Data, Extrinsic_Value)
print "Detection_Ratio ="
print Detection_Ratio
print

Extrinsic_Value = Detection_Ratio[0]
print "Extrinsic_Value ="
print Extrinsic_Value
print

# Iteration 4 Through Decoder 1

Iter_Data[1] = Adj_Data[1]

Calc_Metrics(Extrinsic_Value, Transition_T, Iter_Data,
             Full_Branch_Metrics, Partial_Branch_Metrics)

print "Done"
print "FBM ="
print Full_Branch_Metrics
print
print "PBM ="
print Partial_Branch_Metrics
print

print "Before Calc_Forward_Branch_Metrics"
print "Full_Branch_Metrics ="
print Full_Branch_Metrics
print
print "Forward_Branch_Metrics ="
print Forward_Branch_Metrics
print
print "Norm_Forward_Branch_Metrics ="
print Norm_Forward_Branch_Metrics
print

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

Calc_Product_Of_Metrics(Product_Of_Metrics, Norm_Forward_Branch_Metrics, \
                        Partial_Branch_Metrics, Norm_Backward_Branch_Metrics)
print "Product_Of_Metrics ="
print Product_Of_Metrics
print

Detection_Ratio = np.zeros(3*7,dtype = float).reshape(3,7)
Calc_Ratio(Product_Of_Metrics, Detection_Ratio, Received_Data, Extrinsic_Value)
print "Detection_Ratio ="
print Detection_Ratio
print

Extrinsic_Value = Detection_Ratio[0]
print "Extrinsic_Value ="
print Extrinsic_Value
print

# Iteration 4 Through Decoder 2

Iter_Data[1] = Adj_Data[2]

Calc_Metrics(Extrinsic_Value, Transition_T, Iter_Data,
             Full_Branch_Metrics, Partial_Branch_Metrics)

print "Done"
print "FBM ="
print Full_Branch_Metrics
print
print "PBM ="
print Partial_Branch_Metrics
print

print "Before Calc_Forward_Branch_Metrics"
print "Full_Branch_Metrics ="
print Full_Branch_Metrics
print
print "Forward_Branch_Metrics ="
print Forward_Branch_Metrics
print
print "Norm_Forward_Branch_Metrics ="
print Norm_Forward_Branch_Metrics
print

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

Calc_Product_Of_Metrics(Product_Of_Metrics, Norm_Forward_Branch_Metrics, \
                        Partial_Branch_Metrics, Norm_Backward_Branch_Metrics)
print "Product_Of_Metrics ="
print Product_Of_Metrics
print

Detection_Ratio = np.zeros(3*7,dtype = float).reshape(3,7)
Calc_Ratio(Product_Of_Metrics, Detection_Ratio, Received_Data, Extrinsic_Value)
print "Detection_Ratio ="
print Detection_Ratio
print

Extrinsic_Value = Detection_Ratio[0]
print "Extrinsic_Value ="
print Extrinsic_Value
print

#exit()


