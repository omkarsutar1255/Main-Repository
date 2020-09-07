# visualize distributions with seaborn
# seaborn is a library that uses matplotlib underneath to plot graphs.
# it will be used to visualize random distributions.
# Distplots takes array as input and plots curve corresponding to distribution of points in array.

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5])                   # to visualize random distribution
plt.show()
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)       # plotting a distplot without histogram
plt.show()
