# todo: Training And Testing Available Data

# todo: Importing Library
import pandas as pd
import matplotlib.pyplot as plt

# todo: Load DataSet
df = pd.read_csv("carprices.csv")
df.head()

# todo: Car Mileage Vs Sell Price ($)
plt.scatter(df['Mileage'], df['Sell Price($)'])

# todo: Car Age Vs Sell Price ($)
plt.scatter(df['Age(yrs)'], df['Sell Price($)'])

# todo: Splitting into Features and label dataSet
X = df[['Mileage', 'Age(yrs)']]
y = df['Sell Price($)']

# todo: splitting into train and test dataSet
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
print(X_train)
print(X_test)
print(y_train)
print(y_test)

# todo: Lets run linear regression model now
from sklearn.linear_model import LinearRegression
clf = LinearRegression()
clf.fit(X_train, y_train)
print(X_test)
print(clf.predict(X_test))
print(y_test)
print(clf.score(X_test, y_test))

# todo: random_state argument
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)
print(X_test)
