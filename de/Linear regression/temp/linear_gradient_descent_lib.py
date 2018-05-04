import math
from csv_reader import reader

class myclass:


	def __init__(self,x = None,y = None,theta0 = None,theta1 = None,learning_rate = None,col1 = None,col2 = None,sp = None, ep = None):
		error=[]
		xiyit0=xiyit1=0
	
		self.theta0 = theta0
		self.theta1 = theta1
		self.learning_rate = learning_rate
		if type(x) is list:
			self.x=x
			self.y=y

			self.n=len(x)
		elif isinstance(x, str):
			self.x = x
			self.col1 = col1
			self.col2 = col2
			
			obj = reader(x,col1,col2,sp,ep)
			self.x = []
			self.y = []
			#print(obj.read())
			self.x,self.y = obj.read()
			#print(self.x)
			
			self.n=len(self.x)
			"""print(self.x,type(self.x))
			print(self.x,type(self.y))"""
			

	def fun(self):
		y_cap=[]
		self.error=[]
		self.xiyit0=self.xiyit1=0
		for i in range(self.n):
			#print( int(x[i]) )
			y_cap.append( int(self.theta0) + (int(self.theta1) * int(self.x[i])) )
		
		for i in range(self.n):
			self.xiyit0 += ( int(y_cap[i]) - int(self.y[i]))
		for i in range(self.n):
			self.xiyit1 += (( int(y_cap[i]) - int(self.y[i])) * int(self.x[i]))
		
		for i in range(self.n):
			self.error.append(( int(y_cap[i]) - int(self.y[i])) ** 2 )
			#print(error)
		return;
			
	def minimize(self):
		
		temp0 = self.theta0 - ( self.learning_rate * (1/(self.n)) * self.xiyit0 )
		temp1 = self.theta1 - ( self.learning_rate * (1/(self.n)) * self.xiyit1 )
		
		self.theta0 = temp0
		self.theta1 = temp1
		
		return;

		
	def iterate(self,val):
		
		for i in range(val):
			self.fun()
			initial_error = sum(self.error)
			print("Error : ",initial_error)
			print(self.theta0,self.theta1)

			self.minimize()

