from normal_lr_lib import myclass

x = [0,1,2,3,4]
y = [2,3,5,4,6]

test = [10,11,12]

"""
obj = myclass("data-01",None,"Code","Value",0,500)
obj.fun()
obj.printeqn()
obj.predict("data-01","Code",500,944)

"""
obj = myclass(x,y)
obj.fun()
obj.printeqn()
obj.predict(10)

