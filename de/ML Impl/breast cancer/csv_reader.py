import numpy as np
import pandas as pd

class reader:
	def __init__(self,url,delimiter):
		self.url = url
		self.delimiter = delimiter
		
	def read(self):
		dataset = pd.read_csv(self.url,delimiter=self.delimiter)
		dataset.replace('?', 0, inplace=True)
		dataset = dataset.applymap(np.int64)
		X = dataset.iloc[:, 1:-1].values    
		Y = dataset.iloc[:, -1].values
		
		return X,Y;
	
	def readgraph(self):
		data = pd.read_csv('file.csv',delimiter=",")

		Name = data['Name'].values
		Acc = data['Acc'].values
		"""		
		plt.plot(code,val,color="black",linewidth=".5")
		plt.show()
		"""
		return Name,Acc;