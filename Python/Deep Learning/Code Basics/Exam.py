import keras
from keras.models import Sequential
from keras.layers import Flatten, Dense, Activation
from tensorflow import keras

print(keras.backend.backend())

model = Sequential()
model.add(Flatten(input_shape=[28, 28]))
model.add(Dense(100, activation="relu"))
model.add(Dense(10, activation="softmax"))

model = keras.Sequential([
    keras.layers.Dense(10, input_shape=(784, ), activation="sigmoid")
])
