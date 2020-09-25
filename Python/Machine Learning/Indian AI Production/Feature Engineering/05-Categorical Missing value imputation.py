# todo : Data Cleaning
# todo : Categorical Missing value imputation Part-5

# todo : Importing library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# todo : import data
df = pd.read_csv(r"G:\DataSet\House Price Prediction\train.csv")

# todo : analysis data
df.head()

# todo : selecting categorical columns
cat_vars = df.select_dtypes(include='object')

# todo : analysis of categorical data
cat_vars.head()
cat_vars.isnull().sum()
miss_val_per = cat_vars.isnull().mean() * 100
print(miss_val_per)

# todo : dropping column that has more missing values
drop_vars = ['Alley', 'FireplaceQu', 'PoolQC', 'Fence', 'MiscFeature']
cat_vars.drop(columns=drop_vars, axis=1, inplace=True)
print(cat_vars.shape)

# todo : getting column name that has missing values in less amount
isnull_per = cat_vars.isnull().mean() * 100
miss_vars = isnull_per[isnull_per > 0].keys()
print(miss_vars)


cat_vars['MasVnrType'].fillna('Missing')

# todo : it shows mode value of that column
cat_vars['MasVnrType'].mode()

# todo : it shows how much which value is present
cat_vars['MasVnrType'].value_counts()

# todo : filling mode value in missing values of column
cat_vars['MasVnrType'].fillna(cat_vars['MasVnrType'].mode()[0])


cat_vars['MasVnrType'].fillna(cat_vars['MasVnrType'].mode()[0]).value_counts()

cat_vars_copy = cat_vars.copy()

# todo : filling mode values in each categorical column
for var in miss_vars:
    cat_vars_copy[var].fillna(cat_vars[var].mode()[0], inplace=True)
    print(var, "=", cat_vars[var].mode()[0])

# todo : check how null values are present in data
cat_vars_copy.isnull().sum().sum()

# todo : checking changes in original dataset after impute mode value in visualize format
plt.figure(figsize=(16, 9))
for i, var in enumerate(miss_vars):
    plt.subplot(4, 3, i + 1)
    plt.hist(cat_vars_copy[var], label="Impute")
    plt.hist(cat_vars[var].dropna(), label="Original")
    plt.legend()

# todo : updating main dataset
df.update(cat_vars_copy)

# todo : deleting column from main dataset that has more missing values
df.drop(columns=drop_vars, inplace=True)

# todo : checking now which categorical column has null values
df.select_dtypes(include='object').isnull().sum()
