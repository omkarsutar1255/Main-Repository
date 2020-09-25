# todo: Data Cleaning
# todo: Missing value imputation using Scikit-Learn
# todo: Different strategy for different variables(Numerical & Categorical) with Scikit-Learn

# todo: importing libraries
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# todo: Loading data
train = pd.read_csv(r"G:\DataSet\House Price Prediction\train.csv")
test = pd.read_csv(r"G:\DataSet\House Price Prediction\test.csv")

# todo: analysing datasets
print("Shape of train df = ", train.shape)
print("Shape of test df =", test.shape)

# todo: creating features and labels from training dataset
X_train = train.drop(columns="SalePrice", axis=1)
y_train = train["SalePrice"]
X_test = test.copy()

# todo: analysis datasets
print("Shape of X_train = ", X_train.shape)
print("Shape of y_train = ", y_train.shape)
print("Shape of X_test =", X_test.shape)

# todo: Missing value imputation
# todo: checking number of null values present in training dataset
isnull_sum = X_train.isnull().sum()
print(isnull_sum)

# todo: selecting columns that contains numerical values
num_vars = X_train.select_dtypes(include=["int64", "float64"]).columns

# todo: creating list that exclude numerical columns which not contain na values
num_vars_miss = [var for var in num_vars if isnull_sum[var] > 0]
print(num_vars_miss)

# todo: selecting columns that contains categorical values
cat_vars = X_train.select_dtypes(include=["O"]).columns

# todo: creating list that exclude categorical columns which not contain na values
cat_vars_miss = [var for var in cat_vars if isnull_sum[var] > 0]
print(cat_vars_miss)

# todo: creating various list of columns based on type of imputation strategy
num_var_mean = ["LotFrontage"]
num_var_median = ['MasVnrArea', 'GarageYrBlt']
cat_vars_mode = ['Alley',
                 'MasVnrType',
                 'BsmtQual',
                 'BsmtCond',
                 'BsmtExposure',
                 'BsmtFinType1',
                 'BsmtFinType2',
                 'Electrical',
                 'FireplaceQu', ]
cat_vars_missing = ['GarageType',
                    'GarageFinish',
                    'GarageQual',
                    'GarageCond',
                    'PoolQC',
                    'Fence',
                    'MiscFeature']

# todo: creating different pipeline for different types of imputation
num_var_mean_imputer = Pipeline(steps=[("imputer", SimpleImputer(strategy="mean"))])
num_var_median_imputer = Pipeline(steps=[("imputer", SimpleImputer(strategy="median"))])
cat_vars_mode_imputer = Pipeline(steps=[("imputer", SimpleImputer(strategy="most_frequent"))])
cat_vars_missing_imputer = Pipeline(steps=[("imputer", SimpleImputer(strategy="constant", fill_value="missing"))])

# todo: giving column names with respective pipeline strategy to transformer.
preprocessor = ColumnTransformer(transformers=[("mean_imputer", num_var_mean_imputer, num_var_mean),
                                               ("median_imputer", num_var_median_imputer, num_var_median),
                                               ("mode_imputer", cat_vars_mode_imputer, cat_vars_mode),
                                               ("missing_imputer", cat_vars_missing_imputer, cat_vars_missing)])

# todo: fit transformer on training dataset to calculate values for na values
preprocessor.fit(X_train)

# todo: to show what transformer did on original dataset
print(preprocessor.transform)

# todo: showing mean, median, mode values calculated by fit_transformer
print(preprocessor.named_transformers_["mean_imputer"].named_steps["imputer"].statistics_)
train["LotFrontage"].mean()
print(preprocessor.named_transformers_["mode_imputer"].named_steps["imputer"].statistics_)

# todo: placing calculated values in original dataset and getting new clean dataset for train and test dataset
X_train_clean = preprocessor.transform(X_train)
X_test_clean = preprocessor.transform(X_test)

# todo: showing new clean dataset
print(X_train_clean)

# todo: shows the how transformer replacing values by dropping not na contain columns(use passthrough)
print(preprocessor.transformers_)

# todo: to regain not na contain column pasting clean data in original columns
X_train_clean_miss_var = pd.DataFrame(X_train_clean,
                                      columns=num_var_mean + num_var_median + cat_vars_mode + cat_vars_missing)

# todo: analysis dataset
X_train_clean_miss_var.head()
X_train_clean_miss_var.isnull().sum().sum()
train["Alley"].value_counts()
X_train_clean_miss_var["Alley"].value_counts()
X_train_clean_miss_var["MiscFeature"].value_counts()

# todo: Home Work
# todo: Create Clean X_train DataFrame with call variables

# no missing values variables index
remainder_vars_index = [0, 1, 2, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 27, 28, 29,
                        34, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 61, 62, 65,
                        66, 67, 68, 69, 70, 71, 75, 76, 77, 78, 79]

# get no missing values variables name using there index
remainder_vars = [isnull_sum.keys()[var_index] for var_index in remainder_vars_index]
print(remainder_vars)

len(remainder_vars)

# concatinate X_train_clean_miss_var df and remainder_vars
X_train = pd.concat([X_train_clean_miss_var, train[remainder_vars]], axis=1)

print(X_train.shape)

X_train.isnull().sum().sum()

# Create test DataFrame with missing value imputed variables
X_test_clean_miss_var = pd.DataFrame(X_test_clean,
                                     columns=num_var_mean + num_var_median + cat_vars_mode + cat_vars_missing)
print(X_test_clean_miss_var.shape)

X_test_clean_miss_var.isnull().sum().sum()

# concatinate X_test_clean_miss_var df and remainder_vars
X_test = pd.concat([X_test_clean_miss_var, test[remainder_vars]], axis=1)
print(X_test.shape)

X_test.isnull().sum().sum()

# 22 <= What is this, in X_test df still missing values as available but why 
# because we fill missing values in those columns which have missing value present in only X_train df
# Basicaly we get df then  find missing values variables then split df into X_train, X_test, y_train, y_test
# after that we fill missing value

# so if you have train and test df seperatly then first thing you should concatinate then find the missing 
# values variables it's is great strategy and carry on
# so you can try yourself

isnull_sum_test = X_test.isnull().sum()
print(isnull_sum_test)

# finding the numerical variable which have mising value
num_vars_test = X_test.select_dtypes(include=["int64", "float64"]).columns
num_vars_miss_test = [var for var in num_vars_test if isnull_sum_test[var] > 0]
print(num_vars_miss_test)

# finding the categorical variable which have mising value
cat_vars_test = X_test.select_dtypes(include=["O"]).columns
cat_vars_miss_test = [var for var in cat_vars_test if isnull_sum_test[var] > 0]
print(cat_vars_miss_test)
