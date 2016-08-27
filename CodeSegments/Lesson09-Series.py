
# Introduction to pandas Series


# Preliminaries
# Imports
#  - not everything here is necessary for this particular exercise
#  - Saves some typing for these exercises.
​
from __future__ import division
from __future__ import print_function
from __future__ import print_function, division
from numpy import array
from numpy import sqrt
from pandas import Series
#from pandas import date_range 
import pandas
import scipy.stats as stats
from numpy import *
# End Imports
​

#############################################################################

# Create an numpy array (called it "a")

a = array([1.2, 2.33, 3.14, 4.56,5,6.2])
a


# Some Information about "a"
print(len(a))
print(type(a))
6

mySeries = Series([0.1, 1.113, 2.63, 3.4, 4.6])
print(mySeries)


## Convert our numpy array "a" into a Series
mySer2 = Series(a)
print(mySer2)


len(mySer2)

#############################################################################

print(type(mySer2))
print(type(a))


s = Series([0.1, 1.2, 2.3, 3.4, 4.5], index = ['a','b','c','d','e'])
s


s = Series([0.1, 1.2, 2.3, 3.4, 4.5], index = ['a','b','c','d','e'])
print(s['e'])
​
## Same as this
print(s[4])
​
4.5
4.5

print(s[['a','c']])
​
## Same as this
print(s[[0,2]])
​


print(s[:3])
print(s[s>2.5])

# Selecting items with the index "a"


# s = Series([0.1, 1.2, 2.3, 3.4, 4.5], 
#    index = ['a', 'b', 'c', 'a', 'b'])
# First and Fourth items have index "a"
s['a']

#############################################################################

a = array([0.1, 1.2, 2.3, 3.4, 4.5])
a

#############################################################################

s = Series({'a': 0.1, 'b': 1.2, 'c': 2.3})
s * 2.0

#############################################################################

s - 1.0

#############################################################################

s1 = Series({'a': 0.1, 'b': 1.2, 'c': 2.3})
s2 = Series({'a': 1.0, 'b': 2.0, 'c': 3.0})
s3 = Series({'c': 0.1, 'd': 1.2, 'e': 2.3})

s1 + s2

s1 * s2


s1 + s3

#############################################################################

​
s1 = Series([1.0,2,3],index=['a']*3)
s2 = Series([4.0,5],index=['a']*2)
s1 + s2
​
​

#############################################################################

s1 = Series([1.0,2,3])
print(s1.values)
print(s1.index)
[ 1.  2.  3.]
RangeIndex(start=0, stop=3, step=1)

​
s1.index = ['cat','dog','elephant']
s1.index

#############################################################################

s1 = Series(arange(10.0,20.0))
print(s1)
s1.describe()

#############################################################################

summ = s1.describe()
summ['mean']

#############################################################################

s1 = Series(arange(1.0,6),index=['a','a','b','c','d'])
print(s1)
s1.drop('a')


#############################################################################

​
s1 = Series(arange(1.0,4.0),index=['a','b','c'])
s2 = Series(arange(1.0,4.0),index=['c','d','e'])
s3 = s1 + s2
​
print(s3)
s3.dropna()
​

#############################################################################

s1 = Series(arange(1.0,4.0),index=['a','b','c'])
s2 = Series(arange(1.0,4.0),index=['c','d','e'])
s3 = s1 + s2
s3.fillna(-1.0)
#############################################################################
