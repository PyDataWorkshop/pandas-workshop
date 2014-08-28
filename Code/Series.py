import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('max_columns', 50)

# create a Series with an arbitrary list
s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'])
s

s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'],
index=['A', 'Z', 'C', 'Y', 'E'])
s

d = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100,
'Austin': 450, 'Boston': None}
cities = pd.Series(d)
cities

cities['Chicago']
cities[['Chicago', 'Portland', 'San Francisco']]

# Boolean Selection
cities[cities < 1000]

less_than_1000 = cities < 1000
print less_than_1000
print '\n'
print cities[less_than_1000]

# changing based on the index
print 'Old value:', cities['Chicago']
cities['Chicago'] = 1400
print 'New value:', cities['Chicago']

# changing values using boolean logic
print cities[cities < 1000]
print '\n'
cities[cities < 1000] = 750

print cities[cities < 1000]

print 'Seattle' in cities
print 'San Francisco' in cities

# divide city values by 3
cities / 3

# square city values
np.square(cities)

print cities[['Chicago', 'New York', 'Portland']]
print'\n'
print cities[['Austin', 'New York']]
print'\n'
print cities[['Chicago', 'New York', 'Portland']] + cities[['Austin', 'New York']]

# returns a boolean series indicating which values aren't NULL
cities.notnull()

# use boolean logic to grab the NULL cities
print cities.isnull()
print '\n'
print cities[cities.isnull()]
