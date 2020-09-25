# loading required module
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

# load iris dataset
iris = datasets.load_iris()

# print(iris.DESCR)        # getting description of dataset
features = iris.data
labels = iris.target
print(features[0], labels[0])      # lebel[0]=0 hence take values of 0 from description

# Training the classifier
clf = KNeighborsClassifier()
clf.fit(features, labels)

preds = clf.predict([[9.1, 9.5, 9.4, 0.2]])    # it takes 2D array
print(preds)                                   # printing prediction
