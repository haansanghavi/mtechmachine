import pandas


def compute_error(thetaone, thetazero, data):
    total_error = 0
    for i in range(0, len(data)):
        x = data[i, 0]
        y = data[i, 1]
        total_error = total_error + (y - ((thetaone * x) + thetazero)) ** 2
    return total_error/float(len(data))



def main(alpha,thetazero,thetaone,trainingset,testset):
   
    #Computing Initial Error
    initial_error = compute_error(thetaone,thetazero,trainingset)
    print('initial error=',initial_error)
    
    count = 0
    final_error = 0
    a =5
    while a > 0.001:
        #Learning the model
        for i in range(len(trainingset)):
            thetaone_gradient = 0
            thetazero_gradient = 0
            n = (len(trainingset))
            '''print('aaaaa',n)'''
            thetazero_sum = 0
            thetaone_sum = 0
            '''print('abc',type(thetazero_sum))'''
            '''print(type(thetaone_sum))'''
            for j in range(0,n):
            
                thetaone_sum += int((-1 * trainingset[j][0] * (trainingset[j][1] -(thetaone * trainingset[j][0] + thetazero))))
                thetazero_sum += int((-1 * (trainingset[j][1] - (thetaone * trainingset[j][0] + thetazero))))
     	    	
            '''print(thetaone_sum)
            print(thetazero_sum)'''
            thetaone_gradient = ((2 / n) * thetaone_sum)
            thetazero_gradient = ((2 / n) * thetazero_sum)
            
            '''print('thetaone',thetaone_gradient)
            print('thetazero',thetazero_gradient)'''
            
            thetaone = ( thetaone - (alpha * thetaone_gradient))
            thetazero = ( thetazero - (alpha * thetazero_gradient))
        
        #print( 'new value of thetaone = ',thetaone, ' and thetazero =', thetazero)
        
        #Computing Test Case
        
        '''print('aaa',testset[0][0])
        print('bbb',testset[1][0])'''
        final_error = compute_error(thetaone,thetazero,testset)
        
        a = final_error - initial_error
        print ('value of jtheta',a )
        
        #count = count + 1
        
        #print('Final Error = ',final_error )
        
        count = count + 1
    
    print('total count: ',count)
        


alpha = float(input('Enter alpha:'))
thetazero = float(input('Enter theta zero :'))
thetaone = float(input('Enter theta one :'))
    
data = pandas.read_csv('pavan.csv',header=None)
data2 = data.as_matrix()
print(data2)

trainingset = data2[0:3]
print('trainingset',trainingset)
    #trainigsettarget = data2.target[0:3]

testset = data2[3:5]
print('testset',testset)
    #testsettarget = data2.target[4:]
main(alpha,thetazero,thetaone,trainingset,testset)

