# zipf distribution are used to sample data based in zipf's law.
# zipf's law - in a collection the nth common term is 1/n times of the most common term.
# E.g. 5th common word in english has occurs nearly 1/5th times as of the most used word.
# it has two parameters
# a = distribution parameter.
# size - shape of returned array.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

arr1 = random.zipf(a=2, size=1000)
print(arr1)
sns.distplot(arr1[arr1 < 25], kde=False)       # shows how many of 1000 values are below 25
plt.show()
