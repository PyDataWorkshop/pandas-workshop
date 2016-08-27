

## --------------------------------------------------------------------## 
##- DataFrame

## While the Series class is the building block of data structures in pandas, the DataFrame is the work-horse.
## DataFrames collect multiple series in the same way that a spreadsheet collects multiple columns of data.
## In a simple sense, a DataFrame is like a 2-dimensional NumPy array – and when all data is numeric and
## of the same type (e.g. float64), it is virtually indistinguishable. However, a DataFrame is composed of
## Series and each Series has its own data type, and so not allDataFrames are representable as homogeneous
## NumPy arrays.
## A number of methods are available to initialize a DataFrame. 
## The simplest is from a homogeneous NumPy array.

	
from pandas import DataFrame
a = array([[1.0,2],[3,4]])
df = DataFrame(a)
df


## -------------------------------------------## 

## Like a Series, a DataFrame contains the input data as well as row labels. 
## However, since a DataFrame is a collection of columns, it also contains column 
## labels (located along the top edge). When none are
## provided, the numeric sequence 0, 1, . . . is used.
## Column names are entered using a keyword argument or later by assigning to columns.

	
df = DataFrame(array([[1,2],[3,4]]),columns=["a","b"])
df

df = DataFrame(array([[1,2],[3,4]]))
df.columns = ["dogs","cats"]
df


## -------------------------------------------## 
	
df = DataFrame(array([[1,2],[3,4]]), columns=["dogs","cats"], index=["Alice","Bob"])
df


## -------------------------------------------## 
## DataFrames can also be created from NumPy arrays with structured data.

	
import datetime
t = dtype([("datetime", "O8"), ("value", "f4")])
x = zeros(1,dtype=t)
x[0][0] = datetime.datetime(2013,01,01)
x[0][1] = 99.99
x

df = DataFrame(x)
df


## -------------------------------------------## 

	
s1 = Series(arange(0.0,5))
s2 = Series(arange(1.0,3))
DataFrame({"one": s1, "two": s2)
	
s3 = Series(arange(0.0,3))
DataFrame({"one": s1, "two": s2, "three": s3)
