# Lesson 13
# - Linear Algebra Functions

#############################

# 1. det()
# 2. solve()
# 3. eig()

import numpy as np
from numpy.linalg import *

#--------------------------------------------#

### det()

# det() computes the determinant of a square matrix or array.


​
x = np.matrix([1,.5,.5,1])
​
print(x)
type(x)


#--------------------------------------------#

a = np.matrix('1 2; 3 4')
print(a)

b = np.matrix([[1, 2], [3, 4]])
print(b)

a * b #matrix Multiplication



np.array(a) * np.array(b) #element-wise multiplication 

# We are working backwards here

#--------------------------------------------#
## solve()

# solve() solves the system Ax=b when X is square and invertible so that the solution is exact. [Ax = b]


A = np.array([[1.0,2.0,3.0],[3.0,3.0,4.0],[1.0,1.0,4.0]])

b = np.array([[1.0],[2.0],[3.0]])

solve(A,b)


#--------------------------------------------#

## eig

# eig computes the eigenvalues and eigenvectors of a square matrix. 
# When used with one output, the eigenvalues and eigenvectors are returned as a tuple.
# eigvals can be used if only eigenvalues are needed.

x = np.matrix([[1,.5],[.5,1]])
val,vec = eig(x)
vec*np.diag(val)*vec.T
​
​
​
