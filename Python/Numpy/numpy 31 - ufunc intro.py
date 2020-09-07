# ufunc = universal function (numpy function that operates on ndarray object).
# ufubc are used to implement vectorization in numpy which is way faster than iterating over elements.
# They also provide broadcasting and additional methods
# like reduce, accumulate etc. that are very helpful for computation.
# ufunc also take additional arguments, like:
# "where" boolean array or condition defining where operations should take place.
# "dtype" defining the return type of elements.
# "out" output array where the returned value should be copied.
# converting iterative statements into a vector based operation is called vectorization.

# without ufunc, we can use python's built-in zip() method:
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
z = []
for i, j in zip(x, y):
    z.append(i + j)
print(z)

# numpy has ufunc for this, called add(x, y) that will produce same result.
import numpy as np
x = [11, 12, 13, 14]
y = [21, 22, 23, 24]
z = np.add(x, y)                  # vectorization
print(z)
