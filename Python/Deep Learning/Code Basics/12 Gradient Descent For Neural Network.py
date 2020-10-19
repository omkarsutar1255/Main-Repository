# todo: Implement Gradient Descent For Neural Network (or Logistic Regression)

# todo: importing libraries
import numpy as np
from tensorflow import keras
import pandas as pd

# todo: load dataSet
df = pd.read_csv("insurance_data.csv")
print("head", df.head())

# todo: Split train and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df[['age', 'affordibility']], df.bought_insurance, test_size=0.2,
                                                    random_state=25)

# todo: PreProcessing: Scale the data so that both age and affordability are in same scaling range
X_train_scaled = X_train.copy()
X_train_scaled['age'] = X_train_scaled['age'] / 100

X_test_scaled = X_test.copy()
X_test_scaled['age'] = X_test_scaled['age'] / 100

# todo: DL model
model = keras.Sequential([
    keras.layers.Dense(1, input_shape=(2,), activation='sigmoid', kernel_initializer='ones', bias_initializer='zeros')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(X_train_scaled, y_train, epochs=5000)

# todo: Evaluate the model on test set
model.evaluate(X_test_scaled, y_test)
print("model predict", model.predict(X_test_scaled))
print("y_test", y_test)

# todo: Now get the value of weights and bias from the model
coef, intercept = model.get_weights()
print("coef, intercept", coef, intercept)
# todo: This means w1=5.060867, w2=1.4086502, bias =-2.9137027


def sigmoid(x):
    import math
    return 1 / (1 + math.exp(-x))


print("sigmoid(18)", sigmoid(18))
print("X_test", X_test)


# todo: Instead of model.predict, write our own prediction function that uses w1,w2 and bias
def prediction_function(age, affordibility):
    weighted_sum = coef[0] * age + coef[1] * affordibility + intercept
    return sigmoid(weighted_sum)


print(".47, 1", prediction_function(.47, 1))
print(".18, 1", prediction_function(.18, 1))


def sigmoid_numpy(x):
    return 1 / (1 + np.exp(-x))


print("sigmoid_numpy", sigmoid_numpy(np.array([12, 0, 1])))


def log_loss(y_true, y_predicted):
    epsilon = 1e-15
    y_predicted_new = [max(i, epsilon) for i in y_predicted]
    y_predicted_new = [min(i, 1 - epsilon) for i in y_predicted_new]
    y_predicted_new = np.array(y_predicted_new)
    return -np.mean(y_true * np.log(y_predicted_new) + (1 - y_true) * np.log(1 - y_predicted_new))


def gradient_descent(age, affordability, y_true, epochs, loss_thresold):
    w1 = w2 = 1
    bias = 0
    rate = 0.5
    n = len(age)
    for i in range(epochs):
        weighted_sum = w1 * age + w2 * affordability + bias
        y_predicted = sigmoid_numpy(weighted_sum)
        loss = log_loss(y_true, y_predicted)
        w1d = (1 / n) * np.dot(np.transpose(age), (y_predicted - y_true))
        w2d = (1 / n) * np.dot(np.transpose(affordability), (y_predicted - y_true))
        bias_d = np.mean(y_predicted - y_true)
        w1 = w1 - rate * w1d
        w2 = w2 - rate * w2d
        bias = bias - rate * bias_d
        print(f'Epoch:{i}, w1:{w1}, w2:{w2}, bias:{bias}, loss:{loss}')
        if loss <= loss_thresold:
            break
    return w1, w2, bias


print("w1, w2, bias", gradient_descent(X_train_scaled['age'], X_train_scaled['affordibility'], y_train, 1000, 0.4631))
print("coef, intercept", coef, intercept)
