import numpy as np


def adding(x, y):
    return x + y


adding = np.frompyfunc(adding, 2, 1)           # adding into numpy func library with 2 input and 1 output
print(adding([1, 2, 3, 4], [5, 6, 7, 8]))
print(type(np.add))                            # check type of function
print(type(np.concatenate))                    # check type of another function

if type(np.add) == np.ufunc:                   # to test function is a ufunc
    print("add is ufun")
else:
    print("add is not ufunc")
