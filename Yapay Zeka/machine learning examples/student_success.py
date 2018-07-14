#-*-coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
#import matplotlib.pyplot as plt

data=pd.read_csv("data/student/student-mat.csv",delimiter=";")

#print data.columns.values
#print "ilk sinav max not: ",data.G1.max()

sinav_sonucu = data[["G1","G2","G3"]]
#print sinav_sonucu

data = data.drop(["school","sex","age","address","Mjob","Fjob","reason","guardian",
		  "activities","nursery","higher","internet","romantic","famrel",
		  "freetime","goout","Dalc","Walc","health","absences","G1","G2","G3"], axis=1)

#tum degerleri sayı haline getirdik.
data = data.replace({"GT3":1,"LE3":0,"yes":1,"no":0,"T":1,"A":0})
#print data

#Normalizasyon islemlerini yaptık.
min_max_scaler=MinMaxScaler()
data = min_max_scaler.fit_transform(data) #degerleri 0-1 arasına cektik.
data = pd.DataFrame(data) #dataları tekrar pandas verisi olarak atadık.

sinav_sonucu=(sinav_sonucu - 0)/(20 - 0) #sınav sonuclarını normalize ettik.
#print sinav_sonucu


not_ortalamasi = sinav_sonucu.sum(axis=1)/3
#print not_ortalamasi

#sınav sonuclarını datamıza ekledik.
data["toplam"]=not_ortalamasi
#print data
print data.describe() #data hakkında detaylı bilgi verir.

#not ortalamasının histogramını cizdirelim.
#plt.hist(not_ortalamasi)
#plt.show()

#not ortalamasını iyi,orta,kotu olarak sınıflandırdık.
birinci = data.toplam<0.425
ikinci = (data.toplam>=0.425) & (data.toplam<1.788)
ucuncu = data.toplam>=1.788
#print ikinci

data.loc[birinci,"toplam"] = 0 #toplam kolununda birinci sartını saglayanları 0 yapar.
data.loc[ikinci,"toplam"] = 1
data.loc[ucuncu,"toplam"] = 2

print data

train, test = train_test_split(data, test_size=0.2)

train_x = train.drop(["toplam"],axis=1)
train_y = train.toplam

test_x = test.drop(["toplam"],axis=1)
test_y = test.toplam
