import numpy as np
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, Convolution2D, Activation, Dropout,MaxPooling2D

class CNN:
  def init (self):
   model = Sequential ()
# self.model = Sequential()
# self.model.add (Conv2D (64, kernel_size=3, activation='relu', input_shape=(128, 128, 1)))
# self.model.add (Conv2D (32, kernel_size=3, activation='relu'))
# self.model.add(Flatten())
# self.model.add (Dense (1, activation='softmax'))
# self.model.compile (loss='binary_crossentropy',Optimizer='rmsprop',metrics=['accuracy'])
   model.add(Convolution2D(32,kernel_size=3,activation='relu', input_shape=(128, 128, 1)))
# model.add(Activation('relu'))

   model.add (MaxPooling2D(pool_size=(3, 3)))
   model.add(Convolution2D(32,kernel_size=3,activation='relu'))
# model.add(Activation('relu'))
   model.add (MaxPooling2D(pool_size=(3, 3)))
   model.add(Convolution2D(64,kernel_size=3,activation='relu'))
# model.add(Activation('relu'))
   model.add(MaxPooling2D(pool_size=(3, 3)))
   model.add(Flatten())
   model.add(Dense(64))
   model.add(Activation('relu'))
   model.add(Dropout(0.5))
   model.add(Dense(1))
   model.add(Activation('sigmoid'))
   model.compile(loss='binary_crossentropy',optimizer='rmsprop',metrics=['accuracy'])
   self.model = model
def fit(self, images,labels):
  return self.model.fit(images,labels ,epochs=10, batch_size=5)
def predict(self, images):
   probabilities = self.model.predict(images)
   return probabilities