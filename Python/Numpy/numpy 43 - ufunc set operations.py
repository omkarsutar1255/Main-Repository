# set in mathematics is a collection of unique elements.
# set arrays should only be 1-d arrays.
import numpy as np
x1 = np.array([1, 1, 1, 3, 4, 4, 6, 6, 8, 4, 3, 5, 7, 3, 2, 5, 6])
x2 = np.unique(x1)                     # finding unique elements from set of array
print(x2)

x3 = np.array([1, 1, 1, 3, 4, 4, 6, 6])
x4 = np.array([8, 4, 3, 5, 7, 3, 2, 5, 6])
x5 = np.union1d(x3, x4)                    # finding unique elements from both arrays
print(x5)

x6 = np.array([1, 1, 1, 3, 4, 4, 6, 6])
x7 = np.array([8, 4, 3, 5, 7, 3, 2, 5, 6])
x8 = np.intersect1d(x6, x7, assume_unique=True)         # assume_unique speed up computation
print(x8)                                               # finding similar values from both arrays

y1 = np.array([1, 1, 1, 3, 4, 4, 6, 6])
y2 = np.array([8, 4, 3, 5, 7, 3, 2, 5, 6])
y3 = np.setdiff1d(y1, y2, assume_unique=True)       # finding only values of first set that is not present in second set
print(y3)

y4 = np.array([1, 1, 1, 3, 4, 4, 6, 6])
y5 = np.array([8, 4, 3, 5, 7, 3, 2, 5, 6])
y6 = np.setxor1d(y4, y5, assume_unique=True)        # finding values that present in both sets
print(y6)
