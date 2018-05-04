from numpy import *


def step_gradient(t0, t1, data, learning_rate, 100<traning_data_size>):
	'''
	t0 = 1/N sigma((yi - (t0 + t1*xi)))
	t1 = 1/N sigma((yi - (t0 + t1*xi))*xi)
	'''
	t0_gradient = 0
	t1_gradient = 0
	N = float(training_data_size)
	for i in range(0,N):
		x = data[i, 0]
		y = data[i, 1]
		t0_gradient = t0_gradient + (-1/N * (y - (t0_gradient + t1_gradient*x)))
		t1_gradient = t1_gradient + (-1/N * (y - (t0_gradient + t1_gradient*x)) * x)
	updated_t0 = t0 - (learning_rate * t0_gradient)
	updated_t1 = t1 - (learning_rate * t1_gradient)
	return [updated_t0, updated_t1]

def calculate_error(t0, t1, data, 0, 100):
	'''1/N sigma((yi - (t0 + t1*xi)))^2'''
	total_error = 0
	for i in range(0, 100):
		x = data[i, 0]
		y = data[i, 1]
		total_error = total_error + ((y - (t0 + t1*x)))**2
	return total_error/100


def gradient_descent(data, initial_t0, initial_t1, learning_rate):
	t0 = initial_t0
	t1 = initial_t1
	temp = -5
	temp1 = calculate_error(t0, t1, data, 0<from_data>, 100<training_data_size>)
	count = 0
	while abs(temp1 - temp) > 0.001:
		t0, t1 = step_gradient(t0, t1, array(data), learning_rate, 100<training_data_size>)
		temp1 = temp
		temp = calculate_error(t0, t1, data, 0, 100)
		count++
	return [t0, t1, temp, count]


def code():
	csv_file = input("name : ")
	data = genfromtxt("path.."+csv_file,delimeter = ",")
	
	learning_rate = float(input("learn rate : "))
	initial_t0 = float(input("initial t0 : "))
	initial_t1 = float(input("initial t1 : "))
	[t0,t1,temp,count] = gradient_descent(data, initial_t0, initial_t1, learning_rate)

if __name__ == '__main__'
	code()

