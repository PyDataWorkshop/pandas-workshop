

>>> from scipy.stats import ks_2samp
>>> import numpy as np
>>> 
>>> np.random.seed(12345678);
>>> x = np.random.normal(0,1,1000)
>>> y = np.random.normal(0,1,1000)
>>> z = np.random.normal(1.1,0.9, 1000)
>>> 
>>> ks_2samp(x, y)
(0.022999999999999909, 0.95189016804849658)
>>> ks_2samp(x, z)
(0.41800000000000004, 3.7081494119242173e-77)
