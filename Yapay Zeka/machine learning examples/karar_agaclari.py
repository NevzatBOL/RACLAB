from sklearn.datasets import load_iris
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn import cross_validation
import numpy as np

dataset = datasets.load_iris()
#print dataset.data
#print dataset.target

x_train,x_test,y_train,y_test=cross_validation.train_test_split(dataset.data,dataset.target,test_size=0.33)

model=DecisionTreeClassifier()
model.fit(x_train,y_train)
basari=model.score(x_test,y_test)

print "Dogruluk : ",basari
print model.predict(np.array([6.9,3.1,5.1,2.3]).reshape(1,-1))
