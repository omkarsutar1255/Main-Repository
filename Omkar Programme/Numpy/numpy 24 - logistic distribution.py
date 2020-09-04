# logistic distribution is used to describe growth.
# used extensively in machine learning in logistic regression, neural networks etc.
# it has three parameters:
# loc = mean, where peak is. Default = 0.
# scale = standard deviation, flatness of distribution. Default 1.
# size = Shape of returned array.

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

arr1 = random.logistic(loc=10, scale=2, size=10)
print(arr1)
arr2 = random.normal(loc=10, scale=2, size=10)
print(arr2)
sns.distplot(arr1, hist=False, label='logistic')
sns.distplot(arr2, hist=False, label='normal')
plt.show()

# both are near identical, but logistic has more area under tails.
# i.e. possibility of more occurrence of number that are futher away from mean
