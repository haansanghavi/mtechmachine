import numpy as np
import pydot as pd
from sklearn import datasets,metrics
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals.six import StringIO

iris  = datasets.load_iris()

trainingset  = iris.data[list(range(0,150,2)), :]
trainingsettarget  = iris.target[list(range(0,150,2))]

testset  = iris.data[list(range(1,150,2)), :]
testsettarget  = iris.target[list(range(1,150,2))]

clf  = DecisionTreeClassifier(criterion="gini")
clf.fit(trainingset,testsettarget)
predictions  = clf.predict(testset)

print("Accuarcy : {0}".format(metrics.accuracy_score(testsettarget,predictions,normalize="True")))

print(metrics.classification_report(testsettarget,predictions))
print(metrics.confusion_matrix(testsettarget,predictions))

  
