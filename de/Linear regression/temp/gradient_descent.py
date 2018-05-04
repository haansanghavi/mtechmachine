from linear_gradient_descent_lib import myclass

x=[10,15,20,25,30]
y=[8,10,12,15,18]

learning_rate = float(input("Enter learning rate: "))
print("Enter values of theta 0 and 1\n")
theta0 = int(input("Theta 0:"))
theta1 = int(input("Theta 1:"))


obj = myclass("data-01",None,theta0,theta1,learning_rate,"Code","Value",0,500)
obj.fun()
obj.minimize()
obj.iterate(10)


"""
obj = myclass(x,y,theta0,theta1,learning_rate)
obj.fun()
obj.minimize()
obj.iterate(10)
"""