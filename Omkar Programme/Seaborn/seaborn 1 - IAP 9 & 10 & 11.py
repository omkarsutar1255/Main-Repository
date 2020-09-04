# ============ SEABORN HEATMAP ============
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
arr_2d = np.linspace(1, 5, 12).reshape(4, 3)
# # linspace = it gives 12 equispaced values between 1 to 5
sns.heatmap(arr_2d)    # it show dark color for min value and faint color for max value
plt.show()

pda = pd.read_csv("friends_index_false.csv")  # pandas function to read csv file
pd1 = pda.set_index('country name')  # setting index for csv file

annot_kws = {'fontsize': 10, 'fontstyle': 'italic', 'color': 'k', 'alpha': 0.9,
             'rotation': 'vertical', 'verticalalignment': 'center', 'backgr;oundcolor': 'w'}
# annot ketwords = it takes values for annot size, style, color, alpha, rotation, etc.

cbar_kws = {'orientation': 'horizontal', 'shrink': 1, 'extend': 'min',
            'extendfrac': 0.1, 'ticks': np.arange(300, 501, 50), 'drawedges': True}
# heatmap bar keywords = orientation makes it vertical and horizontal
# shrink increase & decrease size of bar
# extend = it extend bar with knife edge on max, min or both side
# extend fraction = it extend bar up to fraction values
# ticks = it gives values for bar
# drawedges = if true then show edges between two colors on bar

ax = sns.heatmap(pd1, vmin=300, vmax=800, cmap='coolwarm', center=None, robust=False,
            annot=True, fmt="d", annot_kws=annot_kws,
            linewidths=4, linecolor="g",
            cbar=True, cbar_kws=cbar_kws, cbar_ax=None,
            square=False, xticklabels=np.arange(16, 21), yticklabels=['hindustan', 'america', 'england', 'aus'],
            mask=None, ax=None)
# heatmap takes 2D data and set with heatmap
# vmin and vmax = they are min and max values of heatmap side bar
# cmap = colormap are used as palette for heatmap
# annot = it takes boolean value or list of values to show values on heatmap
# fmt = format of numbers is needed to show numbers on heatmap
# linewidth and linecolor = it takes values for separate two boxes of heatmap with some width and color
# cbar = if false then don't show heatmap bar in chart
# xticklabel and yticklabel = if False then don't show labels on x, y axis and we can assign values to them in list form
ax.set(title="Heat Map",
       xlabel="year",
       ylabel='country')   # setting title, x and y label in seaborn
sns.set(font_scale=0.9)     # changing font size of annot
plt.show()

print(pd1)
az1 = sns.heatmap(pd1.corr(), annot=True, linewidths=3)
# # corr = this feature gives correlation between x and y axis in form of 1 to -1 number
# # if correlation is 1 (positive) = x increase then y increase
# # if correlation is 0 (neutral) = x increase no effect on y and vise versa
# # if correlation is -1 (negative) = x increase then y decrease
az1.tick_params(size=5, color="k", labelsize=10, labelcolor="k")
# # size = it use for size of label marking on graph, color = label marking color
# # labelsize = label size on graph and labelcolor = label color on graph
plt.show()

from sklearn.datasets import load_breast_cancer
cancer_data = load_breast_cancer()
# importing data from github and assigning it to others
cancer_df = pd.DataFrame(np.c_[cancer_data["data"], cancer_data['target']],
                         columns=np.append(cancer_data['feature_names'], ['target']))
# concating 2 columes and set them with target column and append feature_names values as columns and target as column

plt.figure(figsize=(25, 25))
az1 = sns.heatmap(cancer_df.corr(), annot=True, linewidths=3)
# first data is converted into data frame then find out correlation between every columns
# finally putting correlation into heat map for better understanding
az1.tick_params(size=5, color="k", labelsize=10, labelcolor="k")
plt.show()
