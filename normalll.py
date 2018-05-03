import numpy as np
from numpy.linalg import inv
import pandas
import matplotlib.pyplot as plt 


def main():
    data = pandas.read_csv('abc.csv',header=None)
    data2 = data.as_matrix()
   # print(data2)
    
    trainingset = data2[0:4,0:3]
    trainingsettarget = data2[0:4,3:4]
    
    testset = data2[4:6,0:3]
    testsettarget = data2[4:6,3:4]
    
    print('trainingset\n\n',trainingset)
    print('\ntrainingsettarget\n\n',trainingsettarget)
    
    print('\ntestset\n\n',testset)
    print('\ntestsettarget\n\n',testsettarget)
    
    plt.plot(trainingset, trainingsettarget, "r.")
    
    trainingset_b = np.c_[np.ones((4, 1)), trainingset]
    print('\nBaised\n\n',trainingset_b)

    transpose_tariningset = trainingset_b.T
    print('\ntranspose_tariningset\n\n',transpose_tariningset)
    
    multiplication1  = np.matmul(transpose_tariningset,trainingset_b)
    print('\nmultiplication1\n\n',multiplication1)
    
    inverse = inv(np.matrix(multiplication1))
    print('\ninverse\n\n',inverse)
    
    multiplication2 = np.matmul(inverse,transpose_tariningset)
    print('\nmultiplication2\n\n',multiplication2)

    theta = multiplication2.dot(trainingsettarget)
    print('\ntheta\n\n',theta)
    
    
    
    theta_transpose = theta.T
    print('\nTheta_transpose\n\n',theta_transpose)
  
    
    testset_b = np.c_[np.ones((1, 1)), testset] 
    testset_b_transpose = testset_b.T
    print('\ntestset_b\n\n',testset_b)
    prediction = theta_transpose.dot(testset_b_transpose)  
      
    
    print('\nPredictions\n',prediction)  
    
    error = 0
    for i in range(len(prediction)):
        error += testsettarget[i] - prediction[i]
        
    print('\nerror\n\n',error )
    
main()
