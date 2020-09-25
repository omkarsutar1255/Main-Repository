# todo: Arbitrary Value Imputation
# this technique was derived from kaggle competition
# It consists of replacing NAN by an arbitrary value

# todo: import library
import pandas as pd
import numpy as np

# todo: load dataset
df = pd.read_csv("titanic.csv", usecols=["Age", "Fare", "Survived"])
df.head()

# todo: creating function that create new two column with filling 0 and 100 values at null values
def impute_nan(df, variable):
    df[variable + '_zero'] = df[variable].fillna(0)
    df[variable + '_hundred'] = df[variable].fillna(100)

# todo: creating histogram on age column
df['Age'].hist(bins=50)

# todo: Advantages
# - Easy to implement
# - Captures the importance of missingess if there is one

# todo: Disadvantages
# - Distorts the original distribution of the variable
# - If missingess is not important, it may mask the predictive power of the original variable by distorting its distribution
# - Hard to decide which value to use

# todo: How To Handle Categroical Missing Values
# todo: 1)Frequent Category Imputation (mode)

# todo: load dataset
df = pd.read_csv('loan.csv', usecols=['BsmtQual', 'FireplaceQu', 'GarageType', 'SalePrice'])
print(df.columns)            # to check all columns to select categorical columns

# todo: analysis dataset
print(df.shape)
df.isnull().sum()
df.isnull().mean().sort_values(ascending=True)  # percentage of null values in each column

# todo: Compute the frequency of values in every feature
df['BsmtQual'].value_counts().plot.bar()           # in plotting way
df.groupby(['BsmtQual'])['BsmtQual'].count().sort_values(ascending=False).plot.bar()
df['GarageType'].value_counts().plot.bar()
df['FireplaceQu'].value_counts().plot.bar()

# todo: this gives mode value of that column
print(df['GarageType'].value_counts().index[0])
print(df['GarageType'].mode()[0])

# creating function that fill mode values in null values
def impute_nan(df, variable):
    most_frequent_category = df[variable].mode()[0]
    df[variable].fillna(most_frequent_category, inplace=True)

# todo: calling function for each features of dataset
for feature in ['BsmtQual', 'FireplaceQu', 'GarageType']:
    impute_nan(df, feature)

# todo: gives percentage of null value in features
df.isnull().mean()

# todo: Advantages
# 1. Easy To implement
# 2. Fater way to implement
# todo: Disadvantages
# 1. Since we are using the more frequent labels, it may use them in an over represented way, if there are many nan's
# 2. It distorts the relation of the most frequent label

# todo: 2)Adding a feature to capture NAN

# todo: load dataset
df = pd.read_csv('loan.csv', usecols=['BsmtQual', 'FireplaceQu', 'GarageType', 'SalePrice'])
df.head()

# todo: creating new column that has 1 value if null value present in base column and fill mode value in base column
df['BsmtQual_Var'] = np.where(df['BsmtQual'].isnull(), 1, 0)
df.head()
frequent = df['BsmtQual'].mode()[0]
df['BsmtQual'].fillna(frequent, inplace=True)
df.head()

# todo: creating new column that has 1 value if null value present in base column and fill mode value in base column
df['FireplaceQu_Var'] = np.where(df['FireplaceQu'].isnull(), 1, 0)
frequent = df['FireplaceQu'].mode()[0]
df['FireplaceQu'].fillna(frequent, inplace=True)
df.head()

# todo: Suppose if you have more mode values, we just replace null value as "missing"

# todo: load dataset
df = pd.read_csv('loan.csv', usecols=['BsmtQual', 'FireplaceQu', 'GarageType', 'SalePrice'])
df.head()

# todo: create function that replace null value as "missing" and if not null then df[variable]
def impute_nan(df, variable):
    df[variable + "newvar"] = np.where(df[variable].isnull(), "Missing", df[variable])

# todo: applying function for each column
for feature in ['BsmtQual', 'FireplaceQu', 'GarageType']:
    impute_nan(df, feature)
df.head()

# todo: delete the base column after new column created
df = df.drop(['BsmtQual', 'FireplaceQu', 'GarageType'], axis=1)
df.head()
