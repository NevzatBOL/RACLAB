#-*-coding: utf-8 -*-
#Countours Cizdirme
import numpy as np
import cv2

img=cv2.imread('resimler/python.jpg')
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imgray,225,255,0)
image, contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#contours ile resmin kenarlarına kenarlık ekleye biliriz. #-1 yerine counters sayısı yazılarak image'in belirli bir kısmına kenarlık eklenebilir.
img=cv2.drawContours(img,contours,-1,(0,255,0),3)
#img=cv2.drawContours(img,contours,1,(0,255,0),3) #Diger satırı yorum satırı yapın.

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
