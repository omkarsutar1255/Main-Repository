import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

diabetes = datasets.load_diabetes()          # loading dataset of diabetes

diabetes_X = np.array([[1], [2], [3]])        # scikit learn use numpy array to work

diabetes_X_train = diabetes_X            # getting feature values except last 30 values to train
diabetes_X_test = diabetes_X               # getting last 30 feature values to test our programme

diabetes_Y_train = np.array([3, 2, 4])         # these are the labels for train model
diabetes_Y_test = np.array([3, 2, 4])          # these are labels for test model

model = linear_model.LinearRegression()          # making model of linear regression

model.fit(diabetes_X_train, diabetes_Y_train)    # giving value to model to train

diabetes_Y_predicted = model.predict(diabetes_X_test)     # giving values to model to predict

print("mean squared error is : ", mean_squared_error(diabetes_Y_test, diabetes_Y_predicted))
# checking spread of points from simple linear regression line

print("weight : ", model.coef_)              # value of slope of regression line
print("intersect : ", model.intercept_)      # initial value of slope of regression line

plt.scatter(diabetes_X_test, diabetes_Y_test)    # give scatter plot of actual datapoints
plt.plot(diabetes_X_test, diabetes_Y_predicted, c='r')  # give line plot of predicted datapoints in red
plt.show()
