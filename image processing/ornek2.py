#-*-coding: cp1254-*-
###Resim Üzerinde Birden Çok Parça Arama###

import numpy as np
import cv2

img_rgb=cv2.imread('resimler/mario.jpg')
img_gray=cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
template=cv2.imread('resimler/mario2.jpg',0)
w,h=template.shape[::-1]

res=cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
#Eşik değeri değiştirilerek resim üzerindeki nesne yakalama hataları düzeltile bilir.
threshold=0.75
loc=np.where(res>=threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb,pt,(pt[0]+w,pt[1]+h),(0,0,255),2)

cv2.imshow('select image', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
