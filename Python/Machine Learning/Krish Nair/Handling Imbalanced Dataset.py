# todo: Handling Imbalanced Dataset with Machine Learning

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import KFold, GridSearchCV, train_test_split
from sklearn.ensemble import RandomForestClassifier
from collections import Counter
from imblearn.under_sampling import NearMiss
from imblearn.over_sampling import RandomOverSampler
from imblearn.combine import SMOTETomek
from imblearn.ensemble import EasyEnsembleClassifier

df = pd.read_csv('creditcard.csv')
df.head()

print(df.shape)

df['Class'].value_counts()

# todo: Independent and Dependent Features
X = df.drop("Class", axis=1)
y = df.Class

# todo: Cross Validation Like KFOLD and Hyperpaqrameter Tuning

10.0 ** np.arange(-2, 3)

log_class = LogisticRegression()
grid = {'C': 10.0 ** np.arange(-2, 3), 'penalty': ['l1', 'l2']}
cv = KFold(n_splits=5, random_state=None, shuffle=False)

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7)

clf = GridSearchCV(log_class, grid, cv=cv, n_jobs=-1, scoring='f1_macro')
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

print(347 * 100)

y_train.value_counts()

class_weight = dict({0: 1, 1: 100})

classifier = RandomForestClassifier(class_weight=class_weight)
classifier.fit(X_train, y_train)

# y_pred=classifier.predict(X_test)
# print(confusion_matrix(y_test,y_pred))
# print(accuracy_score(y_test,y_pred))
# print(classification_report(y_test,y_pred))

y_pred = classifier.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# todo: Under Sampling

Counter(y_train)

ns = NearMiss(0.8)
X_train_ns, y_train_ns = ns.fit_sample(X_train, y_train)
print("The number of classes before fit {}".format(Counter(y_train)))
print("The number of classes after fit {}".format(Counter(y_train_ns)))

classifier = RandomForestClassifier()
classifier.fit(X_train_ns, y_train_ns)

y_pred = classifier.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# todo: Over Sampling

os = RandomOverSampler(0.75)
X_train_ns, y_train_ns = os.fit_sample(X_train, y_train)
print("The number of classes before fit {}".format(Counter(y_train)))
print("The number of classes after fit {}".format(Counter(y_train_ns)))

classifier = RandomForestClassifier()
classifier.fit(X_train_ns, y_train_ns)

y_pred = classifier.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# todo: SMOTETomek

os = SMOTETomek(0.75)
X_train_ns, y_train_ns = os.fit_sample(X_train, y_train)
print("The number of classes before fit {}".format(Counter(y_train)))
print("The number of classes after fit {}".format(Counter(y_train_ns)))

classifier = RandomForestClassifier()
classifier.fit(X_train_ns, y_train_ns)

y_pred = classifier.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# todo: Ensemble Techniques

easy = EasyEnsembleClassifier()
easy.fit(X_train, y_train)

print(easy)

y_pred = easy.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
