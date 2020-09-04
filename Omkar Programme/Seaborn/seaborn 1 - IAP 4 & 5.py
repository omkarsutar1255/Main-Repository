# ============== SEABORN HISTOGRAM USING DISTPLOT =================
import seaborn as sns
from scipy.stats import norm
import matplotlib.pyplot as plt
tip_df = sns.load_dataset("tips")  # requires internet so it can download data from github
sns.distplot(tip_df["size"])
plt.show()
sns.distplot(tip_df["total_bill"], bins=100, hist=True, kde=True, rug=True,
             fit=norm, color="r", vertical=True, axlabel="Y AXIS",
             label="BILL")
plt.title("Bills of a Hotel")
plt.legend()
# bins will 100 bars in histogram
# hist False will remove histogram bars from chart
# kde is line plot of chart
# rug show where on x axis the values are occurs
# fit gives normalize line in chart
# we can give color to histogram through color feature
# vertical=True gives graph in horizontal way
# to give name to x axis in chart
# we can give label for information of chart using label function
plt.show()

# print(tip_df.total_bill.sort_values())   # to get values in ascending order
bins1 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51]
sns.distplot(tip_df["total_bill"], bins=bins1,
             hist_kws={"color": '#DC143C', "edgecolor": '#aaff00', 'linewidth': 3, 'linestyle': '--', "alpha": 0.9},
             kde_kws={"color": '#8e00ce', 'linewidth': 5, 'linestyle': '--', "alpha": 0.9},
             rug=True,
             rug_kws={"color": '#0426d0', "edgecolor": '#00dbff', 'linewidth': 1, 'linestyle': '--', "alpha": 0.9},
             fit=norm,
             fit_kws={"color": '#8e00ce', 'linewidth': 5, 'linestyle': '--', "alpha": 0.9},
             label="TB")
# bins are position of each bar (width of bars will change accordingly)
# hist_keywords are used to do various changes like color of bars, edgecolor of bars, width of edgecolor,
# edgeline style, alpha to dark or faint chart
# kde keywords do same on line in chart except edgecolor
# same with rug keywords as hist keywords bt set rug as True
# same with fit keywords as kde keywords bt set fit as normalizing line
# label is used to give inside bar information of graph
plt.xticks(bins1)        # xticks are names of each bar in histo chart
plt.xlabel("total bill")  # label for x axis
plt.legend()
plt.show()

# THREE HISTOGRAM IN ONE CHART
sns.distplot(tip_df["total_bill"], bins=9, label="total bill")
sns.distplot(tip_df["tip"], bins=9, label="tip")
sns.distplot(tip_df["size"], bins=9, label="size")
plt.legend()
plt.show()
