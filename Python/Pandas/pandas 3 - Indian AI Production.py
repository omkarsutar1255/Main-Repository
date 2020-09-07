# what is pandas?
# 1) Pandas is a powerful python data analysis toolkit.
# 2) Open source
# 3) A fast and efficient dataframe object for data manipulation.
# 4) Reading and writing data structures and different formates:
# csv, tsv, txt, XML, JSON, ZIP, etc.
# series: 1D array in pandas(only one column), dataframe: 2D array in pandas(multiple columns).
# numpy vs pandas: numpy array is used for implementation of pandas data objects

import pandas as pd
# print(pd.__version__)               # to check version of pandas module
# series1 = pd.Series([1, -2, "omkar", 2.5])         # basic pandas series creation
# series2 = pd.Series([1, -2], index=["a", "b"], dtype=float)     # set index and datatype while create series in pandas
# print(series2[0:2])                              # to retrieve particular data from dataframe use colon
# print(series1 + series2)                        # performing arithmetic operation on two pandas series

# df1 = pd.DataFrame([[1, 2, 3], [-2, "omkar", 2.5]])     # creating dataframe with only lists
# df2 = pd.DataFrame([{"a": 1, "b": 2}, {"a": 11, "b": 22, "c": 33}])# another way to create dataframes (NaN=miss value)

# print(df.columns)                           # to get all columns name from dataframe
# print(pd.read_csv("friends.csv", nrows=2))    # to retrieve certain rows from dataframe
# print(pd.read_csv("friends.csv", usecols=[1, 2]))    # to retrieve specific column from dataframe
# print(pd.read_csv("friends.csv", index_col=2))    # to set any column as index

# print(pd.read_csv("friends.csv", header=None, prefix="col"))  # to create header to dataframe as col0, col1, so on.

# print(pd.read_csv("friends.csv", dtype={"marks": "float64"}))      # change dtype of data in columns
# print(pd.read_csv("friends.csv", true_values=["yes"], false_values=["no"]))
# # give True value where "yes" value and False value where "no" values in dataset

# print(pd.read_csv("friends.csv", na_values={"1stcolumn": "not", "3rdcol": "null"}))
# # this is the way we can remove specific values from specific columns
# print(pd.read_csv("friends.csv", keep_default_na=False))  # keep null, none, na, etc. values as it is
# print(pd.read_csv("friends.csv", na_filter=False))
# # pandas check each values for converting in na_values so to stop this long process and boost the process
# # we can use na_filter as false if we don't have na values in dataset

# import numpy as np
df = pd.DataFrame({"omkar": [24, np.nan], "sutar": [np.NaN, 77]})
# print(df.isnull().sum())              # gives how many null values are present in each column
# print(df.isnull().sum().sum())        # gives total number of null values present in all dataframe
# # same with notnull().sum().sum()     # gives false where null values are present

# print(df.dropna(subset=["omkar"]))      # drop rows where null values present in omkar column
# df.dropna(inplace=True)                 # inplace=True make changes in original dataset

# df.loc([0, 3])                  # show 0th and 3rd row from table
# newdf = df.loc[3, 5]            # show values which at 3rd row in 5th column
# newdf2 = df.loc[0:2, 4:5]       # show values between row 0-2 and column 4-5
# n2 = df.loc[df["class"] < 11, ["percentage"]]     # show percentage where class number is less than 11

# df.join(newdf)                 # join second dataset on first dataset
# df.join(newdf, how="left")     # left is by default
# # left show all indexes from first dataframe and put nan values if index not in second dataframe
# # right show all indexes from second dataframe and put nan values if index not in first dataframe
# # inner show common indexes from both dataframe
# # outer show all indexes from both dataframe and put nan values if index not common in both dataframe
# df.join(newdf, lsuffix="_1")     # if both dataframe have same column names then it will put "_1" at end of left column
# df.join(newdf, rsuffix="_1")     # if both dataframe have same column names then it will put "_1" at end of right column

# df.append(newdf)          # append second dataframe to first dataframe
# df.append(newdf, ignore_index=True)   # this will create new index for second dataframe for continuous indexing

pd.melt(df)           # gives two column first with all column names and second with all values of tables
pd.melt(df, id_vars=["city"])    # id_vars set city as variable(first column) in melt table
pd.melt(df, id_vars=["city"], value_vars=["year"])
# this gives city as main column and gives values where values are year
