## pandas - two way tables
## Diamonds 


import os
import numpy as np
​
os.getcwd()

## Task

#- How many cases are there in Diamond Data Set?
#- Create a Two Way Frequency Table for Cut and Color
#- Data Set at PyDataWorkshop.github.io


import pandas as pd
​
diamonds = pd.read_csv("diamonds.csv")

#################################

diamonds.tail(5)


diamonds.shape

diamonds.describe()



byCutColor = diamonds.groupby(["cut","color"])

byCutColor["carat"].count().unstack()

# byCutColor["carat"].count().unstack()

