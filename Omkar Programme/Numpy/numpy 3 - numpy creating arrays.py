import numpy as np

# Dimensions in arrays = one level of array depth (nested array)
# nested array are arrays in which array considered as element
# in array, values are within 0-D element

arr3 = np.array(42)                         # create array with value 42
print(arr3)                                 # its a 0-D dimensional array
print(arr3.ndim)                            # tells have many dimensions arrays have.

# 1-D Array
# array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
# above examples are example of 1-D array.
arr = np.array([1, 2, 3, 4, 5])             # arr object is ndarray and its create by array() function
print(arr)
print(arr.ndim)                             # its 1-D dimensional array
print(type(arr))

arr1 = np.array((1, 2, 3, 4))               # can pass list, tuple, any array-like object
print(arr1)
print(arr1.ndim)                            # its 1-D dimensional array

# 2-D array
# array that has 1-D arrays as its elements is called 2-D array,
# numpy.mat module dedicated towards matrix operations
arr4 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr4)
print(arr4.ndim)                            # its 2-D dimensional array

# 3-D arrays
# an array that has 2-D arrays(matrices) as its elements is called 3-D array.
arr5 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr5)
print(arr5.ndim)                            # its 3-D dimensional array

# higher dimensional arrays
# when array is created, you can define the number of dimensions by using the ndmin argument
arr6 = np.array([1, 2, 3, 4], ndmin=5)
print(arr6)
print("number of dimensions : ", arr6.ndim)
