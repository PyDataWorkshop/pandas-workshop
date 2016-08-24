

## Lesson 10
## A. From DataFrame to Excel
## B. From Excel to DataFrame
## C. From DataFrame to JSON
## D. From JSON to DataFrame

#--------------------------------------------------------#
import pandas as pd
import sys

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)

#--------------------------------------------------------#
## A. From DataFrame to Excel

# Create DataFrame
d = [1,2,3,4,5,6,7,8,9]
df = pd.DataFrame(d, columns = ['Number'])
df

#--------------------------------------------------------#
# Export to Excel
df.to_excel('Lesson10.xlsx', sheet_name = 'testing', index = False)
print('Done')
Done

#--------------------------------------------------------#
## B. From Excel to DataFrame

# Path to excel file
# Your path will be different, please modify the path below.
location = r'C:\WorkArea\Lesson10.xlsx'

# Parse the excel file
df = pd.read_excel(location, 0)

df.head()
df.tail()

#--------------------------------------------------------#
## C. From DataFrame to JSON
In [8]:
df.to_json('Lesson10.json')
print('Done')
Done


#--------------------------------------------------------#
## D. From JSON to DataFrame

# Your path will be different, please modify the path below.
jsonloc = r'C:\Users\david\notebooks\update\Lesson10.json'

# read json file
df2 = pd.read_json(jsonloc)

df2

#--------------------------------------------------------#

df2.dtypes

