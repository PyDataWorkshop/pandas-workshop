
# Lesson 5
 #We will be taking a brief look at the stack and unstack functions.

## --- Part 1:
# Import libraries
import pandas as pd
import sys

## --- Part 2:
print('Python version ' + sys.version)
print('Pandas version: ' + pd.__version__)


## --- Part3:
# Our small data set
d = {'one':[1,1],'two':[2,2]}
i = ['a','b']

# Create dataframe
df = pd.DataFrame(data = d, index = i)
df

## --- Part4:
df.index

## --- Part5:
# Bring the columns and place them in the index
stack = df.stack()
stack

## --- Part6:
# The index now includes the column names
stack.index


## --- Part7:
unstack = df.unstack()
unstack

## --- Part8:
unstack.index

## We can also flip the column names with the index using the T (transpose) function.

## --- Part9:
transpose = df.T
transpose

## --- Part10:
transpose.index
