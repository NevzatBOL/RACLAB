#-*- coding: utf-8 -*-
#Resim Okuma ve Görüntüleme
import numpy as np
import cv2

img=cv2.imread('resimler/python.jpg',0) #resmi okuduk. (0 gray olarak okur.)
cv2.imshow('image',img) #resmi gösterdik.
cv2.waitKey(0)
cv2.destroyAllWindows() #Tüm pencereleri kapatır.
