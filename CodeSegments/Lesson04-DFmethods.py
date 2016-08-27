
##- Notable Properties and Methods

from pandas import *
from numpy import *
## ----------------------------------------------------------------------------------------------## 

## drop, dropna and drop_duplicates
## - 
## - drop(), dropna() and drop_duplicates() can all be used to drop rows or columns from a DataFrame.
## - drop(labels) drops rows based on the rowlabels in a label or list labels. drop(column_name,axis=1) drops
## - columns based on a column name or list column names.
## - 
## - dropna() drops rows with anyNaN(or null) values. It can be used with the keyword argument dropna(how="all")
## - to only drop rows which have missing values for all variables. It can also be used with the keyword argument
## - dropna(axis=1) to drop columns with missing values. Finally, drop_duplicates() removes rows
## - which are duplicates or other rows, and is used with the keyword argument drop_duplicates(cols=col_list)
## - to only consider a subset of all columns when checking for duplicates.

## --------------------------------------------------------------------------## 
## - values and index
## - values retrieves a the NumPy array (structured if the data columns are heterogeneous) underlying the
## - DataFrame, and index returns the index of the DataFrame or can be assigned to to set the index.
## --------------------------------------------------------------------------## 

## --fillna

# fillna() fills NaN or other null values with other values. The simplest use fill all NaNs with a single value
# and is called fillna(value=value ). Using a dictionary allows for more sophisticated na-filling with column
# names as the keys and the replacements as the values.


df = DataFrame(array([[1, nan],[nan, 2]]))
df.columns = ["one","two"]
replacements = {"one":1,"two":2}
df.fillna(value=replacements)

################

### T and transpose
## T and transpose are identical – both swap rows and columns of a DataFrame. 
##T operates like a property, while transpose is used as a method.

## --------------------------------------------------------------------------## 

## sort and sort_index
## - 
## - sort and sort_index are identical in their outcome and only differ in the inputs. 
## - The default behavior of sort is to sort using the index. 
## - Using a keyword argument axis=1 sorts the DataFrame by the column names. 




df = DataFrame(array([[1, 3],[1, 2],[3, 2],[2,1]]), columns=["one","two"])
df.sort(columns="one")
df.sort(columns=["one","two"])			
df.sort(columns=["one","two"], ascending=[0,1])

#####################################################################

## pivot


prices = [101.0,102.0,103.0]
tickers = ["GOOG","AAPL"]
import itertools
data = [v for v in itertools.product(tickers,prices)]
import pandas as pd
dates = pd.date_range("20130103",periods=3)
df = DataFrame(data, columns=["ticker","price"])
df["dates"] = dates.append(dates)
df
df.pivot(index="dates",columns="ticker",values="price")

####################################################################		
## - stack and unstack
## - 
## - stack and unstack transform a DataFrame to a Series (stack) and back to a DataFrame (unstack). 
## - The stacked DataFrame (a Series) uses an index containing both the original row and column labels.
## - 
## - 
## - concat and append


df1 = DataFrame([1,2,3],index=["a","b","c"],columns=["one"])
df2 = DataFrame([4,5,6],index=["c","d","e"],columns=["two"])
pd.concat((df1,df2), axis=1)

pd.concat((df1,df2), axis=1, join="inner")

## --------------------------------------------------------------------------## 

## - reindex, reindex_like and reindex_axis

original = DataFrame([[1,1],[2,2],[3.0,3]],index=["a","b","c"],	columns=["one","two"])

original.reindex(index=["b","c","d"])

different = DataFrame([[1,1],[2,2],[3.0,3]],index=["c","d","e"], columns=["one","two"])

original.reindex_like(different)

original.reindex_axis(["two","one"], axis = 1)

###########################################################
