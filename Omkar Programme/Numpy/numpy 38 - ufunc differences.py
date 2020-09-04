# find differences between 2 elements of array
# e.g. for [1, 3, 5, 7, 9] here the diff between two number is 2 so output is [2, 2, 2, 2]
# to find discrete function use diff() function and use "n" to performs this operation repeatedly

import numpy as np
r1 = np.array([1, 2, 6, 15, 36])
r2 = np.diff(r1)
r3 = np.diff(r1, n=2)
print(r2)
print(r3)
