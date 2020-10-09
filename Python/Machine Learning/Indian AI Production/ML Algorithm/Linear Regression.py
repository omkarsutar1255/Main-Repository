# Business Problem - Predict the Price of Bangalore House
# Using Linear Regression - Supervised Machine Learning Algorithm

# todo: Load Libraries

import pandas as pd

# todo: Load Data

df = pd.read_csv('Bengaluru_House_Data.csv')

df.head()

df['bath'] = df['bath'].fillna(df['bath'].mean())
df['balcony'] = df['balcony'].fillna(df['balcony'].mean())

"""### Split Data"""
X = pd.DataFrame()
X['bath'] = df['bath']
X['balcony'] = df['balcony']
y = df['price']


print('Shape of X = ', X.shape)
print('Shape of y = ', y.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=51)

print('Shape of X_train = ', X_train.shape)
print('Shape of y_train = ', y_train.shape)
print('Shape of X_test = ', X_test.shape)
print('Shape of y_test = ', y_test.shape)

"""### Feature Scaling"""

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)

"""## Linear Regression - ML Model Training"""

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(X_train, y_train)

print(lr.coef_)

print(lr.intercept_)

"""## Predict the value of Home and Test"""

print(X_test[0, :])

lr.predict([X_test[0, :]])

lr.predict(X_test)

print(y_test)


print(type(X_test))
print(type(y_test))
print(lr.score(X_test, y_test))
