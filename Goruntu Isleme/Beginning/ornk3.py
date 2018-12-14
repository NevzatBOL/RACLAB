#-*- coding: utf-8 -*-
#Resim Kaydetme
import numpy as np
import cv2

img=cv2.imread('resimler/python.jpg',0) #resmi okuduk. (0 gray olarak okur.)
cv2.imshow('image',img) #resmi gösterdik.
cv2.waitKey(0)
cv2.imwrite('resimler/pythonkayit.jpg',img) #Resmi kaydeder.
cv2.destroyAllWindows() #Tüm pencereleri kapatır.


