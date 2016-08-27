

#####################################################################

##  Series
##series are the primary building block of the data structures in pandas, and in many ways a Series behaves
##similarly to a NumPy array. A Series is initialized using a list or tupel, or directly from a NumPy array.
	
a = array([0.1, 1.2, 2.3, 3.4, 4.5])
a

from pandas import Series
s = Series([0.1, 1.2, 2.3, 3.4, 4.5])
s

s = Series(a) # NumPy array to Series
		

################
	
s = Series([0.1, 1.2, 2.3, 3.4, 4.5], index = ["a","b","c","d","e"])
s
		
################
##	The index enhances the usefulness of the pandas"s data structures (Series andDataFraame) and allows for
##	dictionary-like access to elements in the index (in addition to both numeric slicing and logical indices).
	
		
s["a"]
		
s[0]
		
s[["a","c"]]
		
s[[0,2]]
		
s[:2]

s[s>2]

################
		
s = Series([0.1, 1.2, 2.3, 3.4, 4.5], index = ["a","b","c","a","b"])

s
s["a"]

#dictionary

s = Series({"a": 0.1, "b": 1.2, "c": 2.3)
s

# Series are like NumPy arrays in that they support most numerical operations.
	
		
s = Series({"a": 0.1, "b": 1.2, "c": 2.3)
s * 2.0
s- 1.0

s1 = Series({"a": 0.1, "b": 1.2, "c": 2.3})
s2 = Series({"a": 1.0, "b": 2.0, "c": 3.0})
s3 = Series({"c": 0.1, "d": 1.2, "e": 2.3})

s1 + s2
s1 * s2

s1 + s3

## Mathematical operations performed on series which have non-unique indices will broadcast the operation
## to all indices which are common. For example, when one array has 2 elements with the same
## index, and another has 3, adding the two will produce 6 outputs.
	
s1 = Series([1.0,2,3],index=["a"]*3)
s2 = Series([4.0,5],index=["a"]*2)
s1 + s2
		
s1 = Series([1.0,2,3])
s1.values
s1.index
s1.index.values
s1.index = ["cat","dog","elephant"]
s1.index

##########################################################


##- Notable Methods and Properties
tail
## head() shows the first 5 rows of a series
## tail() shows the last 5 rows. 
## An optional argument can be used to return a different number of entries, as in head(10).

#########################################################

## isnull notnull

##-- isnull() returns a Series with the same indices containing Boolean values 
##--  indicating True for null values which include NaN and None, among others. 
		
##-- notnull() returns the negation of isnull() 
##-– that is, True for non-null values, and False otherwise.


## describe() returns a simple set of summary statistics about a Series. 
## The values returned is a series where

########################################################

s1 = Series(arange(10.0,20.0))
s1.describe()
summ = s1.describe()
summ["mean"]
########################################################

	unique and nunique
## unique() returns the unique elements of a series 
## nunique() returns the number of unique values in a Series.

drop and dropna
drop(labels) drop elements with the selected labels from a Series.

	
## drop(labels) drop elements with the selected labels from a Series.
s1 = Series(arange(1.0,6),index=["a","a","b","c","d"])
s1
s1.drop("a")
	################

	dropna() is similar to drop() except that it only drops null values – NaN or similar.

	
s1 = Series(arange(1.0,4.0),index=["a","b","c"])
s2 = Series(arange(1.0,4.0),index=["c","d","e"])
s3 = s1 + s2
s3
s3.dropna()

##############################################################################

#### fillna

##  fillna(value) fills all null values in a series with a specific value.


s1 = Series(arange(1.0,4.0),index=["a","b","c"])
s2 = Series(arange(1.0,4.0),index=["c","d","e"])
s3 = s1 + s2
s3.fillna(1.0)

################

## append
## append(series) appends one series to another, and is similar to list.append.

################

## replace
## replace(list,values) replaces a set of values in a Series with a new value. 
## replace is similar to fillna except that replace also replaces non-null values.

################

## update
## update(series) replaces values in a series with those in another series, 
## matching on the index, and is similar to a SQL update operation.

	
s1 = Series(arange(1.0,4.0),index=["a","b","c"])
s1
	
s2 = Series(1.0	* arange(1.0,4.0),index=["c","d","e"])
s1.update(s2)
s1
