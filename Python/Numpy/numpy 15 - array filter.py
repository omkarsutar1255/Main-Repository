# getting some elements out of an existing arrays and creating a new array out of them is called filtering.
# in numpy, you filter an array using a boolean index list.
# a boolean index list is a list of booleans corresponding to indexes in the array.
# if value at index is true, that element is contained in filtered array
# if value at index is false, that element is filtered excluded filtered array
import numpy as np
arr1 = np.array([41, 42, 53, 64])
arr2 = arr1[[True, False, True, False]]           # at index 0 and 2 filter array have value true
print(arr2)

arr3 = np.array([2, 3, 6, 8, 465, 2, 56, 568, 34, 8, 546, 2, 24, 9, 54, 85])
arr4 = []
for x in arr3:
    if x % 2 == 0:
        arr4.append(True)
    else:
        arr4.append(False)
print(arr3[arr4])

arr5 = np.array([2, 3, 6, 8, 465, 2, 56, 568, 34, 8, 546, 2, 24, 9, 54, 85])
arr6 = arr5 % 2 == 0
print(arr5[arr6])
