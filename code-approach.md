# The Coding Approach

Please note that, if you are a first timer, it will not be easy to grasp all the concepts in one go. I strongly recommend that you go through the following steps to understand what is actually happening inside the code, before you actually go and run it by yourself. 

As a rule of thumb, before we actually start coding, we need to have a clear idea of what we are going to actually do to train our model. Here are the steps we actually be performing in our code:

#### 1.	Load the iris Dataset

#### 2.	Grab the features in X variable

Note: The capital X is used to denote the features normally as standard, but if you want, you can use different naming conventions. Also, the features here refer to the four values which are contained in the dataset (i.e. sepal length, sepal width, petal length, petal width)

#### 3.	Grab the Labels in y variable

Note: the small y is a standard variable which points to the classes in our example (as we know that there are 3 classes in this dataset and each class has more or less 50 records)

#### 4.	Convert the y into (1 constant structure) which is a format understandable to the Model
i.e. the structure is [0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2] and after converting it to (1-constant structure, it will look like the following:
```
[
[1. 0. 0.] #this is for 0, denoting the index position as 0 for class 0

[0. 1. 0.] #this is for 1, denoting the index position as 1 for class 1

[0. 0. 1.] #this is for 1, denoting the index position as 2 for class 2
]
```

#### 5.	Split the data into X_train, X_test, y_train, y_test

We need to split the data so that we can train our model on training data (X_train) and then test our prediction later on (X_test) while the (y_test) is the correct values, which will be able to do the scoring of our prediction, and measuring it.

#### 6.	 Convert the data of X_train and y_train into the 0 and 1 format, instead of actual measurements as this is what the model wants in order to learn and run effectively, so we will transform the data through the Scaler object (will be shown in the code)

#### 7.	Start building the neural network using Keras

#### 8.	Add Two input classes 

Here we specify, how many neurons we are going to use and what activation function will be performed by the neurons as well as how many input dimensions (i.e. the four values contained in X_train or X_test, which are four) will be passed to it

#### 9.	Add an output class 

Specify the Activation function and number of neurons

#### 10.	Compile the model

#### 11.	Once the model is read and compiled, it is time to fit the training data into it, 

In this case, we’ve the data which we prepared/extracted from the iris dataset earlier in Step#5 
which is converted X_train data (Step#6) and y_train (Step#5)

#### 12.	Time to Predict, because out Model is now trained.

Note that we used training data to train our model, and now if we are going to predict then we will not pass the training data, instead, we will pass the Test Data (X_test)

#### 13.	Check the Accuracy of Prediction. We can check the accuracy of our Model’s prediction by using the following three classes provided by Scikit-Learn.

o	Print the Confusion Matrix (you need to pass the prediction & y_test)
o	Print the Classification Report (you need to pass the prediction & y_test)
o	Print the Accuracy Score (you need to pass the prediction & y_test)

Note: We are passing y_test is because this is the standard against which our model’s accuracy will be checked.

#### 14.	Print the results

- [Main Page](README.md)
- [The Code](source/iris-keras.py)
