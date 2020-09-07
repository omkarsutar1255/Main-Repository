# poisson distribution is discrete trial with continuous trial
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

omk1 = random.normal(loc=10, scale=3, size=10)
print(omk1)
sns.distplot(omk1, hist=False, label='normal')
# plt.show()

omk2 = random.binomial(n=40, p=0.3, size=10)
print(omk2)
sns.distplot(omk2, hist=False, label='binomial')
# plt.show()

omk3 = random.poisson(lam=10, size=10)              # lam = n * p = what is more occurred number
print(omk3)                                         # lam is the value around which other values will show
sns.distplot(omk3, hist=False, label='poission')
plt.show()
