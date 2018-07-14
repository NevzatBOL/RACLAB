#-*-coding: utf-8 -*-
from student_success import train_x,train_y,test_x,test_y

import numpy as np
import pandas as pd
from matplotlib.colors import ListedColormap
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from imblearn import over_sampling

def training(metod, name, train_X,train_Y, test_X=test_x, test_Y=test_y):
	train_model = model.fit(train_X,train_Y)
	train_result = train_model.score(train_X,train_Y)
	test_result = train_model.score(test_X,test_Y)

	print "Metod : %s Model : %s Train result : %f Validation Result : %f"%(metod,name,train_result,test_result)


print train_x.shape

ROS = over_sampling.RandomOverSampler()
ROS_x, ROS_y = ROS.fit_sample(train_x,train_y)

print ROS_x.shape

smote = over_sampling.SMOTE()
smote_x, smote_y = smote.fit_sample(train_x,train_y)

print smote_x.shape

adasyn = over_sampling.ADASYN()
adasyn_x, adasyn_y = adasyn.fit_sample(train_x,train_y)

print adasyn_x.shape

models = []
models.append(("LR",LogisticRegression()))
models.append(("LDA",LinearDiscriminantAnalysis()))
models.append(("KNN",KNeighborsClassifier()))
models.append(("DCT",DecisionTreeClassifier()))
models.append(("GNB",GaussianNB()))
models.append(("SVC",SVC()))
models.append(("GPC",GaussianProcessClassifier(1.0*RBF(1.0))))
models.append(("MLP",MLPClassifier()))
models.append(("ADB",AdaBoostClassifier()))

for name, model in models:
	training("Normal",name,train_x,train_y)
	training("ROS",name,ROS_x,ROS_y)
	training("SMOTE",name,smote_x,smote_y)
	training("ADASYN",name,adasyn_x,adasyn_y)
	print "----------------------------------------------"

