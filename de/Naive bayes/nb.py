from sklearn import datasets,metrics
import matplotlib.pyplot as plt
iris = datasets.load_iris()
from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB


#print(iris)
#print(y_pred)


# Gaussian Naive Bayes

gnb = GaussianNB()
gnb.fit(iris.data, iris.target)
gnb_pred = gnb.predict(iris.data)

"""
plt.plot(iris.target,color="red")
plt.show()
plt.plot(gnb_pred,color="black")
plt.show()
"""

print("\nNumber of mislabeled points out of a total %d points : %d (GNB)"% (iris.data.shape[0],(iris.target != gnb_pred).sum()))
print ("Accuracy= {0}".format(metrics.accuracy_score(iris.target,gnb_pred,normalize=True)))

# Multinomial Naive Bayes
mnb = MultinomialNB()
mnb.fit(iris.data, iris.target)

mnb_predict = mnb.predict(iris.data)

print("\nNumber of mislabeled points out of a total %d points : %d (MNB)"% (iris.data.shape[0],(iris.target != mnb_predict).sum()))
print ("Accuracy= {0}".format(metrics.accuracy_score(iris.target,mnb_predict,normalize=True)))


"""
plt.plot(iris.target,color="red")
plt.show()
plt.plot(mnb_predict,color="black")
plt.show()
"""


# Bernoulli Naive Bayes
bnb = BernoulliNB()
bnb.fit(iris.data, iris.target)
bnb_predict = bnb.predict(iris.data)

print("\nNumber of mislabeled points out of a total %d points : %d (BNB)"% (iris.data.shape[0],(iris.target != bnb_predict).sum()))
print ("Accuracy= {0}".format(metrics.accuracy_score(iris.target,bnb_predict,normalize=True)))


plt.plot(iris.target,color="red")
plt.show()
plt.plot(gnb_pred,color="red")
plt.show()
plt.plot(mnb_predict,color="blue")
plt.show()
plt.plot(bnb_predict,color="black")
plt.show()








