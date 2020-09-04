# joining means putting contents of two or more arrays in a single array
import numpy as np

# ========== CONCATENATE ==========
arr1 = np.array([[[11, 12], [13, 14]], [[21, 22], [23, 24]]])
arr2 = np.array([[[16, 17], [18, 19]], [[26, 27], [28, 29]]])    
arr3 = np.concatenate((arr1, arr2), axis=0)                      # axis is by default 0 if not givem
print(arr3.base)                                                 # concatenate is view
print(arr3)                                                      # axis is 0 so two arrays are considered as 1-D

arr4 = np.array([[[11, 12], [13, 14]], [[21, 22], [23, 24]]])
arr5 = np.array([[[16, 17], [18, 19]], [[26, 27], [28, 29]]])
arr6 = np.concatenate((arr4, arr5), axis=1)
print(arr6.base)                                                 # concatenate is view
print(arr6)                                              
# axis is 1 so two arrays are considered as 2-D so concatenate corresponding elements of both arrays

arr7 = np.array([[[11, 12], [13, 14]], [[21, 22], [23, 24]]])
arr8 = np.array([[[16, 17], [18, 19]], [[26, 27], [28, 29]]])
arr9 = np.concatenate((arr7, arr8), axis=2)
print(arr9.base)                                                 # concatenate is view
print(arr9)
# axis is 2 so two arrays are considered as 3-D so concatenate corresponding elements of both arrays

# joining arrays using stack functions using .stack, .hstack, .vstack, .dstack
# similar as concatenate just look of output is different
# here we can access each element of 1-D array by using concatenate axis +1 i.e. equal to array dimension

# ========= STACK =========
arr1 = np.array([[[11, 12], [13, 14]], [[21, 22], [23, 24]]])
arr2 = np.array([[[16, 17], [18, 19]], [[26, 27], [28, 29]]])
arr3 = np.stack((arr1, arr2), axis=3)                      # here axis is equal to array dimension i.e. 3
print(arr3.base)                                           # concatenate is view
print(arr3)                                                # making stack of each single element of array

# ========= VSTACK, HSTACK, DSTACK =========
arr1 = np.array([[[11, 12], [13, 14]], [[21, 22], [23, 24]]])
arr2 = np.array([[[16, 17], [18, 19]], [[26, 27], [28, 29]]])
#arr3 = np.vstack((arr1, arr2))                             # vstack = axis 0
#arr3 = np.hstack((arr1, arr2))                             # hstack = axis 1
arr3 = np.dstack((arr1, arr2))                             # dstack = axis 2
print(arr3.base)                                           # concatenate is view
print(arr3)                                                # output is similar as stack
