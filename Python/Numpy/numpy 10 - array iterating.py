# iterating using for loop
# iterating using for loop
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
for x in arr:
    print(x)                # after iterate shows 2-D array
    for y in x:
        print(y)            # after iterate shows 1-D array
        for z in y:
            print(z)        # after iterate shows elements

arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
for x in np.nditer(arr2):
    print(x)

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
for x in np.nditer(arr3, flags=["buffered"], op_dtypes=["S"]):
    print(x)
# buffered = extra space for change data types of elements
# op_types = change datatypes while iterating
# there are op_flags also for various operation

# iterating any elements from array using array slicing
arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in np.nditer(arr4[:1, :1, :2]):
    print(x)

arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in np.nditer(arr4, order="F"):
    print(x)
# if order is C then it retrieve row wise
# if order is F then it retrieve column wise

# enumerated iteration using ndenumerate()
arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x, y in np.ndenumerate(arr4):
    print(y, x)
# this gives position of element in dimensional array

for cell in arr4.flat:
    print(cell)
# this will flatten array and retrieve all elements from array
