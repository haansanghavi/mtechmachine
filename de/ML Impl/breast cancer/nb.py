from csv_reader import reader
from accuracy import acc
from file_write import writer


filename="breastCancer.csv"
delimiter=","

obj = reader(filename,delimiter)

X,Y = obj.read()

print(Y)

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

from sklearn.naive_bayes import GaussianNB
NB = GaussianNB()
NB.fit(X_train, y_train)

y_pred = NB.predict(X_test)

acc_obj = acc(y_test, y_pred)

final_accuracy = acc_obj.accuracy()

print("NB Accuracy: ",final_accuracy, "%")


wrt_obj = writer("file.csv", "NB",final_accuracy)

wrt_obj.write()
