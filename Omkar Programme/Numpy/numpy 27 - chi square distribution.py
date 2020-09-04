# chi square distribution is used as a basis to verify hypothesis.
# it has two parameters
# df - (degree of freedom).
# size - shape of returned array.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

arr1 = random.chisquare(df=1000, size=10)
print(arr1)
sns.distplot(arr1, hist=False)
plt.show()
