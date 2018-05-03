import numpy
from sklearn import datasets, metrics, svm
from sklearn.neural_network import MLPClassifier

data_iris = datasets.load_iris()
train_set = data_iris.data[list(range(0, 150, 2)), :]
train_target_set = data_iris.target[list(range(0, 150, 2))]
test_set = data_iris.data[list(range(1, 150, 2)), :]
test_target_set = data_iris.target[list(range(1, 150, 2))]


clf = MLPClassifier(solver="adam",activation='logistic',alpha=0.0001,learning_rate='constant', learning_rate_init=0.001,hidden_layer_sizes=(65), random_state= 1,max_iter= 1000  )
clf.get_params()
clf.fit(train_set, train_target_set)
predictions = clf.predict(test_set)

print("Accuracy : {0}".format(metrics.accuracy_score(test_target_set, predictions, normalize=True)))    #printing accuracy..
print(metrics.classification_report(test_target_set, predictions))                                      #printing report..
print(metrics.confusion_matrix(test_target_set, predictions))                                           #printing confusion matrix..

print(clf.predict_proba(test_set))