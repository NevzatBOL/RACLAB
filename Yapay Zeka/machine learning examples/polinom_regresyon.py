import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures as pf
from sklearn.linear_model import Perceptron
from sklearn import linear_model

data=pd.read_csv("data/linear.csv")

x=data["metrekare"]
y=data["fiyat"]

x=np.array(x)
y=np.array(y)

a,b,c=np.polyfit(x,y,2)

z=np.arange(150)

plt.scatter(x,y)

plt.plot(z,a*z**2+b*z+c)
plt.show()
