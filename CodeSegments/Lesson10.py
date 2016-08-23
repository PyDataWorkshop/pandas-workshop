
JUPYTER
FAQ
Lesson 10
From DataFrame to Excel
From Excel to DataFrame
From DataFrame to JSON
From JSON to DataFrame
In [1]:
import pandas as pd
import sys
In [2]:
print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
Python version 3.4.3 |Anaconda 2.4.0 (64-bit)| (default, Dec  1 2015, 11:39:45) [MSC v.1600 64 bit (AMD64)]
Pandas version 0.17.1
From DataFrame to Excel¶
In [3]:
# Create DataFrame
d = [1,2,3,4,5,6,7,8,9]
df = pd.DataFrame(d, columns = ['Number'])
df
Out[3]:
Number
0	1
1	2
2	3
3	4
4	5
5	6
6	7
7	8
8	9
In [4]:
# Export to Excel
df.to_excel('Lesson10.xlsx', sheet_name = 'testing', index = False)
print('Done')
Done
From Excel to DataFrame
In [5]:
# Path to excel file
# Your path will be different, please modify the path below.
location = r'C:\Users\david\notebooks\update\Lesson10.xlsx'

# Parse the excel file
df = pd.read_excel(location, 0)
df.head()
Out[5]:
Number
0	1
1	2
2	3
3	4
4	5
In [6]:
df.dtypes
Out[6]:
Number    int64
dtype: object
In [7]:
df.tail()
Out[7]:
Number
4	5
5	6
6	7
7	8
8	9
From DataFrame to JSON
In [8]:
df.to_json('Lesson10.json')
print('Done')
Done
From JSON to DataFrame
In [9]:
# Your path will be different, please modify the path below.
jsonloc = r'C:\Users\david\notebooks\update\Lesson10.json'

# read json file
df2 = pd.read_json(jsonloc)
In [10]:
df2
Out[10]:
Number
0	1
1	2
2	3
3	4
4	5
5	6
6	7
7	8
8	9
In [11]:
df2.dtypes
Out[11]:
Number    int64
dtype: object
