#-*-coding: utf-8-*-
#Performans Olcme
import numpy as np
import cv2

img1 = cv2.imread('resimler/futbol.jpg')
e1 = cv2.getTickCount()
#fonksiyon
for i in xrange(5,49,2):
    img1 = cv2.medianBlur(img1,i)
#
e2 = cv2.getTickCount()
#baslangıc ve bitis degerlerini cıkartıp
#frekans degerine böldügümüzde bize fonksiyonun calısma süresini verir.
t = (e2 - e1)/cv2.getTickFrequency() 
print t
