import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class LinearClassification(object):
    
    def __init__(self):
        self.learning_rate = 0.0001
        self.batch_size = 200
        self.no_of_iter = 1000
        self.reg = 0.000001
        
    
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
        
        self.no_of_classes = np.max(y) + 1
        
        self.W = np.random.rand(self.no_of_classes, self.X_train.shape[1]) * 0.001
        
        self.W, loss_history = self.SGD(self.W, self.X_train, self.y_train, self.learning_rate, self.batch_size, self.no_of_iter, self.reg)
        
        return loss_history
    def SGD(self, W, X, y, learning_rate, batch_size, no_of_iter, reg):
        W_updated = W
        
        no_of_train = X.shape[0]
        loss_history = []
        
        for i in range(no_of_iter):
            batch_inx = np.random.choice(no_of_train, batch_size, replace=True)
            X_batch = X[batch_inx,:]
            y_batch = y[batch_inx]
            
            
            loss, grad = self.SVM_classfier(W_updated, X_batch, y_batch, reg)
            loss_history.append(loss)
            W_updated = W_updated - (learning_rate * grad)
            
        return W_updated, loss_history
    def SVM_classfier(self, W, X, y, reg):
        
        no_of_classes = np.max(y) + 1
        #creating matrix with zeros, same shape as starting weights
        
        gradient_W = np.zeros(W.shape)
        
        loss = 0.0 
        for i in range(X.shape[0]):
            scores = W.dot(X[i, :].T)
            correct_class = scores[y[i]]
            for j in range(no_of_classes):
                if j == y[i]:
                    continue
                current_class_margin = scores[j] - correct_class + 1 #one is 
                if current_class_margin > 0:
                    loss +=  current_class_margin
                
                    gradient_W[y[i]:1, :] -= X[i, :]
                    gradient_W[j:1, :] += X[y[i], :]
        
        loss /= X.shape[0]
        gradient_W /= X.shape[0]
        
        loss += 0.5 * reg * np.sum(W * W)
        
        gradient_W += reg*W
    
        return loss, gradient_W
    
    def predict(self, X):
        pred = []
        for i in range(X.shape[0]):
            pred.append(np.argmax(np.dot(self.W,X[i, :].T)))
        return pred


def accuracy(y_tes, y_pred):
    correct = 0
    for i in range(len(y_pred)):
        if(y_tes[i] == y_pred[i]):
            correct += 1
    return (correct/len(y_tes))*100



def run():
    dataset = pd.read_csv('breastCancer.csv')
    dataset.replace('?', 0, inplace=True)
    dataset = dataset.applymap(np.int64)
    X = dataset.iloc[:, 1:-1].values    
    y = dataset.iloc[:, -1].values
    y_new = []
    for i in range(len(y)):
        if y[i] == 2:
            y_new.append(0)
        else:
            y_new.append(1)
    y_new = np.array(y_new)

    
    from sklearn.cross_validation import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y_new, test_size = 0.25, random_state = 0)
   
    classifier = LinearClassification()
    loss_history = classifier.fit(X_train, y_train)
    
    y_pred = classifier.predict(X_test)
    
    from sklearn.linear_model import LogisticRegression
    reg = LogisticRegression(random_state=0)
    reg.fit(X_train, y_train)
    
    y_pred_sk = reg.predict(X_test)
    
    print("My algorithm on this dataset: ",accuracy(y_test, y_pred), "%")
    print("Sklearn Logistic regression score: ",accuracy(y_test, y_pred_sk),"%")



run()

