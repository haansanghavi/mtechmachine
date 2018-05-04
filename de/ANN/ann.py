import math



w = [0.15, 0.20, 0.25, 0.30, 0.40, 0.45, 0.50, 0.55]

ip = [.05, .1]
b = [.35, .60]
o1 = [.01, .99]

def net(w1,w2,b,i1,i2):
	
	q=w1*i1+w2*i2+b*1
	print(q)
	return q
	
def out(neth):
	#net=net*(-1)
	x = math.exp(neth*(-1))
	y=1/(1+x)
	print("out",y)
	return y
	

def error(i1,i2):
	
	Etot = (0.5)*(ip[0]-i1)**2 + (0.5)*(ip[1]-i2)**2
	print("e",Etot)
	return Etot

def main():
	
	_2=0
	i1=ip[0]
	i2=ip[1]

	neth=net(w[_],w[_+1],b[_2],i1,i2)
	outh=out(neth)
	_=_+2
	
	neth=net(w[_],w[_+1],b[_2],i1,i2)
	outh=out(neth)
	_=_+2
	
	
	
	_2=_2+1
	
	
	
	
			
	ertot = error(i1,i2)
	print(ertot)
	
	
main()
