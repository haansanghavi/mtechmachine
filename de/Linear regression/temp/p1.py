Train1 = [[0],[1],[2],[3],[4]]
Train2 = [[2],[3],[5],[4],[6]]


Test1=[[10]]

from sklearn import linear_model
regr=linear_model.LinearRegression()
regr.fit(Train1,Train2)
print(regr.predict(Test1))
