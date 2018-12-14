#-*-coding: utf-8-*-
#Image Resize
import numpy as np
import cv2

img = cv2.imread('resimler/python.jpg')
res=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC) #resmi yeniden boyutlandırdık.
#resmi yeniden boyutlandırmak icin asagıdaki metodlar kullanılabilir.
#cv2.INTER_AREA
#cv2.INTER_CUBIC (slow)
#cv2.INTER_LINEAR

cv2.imshow('yeni boyut',res)

cv2.waitKey(0)
cv2.destroyAllWindows()

