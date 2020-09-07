# there are primarily five ways of rounding off decimals in numpy.
# truncation , fix , rounding , floor , ceil .
# truncation removes decimals - use trunc() and fix() functions.
import numpy as np
arr = np.trunc([-3.47874, 8.278349])
print(arr)

arr = np.fix([-3.47874, 8.278349])
print(arr)

# rounding - around() function increments preceding digit or decimal by 1 if >=5 else do nothing
arr = np.around([-3.454545, 8.54545])
print(arr)

# floor() function rounds off decimal to nearest lower integer.
arr = np.floor([-3.454545, 8.54545])          # first value is between -3 and -4 so lowest is -4
print(arr)                                    # second value is between 8 and 9 so lowest is 8

# ceil() function rounds off decimal to nearest upper integer
arr = np.around([-3.454545, 8.54545])          # first value is between -3 and -4 so highest is -3
print(arr)                                    # second value is between 8 and 9 so highest is 9
