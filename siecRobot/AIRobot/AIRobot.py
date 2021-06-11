from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, BatchNormalization, Dense, Activation, Flatten
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import SparseCategoricalCrossentropy
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import os
import cv2
import math


path='C:\\Users\\magdz\\database\\test'


train= ImageDataGenerator(rescale=1/255)
validation=ImageDataGenerator(rescale=1/255)
train_dataset = train.flow_from_directory('C:\\Users\\magdz\\database\\test', target_size=(200,200), batch_size=50)
validation_dataset=validation.flow_from_directory('C:\\Users\\magdz\\database\\validation', target_size=(200,200), batch_size=50)
test = ImageDataGenerator(rescale=1/255)
test_dataset = test.flow_from_directory('C:\\Users\\magdz\\database\\test',target_size=(200,200))

model=Sequential(name="Robot")

#1 
model.add(Conv2D(16, kernel_size=(7,7), strides=(3,3),activation='elu', padding='same', input_shape=(200,200,3)))
model.add(BatchNormalization())

#2
model.add(MaxPooling2D(pool_size=(3,3), strides=(1,1)))

#3
model.add(Conv2D(32, strides=(1,1), kernel_size=(3,3), activation='elu'))
model.add(BatchNormalization())

#4
model.add(MaxPooling2D(pool_size=(2,2), strides=(1,1)))

#5
model.add(Conv2D(32, strides=(1,1), kernel_size=(3,3), activation='elu'))
model.add(BatchNormalization())

#6
model.add(MaxPooling2D(pool_size=(2,2), strides=(1,1)))

#7
model.add(Conv2D(16, strides=(1,1), kernel_size=(3,3), activation='elu'))
model.add(BatchNormalization())

#8
model.add(MaxPooling2D(pool_size=(2,2), strides=(1,1)))
model.add(Flatten())
#9
#model.add(Dense(512, activation='relu'))
model.add(Dense(4,activation='softmax'))


model.summary()
epochs=15
compute_steps_per_epoch=lambda x: int(math.ceil(1. * x / 50))
steps_per_epoch=compute_steps_per_epoch(16000)
validation_steps=compute_steps_per_epoch(8000)

model.compile(optimizer=Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(train_dataset,steps_per_epoch=steps_per_epoch, epochs=26,validation_data=validation_dataset,validation_steps=validation_steps)

model.save('C:\\Users\\magdz\\database')

result=model.evaluate(test_dataset)
print(result)
dict(zip(model.metrics_names,result))





