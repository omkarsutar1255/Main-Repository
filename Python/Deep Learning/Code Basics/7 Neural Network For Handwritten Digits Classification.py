# todo: import DataSet
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

# todo: Splitting data into train test
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

# todo: analysis of data
# print(len(X_train))
# print(len(X_test))
# print(X_train[0].shape)
# print(X_train[0])

# todo: visualization of data
plt.matshow(X_train[1])
# plt.show()
# print(y_train[:5])   # actual values of data

# todo: feature scaling (converting values between 0-1)
X_train = X_train/255
X_test = X_test/255

# todo: Flatten 2D array of train and test data
# print(X_train.shape)
X_train_flattened = X_train.reshape(len(X_train), 28*28)
# print(X_train_Flatten.shape)

# print(X_test.shape)
X_test_flattened = X_test.reshape(len(X_test), 28*28)
# print(X_test_flattened.shape)
# print(X_test_flattened[0])   # all values are flatten in 784

# todo: Creating Neural Network
model = keras.Sequential([
    keras.layers.Dense(10, input_shape=(784,), activation='sigmoid')
    # 10 is output neural network and 784 is input neural network
])

# todo: optimizing neural network to reduce loss
model.compile(optimizer='adam',            # to reach global minima faster
              loss='sparse_categorical_crossentropy',   # way to calculate loss
              metrics=['accuracy'])                  # find accuracy of model regarding given data

# todo: training DL model
model.fit(X_train_flattened, y_train, epochs=5)   # epochs is no. of iteration of train model

# todo: prediction of model
model.evaluate(X_test_flattened, y_test)
y_predicted = model.predict(X_test_flattened)
print(y_predicted[0])     # prediction of 0th features of test data
plt.matshow(X_test[0])    # visualization of 0th feature of test data
plt.show()
print(np.argmax(y_predicted[0]))   # predication by model of 0th values of test data
y_predicted_labels = [np.argmax(i) for i in y_predicted]
print(y_predicted_labels[:5])

# todo: creating Confusion matrix
cm = tf.math.confusion_matrix(labels=y_test, predictions=y_predicted_labels)
print(cm)
import seaborn as sn
plt.figure(figsize=(10, 7))
sn.heatmap(cm, annot=True, fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.show()

# todo: Creating Neural Network
model = keras.Sequential([
    keras.layers.Dense(100, input_shape=(784,), activation='relu'),
    keras.layers.Dense(10, activation='sigmoid')
])

# todo: optimizing neural network to reduce loss
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# todo: training DL model
model.fit(X_train_flattened, y_train, epochs=5)

# todo: prediction of model
model.evaluate(X_test_flattened, y_test)
y_predicted = model.predict(X_test_flattened)
y_predicted_labels = [np.argmax(i) for i in y_predicted]

# todo: creating Confusion matrix
cm = tf.math.confusion_matrix(labels=y_test, predictions=y_predicted_labels)
plt.figure(figsize=(10, 7))
sn.heatmap(cm, annot=True, fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.show()

# todo: Creating Neural Network
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(100, activation='relu'),
    keras.layers.Dense(10, activation='sigmoid')
])

# todo: optimizing neural network to reduce loss
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# todo: training DL model
model.fit(X_train, y_train, epochs=10)
model.evaluate(X_test, y_test)
