# todo: Using Randome Forest Regression - Supervised Machine Learning Algorithm

# todo: Load Libraries
import pandas as pd

# todo: Load Data
df = pd.read_csv('bangalore house price prediction OHE-data.csv')
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

# todo: Randome Forest Regression - ML Model Training
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=100, criterion='mse')  # n_estimators = Number of Decision Tree
regressor.fit(X_train, y_train)         # after getting values from all decision tree for classification majority value
print(regressor.score(X_test, y_test))  # selected and in regression average of all decision trees values

regressor_100 = RandomForestRegressor(n_estimators=500, criterion='mse')
regressor_100.fit(X_train, y_train)
print(regressor_100.score(X_test, y_test))

# todo: Predict the value of Home

print(X_test.iloc[-1, :])
print(regressor.predict([X_test.iloc[-1, :]]))
print(y_test.iloc[-1])

y_pred = regressor.predict(X_test)
print(y_pred)
print(print(y_test))
