"""from sklearn import tree
X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

print(clf.predict([[2., 2.]]))
print(clf.predict([[-5., -5.]]))
print(clf.predict_proba([[2., 2.]]))
"""

from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.metrics import r2_score
iris = load_iris()
clf = tree.DecisionTreeClassifier()


#print(iris)

x = iris.data[:120]
y = iris.target[:120]
print(len(iris.data))
clf = clf.fit(x,y)

prediction = clf.predict(iris.data[120:,:])
test = iris.target[120:]
print(prediction)
print(test)


#print(r2_score(prediction, test))

#print(iris.data[:1, :])
