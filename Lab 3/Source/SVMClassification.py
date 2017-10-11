import numpy as np
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import metrics


# Splitting the test and training data
digits = datasets.load_digits()
x = digits.data[:, :2]
y = digits.target
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2)



#  Code that finds accuracy of the data using linear kernel
linearKernel = svm.SVC()

linearPrediction = linearKernel.set_params(kernel='linear').fit(xtrain, ytrain).predict(xtest)

linearAccuracy = metrics.accuracy_score(ytest, linearPrediction)

print ("Linear Kernel Accuracy:", linearAccuracy)


# Code that finds accuracy of data using rbf kernel

rbfKernel = svm.SVC()

rbfPrediction = rbfKernel.set_params(kernel='rbf').fit(xtrain, ytrain).predict(xtest)

rbfAccuracy = metrics.accuracy_score(ytest, rbfPrediction)

print ("RBF Kernel Accuracy:", rbfAccuracy)
