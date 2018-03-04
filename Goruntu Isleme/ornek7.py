#-*-coding: cp1254-*-
###Hareket Algılama1###

import numpy as np
import cv2

cam=cv2.VideoCapture('videolar/test.mp4')

ret, frame1 = cam.read()
prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255

while(1):
	ret, frame2 = cam.read()
	next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
	flow = cv2.calcOpticalFlowFarneback(prvs,next,None,0.5,3,15,3,5,1.2,0)
	mag, ang = cv2.cartToPolar(flow[...,0],flow[...,1])
	cv2.imshow('frame', mag)
	if cv2.waitKey(60) & 0xFF == 27:
		break

cam.release()
cv2.destroyAllWindows()
