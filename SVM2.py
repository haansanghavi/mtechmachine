#SVM Classifier

from sklearn import svm,metrics
import pandas

file=input('Enter dataset File :\n')
data=pandas.read_csv(file)
rows=data.shape[0]
cols=data.shape[1]

#divide into traingset and test set
trainingset_length=int(rows*.5)
testingset_length=rows-trainingset_length
trainingset=data.iloc[0:rows, 0:(cols-1)]
trainingsettarget=data.iloc[0:rows, -1]
testingset=data.iloc[trainingset_length:, 0:(cols-1)]
testingsettarget=data.iloc[trainingset_length:, -1]
reg_param=[]
n = int(input("Enter no. of iterations : "))
for index in range(0,n):
    P=int(input("Enter Regularization Param. : "))
    reg_param.append(P)
    
#Learn the model using training data set
for index in reg_param:
    clf = svm.LinearSVC(P=index)
    clf.fit(trainingset,trainingsettarget)
    predictions=clf.predict(testingset)
    print("Regularization parameter P : ",index," ","Accuracy:",metrics.accuracy_score(testingsettarget,predictions,normalize=True))


