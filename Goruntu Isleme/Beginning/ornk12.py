#-*-coding: utf-8 -*-
#Imagelerde Aritmatik Islemler - Resim Birlestirme
import numpy as np
import cv2

img1=cv2.imread('resimler/cameraman.tif')
img2=cv2.imread('resimler/text.tif')

#birlestirilecek resimler aynı boyutta olmalı.
#g(X)=(1-a)xF0(X)+axF1(X) denklemi kullanılarak eklenecek
#resimlerin agırlık degerleri belirlenir.
#dst=a x img1 + b x img2 + y
#resimleri belirlenen agırlık degerleri ile birbirine ekler.
birlestir=cv2.addWeighted(img1,0.3,img2,0.7,0) 

cv2.imshow('birsestir',birlestir)
cv2.waitKey(0)
cv2.destroyAllWindows()
