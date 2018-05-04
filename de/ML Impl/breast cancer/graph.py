import matplotlib.pyplot as plt
from csv_reader import reader
import numpy as np

filename="file.csv"
delimiter=","

obj = reader(filename,delimiter)

X,Y = obj.readgraph()

print(X,Y)

x = np.arange(len(X))
"""
plt.bar(x, height=Y,align="center",alpha=0.5)
plt.xticks(Y, X);

plt.plot(Y,color="black")
"""
plt.bar(x, Y, color=(0.4, 0.7, 0.15, 0.3),  edgecolor='blue')
plt.xticks(x, X)
plt.show()
#plt.show()		
