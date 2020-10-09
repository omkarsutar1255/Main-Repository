# Todo: Artificial Neural Network

# todo: Part 1 - Data Preprocessing

# todo: Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# todo: Importing the Keras libraries and packages
import tensorflow
from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.metrics import confusion_matrix, accuracy_score

# todo: Importing the dataset
dataset = pd.read_csv('Churn_Modelling.csv')

# todo: splitting features and label from dataset
X = dataset.iloc[:, 3:13]
y = dataset.iloc[:, 13]

# todo: Create dummy variables
geography = pd.get_dummies(X["Geography"], drop_first=True)
gender = pd.get_dummies(X['Gender'], drop_first=True)

# todo: Concatenate the Data Frames
X = pd.concat([X, geography, gender], axis=1)

# todo: Drop Unnecessary columns
X = X.drop(['Geography', 'Gender'], axis=1)

# todo: Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# todo: Feature Scaling
# if features and weights are large then it takes time for mathematical process hence feature engineering helps to
# reduce numbers and this boost speed of neural network
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# todo: Part 2 - Now let's make the ANN!

# todo: Initialising the ANN
# 1)creates empty neural network
classifier = Sequential()
# 2)Adding the input layer and the first hidden layer
classifier.add(Dense(10, kernel_initializer='he_normal', activation='relu', input_dim=11))
classifier.add(Dropout(0.3))
# 2)Adding the second hidden layer
classifier.add(Dense(20, kernel_initializer='he_normal', activation='relu'))
classifier.add(Dropout(0.4))
# 2)Adding the third hidden layer
classifier.add(Dense(15, kernel_initializer='he_normal', activation='relu'))
classifier.add(Dropout(0.3))
# 2)Adding the output layer
classifier.add(Dense(1, kernel_initializer='glorot_uniform', activation='sigmoid'))

# 3)Compiling the ANN
classifier.compile(optimizer='Adamax', loss='binary_crossentropy', metrics=['accuracy'])
# 4)Fitting the ANN to the Training set
model_history = classifier.fit(X_train, y_train, validation_split=0.33, batch_size=10, epochs=100)

# list all data in history
print(model_history.history.keys())

# summarize history for accuracy
# plt.plot(model_history.history['acc'])
# plt.plot(model_history.history['val_acc'])
# plt.title('model accuracy')
# plt.ylabel('accuracy')
# plt.xlabel('epoch')
# plt.legend(['train', 'test'], loc='upper left')
# plt.show()
#
# # summarize history for loss
# plt.plot(model_history.history['loss'])
# plt.plot(model_history.history['val_loss'])
# plt.title('model loss')
# plt.ylabel('loss')
# plt.xlabel('epoch')
# plt.legend(['train', 'test'], loc='upper left')
# plt.show()

# todo: Part 3 - Making the predictions and evaluating the model

# todo: 1)Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

# todo: 2)Making the Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

# todo: 2)Calculate the Accuracy
score = accuracy_score(y_pred, y_test)
print(score)
