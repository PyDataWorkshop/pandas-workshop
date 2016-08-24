x = reshape(arange(4.0),(2,2))
x
s1 = x[0,:] # First row
s2 = x[:,0] # First column
s1[0] = -3.14 # Assign first element
s1
s2
x

x = reshape(arange(4.0),(2,2))
s1 = copy(x[0,:]) # Function copy
s2 = x[:,0].copy() # Method copy
s3 = array(x[0,:]) # Create a new array
s1[0] = -3.14
s1
s2
s3
x[0,0]

x = arange(5.0)
y = x[0] # Pure scalar selection
z = x[:1] # A pure slice
y = -3.14
y # y Changes
x # No propagation
z  # No changes to z either
z[0] = -2.79
y # No propagation since y used pure scalar selection
x # z is a view of x, so changes propagate

x = array([[0.0, 1.0],[2.0,3.0]])
y = x
print(id(x),id(y)) # Same
y = x + 1.0
y
print(id(x),id(y)) # Different
x # Unchanged
y = exp(x)
print(id(x),id(y)) # Also Different




array(object, dtype=None, copy=True, order=None, subok=False, ndmin=0)

array([[1.0,2.0],[3.0,4.0]])
array([[1.0,2.0],[3.0,4.0]], 'int32')

array(object=[[1.0,2.0],[3.0,4.0]])
array([[1.0,2.0],[3.0,4.0]], dtype=None, copy=True, order=None, subok=False, ndmin=0)

array(dtype='complex64', object = [[1.0,2.0],[3.0,4.0]], copy=True)

x = array([[1.0,2.0],[3.0,4.0]])
s = shape(x)
s

x = array([[1.0,2.0],[3.0,4.0]])
M,N = shape(x)
M
N

## try:
##    M,N,P = shape(x) # Error

x = randn(10,10,10)
shape(x)
