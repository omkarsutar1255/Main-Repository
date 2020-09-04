import numpy as np

# axis 0 = selecting elements in vertical direction
# axis 1 = selecting elements in horizontal direction

a = np.linspace(1, 5, 4)          # gives 4 values between 1 to 5 with equal distance
print(a)

b = np.empty(shape=(2, 4))        # gives empty 2 arrays with 4 elements in each with random numbers in it
print(b)

c = np.empty_like(a)             # copying shape of other array
print(c)

d = np.identity(3)                # create 3*3 shape array
print(d)

e = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(e.T)                    # transverse elements from row to column and column to row

f = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f.flatten())                            # gives iterator for iteration of array

g = np.array([1, 2, 3, 4, 6, 7, 35, 2, 2, 45, 34, 2, 43, 46])
print(g.argmin())                            # to find index of minimum values from array
print(g.argmax())                            # to find index of maximum values from array
print(g.argsort())                           # find indexes to sort the array

h = np.array([1, 2, 3, 4, 5])
i = np.array([1, 4, 9, 16, 25])
print(h + i)                       # also can other arithmetic operations like divide, subtract, addition
print(np.square(h))                # to square elements of array
print(np.sqrt(i))                  # for square root of elements in array
