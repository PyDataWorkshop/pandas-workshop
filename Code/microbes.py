# http://bconnelly.net/2013/10/summarizing-data-in-python-with-pandas/

import pandas

# Load the data into a DataFrame
data = pandas.read_csv('TradeoffData.csv')

data.head(n=10)

# This stores the grouping in a pandas DataFrameGroupBy object, 
# which you will see if you try to print it.
bytreatment = data.groupby('Treatment')

bygroup_treatment = data.groupby(['Group', 'Treatment'])
 
# We can then get similar statistics for this two-level grouping

bygroup_treatment['RelativeFitness'].describe()

# The describe() method produces some very useful statistics about 
# the "RelativeFitness" values for the grouped data. 
# Pandas includes a number of common ones such as mean(), max(), median(), etc.:
 
bygroup_treatment['RelativeFitness'].mean()

bygroup_treatment['RelativeFitness'].aggregate(np.sum)

# We can also apply multiple functions to the groups using agg():

bygroup_treatment['RelativeFitness'].agg([np.sum, np.mean, np.std, len])
