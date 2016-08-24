

import os
import pandas as pd
from pandas import read_csv
from urllib import urlopen



page = urlopen("http://econpy.pythonanywhere.com/ex/NFL_1979.csv")
df = read_csv(page)
print(df)
​


print(df['Visitor'])

