
Lesson 11
Grab data from multiple excel files and merge them into a single dataframe.

### ---- Part 1:
import pandas as pd
import matplotlib
import os
import sys
%matplotlib inline

### ---- Part 2:
print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)


Create 3 excel files
### ---- Part 3:
# Create DataFrame
d = {'Channel':[1], 'Number':[255]}
df = pd.DataFrame(d)
df

### ---- Part 4:
# Export to Excel

df.to_excel('test1.xlsx', sheet_name = 'test1', index = False)
df.to_excel('test2.xlsx', sheet_name = 'test2', index = False)
df.to_excel('test3.xlsx', sheet_name = 'test3', index = False)
print('Done')
Done

Place all three Excel files into a DataFrame
Get a list of file names but make sure there are no other excel files present in the folder.

### ---- Part 5:
# List to hold file names
FileNames = []

# Your path will be different, please modify the path below.
os.chdir(r"C:\Users\david\notebooks\pandas")

# Find any file that ends with ".xlsx"
for files in os.listdir("."):
    if files.endswith(".xlsx"):
        FileNames.append(files)
        
FileNames

Create a function to process all of the excel files.

### ---- Part 6:
def GetFile(fnombre):

    # Path to excel file
    # Your path will be different, please modify the path below.
    location = r'C:\Users\david\notebooks\update\\' + fnombre
    
    # Parse the excel file
    # 0 = first sheet
    df = pd.read_excel(location, 0)
    
    # Tag record to file name
    df['File'] = fnombre
    
    # Make the "File" column the index of the df
    return df.set_index(['File'])
Go through each file name, create a dataframe, and add it to a list.

i.e.
df_list = [df, df, df]

### ---- Part 7:
# Create a list of dataframes
df_list = [GetFile(fname) for fname in FileNames]
df_list

### ---- Part 8:
# Combine all of the dataframes into one
big_df = pd.concat(df_list)
big_df

### ---- Part 9:
big_df.dtypes

### ---- Part 10:
# Plot it!
big_df['Channel'].plot.bar();
