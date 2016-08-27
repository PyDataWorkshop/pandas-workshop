
	

## -----------------------------------------------------------------## 
## Manipulating DataFrames
# The use of DataFrames will be demonstrated using a data set containing a mix of data types using statelevel
# GDP data from the US. The data set contains both the GDP level between 2009 and 2012 (constant
# 2005 US\$) and the growth rates for the same years as well as a variable containing the region of the state.
# The data is loaded directly into a DataFrame using read\_excel.


from pandas import read_excel
state_gdp = read_excel("US_state_GDP.xls","Sheet1")
state_gdp.head()

################


##-  Single columns are selectable using the columnname, as in state_gdp["state"], and the value returned in
##- a Series. Multiple columns are similarly selected using a list of column names as in state_gdp [["state\_code",
##- ##- "state"]], or equivalently using an Index object. Note that these two methods are slightly different – selecting
a single column returns a Series while selecting multiple columns returns a DataFrame. This is
##- similar to how NumPy"s scalar selection returns an array with a lower dimension. Use a list of column

names containing a single name to return a DataFrame with a single column.


state_gdp["state_code"].head() # Series
state_gdp[["state_code"]].head() # DataFrame
state_code
state_gdp[["state_code","state"]].head()
state_code state
index = state_gdp.index
state_gdp[index[1:3]].head() 
# Elements 1 and 2 (0 based counting)
state gdp_2009


# Finally, single columns can also be selected using dot-notation and the column name.
# This is identical to using df["column"] and so the value returned is a Series.


state_gdp.state_code.head()


## -------------------------------------------## 

## The column name must be a legal Python variable name, 
## and so cannot contain spaces or reserved notation.


type(state_gdp.state_code)


###########################################################

## Selecting Rows
## Rows can be selected using standard numerical slices.


state_gdp[1:3]
# state_code state gdp_2009 gdp_2010 gdp_2011 gdp_2012

################
.


state_long_recession = state_gdp["gdp_growth_2010"]<0
state_gdp[state_long_recession].head()
state_code state gdp_2009 gdp_2010 gdp_2011 gdp_2012

################

##- Selecting Rows and Columns
##- Since the behavior of slicing depends on whether the input is text (selects columns) or numeric/Boolean
##- (selects rows), it isn"t possible to use standard slicing to select both rows and columns. 


## Instead, the selector
## method ix[rowselector,colselector] allows joint selection where rowselector is either a scalar selector, a
## slice selector, a Boolean array, a numeric selector or a row label or list of row labels and colselector is a
## scalar selector, a slice selector, a Boolean array, a numeric selector or a column name or list of column
## names.


state_gdp.ix[state_long_recession,"state"]

state_gdp.ix[state_long_recession,["state","gdp_growth_2009","gdp_growth_2010"]]

state_gdp.ix[10:15,:2] # Slice and slice

################


##- Adding Columns
##- Columns are added using one of three methods. The most obvious is to add a 
##- Series merging along the index using a dictionary-like syntax.


state_gdp_2012 = state_gdp[["state","gdp_2012"]]
state_gdp_2012.head()

################


state_gdp_2012 = state_gdp[["state","gdp_2012"]]
state_gdp_2012.insert(1,"gdp_growth_2012",state_gdp["gdp_growth_2012"])
state_gdp_2012.head()

################

## Formally this type of join performs a left join which means that only index values in the base DataFrame
## will appear in the combined DataFrame, and so inserting columns with different indices or fewer items
## than the DataFrame results in a DataFrame with the original indices with NaN-filled missing values in the
## new Series.


state_gdp_2012 = state_gdp.ix[0:2,["state","gdp_2012"]]
state_gdp_2012
state gdp_2012

################
##- Deleting Columns
##- Columns are deleted using the del keyword, using pop(column) on the DataFrame or by calling drop(list
##- of columns,axis=1) . The behavior of these differs slightly: del will simply delete the Series from the
##- DataFrame. 

##- pop() will both delete the Series and return the Series as an output, and drop() will return a
##- DataFrame with the Series dropped by will not modify the original DataFrame.


state_gdp_copy = state_gdp.copy()
state_gdp_copy = state_gdp_copy[["state_code","gdp_growth_2011","gdp_growth_2012"]]
state_gdp_copy.index = state_gdp["state_code"]
state_gdp_copy.head()

gdp_growth_2012 = state_gdp_copy.pop("gdp_growth_2012")
gdp_growth_2012.head()

state_gdp_copy.head()
del state_gdp_copy["gdp_growth_2011"]
state_gdp_copy.head()
state_gdp_copy = state_gdp.copy()
state_gdp_copy = state_gdp_copy[["state_code", "gdp_growth_2011","gdp_growth_2012"]]
state_gdp_dropped = state_gdp_copy.drop(["state_code" ,"gdp_growth_2011"],axis=1)
state_gdp_dropped.head()

################
