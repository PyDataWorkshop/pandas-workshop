
import numpy as np

# Exercises
# - Write a function that accepts one number as an input and returns the square root.
# - Write a function that accepts one number “x” and a value “n” and returns the “n-“th root of “x”
# - Write a function that simulates the roll of a fair die.
# - Write a function that returns 100 simulations of 100 fair dice rolls.


def disk_area(radius):
    return 3.14 * radius * radius


def disk_area2(radius):
    area = 3.14 * radius * radius
    if area >10: 
        print("area greater than 10")
    return area


disk_area2(5)


X=np.array([1,45,6,13])
​
​
def makesum(X):
    return np.sum(X)

makesum(X)


​
