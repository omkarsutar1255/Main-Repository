# todo: Outlier Detection and Removal Using IQR

# todo: importing library
import pandas as pd

# todo: loading dataset
df = pd.read_csv("heights.csv")
print(df)
df.describe()

# todo: plotting histogram for dataset

# todo: Detect outliers using IQR
Q1 = df.height.quantile(0.25)
Q3 = df.height.quantile(0.75)
print(Q1, Q3)
IQR = Q3 - Q1
print(IQR)

# todo: creating upper and lower limit for outlier
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR
print(lower_limit, upper_limit)

# todo: Here are the outliers
print(df[(df.height < lower_limit) | (df.height > upper_limit)])

# todo: Remove outliers
df_no_outlier = df[(df.height > lower_limit) & (df.height < upper_limit)]
print(df_no_outlier)
