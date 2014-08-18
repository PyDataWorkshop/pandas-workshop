
# http://blog.kaggle.com/2013/01/17/getting-started-with-pandas-predicting-sat-scores-for-new-york-city-schools/

###############################################

import pandas as pd

# Load the data

dsProgReports = pd.read_csv('C:/data/NYC_Schools/School_Progress_Reports_-_All_Schools_-_2009-10.csv')
dsDistrict = pd.read_csv('C:/data/NYC_Schools/School_District_Breakdowns.csv')
dsClassSize = pd.read_csv('C:/data/NYC_Schools/2009-10_Class_Size_-_School-level_Detail.csv')
dsAttendEnroll = pd.read_csv('C:/data/NYC_Schools/School_Attendance_and_Enrollment_Statistics_by_District__2010-11_.csv')[:-2] #last two rows are bad
dsSATs = pd.read_csv('C:/data/NYC_Schools/SAT__College_Board__2010_School_Level_Results.csv') # Dependent

###############################################

dsProgReports.info()
dsSATs.info()

###############################################

dsSATS join dsClassSize on dsSATs['DBN'] = dsClassSize['SCHOOL CODE']
join dsProgReports on dsSATs['DBN'] = dsProgReports['DBN']
join dsDistrct on dsProgReports['DISTRICT'] = dsDistrict['JURISDICTION NAME']
join dsAttendEnroll on dsProgReports['DISTRICT'] = dsAttendEnroll['District']

###############################################

pd.DataFrame(data=[dsProgReports['DBN'].take(range(5)), dsSATs['DBN'].take(range(5)), dsClassSize['SCHOOL CODE'].take(range(5))])

#Strip the first two characters off the DBNs so we can join to School Code
dsProgReports.DBN = dsProgReports.DBN.map(lambda x: x[2:])
dsSATs.DBN = dsSATs.DBN.map(lambda x: x[2:])

#We can now see the keys match
pd.DataFrame(data=[dsProgReports['DBN'].take(range(5)), dsSATs['DBN'].take(range(5)), dsClassSize['SCHOOL CODE'].take(range(5))])
