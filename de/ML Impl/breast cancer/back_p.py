from csv_reader import reader
from accuracy import acc
from file_write import writer


filename="breastCancer.csv"
delimiter=","

obj = reader(filename,delimiter)

X,Y = obj.read()

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)


from sklearn.neural_network import MLPClassifier
MLP = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)

MLP.fit(X, Y)   

y_pred = MLP.predict(X_test)

acc_obj = acc(y_test, y_pred)

final_accuracy = acc_obj.accuracy()

print("MLP Accuracy: ",final_accuracy, "%")

wrt_obj = writer("file.csv", "MLP",final_accuracy)

wrt_obj.write()
