# - http://datasciencelab.wordpress.com/2013/11/18/put-some-pandas-in-your-python/

import pandas as pd

df = pd.read_csv('Camera.csv', sep=';')
columns = ['Model', 'Date', 'MaxRes', 'LowRes', 'EffPix', 'ZoomW', 'ZoomT',          
           'NormalFR', 'MacroFR', 'Storage', 'Weight', 'Dimensions', 'Price']
df.columns = columns
df['Maker'] = df['Model'].apply(lambda s:s.split()[0])
df[['Maker','Model','Date','MaxRes','LowRes','Weight','Dimensions','Price']].head()

#######################################################################################

# Sorting data: display 5 most recent models 

df.sort(['Date'], ascending = False).head() 

# Filtering columns by value: show only models made by Nikon 

df[df['Maker'] == 'Nikon'] 

# Filtering columns by range of values: return cameras with prices above 350 and below 500

df[(df['Price'] > 350) & (df['Price'] <= 500)] 

# Get statistical descriptions of the data set: find maxima, minima, averages, standard deviations, percentiles

df[['MaxRes','LowRes','Storage','Weight','Dimensions','Price']].describe() 
#######################################################################################
# MATPLOTLIB
matplotlib.rcParams.update({'font.size': 16})
df[(df['Price'] < 500)][['Price']].hist(figsize=(8,5), bins=10, alpha=0.5)
plt.title('Histogram of camera prices\n')
plt.savefig('PricesHist.png', bbox_inches='tight')

#######################################################################################

# Grouping data with pandas

gDate = df[df['Date'] > 1998].groupby('Date').mean()
dates = [str(s) for s in gDate.index]
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(20,5))
cols = ['b', 'r', 'g']
vars = ['EffPix', 'Weight', 'Storage']
titles = ['effective pixels', 'weight', 'storage']
for i, var in enumerate(vars):    
  gDate[[var]].plot(ax=axes[i], alpha=0.5, legend=False, lw=4, c=cols[i])    
  axes[i].set_xticklabels(dates, rotation=40)    
  axes[i].set_title('Evolution of %s\n' % titles[i])
plt.savefig('CameraEvolution.png', bbox_inches='tight')
