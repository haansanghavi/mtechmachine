import numpy as np
from collections import Counter
import pandas as pd
import os
import PIL.Image
from csv_reader import reader
from accuracy import acc
from file_write import writer


class KNeighborsClassifieR(object):
	def __init__(self):
		pass
	def fit(self, X, y):
		self.X_train = X
		self.y_train = y

	def predict(self, X_test, k=5):
		distances = self.compute_distances(self.X_train, X_test)
		vote_results = []
		for i in range(len(distances)):
			votesOneSample = []
			for j in range(k):
				votesOneSample.append(distances[i][j][1])
			vote_results.append(Counter(votesOneSample).most_common(1)[0][0])
		
		return vote_results
    
	def compute_distances(self, X, X_test):
		distances = []
		for i in range(X_test.shape[0]):
			euclidian_distances = np.zeros(X.shape[0])
			oneSampleList = []
			for j in range(len(X)):
				euclidian_distances[j] = np.sqrt(np.sum(np.square(np.array(X_test[i]) - np.array(X[j]))))
				oneSampleList.append([euclidian_distances[j], self.y_train[j]])
			distances.append(sorted(oneSampleList))
		return distances




def run():
	
	filename="breastCancer.csv"
	delimiter=","

	obj = reader(filename,delimiter)

	X,Y = obj.read()

	from sklearn.cross_validation import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

	classifier = KNeighborsClassifieR()
	classifier.fit(X_train, y_train)
	y_pred = classifier.predict(X_test)
	
	acc_obj = acc(y_test, y_pred)

	final_accuracy = acc_obj.accuracy()

	print("KNN Accuracy: ",final_accuracy, "%")
	
	wrt_obj = writer("file.csv", "KNN Without SK",final_accuracy)

	wrt_obj.write()

run()