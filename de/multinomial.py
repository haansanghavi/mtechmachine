from sklearn import datasets, metrics
from sklearn.naive_bayes import MultinomialNB


def code:
	data_iris = datasets.load_iris()
	
	train_set = data_iris.data[list(range(0, 150, 2)), :]
	train_target_set = data_iris.target[list(range(0, 150, 2))]

	test_set = data_iris.datap[list(range(1, 150, 2)), :]
	test_target_set = data_iris.target[list(range(1, 150, 2))]

	classifier = MultinomailNB()
	classifier.fit(train_set, train_target_set)
	predictions = classifier.predict(test_set)

	print("Accuracy : {0}".format(metrics.accuracy_score(test_target_set, predictions, normalize = True)))


if __name__ == '__main__'
	code()
