
## Lesson 6
## Lets take a look at the groupby function.

## ---- Part1:

# Import libraries

import pandas as pd
import sys

## ---- Part2:
print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)

## ---- Part3:
# Our small data set
somedata = {'one':[1,1,1,1,1],
     'two':[2,2,2,2,2],
     'letter':['a','a','b','b','c']}

# Create dataframe
df = pd.DataFrame(somedata)
df

## ---- Part4:
# Create group object
one = df.groupby('letter')

# Apply sum function
one.sum()

## ---- Part5:
letterone = df.groupby(['letter','one']).sum()
letterone

## ---- Part6:
letterone.index


## You may want to not have the columns you are grouping by become your index, this can be easily achieved as shown below.

## ---- Part7:
letterone = df.groupby(['letter','one'], as_index=False).sum()
letterone

## ---- Part8:
letterone.index


