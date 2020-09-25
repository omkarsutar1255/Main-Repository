# todo : Data Cleaning

# todo : Missing value imputation by Mean, Median

# todo : Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset 
dataset_path = r"https://drive.google.com/uc?export=download&id=1BiGZSedP4BIIuTbVTBodOhVgFImaz08c"
df = pd.read_csv(dataset_path)

print(df.shape)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df.head(6)

df.tail(6)

df.info()

df.isnull().sum()

missing_value_per = df.isnull().sum() / df.shape[0] * 100
print(missing_value_per)

missing_value_clm_gre_20 = missing_value_per[missing_value_per > 20].keys()
print(missing_value_clm_gre_20)

df2_drop_clm = df.drop(columns=missing_value_clm_gre_20)
print(df2_drop_clm.shape)

df3_num = df2_drop_clm.select_dtypes(include=['int64', 'float64'])
df3_num.head()

plt.figure(figsize=(16, 9))
sns.heatmap(df3_num.isnull())

print(df3_num[df3_num.isnull().any(axis=1)])

df3_num.isnull().sum()

missing_num_var = [var for var in df3_num.columns if df3_num[var].isnull().sum() > 0]
print(missing_num_var)

plt.figure(figsize=(10, 10))
sns.set()
for i, var in enumerate(missing_num_var):
    plt.subplot(2, 2, i + 1)
    sns.distplot(df3_num[var], bins=20, kde_kws={'linewidth': 5, 'color': '#DC143C'})

df4_num_mean = df3_num.fillna(df3_num.mean())
df4_num_mean.isnull().sum().sum()

plt.figure(figsize=(10, 10))
sns.set()
for i, var in enumerate(missing_num_var):
    plt.subplot(2, 2, i + 1)
    sns.distplot(df3_num[var], bins=20, kde_kws={'linewidth': 8, 'color': 'red'}, label="Original", )
    sns.distplot(df4_num_mean[var], bins=20, kde_kws={'linewidth': 5, 'color': 'green'}, label="Mean", )
    plt.legend()

df5_num_median = df3_num.fillna(df3_num.median())
df5_num_median.isnull().sum().sum()

plt.figure(figsize=(10, 10))
sns.set()
for i, var in enumerate(missing_num_var):
    plt.subplot(2, 2, i + 1)
    sns.distplot(df3_num[var], bins=20, hist=False, kde_kws={'linewidth': 8, 'color': 'red'}, label="Original", )
    sns.distplot(df4_num_mean[var], bins=20, hist=False, kde_kws={'linewidth': 5, 'color': 'green'}, label="Mean", )
    sns.distplot(df5_num_median[var], bins=20, hist=False, kde_kws={'linewidth': 3, 'color': 'k'}, label="Median", )
    plt.legend()

for i, var in enumerate(missing_num_var):
    plt.figure(figsize=(10, 10))
    plt.subplot(3, 1, 1)
    sns.boxplot(df[var])
    plt.subplot(3, 1, 2)
    sns.boxplot(df4_num_mean[var])
    plt.subplot(3, 1, 3)
    sns.boxplot(df5_num_median[var])

df_concat = pd.concat([df3_num[missing_num_var], df4_num_mean[missing_num_var], df5_num_median[missing_num_var]],
                      axis=1)

print(df_concat[df_concat.isnull().any(axis=1)])

print("Thank You.....-:)")
