# to find product of elements of array - use prod() function
import numpy as np
r1 = np.array([1, 2, 3, 4, 5])
r2 = np.array([6, 7, 8, 9, 10])
r3 = np.prod(r1)                           # gives product of each elements in array
r4 = np.prod([r1, r2])                     # gives product of each elements in both array
r5 = np.prod([r1, r2], axis=1)             # gives product of each elements of single array
r6 = np.cumprod([r1, r2])                  # gives cumulative product of each elements of array
print(r3)
print(r4)
print(r5)
print(r6)
