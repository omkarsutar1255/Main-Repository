# rayleigh distribution used in signal processing.
# it has two parameters.
# scale - (standard deviation) decides how flat the distribution will be (default 1.0).
# size - shape of returned array.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

arr1 = random.rayleigh(scale=2, size=10)
print(arr1)
sns.distplot(arr1, hist=False)
plt.show()
# at unit standard deviation of rayleigh and df=2 in chi square represents same distribution
