# todo: K Nearest Neighbor Regression - Supervised Machine Learning Algorithm

# todo: Load Libraries
import pandas as pd

# todo: Load Data
df = pd.read_csv('bangalore house price prediction OHE-data.csv')
df.head()

# todo: Split Data into feature and Label
X = df.drop('price', axis=1)
y = df['price']
print('Shape of X = ', X.shape)
print('Shape of y = ', y.shape)

# todo: splitting into train and test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=51)
print('Shape of X_train = ', X_train.shape)
print('Shape of y_train = ', y_train.shape)
print('Shape of X_test = ', X_test.shape)
print('Shape of y_test = ', y_test.shape)

# todo: K Nearest Neighbor Regression - ML Model Training
from sklearn.neighbors import KNeighborsRegressor
regressor = KNeighborsRegressor(n_neighbors=5)
regressor.fit(X_train, y_train)
print(regressor.score(X_test, y_test))

# todo: Predict the value of Home

print(X_test.iloc[-1, :])
print(regressor.predict([X_test.iloc[-1, :]]))
print(y_test.iloc[-1])

y_pred = regressor.predict(X_test)
print(y_pred)
print(print(y_test))
