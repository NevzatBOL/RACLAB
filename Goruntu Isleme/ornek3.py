#-*-coding: cp1254-*-
###Renk Filtresi Oluşturma###

import numpy as np
import cv2

##renklerin filitre değerlerinin bulunması:
#blue = np.uint8([[[255,0,0 ]]])
#hsv_blue = cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
#print hsv_blue
#[[[120 255 255]]]
#
#green = np.uint8([[[0,255,0 ]]])
#hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
#print hsv_green
#[[[ 60 255 255]]]
#
#red = np.uint8([[[0,0,255]]])
#hsv_red = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
#print hsv_red
#[[[  0 255 255]]]
#
#yellow = np.uint8([[[0,255,255 ]]])
#hsv_yellow = cv2.cvtColor(yellow,cv2.COLOR_BGR2HSV)
#print hsv_blue
#[[[ 30 255 255]]]
#
#lower = [H-10, 100,100]
#upper = [H+10, 255, 255]

red_lower = np.array([0, 100, 100],np.uint8)
red_upper = np.array([10, 255, 255],np.uint8)

green_lower = np.array([50, 100, 100])
green_upper = np.array([70, 255, 255])	

blue_lower=np.array([100,100,100],np.uint8)
blue_upper=np.array([130,255,255],np.uint8)

yellow_lower=np.array([20,100,100],np.uint8)
yellow_upper=np.array([40,255,255],np.uint8)

cam=cv2.VideoCapture(0)

while(1):
	_,frame=cam.read()
	
	blur=cv2.GaussianBlur(frame,(5,5),0)
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	

	red=cv2.inRange(hsv, red_lower, red_upper)
	green=cv2.inRange(hsv, green_lower, green_upper)
	blue=cv2.inRange(hsv,blue_lower,blue_upper)
	yellow=cv2.inRange(hsv,yellow_lower,yellow_upper)
	

	red=cv2.erode(red,None,iterations=2)
	red=cv2.dilate(red,None,iterations=2)

	green=cv2.erode(green,None,iterations=2)
	green=cv2.dilate(green,None,iterations=2)

	blue=cv2.erode(blue,None,iterations=2)
	blue=cv2.dilate(blue,None,iterations=2)
	
	yellow=cv2.erode(yellow,None,iterations=2)
	yellow=cv2.dilate(yellow,None,iterations=2)

	_,cntr,_=cv2.findContours(red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	for i,c in enumerate(cntr):
		if cv2.contourArea(c)<1000:
			continue
		x,y,w,h=cv2.boundingRect(c)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),0)
		cv2.putText(frame,"Kirmizi",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))

	_,cntr,_=cv2.findContours(green, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	for i,c in enumerate(cntr):
		if cv2.contourArea(c)<1000:
			continue
		x,y,w,h=cv2.boundingRect(c)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),0)
		cv2.putText(frame,"Yesil",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))

	_,cntr,_=cv2.findContours(blue, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	for i,c in enumerate(cntr):
		if cv2.contourArea(c)<1000:
			continue
		x,y,w,h=cv2.boundingRect(c)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),0)
		cv2.putText(frame,"Mavi",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0))

	_,cntr,_=cv2.findContours(yellow, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	for i,c in enumerate(cntr):
		if cv2.contourArea(c)<1000:
			continue
		x,y,w,h=cv2.boundingRect(c)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),0)
		cv2.putText(frame,"Sari",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,0))


	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF ==27:
		break

cam.release()
cv2.destroyAllWindows()
