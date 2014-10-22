http://pandas.pydata.org/pandas-docs/stable/cookbook.html

import pandas as pd

df = pd.DataFrame(
         {'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]}); 
df
  
df.ix[df.AAA >= 5,'BBB'] = -1; 

df

df.ix[df.AAA >= 5,['BBB','CCC']] = 555; 

df

df.ix[df.AAA < 5,['BBB','CCC']] = 2000; 

df

dflow = df[df.AAA <= 5]

df
