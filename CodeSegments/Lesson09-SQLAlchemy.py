##  Lesson 9
## Export data from a microdost sql database to cvs, excel, and txt.

#################################################

## --- Part1:
# Import libraries
import pandas as pd
import sys
from sqlalchemy import create_engine, MetaData, Table, select
## --- Part2:
print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)

#################################################

## Grab Data from SQL
## In this section we use the sqlalchemy library to grab data from a sql database. 
## Note that the parameter section will need to be modified.

## --- Part3:
# Parameters
ServerName = "RepSer2"
Database = "BizIntel"
TableName = "DimDate"

# Create the connection
engine = create_engine('mssql+pyodbc://' + ServerName + '/' + Database)
conn = engine.connect()

# Required for querying tables
metadata = MetaData(conn)

# Table to query
tbl = Table(TableName, metadata, autoload=True, schema="dbo")
#tbl.create(checkfirst=True)

# Select all
sql = tbl.select()

# run sql code
result = conn.execute(sql)

# Insert to a dataframe
df = pd.DataFrame(data=list(result), columns=result.keys())

# Close connection
conn.close()

print('Done')
##Done
## All the files below will be saved to the same folder the notebook resides in.

##### Export to CSV
## --- Part4:
df.to_csv('DimDate.csv', index=False)
print('Done')

#################################################

## Part B Export to EXCEL
## --- Part5:
df.to_excel('DimDate.xls', index=False)
print('Done')


#################################################

## Part C Export to TXT
## --- Part6:
df.to_csv('DimDate.txt', index=False)
print('Done')
