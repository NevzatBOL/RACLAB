#-*-coding: utf-8-*-
import numpy as np
import cv2

frame_cascade = cv2.CascadeClassifier('data/cascade.xml')

img = cv2.imread('kalem.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

frames = frame_cascade.detectMultiScale(img, 1.4, 5)
"""
frame_cascade.detectMultiScale(gri_resim,ScaleFactor,minNeighbors,flags,minSize,mazSize)

Scale=görüntü boyutunun nekadar azaltılacağını belirten parametre 1.3 yani boyutun %30 düşürüldüğü anlamına gelir. Değer ne kadar düşükse algılama modeli ile eşleşen bir boyut bulma ihtimalini artırıyoruz ama daha yavaş çalışıyor.
minNeighbors=her bir aday dikdörtgenin kaç tane komşu bulunduracağını belirten parametredir. yüksek değer daha az algılama ile sonuçlanır ama kalite artar.
minSize= Mümkün olan en düşük nesne boyutu. Bundan küçük nesneler dikkate alınmaz.
maxSize= Maksimum nesne boyutu. Bundan büyük nesneler yoksayılır.
"""


for (x,y,w,h) in frames:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
