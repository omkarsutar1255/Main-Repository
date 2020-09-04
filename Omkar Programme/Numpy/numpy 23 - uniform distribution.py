# used to describe probability where every event has equal chances of occurring.
# it has three parameters
# a = lower bound - default value = 0.0
# a = upper bound - default value = 1.0
# size = the shape of returned array.

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

arr1 = random.uniform(2, 4, size=10)         # returned values are between 2 & 4
print(arr1)
sns.distplot(arr1, hist=False)
plt.show()
