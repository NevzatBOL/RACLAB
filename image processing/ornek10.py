#-*-coding: cp1254-*-
###İnsan Takibi###

import numpy as np
import cv2

hog=cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cam=cv2.VideoCapture('videolar/test.mp4')
while(1):
	_,frame=cam.read()
	found,w=hog.detectMultiScale(frame,winStride=(8,8),padding=(32,32),scale=1.05)
	
	for (x, y, w, h) in found:
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)	
	cv2.imshow('feed',frame)
	if cv2.waitKey(1) & 0xff ==27:
		break
cam.release()
cv2.destroyAllWindows()
