#-*-coding: cp1254-*-
###Yüz ve Göz Algılama###

import numpy as np
import cv2
from matplotlib import pyplot as plt

face_cascade = cv2.CascadeClassifier('DataSet/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('DataSet/haarcascade_eye.xml')

img = cv2.imread('resimler/kvp.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#face_cascade.detectMultiScale(gri_resim,ScaleFactor,minNeighbors,flags,minSize,mazSize)

#Scale=görüntü boyutunun nekadar azaltılacağını belirten parametre 1.3 yani boyutun %30 düşürüldüğü anlamına gelir. Değer ne kadar düşükse algılama modeli ile eşleşen bir boyut bulma ihtimalini artırıyoruz ama daha yavaş çalışıyor.
#minNeighbors=her bir aday dikdörtgenin kaç tane komşu bulunduracağını belirten parametredir. yüksek değer daha az algılama ile sonuçlanır ama kalite artar.
#minSize= Mümkün olan en düşük nesne boyutu. Bundan küçük nesneler dikkate alınmaz.
#maxSize= Maksimum nesne boyutu. Bundan büyük nesneler yoksayılır.

#Yüzler bulunursa, tespit edilen yüzlerin pozisyonlarını Rect (x, y, w, h) olarak döndürür.
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
