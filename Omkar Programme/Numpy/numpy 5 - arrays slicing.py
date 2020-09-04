# slicing means taking elements from one given index to another given index.
# slice = [start:end:step]         its [0:len:1] by default

import numpy as np

# slicing 21D array
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[2:6])                         # returns 4 values that is 6-2.
print(arr[::])                          # uses by default values
print(arr[3:])
print(arr[:3])
print(arr[-3:-1])                       # negative slicing
print(arr[0:7:2])                       # steps of slicing

# slicing 2-D array
arr2 = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 23, 56, 77]])
print(arr2[0:2, 1:6])                                 # due to second list considered excluded, use [:2] for second list
#            ^ = this number is excluded and take 1 instead
