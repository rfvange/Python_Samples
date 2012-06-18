import nnmf
import urllib2
from numpy import *

tickers=['YHOO','AVP','BIIB','BP','CL','CVX',
         'DNA','EXPE','GOOG','PG','XOM','AMGN']

shortest=300
prices={}
dates=None

for t in tickers:
  # Open the URL

  print "Printing URL"
  print "t is ",t
  print 'http://ichart.finance.yahoo.com/table.csv?'+\
                       's=%s&d=11&e=26&f=2006&g=d&a=3&b=12&c=1996'%t +\
                       '&ignore=.csv'
  print

'''
Above prints
http://ichart.finance.yahoo.com/table.csv?s=YHOO&d=11&e=26&f=2006&g=d&a=3&b=12&c=1996&ignore=.csv

"11 26 2006" means start date Dec 26, 2006. "d" means daily. "3 12 1996" means Apr 12, 1996.

'''

  rows=urllib2.urlopen('http://ichart.finance.yahoo.com/table.csv?'+\
                       's=%s&d=11&e=26&f=2006&g=d&a=3&b=12&c=1996'%t +\
                       '&ignore=.csv').readlines()

  print "Printing rows"
  print rows
  print

  
  # Extract the volume field from every line
  prices[t]=[float(r.split(',')[5]) for r in rows[1:] if r.strip()!='']
  if len(prices[t])<shortest: shortest=len(prices[t])
  
  if not dates:
    dates=[r.split(',')[0] for r in rows[1:] if r.strip()!='']

l1=[[prices[tickers[i]][j] 
     for i in range(len(tickers))] 
    for j in range(shortest)]

w,h=nnmf.factorize(matrix(l1),pc=5)

print "Printing h"
print

print h

print "Printing w"
print w

print "Exiting"
exit()

# Loop over all the features
for i in range(shape(h)[0]):
  print "Feature %d" %i
  
  # Get the top stocks for this feature
  ol=[(h[i,j],tickers[j]) for j in range(shape(h)[1])]
  ol.sort()
  ol.reverse()
  for j in range(12):
    print ol[j]
  print
  
  # Show the top dates for this feature
  porder=[(w[d,i],d) for d in range(300)]
  porder.sort()
  porder.reverse()
  print [(p[0],dates[p[1]]) for p in porder[0:3]]
  print
