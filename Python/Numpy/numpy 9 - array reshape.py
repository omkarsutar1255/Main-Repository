# by reshaping we can add or remove dimensions or change number of elements in each dimensions
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

arr2 = arr.reshape(4, 3)              # outer dimension with 4 array and each with 3 elements
print(arr2)
# condition for reshape is old dimension elements should match with new dimension elements
# 1-D total elements == 2-D total elements i.e. multiplication of arrays of both dimension
# == 3-D total elements i.e. multiplication arrays of all three dimension

arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr4 = arr3.reshape(2, 3, 2)
print(arr4)
# in this 1-D to 3-D reshaping
# 1-D has "12 elements" == 3-D has 2*3*2= "12 elements"
print(arr3.reshape(3, 4).base)                              # gives original array so it is view.

arr5 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr6 = arr5.reshape(2, 3, -1)                               # we are allowed once for not to specify dimension(-1)
print(arr6)
# for converting from any dimension to 1-D we only can .reshape(-1)
