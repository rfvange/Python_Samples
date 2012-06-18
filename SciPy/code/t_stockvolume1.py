#import nnmf
import urllib2
from numpy import *

tickers=['YHOO']

shortest=300
prices={}
dates=None

for t in tickers:
  # Open the URL

  print "Printing URL"
  print "t is ",t
  print 'http://ichart.finance.yahoo.com/table.csv?s=BAC&d=8&e=26&f=2010&g=d&a=4&b=29&c=1919&ignore=.csv'
  print

'''
Above prints
http://ichart.finance.yahoo.com/table.csv?s=YHOO&d=11&e=26&f=2006&g=d&a=3&b=12&c=1996&ignore=.csv

"11 26 2006" means start date Dec 26, 2006. "d" means daily. "3 12 1996" means Apr 12, 1996.

'''

rows=urllib2.urlopen('http://ichart.finance.yahoo.com/table.csv?s=BAC&d=8&e=26&f=2010&g=d&a=4&b=29&c=1919&ignore=.csv').readlines()

'''
print "Printing rows"
print rows
print
'''

print "Extracting:"
'''
for stock in range(len(rows)):
  print rows[stock],
print
print "Again"
'''
for stock in rows:
  print stock,
  close=stock.split(',')[4]
  print close


