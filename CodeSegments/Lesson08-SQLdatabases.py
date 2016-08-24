
## Lesson 8
## How to pull data from a microsoft sql database

##############################################
# Import libraries
import pandas as pd
import sys
from sqlalchemy import create_engine, MetaData, Table, select
##############################################
print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)


##############################################
## Version 1

## In this section we use the sqlalchemy library to grab data from a sql database. Make sure to use your own ServerName, Database, TableName.

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
tbl.create(checkfirst=True)

# Select all
sql = tbl.select()

# run sql code
result = conn.execute(sql)
##############################################
# Insert to a dataframe
myDF = pd.DataFrame(data=list(result), columns=result.keys())

# Close connection
conn.close()

print('Done')
Done
Select the contents in the dataframe.


myDF.head()
##############################################

myDF.dtypes
##############################################

## Convert to specific data types. 
## The code below will have to be modified to match your table.

In [17]:
# Convert data types 
myDF.StandardDate = pd.to_datetime(myDF.StandardDate)
myDF.Year = myDF.Year.astype('int')

print('Data Types')


##############################################
## Version 2

import pandas.io.sql
import pyodbc

# Parameters
server = 'repser2'
db = 'BizIntel'

# Create the connection
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Trusted_Connection=yes')

# query db
sql = """

SELECT top 5 *
FROM DimDate

"""
myDF = pandas.io.sql.read_sql(sql, conn)
myDF.head()

##############################################
## Version 3

from sqlalchemy import create_engine

# Parameters
ServerName = "RepSer2"
Database = "BizIntel"

# Create the connection
engine = create_engine('mssql+pyodbc://' + ServerName + '/' + Database)

myDF = pd.read_sql_query("SELECT top 5 * FROM DimDate", engine)
myDF
