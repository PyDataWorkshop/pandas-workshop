## Lesson 4
## In this lesson were going to go back to the basics. 
## We will be working with a small data set so that you can easily understand what I am trying to explain. 
## We will be adding columns, deleting columns, and slicing the data many different ways.

#####################################

# Import libraries
import pandas as pd
import sys
##  -- Part2:
print('Python version ' + sys.version)
print('Pandas version: ' + pd.__version__)

##################################


##  -- Part3:
# Our small data set
somedata = [0,1,2,3,4,5,6,7,8,9]

# Create dataframe
myDF = pd.DataFrame(somedata)
myDF


##  -- Part4:
# Lets change the name of the column
myDF.columns = ['Rev']
myDF


##  -- Part5:
# Lets add a column
myDF['NewCol'] = 5
myDF

##  -- Part6:
# Lets modify our new column
myDF['NewCol'] = myDF['NewCol'] + 1
myDF

##  -- Part7:
# We can delete columns
del myDF['NewCol']
myDF


##  -- Part8:
# Lets add a couple of columns
myDF['test'] = 3
myDF['col'] = myDF['Rev']
myDF


##  -- Part9:
# If we wanted, we could change the name of the index
i = ['a','b','c','d','e','f','g','h','i','j']
myDF.index = i
myDF

## We can now start to select pieces of the dataframe using loc.

##  -- Part10:
myDF.loc['a']

##  -- Part11:
# myDF.loc[inclusive:inclusive]
myDF.loc['a':'d']


##  -- Part12:
# myDF.iloc[inclusive:exclusive]
# Note: .iloc is strictly integer position based. 
# It is available from [version 0.11.0] (http://pandas.pydata.org/pandas-docs/stable/whatsnew.html#v0-11-0-april-22-2013) 
myDF.iloc[0:3]


## We can also select using the column name.

##  -- Part13:
myDF['Rev']


##  -- Part14:
myDF[['Rev', 'test']]

##  -- Part15:
# myDF.ix[rows,columns]
myDF.ix[0:3,'Rev']


##  -- Part16:
myDF.ix[5:,'col']

myDF.ix[:3,['col', 'test']]

################################

## There is also some handy function to select the top and bottom records of a dataframe.

##  -- Part18:
# Select top N number of records (default = 5)
myDF.head()

##  -- Part19:
# Select bottom N number of records (default = 5)
myDF.tail()


##########################################

df = pd.DataFrame(
         {'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]}); 
df
  
df.ix[df.AAA >= 5,'BBB'] = -1; 

df

df.ix[df.AAA >= 5,['BBB','CCC']] = 555; 

df

df.ix[df.AAA < 5,['BBB','CCC']] = 2000; 

df

dflow = df[df.AAA <= 5]

df
