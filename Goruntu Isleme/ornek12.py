#-*-coding: cp1254-*-
###Sekil Algılama2###

import numpy as np
import cv2

def detect(c):
	peri=cv2.arcLength(c,True)
	approx=cv2.approxPolyDP(c,0.04*peri,True)

	if len(approx)==3:
		shape="Ucgen"
	elif len(approx)==4:
		x,y,w,h=cv2.boundingRect(approx)
		ar=w/float(h)
		shape="Kare" if ar>=0.95 and ar<=1.05 else "Dikdortgen"
	elif len(approx)==5:
		shape="Besgen"
	else:
		shape="Daire"

	return shape

img=cv2.imread('resimler/sekiller.png')


gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)
thresh=cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV)[1]

_,cntr,_=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for c in cntr:
	M = cv2.moments(c)
	cX = int((M["m10"] / M["m00"]))
	cY = int((M["m01"] / M["m00"]))
	shape = detect(c)

	c=c.astype("float")
	c=c.astype("int")
	cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
	cv2.putText(img, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
		0.5, (255, 255, 255), 2)
 
	
	cv2.imshow("Image", img)
	cv2.waitKey(0)
