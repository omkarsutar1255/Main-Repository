# todo: Logistic Regression: Multiclass Classification

# todo: Import Libraries
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

# todo: Load DataSet
digits = load_digits()

for i in range(5):
    plt.matshow(digits.images[i], cmap='gray')
    plt.show()
    print(digits.target[i])

# todo: type of data in DataSet of Digit
print(dir(digits))
print(digits.data[0])

# todo: splitting into train and test dataSet
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2)
print(len(X_train), len(X_test), len(y_train), len(y_test))

# todo: Create and train logistic regression model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

# todo: Measure accuracy of our model
print(model.score(X_test, y_test))

# todo: prediction of first 5 digits
print(model.predict(digits.data[0:5]))
y_predicted = model.predict(X_test)

# todo: Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_predicted)
print(cm)

# todo: Plotting graph of accuracy of Model
import seaborn as sn
plt.figure(figsize=(10, 7))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.show()
