# addition is done between two arguments whereas summation happens over n elements
import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
arr3 = np.sum([arr1, arr2])               # add each term of both arrays
print(arr3)

# summation over an axis - if specify axis, numpy will sum numbers in specified array
arr4 = np.array([[1, 2], [3, 4]])
arr5 = np.array([[5, 6], [7, 8]])
arr6 = np.sum([arr4, arr5], axis=2)
print(arr6)

# cumulative sum - partially adding elements in array - use cumsum() function
arr7 = np.array([1, 2, 3, 4, 5, 6, 7])             # out like [1, 3, 6, 10, 15, 21, 28]
arr8 = np.cumsum(arr7)
print(arr8)
