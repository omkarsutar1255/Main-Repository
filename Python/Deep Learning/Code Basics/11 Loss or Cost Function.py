import numpy as np

y_predicted = np.array([1, 1, 0, 0, 1])
y_true = np.array([0.30, 0.7, 1, 0, 0.5])


def mae(y_predicted, y_true):
    total_error = 0
    for yp, yt in zip(y_predicted, y_true):
        total_error += abs(yp - yt)
    print("Total error is:", total_error)
    mae = total_error / len(y_predicted)
    print("Mean absolute error is:", mae)
    return mae


mae(y_predicted, y_true)

# todo: Implement same thing using numpy in much easier way
print("np abs", np.abs(y_predicted - y_true))
print("np mean", np.mean(np.abs(y_predicted - y_true)))


def mae_np(y_predicted, y_true):
    return np.mean(np.abs(y_predicted - y_true))


print("np mean by", mae_np(y_predicted, y_true))

# todo: Implement Log Loss or Binary Cross Entropy
print("np log[0]", np.log([0]))
epsilon = 1e-15
print("np.log[1e-15]", np.log([1e-15]))
print("y_predicted", y_predicted)

y_predicted_new = [max(i, epsilon) for i in y_predicted]
print("y_predicted_new", y_predicted_new)

print("1 - epsilon", 1 - epsilon)
y_predicted_new = [min(i, 1 - epsilon) for i in y_predicted_new]
print("y_predicted_new", y_predicted_new)
y_predicted_new = np.array(y_predicted_new)
print("np.log(y_predicted_new)", np.log(y_predicted_new))

print("long line", -np.mean(y_true * np.log(y_predicted_new) + (1 - y_true) * np.log(1 - y_predicted_new)))


def log_loss(y_true, y_predicted):
    y_predicted_new = [max(i, epsilon) for i in y_predicted]
    y_predicted_new = [min(i, 1 - epsilon) for i in y_predicted_new]
    y_predicted_new = np.array(y_predicted_new)
    return -np.mean(y_true * np.log(y_predicted_new) + (1 - y_true) * np.log(1 - y_predicted_new))


print("last line", log_loss(y_true, y_predicted))
