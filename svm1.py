import numpy as np
from sklearn import datasets,metrics
from sklearn import svm
from sklearn.model_selection import cross_val_score

#load data
data_iris = datasets.load_iris()

#divide into training and testing 
training = data_iris.data[list(range(0, 150)), :]
test = data_iris.target[list(range(0, 150))]


#classifing using support vector classification
classifier = svm.LinearSVC()
k = int(input("Enter K value:\n"))  #value of k for cross-validation
acc = cross_val_score(classifier, training,test, cv=k) #returns output list of accuracy scores


print(acc)
print("Accuracy : %0.2f" % (acc.mean()))

