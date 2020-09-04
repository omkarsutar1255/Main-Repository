# it is generalization of binomial distribution
# it has three parameters
# n = number of possible outcomes (e.g. 6for dice roll).
# pvals = list of probabilities of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).
# size = the shape of the returned array.

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

arr1 = random.multinomial(n=6, pvals=[1/6, 2/6, 3/6])
# similar as binomial but here we can give more than 1 possibilities for every value
# if on one dice with 6 faces write A on 1 face, B on 2 faces, C on 3 faces
# then after throw a dice it shows how many times we got A, B and C inside list
print(arr1)

sns.distplot(arr1, hist=False)
plt.show()
