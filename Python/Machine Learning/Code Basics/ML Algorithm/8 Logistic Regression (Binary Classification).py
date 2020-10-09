# todo: Import Libraries
import pandas as pd
from matplotlib import pyplot as plt
import math

# todo: Load DataSet
df = pd.read_csv("insurance_data.csv")
df.head()

# todo: plotting graph on relationship of features with Label
plt.scatter(df.age, df.bought_insurance, marker='+', color='red')

# todo: splitting into train and test dataSet
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df[['age']], df.bought_insurance, train_size=0.8)
print(X_test)

# todo: create Linear Regression Model
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)
print(X_test)
y_predicted = model.predict(X_test)
model.predict_proba(X_test)           # Gives Probability of getting 0 and 1 in prediction
model.score(X_test, y_test)
print(y_predicted)
print(X_test)

# todo: model.coef_ indicates value of m in y=m*x + b equation
print(model.coef_)
# todo: model.intercept_ indicates value of b in y=m*x + b equation
print(model.intercept_)


# todo: Lets defined sigmoid function now and do the math with hand
def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def prediction_function(age):
    z = 0.042 * age - 1.53  # 0.04150133 ~ 0.042 and -1.52726963 ~ -1.53
    y = sigmoid(z)
    return y


age1 = 35
prediction_function(age1)
# todo: 0.485 is less than 0.5 which means person with 35 age will *not* buy insurance

age2 = 43
prediction_function(age2)
# todo: 0.485 is more than 0.5 which means person with 43 will buy the insurance
