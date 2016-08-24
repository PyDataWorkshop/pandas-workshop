
## Part 1:
## Importing the libraries is the first step we will take in the lesson.
## Numpy will be used to help generate the sample data set. 

# Import all libraries needed for the tutorial

import pandas as pd

from numpy import random

import matplotlib.pyplot as plt
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

# Enable inline plotting
%matplotlib inline


###########

## Part 2:
## Check Environment
## Not absolutely necessary, just good practice to keep an eye on versions

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

#####################################

# Baby Names

#####################################

### Creating Data

## The data set will consist of 2,000 baby names and the number of births recorded for that year (2016). 
## We will also add plenty of duplicates so you will see the same baby name more than once. 
## You can think of the multiple entries per name simply being different hospitals around the country reporting the number of births per baby name. 
## So if two hospitals reported the baby name "Antonia", the data will have two values for the name Antonia. 
## We will start by creating the random set of baby names.

##########

## Part 3:

# The inital set of baby names

names = ['Antonia','Jessica','Gemma','Lucia','David','Rebecca','Camilla','Kevin','Christine','Oscar']


## To make a random list of 2,000 baby names using the ten above we will generate a random number between 0 and 9
## To do this we will be using the functions seed, randint, len, range, and zip.

###########

## Part 4:
# This will ensure the random samples below can be reproduced. 
# This means the random samples will always be identical.

random.seed?

###########

## Part 5:
random.randint?

###########

## Part 6:
len?

###########
## Part 7:
range?

###########

## Part 8:
zip?

##########


names = ['Antonia','Jessica','Gemma','Lucia','David','Rebecca','Camilla','Kevin','Christine','Oscar']

print(names[3])
print(names[0])
print(names[-1])

#########

seed(500) # Create seed

n = randint(low=0,high=len(names)) # Generate a random integer between zero and the length of the list "names".

print(n)
# names[n] # Select the name where its index is equal to n.

##########

## Part 9:


# Loop until i is equal to n, i.e. 1,2,3,....n.

# syntax : for i in range(n) 

# object : random_names = Select a random name from the name list and do this n times.


random.seed(500)
random_names = [names[random.randint(low=0,high=len(names))] for i in range(2000)]

# Print first 10 records
random_names[:10]

######################

## Generate a random numbers between 0 and 2000

## Part 10:
# The number of births per name for the year 2016
births = [random.randint(low=0,high=2000) for i in range(2000)]
births[:10]

# Merge the names and the births data set using the zip function.

##########################

## Part 11:
BabyDataSet = list(zip(random_names,births))
BabyDataSet[:10]

#########################

# Using pandas

# We are basically done creating the data set. 
# We now will use the pandas library to export this data set into a csv file.
# myDF will be a DataFrame object. 
# You can think of this object holding the contents of the BabyDataSet in a format similar to an  excel spreadsheet. 
# Lets take a look below at the contents inside myDF.

## Part 12:
myDF = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
myDF[:10]

########################

## Export the dataframe to a text file. 
## We can name the file births2016.txt. 
## The function to_csv will be used to export. 
## The file will be saved in the same location of the notebook unless specified otherwise.

#######################

## Part 13:
myDF.to_csv?

## The only parameters we will use is index and header. 
## Setting these parameters to False will prevent the index and header names from being exported. 
## Change the values of these parameters to get a better understanding of their use.

## Part 14:
myDF.to_csv('births2016.txt',index=False,header=False)

#################################################
## Getting Data

## To pull in the text file, we will use the pandas function read_csv. 
## Let us take a look at this function and what inputs it takes.

## Part 15:
pd.read_csv?

## Even though this functions has many parameters, we will simply pass it the location of the text file.

## Location = C:\Users\WorkArea\births2016.txt

##############################################

## Part 16:

Location = r'C:\Users\david\notebooks\update\births2016.txt'

myDF = pd.read_csv(Location)

## Notice the r before the string. Since the slashes are special characters, prefixing the string with a r will escape the whole string.

## Part 17:
myDF.info()

#############################################################################

# To actually see the contents of the dataframe we can use the head() function which by default will return the first five records. 
# You can also pass in a number n to return the top n records of the dataframe.

## Part 18:
myDF.head()

## This brings us the our first problem of the exercise. 
## The read_csv function treated the first record in the text file as the header names. 
## This is obviously not correct since the text file did not provide us with header names.

## To correct this we will pass the header parameter to the read_csv function and set it to None (means null in python).

## Part 19:
myDF = pd.read_csv(Location, header=None)
myDF.info()

#--------------------------------------------------------------------------------------------#
# There are 2000 records in the data set
# There is a column named 0 with 2000 values
# There is a column named 1 with 2000 values
# Out of the two columns, one is numeric, the other is non numeric
# Now lets take a look at the last five records of the dataframe

## Part 20:
myDF.tail()

#--------------------------------------------------------------------------------------------#

## Naming Columns

# If we wanted to give the columns specific names, we would have to pass another paramter called names. 
# We can also omit the header parameter.

## Part 21:
myDF = pd.read_csv(Location, names=['Names','Births'])
myDF.head(5)

## You can think of the numbers [0,1,2,3,4,...] as the row numbers in an Excel file. 
## In pandas these are part of the index of the dataframe. You can think of the index as the priGemma key of a sql table with the exception that an index is allowed to have duplicates.
## [Names, Births] can be though of as column headers similar to the ones found in an Excel spreadsheet or sql database.


## Delete the txt file now that we are done using it.

## Part 22:
import os
os.remove(Location)

############################################
## Prepare Data
## The data we have consists of baby names and the number of births in the year 2016. 
## We already know that we have 2,000 records and none of the records are missing (non-null values).
## We can verify the "Names" column still only has five unique names.

# #We can use the unique property of the dataframe to find all the unique records of the "Names" column.

## Part 23:
# Method 1:
myDF['Names'].unique()

## Part 24:
# If you actually want to print the unique values:
for x in myDF['Names'].unique():
    print(x)

## Part 25:
# Method 2:
print(myDF['Names'].describe())

####################################################################

# Since we have multiple values per baby name, we need to aggregate this data so we only have a baby name appear once.
# This means the 2000 rows will need to become 5. 
# We can accomplish this by using the groupby function.

## Part 26:
myDF.groupby?

## Part 27:

# Create a groupby object

name = myDF.groupby('Names')

# Apply the sum function to the groupby object
myDF = name.sum()
myDF


###########################################################################
## Section 4: Analyze Data

# To find the most popular name or the baby name with the higest birth rate, we can do one of the following.

# Sort the dataframe and select the top row

# Use the max() attribute to find the maximum value


## Part 28:
# Method 1:
Sorted = myDF.sort_values(['Births'], ascending=False)
Sorted.head(1)

## Part 29:
# Method 2:
myDF['Births'].max()

###########################################################################
## Section 5 : Present Data

# Here we can plot the Births column and label the graph to show the end user the highest point on the graph. 
# In conjunction with the table, the end user has a clear picture that Antonia is the most popular baby name in the data set.

## Part 30:
# Create graph
myDF['Births'].plot.bar()

print("The most popular name")
myDF.sort_values(by='Births', ascending=False)

