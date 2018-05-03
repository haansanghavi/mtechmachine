#gaussian naive bayes
import numpy as np
from sklearn import datasets,metrics
from sklearn.naive_bayes import GaussianNB

#loading iris datsets from skelearn.datsets
iris  = datasets.load_iris()

#dividing into training and target sets
trainingset  = iris.data[list(range(0,150,2)), :]
trainingsettarget  = iris.target[list(range(0,150,2))]

testset  = iris.data[list(range(1,150,2)), :]
testsettarget  = iris.target[list(range(1,150,2))]


clf = GaussianNB()         
clf.fit(trainingset,trainingsettarget)  
predictions  = clf.predict(testset)

#print('\n#############\n')
print(predictions)
#print('\n#############\n')
      
print("Accuracy  = {0}".format(metrics.accuracy_score(testsettarget,predictions,normalize = True)))

      