import pandas as pd

df = pd.read_csv('Bengaluru_House_Data.csv')
df.head()

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

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)

print(lr.coef_)
print(lr.intercept_)
print(X_test[0, :])
print(lr.predict([X_test[0, :]]))
print(lr.predict(X_test))
print(y_test)
print(lr.score(X_test, y_test))

# todo: Implementing Ridge and Lasso Regression
from sklearn.linear_model import Ridge, Lasso

rd = Ridge()
rd.fit(X_train, y_train)
print(rd.score(X_test, y_test))

ls = Lasso()
ls.fit(X_train, y_train)
print(ls.score(X_test, y_test))

rd2 = Ridge(alpha=2)
rd2.fit(X_train, y_train)
print(rd2.score(X_test, y_test))

ls2 = Lasso(alpha=2)
ls2.fit(X_train, y_train)
print(ls2.score(X_test, y_test))

ls3 = Lasso(alpha=3)
ls3.fit(X_train, y_train)
print(ls3.score(X_test, y_test))
