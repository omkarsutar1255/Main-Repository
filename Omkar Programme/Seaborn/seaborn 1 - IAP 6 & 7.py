# ================ SEABORN BARPLOT ====================
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
tips_df = sns.load_dataset("tips")
sns.barplot(x='day', y='total_bill', hue='sex', data=tips_df, order=['Sat', 'Sun', 'Thur', 'Fri'],
            hue_order=['Male', 'Female'], estimator=np.max, ci=90, n_boot=1000, orient='v', color="g", palette="hot",
            saturation=.6, errcolor=".4", errwidth=5, capsize=0.3, dodge=False)
# x and y takes values for x and y axis and hue takes values for plotting bar on both axises
# order takes list for x axis and hue order takes list for ordering values on each points of x axis
# estimator enables to view data in various type like mean, max, min, sum
# ci = confidence interface and n_boot = number of bootstrap in ci
# we can change orientation from vertical to horizontal if we have numerical values on x axis not string values
# color = we can give various colors to bars
# palette = we can give palette type of colors to bars
# saturation = we can give saturation of colors of bars
# errcolor = we can give saturation of color for err lines of bars
# errwidth = it takes width value for err line of bars
# capsize = adding cap with specific size to err line
# dodge = it is used to show single bar by overlapping multiple bar at each x axis point
plt.show()

sns.set()
kwargs = {'alpha': 0.9, 'linestyle': ':', 'linewidth': 5, 'edgecolor': 'k'}
ax = sns.barplot(x='day', y='total_bill', data=tips_df, **kwargs)
# we can give kwargs parameter to set values in seaborn
ax.set(title='barplot of tips',
       xlabel='days',
       ylabel='total bill')
# .set = this way also we can set values to graphs
plt.show()
