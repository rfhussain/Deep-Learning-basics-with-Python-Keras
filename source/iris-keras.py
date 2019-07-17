# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 14:51:56 2019

@author: RAHEEL
"""

import numpy as np
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

#import the built-in iris dataset class
from sklearn.datasets import load_iris

#get the iris dataset 
iris = load_iris()

#get the data into the X (you may call it features)
#a capital X will normally be used as a norm for features to be loaded
X = iris.data 
#a small y will denote the label
#in this case the target corresponds to the class (as you know there are three classes) 
#the class here are represented by 0 or 1 or 2
y = iris.target

#convert y into a 1-constant-encoding system as follows
y = to_categorical(y)
#p = np.array([0,0,0,0,0,1,1,1,2,2,2,3,4,5,5,5,5,5])

#split the label (class) and features (data) into train and test records
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

"""
The X_train and X_test data which may look like the following.

[[6.1 2.8 4.7 1.2]
 [5.7 3.8 1.7 0.3]
 [7.7 2.6 6.9 2.3]
 [6.  2.9 4.5 1.5]
 [6.8 2.8 4.8 1.4]
 [5.4 3.4 1.5 0.4]]

it has values which are both 0 and more than zero. 

but we want both to display values in 0 or 1

for that we will use the class MinMaxScaler
what MinMaxScaler essentially does is that suppose we've an array as follows
[1,4,5,3] so it will divide each member of that array with the biggest value in the array
[1,4,5,3] / 5 = [0.2 0.8 1 0.6]
"""
scaler_object = MinMaxScaler()
scaler_object.fit(X_train)

scaled_X_train = scaler_object.transform(X_train)
scaled_X_test = scaler_object.transform(X_test)


#we will build the network of keras as follows
model  = Sequential()
#passing 8 neurons and 4 input dimensions as sepal length, sepal width, petal length, petal width
#the activation function will be ReLU
model.add(Dense(8,input_dim=4,activation='relu'))  #input layer 1, 
model.add(Dense(8,input_dim=4,activation='relu'))  #input layer 2
#output layer with the activation function called softmax
model.add(Dense(3,activation='softmax')) #output layer
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

#this will return back what each layer is doing, the output shape and number of parameters
#print(model.summary())
#print(type(scaled_X_test))

#fitting the model 
#this is just like scikit.learn model
#one epochs is running through entire training dataset, we will run 150
#verbose is how much output you want information, if it is 0 then it is not reporting back anything
#if it is 1 then it will actually show you like a progress bar, 
#So two it shows you the pockets on how much loss and what its current accuracy is.
model.fit(scaled_X_train, y_train,epochs=200, verbose=2) #try verbose=0 and verbose=1 to better understand it

predictions = model.predict_classes(scaled_X_test)

#print(confusion_matrix(y_test.argmax(axis=1),predictions))
#print (classification_report(y_test.argmax(axis=1),predictions))
print(accuracy_score(y_test.argmax(axis=1),predictions))

model.save('testmodel.h5')


