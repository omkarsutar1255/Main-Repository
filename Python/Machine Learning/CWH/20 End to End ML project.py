# TODO: Dragon Real Estate - Price Predictor

# todo : Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# todo : import data file
housing = pd.read_csv("new data.csv")

# todo : getting overview of data
# print(housing.head())          # fetch top 5 rows from data
# print(housing.info())          # getting data information to check where null are present
# print(housing['CHAS'].value_counts())     # show how much time 0 or 1 or any other value present in that column
# print(housing.describe())           # show count, mean, std, min, 25%, 50%, 75%, max

# todo: plotting histogram to check which value is more in every column by visualization
housing.hist(bins=50, figsize=(20, 15))
# plotting data in matplotlib to check what kind of values are in each column
plt.show()

# TODO : Train-test splitting data on your own
"""def split_train_test(data, test_ratio):
    np.random.seed(42)                            # after one time shuffled it store into doc
    shuffled = np.random.permutation(len(data))   # gives different shuffled values
    print(shuffled)
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled[:test_set_size]
    train_indices = shuffled[train_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

train_set, test_set = split_train_test(housing, 0.2)
print(f"Rows in train set: {len(train_set)} \n Rows in test set: {len(test_set)}\n")
"""
# todo : test train spliting data by using sklearn function
# from sklearn.model_selection import train_test_split
#
# train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
# # test size 0.2 split 20% of full data into test set and remaining is train set
# print(f"Rows in train set: {len(train_set)} \n Rows in test set: {len(test_set)}\n")

global strat_test_set, strat_train_set
from sklearn.model_selection import StratifiedShuffleSplit

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing['CHAS']):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

strat_test_set['CHAS'].value_counts()
strat_train_set['CHAS'].value_counts()

# todo : here set train data as housing data
housing = strat_train_set.copy()
# due to less data is giving we have use all data as train data

# todo : Correlation between features and label
corr_matrix = housing.corr()
print(corr_matrix['MEDV'].sort_values(ascending=False))
# show which features has more correlation with label hence to focus more on that

# todo : Checking correlation using scatter plot
from pandas.plotting import scatter_matrix
attribute = ['MEDV', 'RM', 'ZN', 'LSTAT']
scatter_matrix(housing[attribute], figsize=(12, 8))
plt.show()

# todo : Checking correlation between two columns using plot
housing.plot(kind='scatter', x="RM", y="MEDV", alpha=0.8)
# check relation between two columns to remove unwanted number
plt.show()

# todo : Trying out attribute combinations and check using correlation and pyplot
housing['TAXRM'] = housing['TAX']/housing["RM"]
print(housing['TAXRM'])
print(housing.head())
corr_matrix1 = housing.corr()
print(corr_matrix1['MEDV'].sort_values(ascending=False))
housing.plot(kind='scatter', x="TAXRM", y="MEDV", alpha=0.8)
plt.show()

# todo : spliting features and labels columns
housing = housing.drop("MEDV", axis=1)
housing_labels = strat_train_set["MEDV"].copy()

# todo : Handling Missing attribute in any column in test and train sets in three way
# 1) Get rid of missing data points - if less number of missing values in column
# 2) Get rid of whole attribute     - if correlation of that column with label is around zero
# 3) Set value to some value(0, mean, mode or median)

# todo : 1) dropping row of missing value
A = housing.dropna(subset=["RM"], inplace=False)  # Change will happen in copy of housing i.e. A
# for save change in original housing data (Inplace=True)
print(A.shape)

# todo : 1) dropping column of missing value
B = housing.drop("RM", axis=1, inplace=False)
print(B.shape)

# todo : before fill values in RM column
print(housing['RM'].count())
# print(housing.describe())

# todo : 1) Set values at missing value
# self of setting median values at missing values
# median = housing['RM'].median()  # first it set values in ascending order then take middle value
# print(median)               # middle value in column
# housing['RM'].fillna(median, inplace=False)   # filling median at missing value

# sklearn module to set 0, mean, mode, median values at missing values
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy="median")  # change strategy to set mode or mean values
imputer.fit(housing)  # fits computes strategies on data and returns nothing
print(imputer.statistics_)  # shows values of median for each columns
X = imputer.transform(housing)  # gets previously compute strategies and make changes in data
print(type(X))  # data is in ndarray form
housing_tr = pd.DataFrame(X, columns=housing.columns)
# created new dataframe that has transform data and housing column name as column

