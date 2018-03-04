#-*-coding: cp1254-*-
###Renk Filtresi###

import numpy as np
import cv2

greenLower = np.array([50, 100, 100])
greenUpper = np.array([70, 255, 255])	

cam=cv2.VideoCapture(0)

while(1):
	_,frame=cam.read()
	
	blurred=cv2.GaussianBlur(frame,(11,11),0)
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	mask=cv2.inRange(hsv,greenLower,greenUpper)
	mask=cv2.erode(mask,None,iterations=2)
	mask=cv2.dilate(mask,None,iterations=2)

	_,cnts,_=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	center= None

	if len(cnts)>0:
		c=max(cnts,key=cv2.contourArea)
		((x,y),radius)=cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
		if radius >10:
			cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,255),2)
			cv2.circle(frame,center,5,(0,0,255),-1)

	cv2.imshow("frame",frame)
	if cv2.waitKey(1) & 0xff == 27:
		break

cam.release()
cv2.destroyAllWindows()
