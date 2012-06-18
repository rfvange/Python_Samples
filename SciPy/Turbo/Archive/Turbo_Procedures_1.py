# These are the procedures

import numpy as np
from pprint import pprint

def Calc_Forward_Branch_Metrics(FB_Full_Branch_Metrics, FB_Forward_Branch_Metrics, FB_Norm_Forward_Branch_Metrics) :
# Calculates the forward branch metrics and the normalized forward branch metrics
# Needs to be customized for every code
  '''
  print "In Calc_Forward_Branch_Metrics"
  print "FB_Full_Branch_Metrics ="
  pprint(FB_Full_Branch_Metrics)
  print
  print "FB_Norm_Forward_Branch_Metrics ="
  print FB_Norm_Forward_Branch_Metrics
  print
  print "FB_Forward_Branch_Metrics ="
  print FB_Forward_Branch_Metrics
  print
  '''
  for bit in range(7):
    '''
    print "bit =",bit
    print "FB_Norm_Forward_Branch_Metrics[0][bit] =",FB_Norm_Forward_Branch_Metrics[0][bit]
    print "FB_Full_Branch_Metrics[0][bit] =",FB_Full_Branch_Metrics[0][bit]
    print "FB_Norm_Forward_Branch_Metrics[1][bit] =",FB_Norm_Forward_Branch_Metrics[1][bit]
    print "FB_Full_Branch_Metrics[5][bit] =",FB_Full_Branch_Metrics[5][bit]
    print
    '''
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


#    print "Reloop"

  print "Exit Calc_Forward_Branch_Metrics"

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
  print "Exit Calc_Norm_Backward_Branch_Metrics_Denom"

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


def Initialize_Tables(IT_Forward_Branch_Metrics, IT_Norm_Forward_Branch_Metrics, \
                      IT_Backward_Branch_Metrics, IT_Norm_Backward_Branch_Metrics):
  IT_Forward_Branch_Metrics[0][0] = 1.0
  IT_Forward_Branch_Metrics[4][0] = 1.0
  IT_Norm_Forward_Branch_Metrics[0][0] = 1.0
  IT_Backward_Branch_Metrics[0][6] = 1.0
  IT_Norm_Backward_Branch_Metrics[0][6] = 1.0

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

def Calc_Product_Of_Metrics(CM_Product_Of_Metrics, CM_Norm_Forward_Branch_Metrics, \
                            CM_Partial_Branch_Metrics, CM_Norm_Backward_Branch_Metrics) :

  for bit in range(7) :
    CM_Product_Of_Metrics[0][bit] = CM_Norm_Forward_Branch_Metrics[0][bit] * CM_Partial_Branch_Metrics[0][bit] * \
                                    CM_Norm_Backward_Branch_Metrics[0][bit]
    CM_Product_Of_Metrics[1][bit] = CM_Norm_Forward_Branch_Metrics[1][bit] * CM_Partial_Branch_Metrics[1][bit] * \
                                    CM_Norm_Backward_Branch_Metrics[2][bit]
    CM_Product_Of_Metrics[2][bit] = CM_Norm_Forward_Branch_Metrics[2][bit] * CM_Partial_Branch_Metrics[2][bit] * \
                                    CM_Norm_Backward_Branch_Metrics[3][bit]
    CM_Product_Of_Metrics[3][bit] = CM_Norm_Forward_Branch_Metrics[3][bit] * CM_Partial_Branch_Metrics[3][bit] * \
                                    CM_Norm_Backward_Branch_Metrics[1][bit]
    CM_Product_Of_Metrics[4][bit] = CM_Norm_Forward_Branch_Metrics[0][bit] * CM_Partial_Branch_Metrics[4][bit] * \
                                    CM_Norm_Backward_Branch_Metrics[2][bit]
    CM_Product_Of_Metrics[5][bit] = CM_Norm_Forward_Branch_Metrics[1][bit] * CM_Partial_Branch_Metrics[5][bit] * \
                                    CM_Norm_Backward_Branch_Metrics[0][bit]
    CM_Product_Of_Metrics[6][bit] = CM_Norm_Forward_Branch_Metrics[2][bit] * CM_Partial_Branch_Metrics[6][bit] * \
                                    CM_Norm_Backward_Branch_Metrics[1][bit]
    CM_Product_Of_Metrics[7][bit] = CM_Norm_Forward_Branch_Metrics[3][bit] * CM_Partial_Branch_Metrics[7][bit] * \
                                    CM_Norm_Backward_Branch_Metrics[3][bit]

def Calc_Ratio(CR_Product_Of_Metrics, CR_Detection_Ratio, CR_Received_Data, CR_Extrinsic_Value) :

  for bit in range(7) :
    pos = neg = 0.0
    for value in range(4) :
      neg += CR_Product_Of_Metrics[value][bit]
      pos += CR_Product_Of_Metrics[value+4][bit]
    CR_Detection_Ratio[0][bit] = np.log(pos/neg)
    CR_Detection_Ratio[1][bit] = CR_Detection_Ratio[0][bit] + CR_Received_Data[0][bit] + CR_Extrinsic_Value[bit]
    if CR_Detection_Ratio[1][bit] >= 0 :
      CR_Detection_Ratio[2][bit] = 1.0
    else :
      CR_Detection_Ratio[2][bit] = 0.0



