# in real world we use real data and just for now we generate random data for use

# random module of numpy
from numpy import random
arr1 = random.randint(100, size=5)           # generate 1 array having 5 random number in it
print(arr1)

arr2 = random.randint(34543, size=(3, 7))    # generate 4 arrays having 7 random number in each
print(arr2)

arr3 = random.rand(2, 5)                     # generate 2 arrays having 5 random float(0-1) in each
print(arr3)

arr3 = random.randn(2, 5)                     # generate 2 arrays having 5 random negative or positive values in float
print(arr3)

arr4 = random.choice([3, 5, 7, 9])           # generate 1 array of 1 value in it from provided array
print(arr4)

arr5 = random.choice([3, 2, 78, 35], size=(3, 8))   # generate 3 arrays of 8 values in each from provided array
print(arr5)                                         # duplicate values are allowed

arr6 = random.random(3)                             # create 3 random values with 0-1
print(arr6)
