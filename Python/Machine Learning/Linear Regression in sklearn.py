import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

diabetes = datasets.load_diabetes()          # loading dataset of diabetes
print(diabetes.keys())       # it shows keys from dataset
# (['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename'])

# print(diabetes.data)          # it shows data in numpy array form
# print(diabetes.DESCR)         # it gives description of dataset

# diabetes_X = diabetes.data[:, np.newaxis, 3]   # : gets all values from 3rd column and put init numpy array
# print(diabetes_X)
diabetes_X = diabetes.data                        # giving all data of all types of features (we cant plot this)

diabetes_X_train = diabetes_X[:-30]              # getting feature values except last 30 values to train
diabetes_X_test = diabetes_X[-30:]               # getting last 30 feature values to test our programme

diabetes_Y_train = diabetes.target[:-30]         # these are the labels for train model
diabetes_Y_test = diabetes.target[-30:]          # these are labels for test model

model = linear_model.LinearRegression()          # making model of linear regression

model.fit(diabetes_X_train, diabetes_Y_train)    # giving value to model to train

diabetes_Y_predicted = model.predict(diabetes_X_test)     # giving values to model to predict

print("mean squared error is : ", mean_squared_error(diabetes_Y_test, diabetes_Y_predicted))
# checking spread of points from simple linear regression line

print("weight : ", model.coef_)              # value of slope of regression line
print("intersect : ", model.intercept_)      # initial value of slope of regression line

# plt.scatter(diabetes_X_test, diabetes_Y_test)    # give scatter plot of actual datapoints
# plt.plot(diabetes_X_test, diabetes_Y_predicted, c='r')  # give line plot of predicted datapoints in red
# plt.show()
