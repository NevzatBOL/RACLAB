#-*-coding: cp1254-*-
###Resmi 16'ya Böleme ve Parçaları Karıştırıp Tekrar Birleştirme###

import numpy as np
import cv2
import random

img=cv2.imread('resimler/racecar-j.jpg')

w,h=img.shape[0:2]

img2=[]
for i in range(0,w,w/4):
    for j in range(0,h,h/4):        
        img2.append(img[i:i+w/4,j:j+h/4])

while(1):
    random.shuffle(img2)
    k=0
    img3=img.copy()
    for i in range(0,w,w/4):
        for j in range(0,h,h/4):
            img3[i:i+w/4,j:j+h/4]=img2[k]
            k+=1
        
    cv2.imshow("random frame",img3)
    if cv2.waitKey(1000)==27:
        break

cv2.destroyAllWindows()
