# Checking Your Environment

# preliminaries
​
import datetime
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

%matplotlib inline
import pandas as pd

# os- Miscellaneous operating system interfaces
import os

#####################

print("numpy version {}".format(np.__version__))
print("matplotlib version {}".format(mpl.__version__))
print("pandas version {}".format(pd.__version__))

#####################

os.getcwd()
​
# os.chdir(path)


#####################

print("Current Working Directory")
print(os.getcwd() + "\n")


#Change Directory
#Tip - Use double backslashes
# Reason : Escape Characters in Text Processing

# Remove the commenting below 
# os.chdir("C:\Users")

​

