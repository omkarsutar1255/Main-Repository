# todo:  Business Problem - Predict the Price of Bangalore House
# todo: Using Linear Regression - Supervised Machine Learning Algorithm

# todo: Load Libraries
import pandas as pd
import numpy as np

# todo: Load Data
df = pd.read_csv('Bengaluru_House_Data.csv')
df.head()

# todo: Split Data
X = df.drop('price', axis=1)
y = df['price']
print('Shape of X = ', X.shape)
print('Shape of y = ', y.shape)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=51)
print('Shape of X_train = ', X_train.shape)
print('Shape of y_train = ', y_train.shape)
print('Shape of X_test = ', X_test.shape)
print('Shape of y_test = ', y_test.shape)

# todo: Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)

# todo: Polynomial Linear Regression - ML Model Training
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

poly_reg = PolynomialFeatures(degree=2)               # Linear regression have straight line bt polynomial regression
# allow that line to bend upto given degree and try to fit with data points
poly_reg.fit(X_train)
X_train_poly = poly_reg.transform(X_train)
X_test_poly = poly_reg.transform(X_test)

print(X_train_poly.shape, X_test_poly.shape)

lr = LinearRegression()
lr.fit(X_train_poly, y_train)

print(lr.score(X_test_poly, y_test))
print(lr.predict([X_test_poly[0, :]]))

y_pred = lr.predict(X_test_poly)
print(y_pred)
print(y_test)

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(mse, rmse)
