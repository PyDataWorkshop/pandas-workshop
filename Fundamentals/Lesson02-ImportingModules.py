## import can be used in a variety of ways. 
## The simplest is to use from module import * which imports all functions in module.
## This method of using import can dangerous since if you use it more than once, it is possible for functions to be hidden by later imports.
## A better method is to just import the required functions.
## This still places functions at the top level of the namespace, but can be used to avoid conflicts.


########################################################

# Will import log2 only
​
from pylab import log2 
​
# Will not import the log2 from SciPy
​
from scipy import log10

########################################################

import pylab as pl
import scipy as sp
import numpy as np

########################################################

It is also possible to rename modules when imported using as


import pylab as pl
import scipy as sp
import numpy as np
import pandas as pd

## The only difference between these two is that import scipy is implicitly calling import scipy as scipy.
## When this form of import is used, functions are used with the shortended as name.
## For example, the load provided by NumPy is accessed using sp.log2, while the pylab load is pl.log2 – and both can be used where appropriate.
## While this method is the most general, it does require slightly more typing.
