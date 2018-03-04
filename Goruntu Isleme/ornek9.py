#-*-coding: cp1254-*-
###Hareket Algılama3###

import numpy as np
import cv2

cam=cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorMOG2()

_,frame1=cam.read()
fgmask=fgbg.apply(frame1)

while(1):
	_,frame2=cam.read()
	fgmask=fgbg.apply(frame2)

	thresh=cv2.erode(fgmask,None, iterations=1)
	thresh=cv2.dilate(fgmask,None, iterations=1)
	_,cnts,_=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

	for i,c in enumerate(cnts):	
		if cv2.contourArea(c)<1000:
			continue
		x,y,w,h=cv2.boundingRect(c)
		#cv2.drawContours(frame2, cnts, i, (0,255,0), 3)		
		cv2.rectangle(frame2,(x,y),(x+w,y+h),(0,255,0),0)
	cv2.imshow('frame',frame2)
	if cv2.waitKey(30) & 0xFF ==27:
		break

cam.release()
cv2.destroyAllWindows()
