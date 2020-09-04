import numpy as np
# arr1 = np.ones((3, 2), dtype="int8")    # we can set dtype to ones and zeros
# print(arr1)
# print(arr1.dtype)
# arr1 = np.ones((3, 2), dtype="bool")    # we can create bool datatype ndarray
# print(arr1)
# arr1 = np.zeros((3, 2), dtype="str")    # we can create string type array
# print(bool(arr1.all()))                 # we can trace true false values from array
arr1 = np.arange(1, 13).reshape(3, 4)     # create particular shape array with certain range of values
# print(arr1)
# arr1 = np.arange(1, 10).reshape(3, 3)
# arr2 = np.arange(1, 10).reshape(3, 3)
# print(arr1.dot(arr2))                     # product of two 2Darray
print(arr1.max(axis=1))                        # give index where value in array is max in any axis
np.exp(arr1)                               # give exponent of arr1 values
print(arr1[:, :])                         # give all elements from array

x = "Omkar Sutar, "
y = "Siddhanerli, Kagal",
z = np.char.add(x, y)                      # adding two string into one string
print(z)
print(np.char.lower(x))                    # to lower numpy string`
print(np.char.upper(y))                    # to capatilize numpy string
print(np.char.center(y, 60))               # to make string in center with total length of string is 60
print(np.char.center(y, 60, fillchar="#"))               # filling empty space around center string
print(np.char.split(y))                            # splitting each word of string
print(np.char.splitlines("hello\nomkar\nsutar"))    # splitting each lines of strings
print(np.char.join([":", "/"], ["dmy", "dmy"]))        # adding character between each character of string
print(np.char.replace(y, "Siddhanerli", "taluka"))       # replacing word from string
print(np.char.equal(x, y))                               # checking two string are equal or not
print(np.char.count(y, "a"))                            # counting of "a" letter in y string
print(np.char.find(y, "a"))                             # finding letter "a" in string
