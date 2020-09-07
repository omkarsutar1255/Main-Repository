import numpy as np

# access from 1-D array
arr = np.array([1, 2, 3, 4])
print(arr[0])                         # access an array element by referring to its index number.
print(arr[1] + arr[3])                # adding third and fourth element

# access from 2-D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2[0, 1])                     # use comma to access elements from 2-D array
print(arr2[0, -1])                    # negative indexing

# access from 3-D array
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[45, 57, 37], [34, 25, 62]]])
print(arr3[0, 1, 2])                     # use comma to access elements from 3-D array
print(arr3[0, -1, -2])                   # negative indexing
