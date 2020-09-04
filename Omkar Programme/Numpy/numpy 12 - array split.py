import numpy as np

# ========== ARRAY_SPLIT ==========
arr1 = np.array([1, 2, 3, 4, 5, 6, 7])
arr2 = np.array_split(arr1, 3)
print(arr2)
print(arr2[0])                                   # to retrieve particular array from split

arr3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])
arr4 = np.array_split(arr3, 3)                   # here 3 is how many arrays we want
print(arr4)

arr5 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])
arr6 = np.array_split(arr5, 2, axis=1)
# axis is depth of splitting array.
# axis=0 means 1 dimension deep (if axis=0 use in 1-D array then its split each single element of array)
# axis=1 means 2 dimension deep (if axis=1 use in 2-D array then its split each single element of array)
# axis=2 means 3 dimension deep (if axis=2 use in 3-D array then its split each single element of array)
print(arr6)                                     

# ======== VSPLIT, HSPLIT, DSPLIT ============
arr7 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[21, 22, 23], [24, 25, 26]], [[27, 28, 29], [30, 31, 32]]])
aar8 = np.vsplit(arr7, 4)                       # vsplit consider 2-D array similar as axis=0
print(aar8)

arr9 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[21, 22, 23], [24, 25, 26]], [[27, 28, 29], [30, 31, 32]]])
aar10 = np.hsplit(arr9, 2)                       # hsplit consider 1-D array similar as axis=1
print(aar10)

arr11 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[21, 22, 23], [24, 25, 26]], [[27, 28, 29], [30, 31, 32]]])
aar12 = np.dsplit(arr11, 3)                       # dsplit consider on single element of array similar as axis=2
print(aar12)
