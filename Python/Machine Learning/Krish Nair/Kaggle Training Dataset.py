# todo : Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# todo : read training file
df = pd.read_csv('train.csv')

# todo : analyzing data overview
df.head()

# todo : check sum of all null values in column
df.isnull().sum()

# todo : This feature is has not null values in train data but 4 na values in test data
# hence to check categorical values of any columns use values_counts
df['MSZoning'].value_counts()

# todo : analysing missing values using heatmap
sns.heatmap(df.isnull(), yticklabels=False, cbar=False)

# todo : info gives what types of values are in each column like float, object
print(df.shape)
df.info()

# todo : Correlation between features and label
corr_matrix = df.corr()
print(corr_matrix['SalePrice'].sort_values(ascending=False))
# show which features has more correlation with label hence to focus more on that

# todo : filling na values using mean, mode, median and which column has more na value will drop
# fill values with mean and median is cannot apply on categorical features hence use mode
df['LotFrontage'] = df['LotFrontage'].fillna(df['LotFrontage'].mean())
# in training data MSZoning column has no values so not mention in fillna process
df.drop(['Alley'], axis=1, inplace=True)
df['BsmtCond'] = df['BsmtCond'].fillna(df['BsmtCond'].mode()[0])
df['BsmtQual'] = df['BsmtQual'].fillna(df['BsmtQual'].mode()[0])
df['FireplaceQu'] = df['FireplaceQu'].fillna(df['FireplaceQu'].mode()[0])
df['GarageType'] = df['GarageType'].fillna(df['GarageType'].mode()[0])
df.drop(['GarageYrBlt'], axis=1, inplace=True)
df['GarageFinish'] = df['GarageFinish'].fillna(df['GarageFinish'].mode()[0])
df['GarageQual'] = df['GarageQual'].fillna(df['GarageQual'].mode()[0])
df['GarageCond'] = df['GarageCond'].fillna(df['GarageCond'].mode()[0])
df.drop(['PoolQC', 'Fence', 'MiscFeature'], axis=1, inplace=True)
print(df.shape)
df.drop(['Id'], axis=1, inplace=True)
df['MasVnrType'] = df['MasVnrType'].fillna(df['MasVnrType'].mode()[0])
df['MasVnrArea'] = df['MasVnrArea'].fillna(df['MasVnrArea'].mode()[0])

# todo : again checking null values
df.isnull().sum()

# todo : analysing missing values using heatmap
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')

# todo : Fill Missing Values using mean, mode, median and which column has more na value will drop
df['BsmtExposure'] = df['BsmtExposure'].fillna(df['BsmtExposure'].mode()[0])

# todo : analysing missing values using heatmap
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')

# todo : Fill Missing Values using mean, mode, median and which column has more than na value will drop
df['BsmtFinType2'] = df['BsmtFinType2'].fillna(df['BsmtFinType2'].mode()[0])

# todo : droping na values rows which are arond 1% of overall rows
df.dropna(inplace=True)
print(df.shape)
df.head()

# todo : Handle Categorical Features from dataset
columns = ['MSZoning', 'Street', 'LotShape', 'LandContour', 'Utilities', 'LotConfig', 'LandSlope', 'Neighborhood',
           'Condition2', 'BldgType', 'Condition1', 'HouseStyle', 'SaleType',
           'SaleCondition', 'ExterCond',
           'ExterQual', 'Foundation', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
           'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType', 'Heating', 'HeatingQC',
           'CentralAir',
           'Electrical', 'KitchenQual', 'Functional',
           'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond', 'PavedDrive']
len(columns)


# todo : Creating function that create dummies [one of the function that handle categorical function]
def category_onehot_multcols(multcolumns):          # takes list of categorical columns
    df_final = final_df                       # creating reference for new dataset
    i = 0
    for fields in multcolumns:

        print(fields)
        df1 = pd.get_dummies(final_df[fields], drop_first=True)  # drop first drops first column of dummies
        # getting dummies of categorical features and set to dummies dataset

        final_df.drop([fields], axis=1, inplace=True)           # delete that column from old dataset
        if i == 0:
            df_final = df1.copy()                       # for first time dummies dataset set in new dataset
        else:
            df_final = pd.concat([df_final, df1], axis=1)   # concatenate new data with dummies dataset
        i = i + 1

    df_final = pd.concat([final_df, df_final], axis=1)   # at end concatenate old dataset with new dataset

    return df_final


