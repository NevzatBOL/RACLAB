#-*-coding: cp1254-*-
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression as lr
import matplotlib.pyplot as plt

data = pd.read_csv("data/linear.csv")

x=data["metrekare"]
y=data["fiyat"] 

x = np.array(x).reshape(99,1)
y = np.array(y).reshape(99,1)

linear=lr()
linear.fit(x,y)

linear.predict(x)

m=linear.coef_
b=linear.intercept_

a=np.arange(150)

plt.scatter(x,y)
plt.scatter(a,m*a+b)
plt.show()


print "Egim: ",m
print "Y de kesistigi yer: ",b

print "Deneklem"
print "y=",m,"x+",b

