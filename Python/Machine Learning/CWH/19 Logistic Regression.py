"""import numpy as np
import bunch
b = bunch.Bunch()          # creating machine learning data for train and test data
b.target = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])   # setting data at various attribute
print(b.target)
b.target_names = np.array(['setosa', 'versicolor', 'virginica'])     # setting data at target name in nd array
print(b.target_names)"""

from sklearn import datasets
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
iris = datasets.load_iris()
x = iris['data'][:, 3:]          # getting data for all row and 3rd column from ndarray
# y = (iris['target'] == 2)        # if iris target value is 2 then gives true
y = (iris['target'] == 2).astype(np.int)    # convert true false values in 1 or 0 number
# print(y)
# print(iris['data'])
# print(x)

# train a logistic regression
clf = LogisticRegression()
clf.fit(x, y)
example = clf.predict(([[2.6]]))      # prediction for example 2.6 test value
print(example)

# Using matplotlib to visualization
x_new = np.linspace(0, 3, 1000).reshape(-1, 1)  # getting 1000 random values between 0 to 3 in 2D array
y_prob = clf.predict_proba(x_new)
print(y_prob)                            # predicting values for test values x_new
plt.plot(x_new, y_prob[:, 1], "g-", label="verginica")
plt.show()
