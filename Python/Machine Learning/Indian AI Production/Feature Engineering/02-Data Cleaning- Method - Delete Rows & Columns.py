# todo : Data Cleaning

# todo : Method - Delete Rows & Columns

# todo : Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# todo : load dataset
df = pd.read_csv(r"G:\DataSet\House Price Prediction\train.csv")

print(df.shape)

df.head(6)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df.head(6)

df.tail(6)

df.info()

df.isnull().sum()

plt.figure(figsize=(25, 25))
sns.heatmap(df.isnull())

null_var = df.isnull().sum() / df.shape[0] * 100
print(null_var)

drop_columns = null_var[null_var > 17].keys()
print(drop_columns)

df2_drop_clm = df.drop(columns=drop_columns)

print(df2_drop_clm.shape)

sns.heatmap(df2_drop_clm.isnull())

df3_drop_rows = df2_drop_clm.dropna()

print(df3_drop_rows.shape)

plt.figure(figsize=(25, 25))
sns.heatmap(df3_drop_rows.isnull())

df3_drop_rows.isnull().sum().sum()

print(df3_drop_rows.select_dtypes(include=['int64', 'float64']).columns)

sns.distplot(df['MSSubClass'])

sns.distplot(df3_drop_rows['MSSubClass'])

sns.distplot(df['MSSubClass'])
sns.distplot(df3_drop_rows['MSSubClass'])

num_var = ['MSSubClass', 'LotArea', 'OverallQual', 'OverallCond',
           'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2',
           'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF',
           'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath',
           'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces',
           'GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF',
           'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal',
           'MoSold', 'YrSold', 'SalePrice']

plt.figure(figsize=(25, 25))
for i, var in enumerate(num_var):
    plt.subplot(9, 4, i + 1)
    sns.distplot(df[var], bins=20)
    sns.distplot(df3_drop_rows[var], bins=20)

print(df3_drop_rows.select_dtypes(include=['object']).columns)

pd.concat([df['MSZoning'].value_counts() / df.shape[0] * 100,
           df3_drop_rows['MSZoning'].value_counts() / df3_drop_rows.shape[0] * 100], axis=1,
          keys=['MSZoning_org', 'MSZoning_clean'])


def cat_var_dist(var1):
    return pd.concat([df[var1].value_counts() / df.shape[0] * 100,
                      df3_drop_rows[var1].value_counts() / df3_drop_rows.shape[0] * 100], axis=1,
                     keys=[var1 + '_org', var1 + 'clean'])


cat_var_dist('MSZoning')

print("Thank You.....-:)")
