## Lession 1

# Import all libraries needed for the tutorial

# General syntax to import specific functions in a library: 
##from (library) import (specific library function)
from pandas import DataFrame, read_csv

# General syntax to import a library but no functions: 
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

# Enable inline plotting
%matplotlib inline
### Part 2:
print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

#################################

### Section 1 : Create Data
## The data set will consist of 5 baby names and the number of births recorded for that year (2016).

### Part 3:
# The inital set of baby names and birth rates
names = ['Kevin','Andrea','Marissa','Paul','David']
births = [811, 155, 77, 665, 973]

### Part 4:
## To merge these two lists together we will use the zip function.
zip?

### Part 5:
BabyNames = list(zip(names,births))
BabyNames

## We are basically done creating the data set. 
## We now will use the pandas library to export this data set into a csv file.

###################################
## myDF will be a DataFrame object. 
## You can think of this object holding the contents of the BabyNames in a format similar to a spreadsheet. 
## Lets take a look below at the contents inside myDF.

### Part 6:
myDF = pd.DataFrame(data = BabyNames, columns=['Names', 'Births'])
myDF

####################################
## Export the dataframe to a csv file. 
## We can name the file births2016.csv. The function to_csv will be used to export the file. 
## The file will be saved in the same location of the notebook unless specified otherwise.

### Part 7:
myDF.to_csv?

## The only parameters we will use is index and header. 
## Setting these parameters to True will prevent the index and header names from being exported. 
## Change the values of these parameters to get a better understanding of their use.

### Part 8:
myDF.to_csv('births2016.csv',index=False,header=False)

## Get Data
## To pull in the csv file, we will use the pandas function read_csv. 
## Let us take a look at this function and what inputs it takes.

### Part 9:
read_csv?

## Even though this functions has many parameters, we will simply pass it the location of the text file.
## myLocation = C:\Users\WorkArea\births2016.csv

################################

### Part 10:
Location = r'C:\WorkArea\births2016.csv'
myDF = pd.read_csv(Location)

## N.B. Notice the r before the string. 
## Since the slashes are special characters, prefixing the string with a r will escape the whole string.

### Part 11:
myDF

## This brings us the our first problem of the exercise. 
## The read_csv function treated the first record in the csv file as the header names. 
## This is obviously not correct since the text file did not provide us with header names.
## To correct this we will pass the header parameter to the read_csv function and set it to None (means null in python).

### Part 12:
myDF = pd.read_csv(Location, header=None)
myDF

#########################################
# If we wanted to give the columns specific names, we would have to pass another parameter called names. 
# We can also omit the header parameter.

### Part 13:
myDF = pd.read_csv(Location, names=['Names','Births'])
myDF


## You can think of the numbers [0,1,2,3,4] as the row numbers in an Excel file. 
## In pandas these are part of the index of the dataframe. 
## You can think of the index as the priMarissa key of a sql table with the exception that an index is allowed to have duplicates.
## [Names, Births] can be though of as column headers similar to the ones found in an Excel spreadsheet or sql database.

#------------------------------------------------------------------#

### Part 14:
## Delete the csv file now that we do not need it anymore.



import os
os.remove(Location)

#############################################
## Prepare Data
## The data we have consists of baby names and the number of births in the year 2016. 
## We already know that we have 5 records and none of the records are missing (non-null values).

## The Names column at this point is of no concern since it most likely is just composed of alpha numeric strings (baby names). 
## There is a chance of bad data in this column but we will not worry about that at this point of the analysis. 
## The Births column should just contain integers representing the number of babies born in a specific year with a specific name. 
## We can check if the all the data is of the data type integer. 
## It would not make sense to have this column have a data type of float. 
## Let's not worry about any possible outliers at this point of the analysis at this stage.

## Realize that aside from the check we did on the "Names" column, briefly looking 
## at the data inside the dataframe should be as far as we need to go at this stage of the game. 
## As we continue in the data analysis life cycle we will have plenty of opportunities 
## to find any issues with the data set.

### Part 15:
# Check data type of the columns
myDF.dtypes

### Part 16]:
# Check data type of Births column
myDF.Births.dtype

## As you can see the Births column is of type int64, thus no floats (decimal numbers) 
## or alpha numeric characters will be present in this column.

##########################################

## Section 4 - Analyze Data
## To find the most popular name or the baby name with the higest birth rate, we can do one of the following.

## Sort the dataframe and select the top row
## Use the max() attribute to find the maximum value

### Part 17:

# Method 1:
Sorted = myDF.sort_values(['Births'], ascending=False)
Sorted.head(1)

### Part 18]:
# Method 2:
myDF['Births'].max()
#------------------------------------------------------------------#
## Present Data
## Here we can plot the Births column and label the graph to show the end user the highest point on the graph. 
## In conjunction with the table, the end user has a clear picture that David is the most popular baby name in the data set.

## plot() is a convinient attribute where pandas lets you painlessly plot the data in your dataframe. 
## We learned how to find the maximum value of the Births column in the previous section. 
## Now to find the actual baby name of the 973 value looks a bit tricky, so lets go over it.

## Explain the pieces:
myDF['Names'] ## - This is the entire list of baby names, the entire Names column
myDF['Births'] ## - This is the entire list of Births in the year 2016, the entire Births column
myDF['Births'].max() ## - This is the maximum value found in the Births column

#------------------------------------------------------------------#

## [myDF['Births'] == myDF['Births'].max()] 
##    IS EQUAL TO 
## [Find all of the records in the Births column where it is equal to 973]

## myDF['Names'][myDF['Births'] == myDF['Births'].max()] 
##   IS EQUAL TO 
## Select all of the records in the Names column WHERE [The Births column is equal to 973]

## An alternative way could have been to use the Sorted dataframe:
Sorted['Names'].head(1).value

## The str() function simply converts an object into a string.

### Part 19
# Create graph
myDF['Births'].plot()

# Maximum value in the data set
MaxValue = myDF['Births'].max()

# Name associated with the maximum value
MaxName = myDF['Names'][myDF['Births'] == myDF['Births'].max()].values

# Text to display on graph
Text = str(MaxValue) + " - " + MaxName

# Add text to graph
plt.annotate(Text, xy=(1, MaxValue), xytext=(8, 0), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points')

print("The most popular name")
myDF[myDF['Births'] == myDF['Births'].max()]
#Sorted.head(1) can also be used


