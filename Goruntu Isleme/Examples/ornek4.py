#-*-coding: utf-8-*-
###En Parlak Nokta Tespiti###

import numpy as np
import cv2

img=cv2.imread("resimler/parlak.jpg")
img=cv2.resize(img,(600,600))
original=img.copy()
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

minval,maxval,minloc,maxloc=cv2.minMaxLoc(gray)
cv2.circle(img,maxloc,10,(255,0,0),2)
cv2.imshow("img1",img)

gray=cv2.GaussianBlur(gray,(21,21),0)
minval,maxval,minloc,maxloc=cv2.minMaxLoc(gray)
img=original.copy()
cv2.circle(img,maxloc,21,(255,0,0),2)


cv2.imshow("img2",img)
cv2.waitKey(0)