# todo : making copy of training data set into main_df
main_df = df.copy()

# todo : Combine Test Data bcoz in train and test data there can be different categorical values hence to combine that
# todo : importing test data set as test_df
test_df = pd.read_csv('formulatedtest.csv')
print(test_df.shape)
test_df.head()

# todo : concatenate train dataset and test dataset into one dataset
final_df = pd.concat([df, test_df], axis=0)
print(final_df['SalePrice'])
print(final_df.shape)

final_df = category_onehot_multcols(columns)
print(final_df.shape)

# todo : way to remove duplicates column from dataset which has same column name
final_df = final_df.loc[:, ~final_df.columns.duplicated()]

print(final_df.shape)
print(final_df)

# todo : splitting test and train dataset which value is already calculated
df_Train = final_df.iloc[:1422, :]
df_Test = final_df.iloc[1422:, :]

df_Train.head()
df_Test.head()
print(df_Train.shape)

# todo : remove label column from test data
df_Test.drop(['SalePrice'], axis=1, inplace=True)

# todo : creating training data as feature and label
x_train = df_Train.drop(['SalePrice'], axis=1)
y_train = df_Train['SalePrice']

# todo : selecting the Algorithm
# first linear regression, decision tree regression, random forest regression
# out of each check RMS value then used xgboost it has less error
from xgboost import XGBRegressor
# first checking xgboost error without giving any parameter
model1 = XGBRegressor()
model1.fit(x_train, y_train)

# secondly create xgboost parameter to put in random cv
regressor = XGBRegressor()

# todo : hyper parameter Optimization [optional] only to increase accuracy of xgboost
# todo : Define the grid of hyper parameters to search
hyperparameter_grid = {
    'n_estimators': [100, 500, 900, 1100, 1500],
    'max_depth': [2, 3, 5, 10, 15],
    'learning_rate': [0.05, 0.1, 0.15, 0.20],
    'min_child_weight': [1, 2, 3, 4],
    'booster': ['gbtree', 'gblinear'],
    'base_score': [0.25, 0.5, 0.75, 1]
}
# todo : Set up the random search with 4-fold cross validation
from sklearn.model_selection import RandomizedSearchCV
random_cv = RandomizedSearchCV(estimator=regressor,
                               param_distributions=hyperparameter_grid,
                               cv=5, n_iter=50,
                               scoring='neg_mean_absolute_error', n_jobs=4,
                               verbose=5,
                               return_train_score=True,
                               random_state=42)

random_cv.fit(x_train, y_train)
print(random_cv.best_estimator_)   # random_cv shows best parameters for regressor

# todo : initializing regressor again with best parameter that has given by random_cv
regressor = XGBRegressor(base_score=0.25, booster='gbtree', colsample_bylevel=1,
                                 colsample_bytree=1, gamma=0, learning_rate=0.1, max_delta_step=0,
                                 max_depth=2, min_child_weight=1, missing=None, n_estimators=900,
                                 n_jobs=1, nthread=None, objective='reg:linear', random_state=0,
                                 reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=None,
                                 silent=True, subsample=1)
regressor.fit(x_train, y_train)   # training model with train data

# todo : pickle contain regression so dont have to train model again and again
import pickle
filename = 'finalized_model.pkl'
# pickle.dump(model1, open(filename, 'wb'))
pickle.dump(regressor, open(filename, 'wb'))

# todo : predication on test data
# y_pred = model1.predict(df_Test)
# print(y_pred)
y_pred = regressor.predict(df_Test)
print(y_pred)

# todo : create a sample submission file to submit
pred = pd.DataFrame(y_pred)           # convert into dataframe
sub_df = pd.read_csv('sample_submission.csv')
datasets = pd.concat([sub_df['Id'], pred], axis=1)
datasets.columns = ['Id', 'SalePrice']              # column names set as ID and Salesprice
datasets.to_csv('sample_submission.csv', index=False)

# todo : after get predicted label for test data use it as label to test and combine train and test data.
# todo : now again train xgboost regressor with same hyper parameter with all data and then test on test data
# todo : this is way to increase accuracy of xgboost
