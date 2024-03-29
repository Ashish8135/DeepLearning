# -*- coding: utf-8 -*-
"""2D CNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wgwd8vkCc2qb6gIkUDAqB6X1uTF8DOIi
"""

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten,Dense,Conv2D,MaxPool2D,Dropout
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import cifar10

print(tf.__version__)

(x_train,y_train),(x_test,y_test)=cifar10.load_data()

class_names=['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']

x_train.max()

x_train=x_train/255
x_test=x_test/255

x_train

x_test

x_train.shape

x_test.shape

plt.imshow(x_test[0])

y_test

"""# Build CNN Model"""

model=Sequential()

model.add(Conv2D(filters=32,kernel_size=(3,3),padding='same',activation='relu',input_shape=[32,32,3]))

model.add(Conv2D(filters=32,kernel_size=(3,3),padding='same',activation='relu'))
model.add(MaxPool2D(pool_size=(2,2),strides=2,padding='Valid'))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(units=128,activation='relu'))
model.add(Dense(units=10,activation='softmax'))

model.summary()

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['sparse_categorical_accuracy'])

history=model.fit(x_train,y_train,batch_size=10,epochs=10,verbose=1,validation_data=(x_test,y_test))

#Plot training and validation accuracy values
  epoch_range=range(1,11)
  plt.plot(epoch_range,history.history['sparse_categorical_accuracy'])
  plt.plot(epoch_range,history.history['val_sparse_categorical_accuracy'])
  plt.title('Model_Accuracy')
  plt.ylabel('Accuracy')
  plt.xlabel('Epoch')
  plt.legend(['Train','acuuracy'],loc='upper_left')
  plt.show()


  # plot training and validationn loss values


  plt.plot(epoch_range,history.history['loss'])
  plt.plot(epoch_range,history.history['val_loss'])
  plt.title('Model_loss')
  plt.ylabel('loss')
  plt.xlabel('Epoch')
  plt.legend(['Train','Val'],loc='upper_left')
  plt.show()

from mlxtend.plotting import plot_confusion_matrix
from sklearn.metrics import confusion_matrix

y_pred=model.predict_classes(x_test)

y_pred

y_test



