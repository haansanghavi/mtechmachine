import pandas as pd
class reader:
	def __init__(self,url,col1,col2 = None,sp = None,ep = None):
		self.url = url
		self.sp = sp
		self.ep = ep
		self.col1 = col1
		self.col2 = col2
		
	def read(self):
		data = pd.read_csv(self.url,delimiter='\t')
		c1 = data[self.col1].values
		c2 = data[self.col2].values

		c1 = c1[self.sp:self.ep]
		c2 = c2[self.sp:self.ep]
		
		return c1,c2;
	
	def readforpredict(self):
		data = pd.read_csv(self.url,delimiter='\t')
		c1 = data[self.col1].values

		c1 = c1[self.sp:self.ep]
		
		return c1;
		
		
		