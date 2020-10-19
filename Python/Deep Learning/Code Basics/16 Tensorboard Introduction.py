#!/usr/bin/env python
# coding: utf-8

# <h2 style="color:blue" align="center">Tensorboard demo using handwritten digits classification using neural network</h2>

# In this notebook we will classify handwritten digits using a simple neural network which has only input and output layers. We will than add a hidden layer and see how the performance of the model improves

# In[1]:


import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np


# In[2]:


(X_train, y_train) , (X_test, y_test) = keras.datasets.mnist.load_data()


# In[3]:


len(X_train)


# In[4]:


len(X_test)


# In[5]:


X_train[0].shape


# In[6]:


plt.matshow(X_train[0])


# In[7]:


y_train[0]


# In[8]:


X_train = X_train / 255
X_test = X_test / 255


# In[9]:


X_train_flattened = X_train.reshape(len(X_train), 28*28)
X_test_flattened = X_test.reshape(len(X_test), 28*28)


# In[10]:


X_train_flattened.shape


# <h3 style='color:purple'>Using Flatten layer so that we don't have to call .reshape on input dataset</h3>

# In[12]:


model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(100, activation='relu'),
    keras.layers.Dense(10, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

tb_callback = tf.keras.callbacks.TensorBoard(log_dir="logs/", histogram_freq=1)

model.fit(X_train, y_train, epochs=5, callbacks=[tb_callback])


# In[ ]:


# %load_ext tensorboard
# %tensorboard --logdir logs/fit


# Either run above inline magic or go to git bash or your command prompt and type below to run it,
# `tensorboard --logdir logs/`
# This will launch tensorboard at this url which you can open in your browser `http://localhost:6006/`

# In[17]:


model.get_weights()

