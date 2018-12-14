#-*-coding: utf-8 -*-
#Image Boyutlandirma
import numpy as np
import cv2

img=cv2.imread('resimler/futbol.jpg')
lower=cv2.pyrDown(img) #resimi küçültür.
higher=cv2.pyrUp(img) #resmi büyütür.

cv2.imshow('Original',img)
cv2.imshow('Lower',lower)
cv2.imshow('Higher',higher)

cv2.waitKey(0)
cv2.destroyAllWindows()
