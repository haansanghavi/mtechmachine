import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA

iris = datasets.load_iris()

x = iris.data  # we only take the first two features.
y = iris.target

print(x)
print("--target--")
print(y)

#print(len(x))

#training and testing

testX = x[-1:]
testY = y[-1:]
trainX = x[:-1]
trainY = y[:-1]
print(len(testX))
#print(trainX[1][2])

#calculatintg distance




distanceList = []
def findDistance():
    distance = 0
    for i in range(len(trainX)):
        distance = 0
        for j in range(len(testX[0])):
            distance += (trainX[i][j]-testX[0][j])**2
        print(distance)
        distanceList.insert(i,distance)
        

findDistance()        
print(distanceList)

minListDistance = []
minDistance = min(distanceList)

print(minDistance)
count = 0
counter = 0
for i in distanceList:
    if i == minDistance:
        count = counter
    else:
        counter += 1

predictedClass = y[count]
print(predictedClass)



predictionList = []
k = 3

for i in range(k):
    count = 0
    counter = 0
    minDistance = min(distanceList)
    for j in distanceList:
        if j == minDistance:
            count = counter
        else:
            counter += 1
    predictionList.insert(i,count)
    distanceList[count] = 10000



print(predictionList)

predictedOp = []
for i in range(k):
    predictedOp.insert(i,y[predictionList[i]])
    
                 
print(predictedOp)    

print(max(set(predictedOp) , key = predictedOp.count))
