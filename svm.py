
from sklearn import datasets, metrics, svm



data_iris = datasets.load_iris()
trainingset = data_iris.data[list(range(0, 150, 2)), :]
trainingsettarget = data_iris.target[list(range(0, 150, 2))]
testset = data_iris.data[list(range(1, 150, 2)), :]
testsettarget = data_iris.target[list(range(1, 150, 2))]

classifier = svm.LinearSVC()
classifier.fit(trainingset, trainingsettarget)
predictions = classifier.predict(testset)

print(predictions)
print("Accuracy : {0}".format(metrics.accuracy_score(testsettarget, predictions, normalize=True)))

