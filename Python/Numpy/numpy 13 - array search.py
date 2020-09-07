import numpy as np

arr1 = np.array([1, 2, 5, 4, 5, 6])
arr2 = np.where(arr1 == 5)              # shows the index where is 5
arr3 = np.where(arr1 % 2 == 0)          # we can give condition where clause
print(arr2)

arr4 = np.array([1, 2, 3, 4, 5, 6])
arr5 = np.searchsorted(arr4, 4)                   # shows index where 4 is should be in "sorted array"
arr6 = np.searchsorted(arr4, 4, side="right")     # shows most right index where 4 should be inserted
print(arr5)
print(arr6)

arr7 = np.array([1, 2, 3, 4, 5, 6])
arr8 = np.searchsorted(arr7, [1, 3, 5], side="right")
print(arr8)                                        # we can search multiple values in sorted array
