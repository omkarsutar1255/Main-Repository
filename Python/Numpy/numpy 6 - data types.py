# Data Types in NumPy

"""
i = integer
b = boolen
u = unsigned
f = float
c = complex float
m = timedelta
M = datetime
O = object
S = string
U = unicode
V = fixed chunk of memory for other type (void)
"""

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)                                # getting data types of an array

arr2 = np.array(["apple", "banana", "cherry"])
print(arr2.dtype)                               # getting data types of an array

arr3 = np.array([1, 2, 3, 4, 5], dtype="S4")    # S = String and bytes size = 4
print(arr3)
print(arr3.dtype)

# if the array is already created then make copy of it and than convert into other datatype
arr4 = arr3.astype("i")                               # convert arr3 string data type to int
print(arr4)
print(arr4.dtype)

arr5 = np.array([0.5, 54.5, 64.23])
print(arr5.dtype)
arr6 = arr5.astype("int")                      # float data type converting to int
print(arr6)
print(arr6.dtype)
arr7 = arr6.astype("bool")                     # again int to boolen
print(arr7)                                    # gives false if value is zero
print(arr7.dtype)
