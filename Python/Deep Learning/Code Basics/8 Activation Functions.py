import math


# todo: sigmoid Activation Function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))


sigmoid(100)
sigmoid(1)
sigmoid(-56)
sigmoid(0.5)


# todo: tanh Activation Function
def tanh(x):
    return (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))


tanh(-56)
tanh(50)
tanh(1)


# todo: ReLU Activation Function
def relu(x):
    return max(0, x)


relu(-100)
relu(8)


# todo: Leaky ReLU Activation Function
def leaky_relu(x):
    return max(0.1 * x, x)


leaky_relu(-100)
leaky_relu(8)
