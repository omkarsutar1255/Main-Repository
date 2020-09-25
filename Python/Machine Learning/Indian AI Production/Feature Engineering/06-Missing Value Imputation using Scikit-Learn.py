# todo : Data Cleaning
# todo : Missing value imputation using Scikit-Learn
# todo : for Numeric and Categorical Variables/Data

# todo : import libraries
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

# todo : loading train and test data
train = pd.read_csv(r"G:\DataSet\House Price Prediction\train.csv")
test = pd.read_csv(r"G:\DataSet\House Price Prediction\test.csv")

# todo : analysis data
print("shape of train df = ", train.shape)
print("shape of test df = ", test.shape)
train.head()

# todo : creating features and labels from training dataset
X_train = train.drop(columns="SalePrice")
y_train = train["SalePrice"]
print("shape of X_train df = ", X_train.shape)
print("shape of y_train df = ", y_train.shape)

# todo : Numerical Missing Value Imputation
# todo : getting columns names that contain numerical values
num_vars = X_train.select_dtypes(include=["int64", "float64"]).columns
print(num_vars)

# todo : checking null values in numerical columns
X_train[num_vars].isnull().sum()

# todo : creating object that calculate mean
imputer_mean = SimpleImputer(strategy='mean')
# imputer_mean = SimpleImputer(strategy='constant', fill_value=99)  # to fill values in global constant values

# todo : calculate mean of each column of giving dataset
imputer_mean.fit(X_train[num_vars])

# todo : showing mean values of each columns
print(imputer_mean.statistics_)

# todo : placing mean values in original dataset (it returns new 2D array)
imputer_mean.transform(X_train[num_vars])

# todo : placing 2D array of mean in original dataset of train and test
X_train[num_vars] = imputer_mean.transform(X_train[num_vars])
test[num_vars] = imputer_mean.transform(test[num_vars])

# todo : again check null values in train and test dataset
X_train[num_vars].isnull().sum()
test[num_vars].isnull().sum()

# todo : Categorical Missing Value Imputation
# todo : Selecting columns that has categorical values
cat_vars = X_train.select_dtypes(include=["O"]).columns
print(cat_vars)

# todo : checking total null values in each categorical column
X_train[cat_vars].isnull().sum()

# todo : creating object that calculate most frequent value in each column of dataset
imputer_mode = SimpleImputer(strategy='most_frequent')
# imputer_mean = SimpleImputer(strategy='constant', fill_value=99)  # for replacing global constant
print(imputer_mode)

# todo : checking mode values for each categorical columns of dataset
imputer_mode.fit(X_train[cat_vars])

# todo : showing mode values for each column
print(imputer_mode.statistics_)

# todo : placing mode values in original dataset's categorical column
X_train[cat_vars] = imputer_mode.transform(X_train[cat_vars])
test[cat_vars] = imputer_mode.transform(test[cat_vars])

# todo : now again check null values in both test and train dataset
X_train[cat_vars].isnull().sum()
test[cat_vars].isnull().sum()

# todo : now checking total null values in all columns
X_train.isnull().sum().sum()
