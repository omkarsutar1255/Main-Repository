# numpy provides function to perform log at base 2, e and 10.
# how we can take log for any base by creating a custom ufunc.
# all of logs function will place -inf or inf in elements if log cannot not be computed.
# log at base 2 - use log2() function to perform log at base 2
import numpy as np
from math import log

arr1 = np.arange(1, 10)           # returns array with 1 to 9 numbers
arr2 = np.log2(arr1)              # returns array with 2^? for 1 to 9 numbers
print(arr2)

arr3 = np.arange(10, 21)
arr4 = np.log10(arr3)             # returns array with 10^? for 10 to 20 numbers
print(arr4)

# natural log or log at base e - use log() function to perform log at base e.
arr5 = np.arange(30, 61)
arr6 = np.log(arr5)                     # here base is "e" i.e. 2.71828183
print(arr6)

# numpy does not provide any function to take log at any base
# so we can use frompyfunc() function along with inbuilt function math.log() with two input parameters
nplog = np.frompyfunc(log, 2, 1)     # function to be done = log, 2 is total inputs, 1 is total output
omk = nplog(100, 15)                 # log 100 with base 15
print("log at any base")
print(omk)
