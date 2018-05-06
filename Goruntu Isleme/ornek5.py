#-*-coding: utf-8-*-
###Daire Algılama###

import numpy as np
import cv2

img=cv2.imread("resimler/daire.jpg")
output=img.copy()
#blur=cv2.GaussianBlur(img,(7,7),0)
#blur = cv2.blur(img,(5,5))
#blur=cv2.medianBlur(img,3)
blur = cv2.bilateralFilter(img,5,50,50)

gray=cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)

circles=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,0.1,1)

if circles is not None:
	circles=np.round(circles[0,:]).astype("int")
	for x,y,r in circles:
		cv2.circle(output,(x,y),r,(0,255,0),4)
		cv2.rectangle(output,(x-5,y-5),(x+5,y+5),(0,128,255),-1)
	cv2.imshow("ouput",np.hstack([img,output]))
	cv2.waitKey(0)
