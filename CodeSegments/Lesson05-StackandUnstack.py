# Lesson 5
 #We will be taking a brief look at the stack and unstack functions.

## --- Part 1 Import Libraries:
# Import libraries
import pandas as pd
import sys

## --- Part 2 Version Checking:
print('Python version ' + sys.version)
print('Pandas version: ' + pd.__version__)


## --- Part3:
# set up a small data set
myData = {'one':[1,1],'two':[2,2]}
i = ['a','b']

# Create dataframe
myDF = pd.DataFrame(data = myData, index = i)
myDF

## --- Part4:
myDF.index

## --- Part5:
# Bring the columns and place them in the index
stack = myDF.stack()
print(stack)

## --- Part6:
# The index now includes the column names
stack.index


## --- Part7:
unstack = myDF.unstack()
unstack

## --- Part8:
unstack.index

## We can also flip the column names with the index using the T (transpose) function.

## --- Part9:
transpose = myDF.T
print(transpose)

## --- Part10:
transpose.index
