
class acc:
	def __init__(self,y_test, y_pred):
		self.y_test = y_test
		self.y_pred = y_pred
		
	def accuracy(self):
		correct = 0
		for i in range(len(self.y_pred)):
			if(self.y_test[i] == self.y_pred[i]):
				correct += 1
		return (correct/len(self.y_test))*100
	