# todo : after set missing values in RM column
print(housing_tr['RM'].count())
# print(housing_tr.describe())

# todo : Scikit-Learn Design
# primarily, three types of objects in scikit learn
# 1. Estimators - It estimates some parameter based on a dataset. Eg. imputer, LabelEncoder, pd.dummies
# It has a fit method and transform method. Fit method - Fits the dataset and calculates internal parameters

# 2. Transformers - transform method takes input and returns output based on the learning from fit().
# It also has a convenience function called fit_transform() which fits and then transforms.

# 3. Predictors - LinearRegression, RandomForest, DecisionTree, XGBoost model are examples of predictor.
# fit() and predict() are two common functions.
# It also gives score() function which will evaluate the predictions.

# todo : Feature Scaling
# if one column values are between 25-75 and other column values are between 200-500 then features scaling make both
# column values in one scale like 0-10. This increase efficiency of machine learning model.
# Primarily, two types of feature scaling methods:
# 1. Min-max scaling (Normalization)
#     (value - min)/(max - min)
#     Sklearn provides a class called MinMaxScaler for this

# 2. Standardization
#     (value - mean)/std
#     Sklearn provides a class called StandardScaler for this

# todo : Creating a Pipeline
# make code flexible that enable easy changeable like models, strategies, etc.
# pipeline helps to do series of steps
from sklearn.pipeline import Pipeline  # library to create pipeline in sklearn
from sklearn.preprocessing import StandardScaler

my_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy="median")),  # it will apply imputer function on data
    #     ..... add as many as you want in your pipeline
    ('std_scaler', StandardScaler()),  # at last it will apply standardization on values
])

housing_num_tr = my_pipeline.fit_transform(housing)
# compute values as per pipeline strategy and transform values into new dataset

print(housing_num_tr.shape)

# todo : Selecting a desired model for Machine learning

# from sklearn.linear_model import LinearRegression
# model = LinearRegression()
# model.fit(housing_num_tr, housing_labels)

# from sklearn.tree import DecisionTreeRegressor
# model = DecisionTreeRegressor()
# model.fit(housing_num_tr, housing_labels)

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(housing_num_tr, housing_labels)

# todo : checking model prediction on 5 rows to manually check accuracy
some_data = housing.iloc[:5]
some_labels = housing_labels.iloc[:5]
prepared_data = my_pipeline.transform(some_data)
print(model.predict(prepared_data))
print(list(some_labels))

# todo : Evaluating the model by root mean square error
from sklearn.metrics import mean_squared_error

housing_predictions = model.predict(housing_num_tr)
mse = mean_squared_error(housing_labels, housing_predictions)
rmse = np.sqrt(mse)
print(mse)
print(rmse)

# todo : Using better evaluation technique - Cross Validation
# 1 2 3 4 5 6 7 8 9 10
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, housing_num_tr, housing_labels, scoring="neg_mean_squared_error", cv=10)
rmse_scores = np.sqrt(-scores)
print(rmse_scores)


# todo : getting scores, mean and std of every model then which has less mean and std it should choose
def print_scores(scores):
    print("Scores:", scores)
    print("Mean: ", scores.mean())
    print("Standard deviation: ", scores.std())
print_scores(rmse_scores)

# todo : Saving the model
from joblib import dump
dump(model, 'Dragon.joblib')

# todo : Testing the model on test data

X_test = strat_test_set.drop("MEDV", axis=1)
Y_test = strat_test_set["MEDV"].copy()
X_test_prepared = my_pipeline.transform(X_test)
final_predictions = model.predict(X_test_prepared)
final_mse = mean_squared_error(Y_test, final_predictions)
final_rmse = np.sqrt(final_mse)
print(final_predictions, list(Y_test))

print(final_rmse)

"""
prepared_data[0]
"""

# todo : Using model
from joblib import dump, load
import numpy as np

model = load('Dragon.joblib')
features = np.array([[-5.43942006, 4.12628155, -1.6165014, -0.67288841, -1.42262747,
                      -11.44443979304, -49.31238772, 7.61111401, -26.0016879, -0.5778192,
                      -0.97491834, 0.41164221, -66.86091034]])
model.predict(features)
