import numpy as np
# we can perform arithmetic operators on numpy array but we have built in function for that

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3, 4, 5])
# add() function sum elements of two array
new = np.add(x, y)
new2 = np.sum(x, y)
print(new)
print(new.base)                         # its view base

# subtract() function subtracts values from one array with values from another array
# multiply() function multiplies values from one array with values from another array
# divide() function divides values from one array with values from another array
# power() function rises values from first array to power of values of second array
# mod() and remainder() function returns remainder of values in first array corresponding to values in second array
# divmod() function returns both quotient and mod
# absolute() function returns positive number
# mean() function returns mean of all elements of array
