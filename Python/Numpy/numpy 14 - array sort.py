import numpy as np

arr1 = np.array([1, 7, 34, 83, 8, 872, 567, 6])
arr2 = np.sort(arr1)                             # sort element of 1-D array in ascending order
print(arr2)
print(arr2.base)

arr3 = np.array([[89, 5, 34], [83, 8, 872], [567, 6]])
arr4 = np.sort(arr3)                             # sort element of 1-D array in ascending order in 2-D array
print(arr4)

arr5 = np.array(["cherry", "banana", "apple"])
arr6 = np.sort(arr5)                             # sort element of 1-D array in alphabetical order
print(arr6)

arr3 = np.array([True, False, True, False])
arr4 = np.sort(arr3)                             # sort boolean array in false true order
print(arr4)
