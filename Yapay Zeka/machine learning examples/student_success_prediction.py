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
from sklearn.utils import class_weight
from sklearn.model_selection import GridSearchCV

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

print np.unique(train_y)
weight=class_weight.compute_class_weight("balanced",np.unique(train_y),train_y)
print weight
result = SVC(class_weight={0:weight[0],1:weight[1],2:weight[2]}).fit(train_x,train_y)
print "class_weight metod and svc models result : ",result.score(test_x,test_y)



# SVC Parametre Optimizasyonu
def svc_param_selection(train_X,train_Y,nfolds):
	C=[0.001,0.01,0.1,0.5,1,2,5,10,50,100,1000]
	Gamma=[0.001,0.01,0.1,1]
	Kernel=['linear','rbf']
	param_grid={'C':C,'gamma':Gamma,'kernel':Kernel}
	
	grid_search=GridSearchCV(SVC(),param_grid,cv=nfolds)
	grid_search.fit(train_X,train_Y)

	return grid_search.best_params_

best_params = svc_param_selection(train_x,train_y,4)
print "best params : ",best_params

svc_train = SVC(C=best_params['C'],kernel=best_params['kernel'],gamma=best_params['gamma'])
svc_train.fit(train_x,train_y)

print "Train result : ",svc_train.score(train_x,train_y)
print "Validation result : ",svc_train.score(test_x,test_y)





