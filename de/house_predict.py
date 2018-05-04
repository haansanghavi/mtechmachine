from sklearn import datasets, metrics, linear_model


def code():
	data_boston = datasets.load_boston()
	
	train_set = data_boston.data[0:400, :]
	train_target_set = data_boston.target[0:400]

	test_set = data_boston.data[400:506, :]
	test_target_set = data_boston.target[400:506]

	regression = linear_model.LinearRegression()
	regression.fit(train_set, train_target_set)
	predictions = regression.predict(test_set)

	print("MAE : {0}".format(metrics.mean_absolute_error(predictions, test_target_set))
	print("MSE : {0}".format(metrics.mean_squared_error(predictions, test_target_set))


if __name__ == '__main__'
	code()
