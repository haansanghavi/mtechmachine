from csv_reader import reader

class myclass:
	
	a=b=0
	def __init__(self,x = None,y = None,col1 = None, col2 = None,sp = None, ep = None):
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
		xi = sum(self.x)
		yi = sum(self.y)
		xiyi=xi2=0
		for i in range(self.n):
			xi2 += int(self.x[i]**2)
			xiyi += self.x[i] * self.y[i]


		#print("xi:",xi,"\nyi:",yi,"\nxiyi:",xiyi)

		self.a = ( (self.n * xiyi) - (xi * yi) ) / ( self.n * (xi2) - (xi ** 2) )

		self.b = ( 1/self.n * (yi - (self.a * xi) ) )
		
		#print(self.a,self.b)
		return;

		
	def predict(self,val = None,col1 = None,sp = None,ep = None):
		#val = int(input("Enter value to predict resut for: "))
		
		if val == None:
			return;
		
		if type(val) is list:
			print("Predicted vales: \n")
			for i in range(len(val)):
				print(self.a*val[i]+self.b)
			return;
		elif isinstance(val, str):
			obj = reader(val,col1,None,sp,ep)
			temp = []

			temp = obj.readforpredict()
			
			print("Predicted values: \n")
			for i in range(len(temp)):
				print(self.a*temp[i]+self.b)
			
			return;
		else:
			print("\nPredicted values: ",val)
			return;
			
		return;
		
	def printeqn(self):
		print("y = ",self.a," + ",self.b)
		return;
