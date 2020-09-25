# todo : Data Cleaning

# todo : Numerical Missing Value Imputation By Class

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
datset_path = r"https://drive.google.com/uc?export=download&id=1BiGZSedP4BIIuTbVTBodOhVgFImaz08c"
df = pd.read_csv(datset_path)

print(df.shape)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df.head()

missing_value_clm_gre_20 = ['Alley', 'FireplaceQu', 'PoolQC', 'Fence', 'MiscFeature']
df2_drop_clm = df.drop(columns=missing_value_clm_gre_20)
print(df2_drop_clm.shape)

df3_num = df2_drop_clm.select_dtypes(include=['int64', 'float64'])
print(df3_num.shape)

df3_num.isnull().sum()

num_var_miss = ['LotFrontage', 'MasVnrArea', 'GarageYrBlt']
print(df3_num[num_var_miss][df3_num[num_var_miss].isnull().any(axis=1)])

df['LotConfig'].unique()

df[df.loc[:, 'LotConfig'] == "Inside"]["LotFrontage"].replace(np.nan, df[df.loc[:, 'LotConfig'] == "Inside"][
    "LotFrontage"].mean())

df_copy = df.copy()
for var_class in df['LotConfig'].unique():
    df_copy.update(df[df.loc[:, 'LotConfig'] == var_class]["LotFrontage"].replace(np.nan, df[
        df.loc[:, 'LotConfig'] == var_class]["LotFrontage"].mean()))

df_copy.isnull().sum()

df_copy = df.copy()
num_vars_miss = ['LotFrontage', 'MasVnrArea', 'GarageYrBlt']
cat_vars = ['LotConfig', 'MasVnrType', 'GarageType']
for cat_var, num_var_miss in zip(cat_vars, num_vars_miss):
    for var_class in df[cat_var].unique():
        df_copy.update(df[df.loc[:, cat_var] == var_class][num_var_miss].replace(np.nan,
                                                                                 df[df.loc[:, cat_var] == var_class][
                                                                                     num_var_miss].mean()))

df_copy[num_vars_miss].isnull().sum()

print(df_copy[df_copy[['MasVnrType']].isnull().any(axis=1)])

print(df_copy[df_copy[['GarageType']].isnull().any(axis=1)])

df_copy = df.copy()
num_vars_miss = ['LotFrontage', 'MasVnrArea', 'GarageYrBlt']
cat_vars = ['LotConfig', 'Exterior2nd', 'KitchenQual']
for cat_var, num_var_miss in zip(cat_vars, num_vars_miss):
    for var_class in df[cat_var].unique():
        df_copy.update(df[df.loc[:, cat_var] == var_class][num_var_miss].replace(np.nan,
                                                                                 df[df.loc[:, cat_var] == var_class][
                                                                                     num_var_miss].mean()))

df_copy[num_vars_miss].isnull().sum()

# todo : Data Distribution

plt.figure(figsize=(10, 10))
sns.set()
for i, var in enumerate(num_vars_miss):
    plt.subplot(2, 2, i + 1)
    sns.distplot(df[var], bins=20, kde_kws={'linewidth': 8, 'color': 'red'}, label="Original", )
    sns.distplot(df_copy[var], bins=20, kde_kws={'linewidth': 5, 'color': 'green'}, label="Mean", )
    plt.legend()

# todo : Median

df_copy_median = df.copy()
num_vars_miss = ['LotFrontage', 'MasVnrArea', 'GarageYrBlt']
cat_vars = ['LotConfig', 'Exterior2nd', 'KitchenQual']
for cat_var, num_var_miss in zip(cat_vars, num_vars_miss):
    for var_class in df[cat_var].unique():
        df_copy_median.update(df[df.loc[:, cat_var] == var_class][num_var_miss].replace(np.nan, df[
            df.loc[:, cat_var] == var_class][num_var_miss].median()))

df_copy_median[num_vars_miss].isnull().sum()

plt.figure(figsize=(10, 10))
sns.set()
for i, var in enumerate(num_vars_miss):
    plt.subplot(2, 2, i + 1)
    sns.distplot(df[var], bins=20, kde_kws={'linewidth': 8, 'color': 'red'}, label="Original")
    sns.distplot(df_copy[var], bins=20, kde_kws={'linewidth': 5, 'color': 'green'}, label="Mean")
    sns.distplot(df_copy_median[var], bins=20, kde_kws={'linewidth': 3, 'color': 'k'}, label="Median")
    plt.legend()

for i, var in enumerate(num_vars_miss):
    plt.figure(figsize=(10, 10))
    plt.subplot(3, 1, 1)
    sns.boxplot(df[var])
    plt.subplot(3, 1, 2)
    sns.boxplot(df_copy[var])
    plt.subplot(3, 1, 3)
    sns.boxplot(df_copy_median[var])

print("Ab milenge next tutorial me,\nTab tak ke liye SIKHATE SIKHATE kuch IMPLEMENT karte raho,\nThank You.....-:)")
