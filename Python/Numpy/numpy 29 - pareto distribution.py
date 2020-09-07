# distribution following pareto's law
# i.e. 80-20 distribution (20% factors cause 80% outcome).
# it has two parameters
# a = shape parameter.
# size = shape of returned array.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

arr1 = random.pareto(a=2, size=1000)
print(arr1)                   # 20% out are similar and 80% out are similar
sns.distplot(arr1, kde=False)
plt.show()
