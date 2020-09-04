from numpy import random
arr1 = random.choice([3, 5, 7, 9], p=[0.1, 0.2, 0.3, 0.4], size=(3, 9))  # this is a data distribution list
print(arr1)                        # we can specify probability each number

# A random distribution is a set of random number that follows a certain probability density function.
# probability density function is describe probability of all values in an array.
# choice method allows us to specify "p=".
# The sum of all probability numbers should be 1.
