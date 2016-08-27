state_gdp = pandas.read_excel('US_state_GDP.xls','Sheet1')
state_gdp.head()

state_gdp[['state_code','state']].head()
index = state_gdp.index
state_gdp[index[1:3]].head() # Elements 1 and 2 (0-based counting)

state_gdp.state_code.head()

state_gdp[1:3]

state_gdp_copy = state_gdp.copy()
state_code = state_gdp_copy.pop('state_code')
state_gdp_copy.index = state_code
state_gdp_copy.head()
state_gdp_copy.loc[['AL','CA']]

state_long_recession = state_gdp['gdp_growth_2010']<0
state_gdp[state_long_recession].head()

state_gdp.ix[state_long_recession,'state']
state_gdp.ix[state_long_recession,['state','gdp_growth_2009','gdp_growth_2010']]
state_gdp.ix[10:15,'state']

state_gdp_2012 = state_gdp[['state','gdp_2012']]
state_gdp_2012.head()
state_gdp_2012['gdp_growth_2012'] = state_gdp['gdp_growth_2012']
state_gdp_2012.head()

state_gdp_2012 = state_gdp[['state','gdp_2012']]
state_gdp_2012.insert(1,'gdp_growth_2012',state_gdp['gdp_growth_2012'])
state_gdp_2012.head()

state_gdp_2012 = state_gdp.ix[0:2,['state','gdp_2012']]
state_gdp_2012
gdp_2011 = state_gdp.ix[1:4,'gdp_2011']
state_gdp_2012['gdp_2011'] = gdp_2011

state_gdp_copy = state_gdp.copy()
state_gdp_copy.index = state_gdp['state_code']
state_gdp_copy = state_gdp_copy[['gdp_growth_2011','gdp_growth_2012']]
state_gdp_copy.head()
gdp_growth_2012 = state_gdp_copy.pop('gdp_growth_2012')
gdp_growth_2012.head()
state_gdp_copy.head()
del state_gdp_copy['gdp_growth_2011']
state_gdp_copy.head()
