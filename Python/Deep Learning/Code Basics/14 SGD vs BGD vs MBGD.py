# todo: Implementation of stochastic and batch grandient descent in python

# todo:  We will use very simple home prices data set to implement batch and stochastic gradient descent in python.
#  Batch gradient descent uses *all* training samples in forward pass to calculate cumulitive error and than we adjust weights using derivaties.
#  In stochastic GD, we randomly pick *one* training sample, perform forward pass, compute the error and immidiately adjust weights.
#  So the key difference here is that to adjust weights batch GD will use *all* training samples where as stochastic GD will use one randomly picked training sample

# todo: Import libraries
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# todo:  Load the dataset in pandas dataframe
df = pd.read_csv("homeprices_banglore.csv")
df.sample(5)

# todo: Preprocessing/Scaling: Since our columns are on different sacle it is important to perform scaling on them
from sklearn import preprocessing
sx = preprocessing.MinMaxScaler()
sy = preprocessing.MinMaxScaler()
scaled_X = sx.fit_transform(df.drop('price', axis='columns'))
scaled_y = sy.fit_transform(df['price'].values.reshape(df.shape[0], 1))
print(scaled_X)
print(scaled_y)

# todo: We should convert target column (i.e. price) into one dimensional array.
#  It has become 2D due to scaling that we did above but now we should change to 1D
scaled_y.reshape(20, )


# todo: Gradient descent allows you to find weights (w1,w2,w3) and bias in following linear equation
# todo: Now is the time to implement mini batch gradient descent.
def batch_gradient_descent(X, y_true, epochs, learning_rate=0.01):
    number_of_features = X.shape[1]
    # numpy array with 1 row and columns equal to number of features. In 
    # our case number_of_features = 2 (area, bedroom)
    w = np.ones(shape=number_of_features)
    b = 0
    total_samples = X.shape[0]  # number of rows in X

    cost_list = []
    epoch_list = []

    for i in range(epochs):
        y_predicted = np.dot(w, X.T) + b

        w_grad = -(2 / total_samples) * (X.T.dot(y_true - y_predicted))
        b_grad = -(2 / total_samples) * np.sum(y_true - y_predicted)

        w = w - learning_rate * w_grad
        b = b - learning_rate * b_grad

        cost = np.mean(np.square(y_true - y_predicted))  # MSE (Mean Squared Error)

        if i % 10 == 0:
            cost_list.append(cost)
            epoch_list.append(i)

    return w, b, cost, cost_list, epoch_list


w, b, cost, cost_list, epoch_list = batch_gradient_descent(scaled_X, scaled_y.reshape(scaled_y.shape[0], ), 500)
print(w, b, cost)

# todo:  Check price equation above. In that equation we were trying to find values of w1,w2 and bias.
#  Here we got these values for each of them,
# w1 = 0.66469087
# w2 = 0.60541671
# bias = -0.17792104056392882

# todo: Now plot epoch vs cost graph to see how cost reduces as number of epoch increases
plt.xlabel("epoch")
plt.ylabel("cost")
plt.plot(epoch_list, cost_list)
plt.show()


# todo: Lets do some predictions now.
def predict(area, bedrooms, w, b):
    scaled_X = sx.transform([[area, bedrooms]])[0]
    # here w1 = w[0] , w2 = w[1], w3 = w[2] and bias is b
    # equation for price is w1*area + w2*bedrooms + w3*age + bias
    # scaled_X[0] is area
    # scaled_X[1] is bedrooms
    # scaled_X[2] is age
    scaled_price = w[0] * scaled_X[0] + w[1] * scaled_X[1] + b
    # once we get price prediction we need to to rescal it back to original value
    # also since it returns 2D array, to get single value we need to do value[0][0]
    return sy.inverse_transform([[scaled_price]])[0][0]


print(predict(2600, 4, w, b))
print(predict(1000, 2, w, b))
print(predict(1500, 3, w, b))

# todo: (2) Stochastic Gradient Descent Implementation

# todo: Stochastic GD will use randomly picked single training sample to calculate error and using this error we backpropage to adjust weights
#  we will use random libary to pick random training sample.
import random
random.randint(0, 6)  # randit gives random number between two numbers specified in the argument


def stochastic_gradient_descent(X, y_true, epochs, learning_rate=0.01):
    number_of_features = X.shape[1]
    # numpy array with 1 row and columns equal to number of features. In 
    # our case number_of_features = 3 (area, bedroom and age)
    w = np.ones(shape=number_of_features)
    b = 0
    total_samples = X.shape[0]

    cost_list = []
    epoch_list = []

    for i in range(epochs):
        random_index = random.randint(0, total_samples - 1)  # random index from total samples
        sample_x = X[random_index]
        sample_y = y_true[random_index]

        y_predicted = np.dot(w, sample_x.T) + b

        w_grad = -(2 / total_samples) * (sample_x.T.dot(sample_y - y_predicted))
        b_grad = -(2 / total_samples) * (sample_y - y_predicted)

        w = w - learning_rate * w_grad
        b = b - learning_rate * b_grad

        cost = np.square(sample_y - y_predicted)

        if i % 100 == 0:  # at every 100th iteration record the cost and epoch value
            cost_list.append(cost)
            epoch_list.append(i)

    return w, b, cost, cost_list, epoch_list


w_sgd, b_sgd, cost_sgd, cost_list_sgd, epoch_list_sgd = stochastic_gradient_descent(scaled_X, scaled_y.reshape(scaled_y.shape[0], ), 10000)
print(w_sgd, b_sgd, cost_sgd)

# todo: Compare this with weights and bias that we got using gradient descent. They both of quite similar.
print(w, b)

plt.xlabel("epoch")
plt.ylabel("cost")
plt.plot(epoch_list_sgd, cost_list_sgd)
plt.show()

print(predict(2600, 4, w_sgd, b_sgd))
print(predict(1000, 2, w_sgd, b_sgd))
print(predict(1500, 3, w_sgd, b_sgd))

# todo: Implement mini batch gradient descent in python and plot cost vs epoch graph.
#  Mini batch is intermediate version of batch GD and stochastic GD.
#  In stochastic we used one randomly picked training sample, In mini gradient descent you will use a batch of samples in each iterations.
#  For example if you have total 50 training samples, you can take a batch of 10 samples, calculate cumulitive error for those 10 samples and then adjust weights.
#  In SGD we adjust weights after every one sample. In Batch we adjust weights after going through all samples but in
#  mini batch we do after every m samples (where m is batch size and it is 0 < m < n, where n is total number of samples
# [Solution](https://github.com/codebasics/py/blob/master/DeepLearningML/8_sgd_vs_gd/mini_batch_gd.ipynb)
