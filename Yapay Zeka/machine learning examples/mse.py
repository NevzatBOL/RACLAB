#-*-coding: cp1254-*-
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression as lr
import matplotlib.pyplot as plt

data = pd.read_csv("data/linear.csv")

x=data["metrekare"]
y=data["fiyat"] 

plt.scatter(x,y)
m,e=np.polyfit(x,y,1)

a,b,c,d=np.polyfit(x,y,3)

z=np.arange(150)

plt.scatter(x,y)
plt.plot(m*z+e)
plt.plot(z,a*z**3+b*z**2+c*z+d)

print "Denklem"
print "y=",m,"x+",b

mse=0
for i in range(len(y)):
	mse+=(y[i]-(m*x[i]+e))**2
print "linear mse : ",mse/len(y)

mse2=0
for i in range(len(y)):
	mse2+=(y[i]-(a*x[i]**3+b*x[i]**2+c*x[i]+d))**2
print "polynom mse : ",mse2/len(y)

plt.show()
