# binomial distribution describes outcome of binary scenarios,
# e.g. toss of a coin, it will either be head or tails.
# it has three parameters:
# n - number of trails
# p - probability of occurrence of each trial (e.g. for toss of a coin 0.5 each).
# size - Shape of returned array.

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

arr1 = random.binomial(n=3, p=0.5, size=10)        # n = how many times probability will use
print(arr1)                                        # p = probability of getting excepted value in returned array

sns.distplot(random.binomial(n=3, p=0.8, size=10), hist=True, kde=False)     # kde is use for line graph
plt.show()

omk = random.normal(loc=50, scale=5, size=10)
# mean = 50 with standard deviation = 5 i.e. 68% chances are there for getting number between 45 - 55
# and 95% chances are there for getting number between 40 to 60
# and 99.7% chances are there for getting number between 35 to 65
print(omk)
sns.distplot(omk, hist=False, label='normal')         # label for graph values

sut = random.binomial(n=100, p=0.5, size=10)
# Here n = 100 and probability = 0.5 i.e. 50% chance are there to get value around 100/0.5 = 50 number
print(sut)
sns.distplot(sut, hist=False, label='binomial')        # specify various label for each graph line

plt.show()
