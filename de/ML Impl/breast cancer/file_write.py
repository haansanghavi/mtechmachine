
class writer:
	def __init__(self,url,algo,acc):
		self.url = url
		self.algo = algo
		self.acc = acc
		
	def write(self):
		pr = str(self.algo)+","+str(self.acc)+"\n"
		with open(self.url,'a+') as wf:
			wf.write(pr)