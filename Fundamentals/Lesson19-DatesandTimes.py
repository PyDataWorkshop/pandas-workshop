
import datetime as dt
import sys
from pylab import *
from numpy import *
# End Imports
#################################################

yr, mo, dd = 2014, 12, 21
dt.date(yr, mo, dd)
hr, mm, ss, ms= 12, 21, 12, 21
dt.time(hr, mm, ss, ms)

dt.datetime(yr, mo, dd, hr, mm, ss, ms)

d1 = dt.datetime(yr, mo, dd, hr, mm, ss, ms)
d2 = dt.datetime(yr + 1, mo, dd, hr, mm, ss, ms)
d2-d1

#################################################
d2 + dt.timedelta(30,0,0)
dt.date(2014,12,21) + dt.timedelta(30,12,0)

d3 = dt.date(2014,12,21)
dt.datetime.combine(d3, dt.time(0))

#################################################
d3 = dt.datetime(2014,12,21,12,21,12,21)
d3.replace(month=11,day=10,hour=9,minute=8,second=7,microsecond=6)

datetime64('2011')
datetime64('2016-04')
datetime64('2016-04-01')
datetime64('2016-04-01T12:00') # Time
datetime64('2016-04-01T12:00:01') # Seconds
datetime64('2016-04-01T12:00:01.123456789') # Nanoseconds


#################################################
datetime64('2015-12-01T00','h')
datetime64('2015-12-01T00','s')
datetime64('2015-12-01T00','ms')
datetime64('2015-12-01','W')

#################################################
dates = array(['2016-04-01','2016-04-02'],dtype='datetime64')
dates
dates[0]

datetime64('2016-04-01T12:00:00-0600')
datetime64('2016-04-01T19:00:00Z')

#################################################
datetime64('2011')==datetime64('2015-12-01')
datetime64('2016-04')==datetime64('2016-04-01')

datetime64('2016-04-01')==datetime64('2016-04-01T00:00:00')
datetime64('2016-04-01')==datetime64('2016-04-01T00:00:00Z')
datetime64('2016-04-01T00:00:00') # Time is 00:00:00+0100
datetime64('2016-04-01T00:00:00Z') # Time is 01:00:00+0100

datetime64('2016-04-02') - datetime64('2016-04-01')
datetime64('2016-04-01') - datetime64('2016-04-01T00:00:00')

