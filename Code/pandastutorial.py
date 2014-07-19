# http://www.bearrelroll.com/2013/05/python-pandas-tutorial/

###################################################
# Loading in Data
#
#Load csv into pandas dataframe
df = pd.read_csv('path_to_file' + '/' + 'nyc-condominium-dataset.csv')
 
#Load csv into pandas dataframe and set an index column
df =pd.read_csv('path_to_file', + '/' + 'nyc-condominium-dataset.csv', index_col = 'property_id')
 
#Load csv into pandas dataframe w/out Excel dialect
dia = csv.excel()
dia.quaoting = csv.QUOTE_NONE
df = pd.read_csv('path_to_file', + '/' + 'nyc-condominium-dataset.csv', index_col='property_id', dialect=dia)


dfg = df[['district','n_units']].groupby('district').agg([np.mean, np.std, np.size])
 
#Access Grouped statistic
fin_mean = dfg.ix['FINANCIAL']['n_units']['mean']
fin_std = dfg.ix['FINANCIAL']['n_units']['std']
print "Mean # of Units in Financial District is %s with %s StDev." % (fin_mean, fin_std)
Mean # of Units in Financial District is 157.580645161 with 176.613660135 StDev

###################################################
# Creating new variables/columns
#

#Get Mean/Standard Deviation of # of units per district
dfg = df[['district','n_units']].groupby('district').agg([np.mean, np.std, np.size])
 
#Access Grouped statistic
fin_mean = dfg.ix['FINANCIAL']['n_units']['mean']
fin_std = dfg.ix['FINANCIAL']['n_units']['std']
print "Mean # of Units in Financial District is %s with %s StDev." % (fin_mean, fin_std)
Mean # of Units in Financial District is 157.580645161 with 176.613660135 StDev



###################################################
# Group By Column
#

df['const'] = 1
 
#Compute statistics by district
dfg = df[['district','n_units']].groupby('district').agg([np.mean, np.std, np.size])
dfg = dfg['n_units'].rename(columns={'mean': 'n_units_mean', 'std': 'n_units_std', 'size': 'n_properties'}, inplace=True)
 
#Impute Missing values
n_units_mean = df['n_units'].mean()
df['n_units'].fillna(n_units_mean, inplace=True)
 
#Normalize the n_units via standard normal transformation
dfn = df.join(dfg)
dfn['nrm_n_units'] = (dfn['n_units'] - dfn['n_units_mean'])/dfn['n_units_std']
 
dfn[['district', 'n_units', 'n_units_mean', 'nrm_n_units']][:5]

###################################################
# Basic Statistics
#
#Get summary stats for all of your data
dfn.describe()
 
#Get summary stats for a subset of variables in your data
x = ['n_units', 'year_built', 'gross_sqft']
dfn[x].describe()

#Get mean of n units
n_units_mean = dfn['n_units'].mean()
n_units_mean
 
#Get percentile/quantiles
n_units_q30 = dfn['n_units'].quantile(q=0.3)
n_units_q30

###################################################
# Regression
#

pd.set_option('display.line_width', 300)
all_vars = ['property_id', 'district', 'n_units', 'year_built', 'market_value_sqft', 'comp_market_value_sqft', 'comp2_market_value_sqft']
df_model = df[all_vars]
df_model['age'] = 2013 - df['year_built'] 
 
#Get summary stats of each variable
df_model.describe()




