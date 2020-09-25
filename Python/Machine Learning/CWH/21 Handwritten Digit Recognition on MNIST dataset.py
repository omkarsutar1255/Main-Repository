# todo : logistic regression classifier
# todo : importing handwriting data
from sklearn.datasets import load_digits
mnist = load_digits()   # loading data to mnist variable
print("load_data", mnist)

# todo : Setting data and targets as features and labels
x, y = mnist['data'], mnist['target']
print(x)
print(y)
print(x.shape)
print(y.shape)
import matplotlib
import matplotlib.pyplot as plt
some_digit = x[900]      # getting some number from x feature
print('some_digit = ', some_digit)
# todo : Reshaping features array to 8x8 square array to plot
some_digit_image = some_digit.reshape(8, 8)
plt.imshow(some_digit_image, cmap=matplotlib.cm.binary, interpolation="nearest")
plt.axis("off")            # disable axis of matplotlib
# plt.show()               # image of some_digit in matplotlib
# print(y[900])            # actual digit
# todo : splitting data into train and test data
x_train, x_test = x[:1500], x[1500:]
y_train, y_test = y[:1500], y[1500:]
print("after split into feature to train", x_train)
print("after split into label to train", y_train)
print("after split into feature to test", x_test)
print("after split into label to check score", y_test)
import numpy as np
shuffle_index = np.random.permutation(1500)  # change order of 1500 training dataset
print("shuffle index", shuffle_index)
x_train, y_train = x_train[shuffle_index], y_train[shuffle_index]  # shuffed for both feature and label of training set
print("x_train data after shuffle :", x_train)
print("y_train data after shuffle :", y_train)

# todo : creating a 4 detector
# y_train = (y_train == 2)  # checking where 2 in labels of train set
# print(y_train)

y_train = y_train.astype(np.int8)     # convert string number into integer
y_test = y_test.astype(np.int8)
print("y_train before == 4", y_train)
print("y_test before == 4", y_test)
y_train_2 = (y_train == 4)      # returns a true false list for 4 number on train label
y_test_2 = (y_test == 4)        # returns a true false list for 4 number of test label
print("printing y_train==4 :", y_train_2)
print("printing y_test==4 :", y_train_2)

# todo : creating algorithm that gives true for 4 and false for other digit
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(tol=0.1, solver='lbfgs')
clf.fit(x_train, y_train_2)         # without y_train_2 for training it returns number
# with y_train_2 it predict for only one number
digit4 = clf.predict([some_digit])
print(digit4)

# todo : cross validation of ml model
from sklearn.model_selection import cross_val_score
crvl = cross_val_score(clf, x_train, y_train_2, cv=3, scoring='accuracy')
print(crvl.mean())      # mean of error
print(crvl.std())       # spread of error from mean
