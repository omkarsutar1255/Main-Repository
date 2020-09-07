# normal distribution fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.
# it has three parameters
# loc - (mean) where peak of bell exists.
# scale - (standard deviation) how flat graph distribution should be.
# size - shape of returned array.

from numpy import random
import matplotlib.pyplot as plt                    # to show the graph
import seaborn as sns

arr1 = random.normal(size=(2, 3))                # gives 2 arrays with 3 values in each
print(arr1)

arr2 = random.normal(loc=5, scale=2, size=(1, 4))   # with mean 2 and standard deviation 2
print(arr2)                                         # 68% of returned values are between (loc - scale) 5-2=3 and
# (loc+scale) 5+2=7 that means between 3 to 7

sns.distplot(random.normal(size=3), hist=False)    # 3 values in a array and kde is true
plt.show()

omkar = random.normal(loc=2, scale=2, size=(2, 20))
print(omkar)
sns.distplot(omkar, hist=False)               # graph create with given values
plt.show()                                    # shows graph on screen
