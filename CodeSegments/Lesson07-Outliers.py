
## Lesson 7
## Outliers

import pandas as pd
import sys

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)

##################################################################

In [3]:
# Create a dataframe with dates as your index
States = ['NY', 'NY', 'NY', 'NY', 'FL', 'FL', 'GA', 'GA', 'FL', 'FL'] 
data = [1.0, 2, 3, 4, 5, 6, 7, 8, 9, 10]
idx = pd.date_range('1/1/2012', periods=10, freq='MS')
myDF1 = pd.DataFrame(data, index=idx, columns=['Revenue'])
myDF1['State'] = States

# Create a second dataframe
data2 = [10.0, 10.0, 9, 9, 8, 8, 7, 7, 6, 6]
idx2 = pd.date_range('1/1/2013', periods=10, freq='MS')
myDF2 = pd.DataFrame(data2, index=idx2, columns=['Revenue'])
myDF2['State'] = States

########################################################

# Combine dataframes

combDF = pd.concat([myDF1,myDF2])
combDF

## Ways to Calculate Outliers
## Note: Average and Standard Deviation are only valid for gaussian distributions.


# Method 1

# make a copy of original df
newDF = combDF.copy()

newDF['x-Mean'] = abs(newDF['Revenue'] - newDF['Revenue'].mean())
newDF['1.96*std'] = 1.96*newDF['Revenue'].std()  
newDF['Outlier'] = abs(newDF['Revenue'] - newDF['Revenue'].mean()) > 1.96*newDF['Revenue'].std()
newDF

########################################################################:
# Method 2
# Group by item

# make a copy of original df
newDF = combDF.copy()

State = newDF.groupby('State')

newDF['Outlier'] = State.transform( lambda x: abs(x-x.mean()) > 1.96*x.std() )
newDF['x-Mean'] = State.transform( lambda x: abs(x-x.mean()) )
newDF['1.96*std'] = State.transform( lambda x: 1.96*x.std() )
newDF

#######################################################

# Method 2
# Group by multiple items

# make a copy of original df
newDF = combDF.copy()

StateMonth = newDF.groupby(['State', lambda x: x.month])

newDF['Outlier'] = StateMonth.transform( lambda x: abs(x-x.mean()) > 1.96*x.std() )
newDF['x-Mean'] = StateMonth.transform( lambda x: abs(x-x.mean()) )
newDF['1.96*std'] = StateMonth.transform( lambda x: 1.96*x.std() )
newDF


# Method 3
# Group by item

# make a copy of original df
newDF = df.copy()

State = newDF.groupby('State')

def s(group):
group['x-Mean'] = abs(group['Revenue'] - group['Revenue'].mean())
group['1.96*std'] = 1.96*group['Revenue'].std()  
group['Outlier'] = abs(group['Revenue'] - group['Revenue'].mean()) > 1.96*group['Revenue'].std()
return group

newmyDF2 = State.apply(s)
newmyDF2

###########################################################################

# Method 3
# Group by multiple items

# make a copy of original df
newDF = combDF.copy()

StateMonth = newDF.groupby(['State', lambda x: x.month])

def s(group):
group['x-Mean'] = abs(group['Revenue'] - group['Revenue'].mean())
group['1.96*std'] = 1.96*group['Revenue'].std()  
group['Outlier'] = abs(group['Revenue'] - group['Revenue'].mean()) > 1.96*group['Revenue'].std()
return group

newmyDF2 = StateMonth.apply(s)
newmyDF2


## Assuming a non gaussian distribution (if you plot it, it will not look like a normal distribution)

# make a copy of original df
newDF = combDF.copy()

State = newDF.groupby('State')

newDF['Lower'] = State['Revenue'].transform( lambda x: x.quantile(q=.25) - (1.5*(x.quantile(q=.75)-x.quantile(q=.25))) )
newDF['Upper'] = State['Revenue'].transform( lambda x: x.quantile(q=.75) + (1.5*(x.quantile(q=.75)-x.quantile(q=.25))) )
newDF['Outlier'] = (newDF['Revenue'] < newDF['Lower']) | (newDF['Revenue'] > newDF['Upper']) 
newDF
