# -*- coding: utf-8 -*-
"""FashionMNIST.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pqDO39H5p_t1j6hrdOMawyGk5W5JYfdS
"""

#Tensorflow is a framework of deep learning and machine learning.
# TensorFlow makes it easy for beginners and experts to create machine learning models for desktop, mobile, web, and cloud. 
# Tensorflow architecture works in three parts
# 1.Preprocessing the data
# 2.Build the model
# 3.train and estimate the model

!pip install tensorflow
!pip install keras
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

!pip install mlxtend

fashion_data=keras.datasets.fashion_mnist

type(fashion_data)

(x_train,y_train),(x_test,y_test)=fashion_data.load_data()

x_train.shape

y_train.shape

np.mean(x_train)

np.max(x_train)

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

#data Exploration
x_test.shape

x_train.shape

# Visualization of the  fashion data
plt.figure()
plt.imshow(x_train[0])
plt.colorbar()

y_train

x_train=x_train/255

x_test=x_test/255



# Visualization of the  fashion data
plt.figure()
plt.imshow(x_train[0])
plt.colorbar()

# Build the model
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten,Dense

model=Sequential()
model.add(Flatten(input_shape=(28,28)))
model.add(Dense(128,activation='relu'))
model.add(Dense(10,activation='softmax'))

model.summary()

#Model Compilation contains Three Properties
# 1.Loss Function
# 2.Optimizer
# 3.Metrics
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

history=model.fit(x_train,y_train,epochs=10,batch_size=10,validation_split=0.2)

# Evaluate Accuracy
test_loss,test_acc=model.evaluate(x_test,y_test)

print(test_acc)

# make prediction
from sklearn.metrics import accuracy_score

y_pred=model.predict_classes(x_test)

accuracy_score(y_test,y_pred)

pred=model.predict(x_test)

pred

np.argmax(pred[0])

help(model)

history.history

plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model_accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epochs')
plt.legend(['Train','Val'],loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model_loss')
plt.ylabel('Loss')
plt.xlabel('Epochs')
plt.legend(['Train','Val'],loc='upper left')
plt.show()

# overfitting :if accuracy is more than validation accuracy then model is overfitted.here in this chart we see that modelis overfitted.



"""Plotting Confusion Matrix"""

from mlxtend.plotting import plot_confusion_matrix
from sklearn.metrics import confusion_matrix

font={
    'family':'Times New Roman',
    'weight':'normal',
    'size':16
}
plt.rc('font',**font)
mat=confusion_matrix(y_test,y_pred)
fig,ax=plot_confusion_matrix(conf_mat=mat,figsize=(10,10),show_normed=True)
plt.tight_layout()
fig.savefig('fashion.png')

