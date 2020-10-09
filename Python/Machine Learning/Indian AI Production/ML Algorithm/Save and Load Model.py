# todo: Random Forest Classification

# todo: import libraries
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

# todo: Split Data into Features and Label
X = df.iloc[:, 0:-1]
y = df.iloc[:, -1]

# todo: Splitting data into Train and test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2020)
print('Shape of X_train = ', X_train.shape)
print('Shape of y_train = ', y_train.shape)
print('Shape of X_test = ', X_test.shape)
print('Shape of y_test = ', y_test.shape)

# todo: Train Random Forest Classification Model
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=100, criterion='gini')
classifier.fit(X_train, y_train)
print(classifier.score(X_test, y_test))

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

# todo: converting list into 2D array
patient1 = np.array([patient1])
print(patient1)

# todo: prediction of model
print(classifier.predict(patient1))
print(data.target_names)

pred = classifier.predict(patient1)
if pred[0] == 0:
    print('Patient has Cancer (malignant tumor)')
else:
    print('Patient has no Cancer (malignant benign)')

# todo: Save Model

# todo: Save Model using Pickle
import pickle
pickle.dump(classifier, open('model_save', 'wb'))
model = pickle.load(open('model_save', 'rb'))
print(model.predict(patient1)[0])

# todo: Save Model using Joblib
import joblib
joblib.dump(classifier, 'model_save2')
model2 = joblib.load('model_save2')
model2.predict(patient1)
