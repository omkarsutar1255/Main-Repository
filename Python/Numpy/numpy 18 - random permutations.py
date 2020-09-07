from numpy import random
import numpy as np
arr1 = np.array([12, 23, 34, 45, 56, 67, 78, 89])
random.shuffle(arr1)                            # shuffle method rearranged original array
print(arr1)

arr2 = np.array([12, 23, 34, 45, 56, 67, 78, 89])
arr3 = random.permutation(arr2)                 # permutation create new array having shuffling values of original array
print(arr2)
print(arr3)
