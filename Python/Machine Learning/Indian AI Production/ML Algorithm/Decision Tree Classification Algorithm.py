# todo: Decision Tree Classification

# todo: Import Libraries
import numpy as np
import pandas as pd

# todo: load dataset
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
print(data.data)
print(data.feature_names)
print(data.target)
print(data.target_names)

# todo: create dtaframe
df = pd.DataFrame(np.c_[data.data, data.target], columns=[list(data.feature_names) + ['target']])
print(df.head())
print(df.tail())
print(df.shape)

# todo: Split Data
X = df.iloc[:, 0:-1]
y = df.iloc[:, -1]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2020)
print('Shape of X_train = ', X_train.shape)
print('Shape of y_train = ', y_train.shape)
print('Shape of X_test = ', X_test.shape)
print('Shape of y_test = ', y_test.shape)

# todo: Train Decision Tree Classification Model
from sklearn.tree import DecisionTreeClassifier

classifier = DecisionTreeClassifier(criterion='gini')
classifier.fit(X_train, y_train)
print(classifier.score(X_test, y_test))

classifier_entropy = DecisionTreeClassifier(criterion='entropy')
classifier_entropy.fit(X_train, y_train)
print(classifier_entropy.score(X_test, y_test))

# todo: Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train_sc = sc.transform(X_train)
X_test_sc = sc.transform(X_test)

# todo: Decision Tree Model on Feature Scaling data
classifier_sc = DecisionTreeClassifier(criterion='gini')
classifier_sc.fit(X_train_sc, y_train)
print(classifier_sc.score(X_test_sc, y_test))

# todo: Predict Cancer

patient1 = [17.99,
            10.38,
            122.8,
            1001.0,
            0.1184,
            0.2776,
            0.3001,
            0.1471,
            0.2419,
            0.07871,
            1.095,
            0.9053,
            8.589,
            153.4,
            0.006399,
            0.04904,
            0.05373,
            0.01587,
            0.03003,
            0.006193,
            25.38,
            17.33,
            184.6,
            2019.0,
            0.1622,
            0.6656,
            0.7119,
            0.2654,
            0.4601,
            0.1189]
# todo: converting data into 2D array
patient1 = np.array([patient1])
print(patient1)

pred = classifier.predict(patient1)
print(pred)

print(data.target_names)

if pred[0] == 0:
    print('Patient has Cancer (malignant tumor)')
else:
    print('Patient has no Cancer (malignant benign)')
