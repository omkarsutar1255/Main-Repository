import numpy as np

# copy
arr = np.array([1, 2, 3, 4, 5])
arr2 = arr.copy()
arr[0] = 32                   # changes in original array
arr2[0] = 64                  # changes in copied array
print(arr)                    # changes in original array not affect copied array
print(arr2)                   # changes in copied array not affect original array
print(arr2.base)              # copy owns data so gives none

# view
arr3 = np.array([1, 2, 3, 4, 5])
arr4 = arr3.view()
arr3[0] = 32                   # changes in original array
print(arr3)                    # changes in original array will affect copied array
print(arr4)                    # changes in copied array will affect original array
print(arr4.base)               # view does not owns data so gives original array
