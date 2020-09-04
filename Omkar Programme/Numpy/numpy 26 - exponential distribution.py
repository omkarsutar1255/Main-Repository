# Exponential distribution is used for describing time till next event e.g. failure or success etc.
# it has two parameters
# scale - inverse of rate (see lam in poisson distribution) defaults to 1.0.
# size - the shape of the returned array.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

arr1 = random.exponential(scale=3, size=10)         # show time can take between 2 events when mean time is 3.
print(arr1)

sns.distplot(arr1, hist=False)
plt.show()
# poisson deals with number of occurrence of event in a time period
# whereas exponential distribution deals with time between these events
