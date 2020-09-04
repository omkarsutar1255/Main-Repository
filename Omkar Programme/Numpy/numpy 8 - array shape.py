# shape of array is number of elements in each dimension
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]])
print(arr.shape)                               # gives elements of 1-D then 2-D and so on.

arr2 = np.array([1, 2, 3, 4], ndmin=7)
print(arr2)
print(arr2.shape)                              # gives only last dimension value 4 other are 1
# in above example at index-7 we have value 4, so we can say that 7th dimension has 4 elements
