import numpy as np
from sklearn import datasets,metrics
from sklearn.naive_bayes import BernoulliNB

iris  = datasets.load_iris()

trainingset  = iris.data[list(range(0,100,2)), :]
trainingsettarget  = iris.target[list(range(0,100,2))]

testset  = iris.data[list(range(1,100,2)), :]
testsettarget  = iris.target[list(range(1,100,2))]

clf = BernoulliNB()
clf.fit(trainingset,trainingsettarget)
predictions  = clf.predict(testset)

#print('\n#############\n')
print(predictions)
#print('\n#############\n')
      
print("Accuracy  = {0}".format(metrics.accuracy_score(testsettarget,predictions,normalize = True)))
