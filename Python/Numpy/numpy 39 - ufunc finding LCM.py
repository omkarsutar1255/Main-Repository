import numpy as np

r1 = 4
r2 = 7
r3 = np.lcm(r1, r2)                 # finding lowest common multiple of 4 and 7
print(r3)

arr = np.array([3, 6, 12])
x = np.lcm.reduce(arr)             # finding lcm for elements of array
print(x)

arr = np.arange(5, 16)             # getting elements from 5 to 15 for finding lcm
x = np.lcm.reduce(arr)
print(x)
