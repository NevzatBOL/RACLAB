#-*-coding: 1254-*-
import numpy as np
from sklearn.preprocessing import Imputer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn import cross_validation
import pandas as pd

veri=pd.read_csv("data/breast-cancer-wisconsin.data")

veri.replace('?',-99999,inplace=True) #? olan yerlere -99999 degerini atadık.
veri=veri.drop(['id'], axis=1) #id sütununu sildik.

y=veri.benormal #benormal sütununu ayrıdık.
x=veri.drop(['benormal'],axis=1) 

imp=Imputer(missing_values=-99999,strategy="mean",axis=0) #-99999 degeri yerine tüm degerlerin ortalamasını yazdık.
x=imp.fit_transform(x)

x_train,x_test,y_train,y_test=cross_validation.train_test_split(x,y,test_size=0.33) #datamızı egitim ve test datası olarak ayırdık.

tahmin=KNeighborsClassifier() #knn modelimizi tanımladık.
tahmin.fit(x_train,y_train) #knn modelimizi egittik.
basari=tahmin.score(x_test,y_test) #knn modelimizin dogruluk oranını tesbit ettik.

print " Dogruluk : ",basari

print tahmin.predict(np.array([2,9,3,5,3,6,1,9,5]).reshape(1,-1))
