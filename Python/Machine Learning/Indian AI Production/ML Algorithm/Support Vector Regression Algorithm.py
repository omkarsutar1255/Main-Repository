# todo: Support Vector Regression Bangalore -  House Price Prediction

# todo: Business Problem - Predict the Price of Bangalore House

# todo: Load Libraries
import pandas as pd

# todo: Load Data
df = pd.read_csv('bangalore house price prediction OHE-data.csv')
print(df.head())

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

# todo: Support Vector Regression - ML Model Training
from sklearn.svm import SVR

svr_rbf = SVR(kernel='rbf')  # )( shape type separation
svr_rbf.fit(X_train, y_train)
print(svr_rbf.score(X_test, y_test))

svr_linear = SVR(kernel='linear')   # || shape type separation
svr_linear.fit(X_train, y_train)
print(svr_linear.score(X_test, y_test))

svr_poly = SVR(kernel='poly', degree=2)  # () shape type separation
svr_poly.fit(X_train, y_train)
print(svr_poly.score(X_test, y_test))

# todo: Predict the value of Home and Test
print(X_test[0])
print(svr_linear.predict([X_test[0]]))
y_pred = svr_linear.predict(X_test)
print(y_pred)
print(y_test)

# todo: calculating Error using RMSE
from sklearn.metrics import mean_squared_error
import numpy as np
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print('MSE = ', mse)
print('RMSE = ', rmse)
