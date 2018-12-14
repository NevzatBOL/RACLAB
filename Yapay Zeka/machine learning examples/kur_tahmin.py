#-*-coding: cp1254-*-
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

veri=pd.read_csv("data/kur.csv")

x=veri["Gün"]
y=veri["Fiyat"]

x=x.values.reshape(102,1)	
y=y.values.reshape(102,1)

plt.scatter(x,y)

Ltahmin=LinearRegression()
Ltahmin.fit(x,y)
Ltahmin.predict(x)

plt.plot(x,Ltahmin.predict(x),c="red")

Ptahmin=PolynomialFeatures(degree=5)
X=Ptahmin.fit_transform(x)

Pmodel=LinearRegression()
Pmodel.fit(X,y)
Pmodel.predict(X)

plt.plot(x,Pmodel.predict(X),c="green")

mse=0
for i in range(len(X)):
	mse+=(float(y[i])-float(Pmodel.predict(X)[i]))**2
print "Polynom mse : ",mse/len(X)

plt.show()

