# todo: Outlier detection and removal using z-score and standard deviation in python pandas

# todo: import library
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
from scipy.stats import norm
import numpy as np

# get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (10, 6)

# todo: We are going to use heights dataset from kaggle.com.
#  Dataset has heights and weights both but I have removed weights to make it simple

# todo: load dataset
df = pd.read_csv("heights.csv")
df.sample(5)

# todo: plotting histogram for visualization of height data
plt.hist(df.height, bins=20, rwidth=0.8)
plt.xlabel('Height (inches)')
plt.ylabel('Count')
plt.show()

# todo: Plot bell curve along with histogram for our dataset using scipy.stats.norm
plt.hist(df.height, bins=20, rwidth=0.8, density=True)
plt.xlabel('Height (inches)')
plt.ylabel('Count')
rng = np.arange(df.height.min(), df.height.max(), 0.1)
plt.plot(rng, norm.pdf(rng, df.height.mean(), df.height.std()))

# todo: mean and std of normal distribution-
df.height.mean()
df.height.std()

# todo: Outlier detection and removal using 3 standard deviation
# One of the ways we can remove outliers is remove any data points that are beyond 3 standard deviation from mean.
# Which means we can come up with following upper and lower bounds

# todo: creating uppper  and lower limit for outlier using mean and std
upper_limit = df.height.mean() + 3 * df.height.std()
print(upper_limit)
lower_limit = df.height.mean() - 3 * df.height.std()
print(lower_limit)

# todo: Here are the outliers that are beyond 3 std dev from mean
print(df[(df.height > upper_limit) | (df.height < lower_limit)])

# Above the heights on higher end is **78 inch** which is around **6 ft 6 inch**. Now that is quite unusual height.
# There are people who have this height but it is very uncommon and it is ok if you remove those data points.
# Similarly on lower end it is **54 inch** which is around **4 ft 6 inch**.
# While this is also a legitimate height you don't find many people having this height
# so it is safe to consider both of these cases as outliers

# todo: Now remove these outliers and generate new dataframe
df_no_outlier_std_dev = df[(df.height < upper_limit) & (df.height > lower_limit)]
df_no_outlier_std_dev.head()
print(df_no_outlier_std_dev.shape)
print(df.shape)

# Above shows original dataframe data 10000 data points. Out of that we removed 7 outliers (i.e. 10000-9993)

# todo: (2) Outlier detection and removal using Z Score
# Z score is a way to achieve same thing that we did above in part (1)
# Z score indicates how many standard deviation away a data point is.
# For example in our case mean is 66.37 and standard deviation is 3.84.
# If a value of a data point is 77.91 then Z score for that is 3 because
# it is 3 standard deviation away (77.91 = 66.37 + 3 * 3.84)

# todo: Calculate the Z Score
# Z = (X - mean)/std
df['zscore'] = (df.height - df.height.mean()) / df.height.std()
df.head(5)
# Above for first record with height 73.84, z score is 1.94. This means 73.84 is 1.94 standard deviation away from mean.
# if Z is the above 3 or below -3 then that height is outlier.

# todo: Get data points that has z score higher than 3 or lower than -3.
# Another way of saying same thing is get data points that are more than 3 standard deviation away**
print(df[df['zscore'] > 3])
print(df[df['zscore'] < -3])

# todo: Here is the list of all outliers
print(df[(df.zscore < -3) | (df.zscore > 3)])

# todo: Remove the outliers and produce new dataframe
df_no_outliers = df[(df.zscore > -3) & (df.zscore < 3)]
df_no_outliers.head()
print(df_no_outliers.shape)
print(df.shape)
# Above shows original dataframe data 10000 data points. Out of that we removed 7 outliers (i.e. 10000-9993)

# (1) Remove outliers using percentile technique first. Use [0.001, 0.999] for lower and upper bound percentiles
# (2) After removing outliers in step 1, you get a new dataframe.
# (3) On step(2) dataframe, use 4 standard deviation to remove outliers
# (4) Plot histogram for new dataframe that is generated after step (3). Also plot bell curve on same histogram
# (5) On step(2) dataframe, use zscore of 4 to remove outliers.
# This is quite similar to step (3) and you will get exact same result
